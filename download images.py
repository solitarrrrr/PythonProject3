from icrawler.builtin import BingImageCrawler
import os
import glob

def download_images_until(keyword, target_count=200, output_dir="./images"):
    save_dir = os.path.join(output_dir, keyword)
    os.makedirs(save_dir, exist_ok=True)

    existing_images = glob.glob(os.path.join(save_dir, '*'))
    existing_count = len(existing_images)
    offset = 0

    while existing_count < target_count:
        remain = target_count - existing_count
        print(f"[{keyword}] Downloading {remain} more images...")

        crawler = BingImageCrawler(storage={'root_dir': save_dir})
        crawler.crawl(keyword=keyword, max_num=remain, offset=offset)

        # 更新现有图片数
        existing_images = glob.glob(os.path.join(save_dir, '*'))
        new_count = len(existing_images)

        # 避免死循环
        if new_count == existing_count:
            print(f"[{keyword}] No more images found. Stopped at {new_count}.")
            break

        existing_count = new_count
        offset += remain

    print(f"[{keyword}] Finished with {existing_count} images.")

if __name__ == "__main__":
    for animal in ["pig", "dog", "fish"]:
        download_images_until(animal, target_count=400)
