import os
import shutil
import random

RAW_TRAIN_DIR = "data/raw/train"
RAW_TEST_DIR = "data/raw/test"

PROCESSED_DIR = "data/processed"
TRAIN_DIR = os.path.join(PROCESSED_DIR, "train")
VAL_DIR = os.path.join(PROCESSED_DIR, "val")
TEST_DIR = os.path.join(PROCESSED_DIR, "test")

SPLIT_RATIO = 0.8  # 80% train, 20% val


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def split_data():
    # Create base folders
    create_dir(TRAIN_DIR)
    create_dir(VAL_DIR)
    create_dir(TEST_DIR)

    # Process TRAIN → split into train + val
    for class_name in os.listdir(RAW_TRAIN_DIR):
        class_path = os.path.join(RAW_TRAIN_DIR, class_name)

        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        random.shuffle(images)

        split_index = int(len(images) * SPLIT_RATIO)

        train_images = images[:split_index]
        val_images = images[split_index:]

        # Create class folders
        create_dir(os.path.join(TRAIN_DIR, class_name))
        create_dir(os.path.join(VAL_DIR, class_name))

        # Copy train images
        for img in train_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(TRAIN_DIR, class_name, img)
            shutil.copy(src, dst)

        # Copy val images
        for img in val_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(VAL_DIR, class_name, img)
            shutil.copy(src, dst)

    # Copy TEST data directly
    for class_name in os.listdir(RAW_TEST_DIR):
        class_path = os.path.join(RAW_TEST_DIR, class_name)

        if not os.path.isdir(class_path):
            continue

        create_dir(os.path.join(TEST_DIR, class_name))

        for img in os.listdir(class_path):
            src = os.path.join(class_path, img)
            dst = os.path.join(TEST_DIR, class_name, img)
            shutil.copy(src, dst)


if __name__ == "__main__":
    split_data()
    print("Data split completed!")