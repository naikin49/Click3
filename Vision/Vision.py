import pyscreenshot as scr
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import ctypes
from array import array

class Vision:

    def __init__ (self):
        self.__lib = ctypes.CDLL('C:/Users/Nail/Desktop/Click3/Vision.dll')
        self.__lib.Find_Img.restype = ctypes.c_void_p
        self.__lib.Find_Img.argtypes = [ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.c_int,
                                            ctypes.c_int,
                                            ctypes.c_int,
                                            ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.POINTER(ctypes.c_int)]

    def Img_show(self, img):
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.show()

    def Screen(self):
        return np.array(scr.grab())
    
    def Screen_area(self, x1, y1, x2, y2):
        return np.array(scr.grab(bbox=(x1,y1,x2,y2)))

    def Img_Readig(self, filename):
        return np.array(Image.open(filename).convert('RGB'))

    def Find_Img(self, acc, img1, img2):
        n = len(img1) * len(img1[0]) * 3
        m = len(img2) * len(img2[0]) * 3
        int_array_n = ctypes.c_int * n
        int_array_m = ctypes.c_int * m


        c_one = int_array_n.from_buffer(array('i', img1.reshape(-1)))
        c_two = int_array_m.from_buffer(array('i', img2.reshape(-1)))

        x = ctypes.c_int()
        y = ctypes.c_int()

        self.__lib.Find_Img(acc, c_one, c_two, len(img1[0]), len(img1), len(img2[0]), len(img2), x, y)

        return (x.value, y.value)


