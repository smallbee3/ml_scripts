import shutil
import os
import numpy as np
import argparse

def get_files_from_folder(path):

    files = os.listdir(path)
    return np.asarray(files)

def main(path_to_data, path_to_save, train_ratio):
    path = os.path.join(path_to_data, 'images')
    files = get_files_from_folder(path)
    img_data_counter = len(files)
    print('img_data_counter: ', img_data_counter)

    test_counter = img_data_counter * (1 - train_ratio)
    print('test_counter: ', test_counter)

    # transfers files
    img_path_to_data = os.path.join(path_to_data, 'images')
    img_path_to_save = os.path.join(path_to_save, 'images')
    ann_path_to_data = os.path.join(path_to_data, 'annotations')
    ann_path_to_save = os.path.join(path_to_save, 'annotations')

    # creates dir
    if not os.path.exists(img_path_to_save):
        os.makedirs(img_path_to_save)
    if not os.path.exists(ann_path_to_save):
        os.makedirs(ann_path_to_save)

    files = get_files_from_folder(img_path_to_data)
    # moves data
    for j in range(int(test_counter)):

        if files[j].find('.jpg') < 0: continue

        # images
        img_src = os.path.join(img_path_to_data, files[j])
        img_dst = os.path.join(img_path_to_save, files[j])
        shutil.move(img_src, img_dst)

        # annotations
        txt_file_name = files[j].replace('jpg', 'txt')
        ann_src = os.path.join(ann_path_to_data, txt_file_name)
        ann_dst = os.path.join(ann_path_to_save, txt_file_name)
        shutil.move(ann_src, ann_dst)

def parse_args():
  parser = argparse.ArgumentParser(description="Dataset divider")
  parser.add_argument("--data_path", required=True,
    help="Path to data")
  parser.add_argument("--test_data_path_to_save", required=True,
    help="Path to test data where to save")
  parser.add_argument("--train_ratio", required=True,
    help="Train ratio - 0.7 means splitting data in 70 % train and 30 % test")
  return parser.parse_args()

if __name__ == "__main__":
  args = parse_args()
  main(args.data_path, args.test_data_path_to_save, float(args.train_ratio))
