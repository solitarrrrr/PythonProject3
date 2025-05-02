# puvip install tensorflow
import cv2
import numpy as np
import tensorflow as tf

# define the path with model name
MODEL_PATH = "models/model_unquant.tflite"
LABELS_FILE_PATH = "models/labels.txt"

def load_labels(file_path):
    labels = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            parts = line.strip().split()
            labels.append(parts[1])
    return labels

CLASS_NAMES = load_labels(LABELS_FILE_PATH)

# load TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape'][1:3]

def preprocess_frame(frame):
    frame_resized = cv2.resize(frame, input_shape)
    frame_normalized = frame_resized.astype(np.float32) / 255.0
    return np.expand_dims(frame_normalized, axis=0)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("click space to freeze the video, click q to quit")

last_frame = None  # save the last_frame
display_last_frame = False  # display the last_frame or not

while True:
    if not display_last_frame:  # video mode
        ret, frame = cap.read()
        if not ret:
            print("Cannot read frame")
            break

        frame = cv2.flip(frame, 1)
        last_frame = frame.copy()  # keep the current frame

        # preprocessing the frame then making prediction
        input_data = preprocess_frame(frame)
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details[0]['index'])[0]

        # show the prediction values of all the categories
        confidence_texts = [f"{CLASS_NAMES[i]}: {predictions[i]*100:.2f}%" for i in range(len(CLASS_NAMES))]
        text = " | ".join(confidence_texts)

        # put text onto the screen
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
        cv2.imshow("Prediction", frame)
    else:  # last_frame mode
        if last_frame is not None:
            cv2.putText(last_frame, text, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
            cv2.imshow("Prediction", last_frame)

    # check the button pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # quit
        break
    elif key == ord(' '):  # switch mode
        display_last_frame = not display_last_frame

cap.release()
cv2.destroyAllWindows()