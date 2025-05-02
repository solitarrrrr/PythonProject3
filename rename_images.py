import os

def rename_images(directory, start_number, increment):
    # 获取目录中的所有文件
    files = os.listdir(directory)
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]

    # 对文件进行排序，确保按数字顺序处理
    jpg_files.sort(key=lambda x: int(x.split('.')[0]))

    for i, filename in enumerate(jpg_files):
        # 获取文件的扩展名
        ext = filename.split('.')[-1]
        
        # 计算新的序号
        new_number = start_number + i * increment
        
        # 创建新的文件名
        new_filename = f"{new_number:06d}.{ext}"
        
        # 构建完整的文件路径
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # 重命名文件
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

# 设置参数
directory = "/Users/victoria/PycharmProjects/PythonProject3/images/dogs"
start_number = 114  # 从000114开始
increment = 1  # 每个序号增加1

# 调用函数
rename_images(directory, start_number, increment)