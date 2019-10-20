from PIL import Image
import os
import numpy as np

# Teacher: Sir Anees Ahmed
# Timings: 9:00 to 1:00
# Institute: Saylani Gulshan
# Name: Zain Ahmed Saleem
# Roll No: AIC017587
# Batch: 01


def check_dir(folder='photos/'):
    if os.path.exists(folder):
        fileslist, total = read_dir_files(folder)
        is_not_empty = check_files(total)
        if is_not_empty:
            return True, total, fileslist
        else:
            print(f'There is No Files in This Directory')
    else:
        print(f'Directory "{folder}"  Does Not Exist')


def read_dir_files(folder):
    total_files = 0
    file_names_list = []
    directory = folder
    for dirName, subdirList, fileList in os.walk(directory):
        for file_name in fileList:
            try:
                img = Image.open(folder + file_name)
            except OSError:
                file = directory + file_name
                print(f'"{file}" file is not a valid image')
                print(f'Please Delete or move "{file[7:]}" file to another folder\n')
                continue
            else:
                file_names_list.append(directory + file_name)
                total_files += 1
    return file_names_list, total_files


def check_files(files):
    if files < 1:
        return False
    else:
        return True


def to_numpy_array(name, no, imgist):
    imgist[no] = np.asarray(name, dtype=np.uint8) / 255


def resize_image(imgist, files_list, h=300, w=200):
    no = 0
    for file_name in files_list:
        img = Image.open(file_name)
        img = img.resize((w, h)).convert('RGB')
        # print(f'Name = {file_name} \nNumber {no+1}: Shape = {np.shape(img)}\n')
        to_numpy_array(img, no, imgist)
        no += 1


def main():
    root_dir = "photos/"     #Directory Which Contains Photos
    h = 200     #Resize Height
    w = 300     #Resize Width

    try:
        dir_status, total, files_list = check_dir(root_dir)
    except TypeError:
        print(f'Program Closed. Please Double check if "{root_dir}" directory exists in the main folder')
    else:
        print(f'Total Images = {total}\n')
        img_list = np.zeros([total, h, w, 3])
        resize_image(img_list, files_list, h, w)

        return img_list


if __name__ == "__main__":
    main()

