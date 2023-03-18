import pyscreenshot as scr
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class Vision:

    def __init__ (self):
        pass

    def Img_show(self, img):
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.show()

    def Screen(self):
        return np.array(scr.grab())
    
    def Screen_area(self, x1, y1, x2, y2):
        return np.array(scr.grab(bbox=(x1,y1,x2,y2)))

    def Img_Readig(self, filename):
        return np.array(Image.open(filename))

    def Is_Color_eq(self, distance, c1, c2):
        #distance - расстояние между цветами (теорема Пифагора)
        if (abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]))**(1/2) <= distance:
            return True
        else:
            return False
    
    def Img_background(self, img):
        colors = {}
        for i in range(len(img)):
            for j in range(len(img[0])):
                if(tuple(img[i][j]) in colors):
                    colors[tuple(img[i][j])] += 1
                else:
                    colors.update({tuple(img[i][j]) : 1})

        max = 0
        color = ()
        for i in colors:
            if colors[i] > max:
                max = colors[i]
                color = i

        return color

    def Is_img_eq(self, acc, img1, img2, back):
        if back == -1:
            sum = 0
            for i in range(len(img1)):
                for j in range(len(img1[0])):
                    if self.Is_Color_eq(6, img1[i][j], img2[i][j]):
                        sum += 1
            print('acc = ',sum / (len(img1) * len(img1[0])) * 100,'%')
            if sum / (len(img1) * len(img1[0])) * 100 >= acc:
                return True
            else:
                return False
        
        else:
            sum = 0
            notback = 0
            for i in range(len(img1)):
                for j in range(len(img1[0])):
                    if self.Is_Color_eq(6, img1[i][j], img2[i][j]):
                        sum += 1
            print('acc = ',sum / (len(img1) * len(img1[0])) * 100,'%')
            if sum / (len(img1) * len(img1[0])) * 100 >= acc:
                return True
            else:
                return False

        

vis = Vision()

img1 = vis.Img_Readig('Img1.png')
img2 = vis.Img_Readig('Img2.png')
img3 = vis.Img_Readig('Img3.png')
img4 = vis.Img_Readig('Img4.png')

print(vis.Img_background(img3))
#img5 = vis.Img_Readig('Img5.png')

#if vis.Is_img_eq(60, img1, img2):
#    print('nice!')



#vis.Img_show(vis.Screen_area(1000,500,1980,1200))
#print(vis.Screen_area(1000,500,1980,1200))

#screen = np.array(scr.grab(bbox=(1700,0,1980,400)))
#screen = np.array(scr.grab())

#image = np.array(Image.open('img1.png'))

#fig, ax = plt.subplots()
#print(screen)
#ax.imshow(image)

#fig.set_figwidth(6)    #  ширина и
#fig.set_figheight(6)    #  высота "Figure"

#plt.show()