from PIL import Image as im
import time
import os
from os import walk


def getFilePath1():
    extension = ['jpg', 'png']
    rootPath = os.path.abspath(os.getcwd())
    files = next(walk(rootPath), (None, None, []))
    folders = files[1]
    inputs = []
    for folder in folders:
        nextPath = rootPath + f'\\{folder}'
        paths = next(walk(nextPath), (None, None, []))[2]
        paths1 = []
        for file in paths:
            if file[-3:] in extension:
                file = nextPath + f'\\{file}'
                paths1.append(file)
        inputs.append((folder, paths1))
    return inputs
    # return [(filename,[imageFiles])...]


def getFilePath():
    rootPath = os.path.abspath(os.getcwd())
    path = rootPath + '\img'
    if not os.path.exists(path):
        print("Please make a folder and name it 'img', copy all image file to it")
        return []
    else:
        paths = next(walk(path), (None, None, []))[2]  # [] if no file
        paths1 = []
        for file in paths:
            file = path + f'\\{file}'
            paths1.append(file)
        return paths1


def img2pdf(files, output='output.pdf'):
    imageList = []
    for file in files:
        im1 = im.open(file)
        im11 = im1.convert('RGB')
        imageList.append(im11)
    image = imageList[0]
    imageList.pop(0)  # del imageList[0]
    image.save(output, save_all=True, append_images=imageList)


def rename():
    pass


def main():
    print('Please copy all needed files to folder naming "img"')
    answer = input("If it was done, press Enter to continue...")
    paths = getFilePath1()
    for path in paths:
        fileOutput = path[0]
        filePath = path[1]
        img2pdf(filePath, fileOutput+'.pdf')


if __name__ == '__main__':
    main()
