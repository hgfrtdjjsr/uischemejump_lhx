from PIL import Image
from PIL import ImageChops
import os
import cv2
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import decode
import base64

class CompareImage():

    def compare_image(self, path_image1, path_image2):
        a = '/Users/lidoudou/PycharmProjects/uischemejump/img.txt'
        with open(a, 'r') as file:
            imgs = file.read()
        imgs = eval(imgs)
        imgs1 = imgs[0]
        fh = open('imagetosave.png', 'wb')
        fh.write(base64.b64decode(imgs1))
        fh.close()
        imageA = cv2.imread('/Users/lidoudou/PycharmProjects/uischemejump/imagetosave.png')
        imageB = cv2.imread(path_image2)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = structural_similarity(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        return score


compare_image = CompareImage()
compare_image.compare_image(os.getcwd() + '/fileimgs/0.png', os.getcwd() + '/fileimgs/1.png')
