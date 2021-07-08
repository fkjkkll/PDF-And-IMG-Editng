from skimage import io
from pdf2image import convert_from_path
import numpy as np
import img2pdf
import os
import shutil

def select_pixel(r,g,b):
    # 判断绿色
    if (r>120 and g>150 and b < 100):
        return True
    else:
        return False

def handle(imgs):
    width = imgs.shape[1]
    height = imgs.shape[0]
    for i in range(0, imgs.shape[0], 10):
        for j in range(0, imgs.shape[1], 10):
            if select_pixel(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
                # 填上白色遮盖
                for m in range(300):
                    for n in range(300):
                        y = i-150+m
                        x = j-150+n
                        # 越界判断
                        if  x < 0 or x >= width or y < 0 or y >= height:
                            continue
                        imgs[y][x][0] =  imgs[y][x][1] = imgs[y][x][2] = 255
                return imgs
    return imgs

fileCount = 1;
pdfList = os.listdir('./pdf')
pdfList = [os.path.join('./pdf/',i) for i in pdfList]
for fi in pdfList:
    print(fi)
    images = convert_from_path(fi, last_page=3, thread_count=4)
    index = 0
    for img in images:
        print(fi + ' ' + str(index))
        index += 1
        img = np.array(img)
        img = handle(img)
        io.imsave('./temp/'+str(index)+'.jpg', img)
    
    # 图片合并为PDF
    photo_list = os.listdir('./temp')
    photo_list.sort(key=lambda t: int(t[:-4]))
    photo_list = [os.path.join('./temp/',i) for i in photo_list]
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open('result/' + fi.split('/')[-1], 'wb') as f:
        f.write(img2pdf.convert(photo_list, layout_fun=layout_fun))
    
    shutil.rmtree('./temp/')
    os.mkdir('./temp/')
    fileCount += 1














