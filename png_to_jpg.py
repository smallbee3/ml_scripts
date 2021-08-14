from PIL import Image

from os import listdir
from os.path import isfile, join

images_png_path = 'gabriel_project_dataset/images-png'
images_jpg_path = 'gabriel_project_dataset/images-jpg'

def main(directory_path):
    all_txt_files = [f for f in listdir(directory_path) if (isfile(join(directory_path, f)) and f.find('.PNG') > -1)]
    # print(all_txt_files)

    for index, filename in enumerate(all_txt_files):
        print(index, filename)

        im1 = Image.open(f'{images_png_path}/{filename}')
        jpg_filename = filename.replace('PNG', 'jpg')
        im1.save(f'{images_jpg_path}/{jpg_filename}')

if __name__ == "__main__":
    main(images_png_path)
