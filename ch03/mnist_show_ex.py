import sys, os
sys.path.append(os.pardir)
import numpy as np
import cv2 as cv
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(img)
    pil_img.show()

def main():

    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

    for x in x_train:
        img = x.reshape(28, 28)
        height, width = img.shape[:2]
        scale = 10
        scaled_img = cv.resize(img, (scale*width, scale*height))
        cv.imshow("img", scaled_img)
        cv.waitKey()
        
    img = x_train[0]
    label = t_test[0]
    print(label)

    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)

    img_show(img)

if __name__ == "__main__":
    main()
