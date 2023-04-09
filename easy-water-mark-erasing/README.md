## erase the watermark

**环境「Environment」**
```
skimage
pdf2image
img2pdf
```

**⚡注意「Notice」⚡**  
只能去除图片所示的水印，其他水印去除请看最后一条！  
It can only erase the watermark like the below picture. See last entry may help you erase other kind of watermarks.  

**用法「Usage」**  
把你待处理的PDF放入pdf文件里，运行watermark.py，处理好的文档自动放在result文件里。  
put your pdf files to 'pdf' directory, then run watermark.py. The result will be saved in 'result' directory.  

**原理「principle」**  
将PDF的每页转化为图片，在我的待处理PDF中包含如图所示的固定大小形式的心型二维码。
通过观察水印形式，对每张图片以跨度10个像素点进行二维遍历，找到绿色的点（微信图标部分），然后将绿色点周围一定大小的方块区域替换成白色，达成去除水印的目的。（观察文档除了水印，内容部分都是黑灰白，因此才可以这样处理）  
Convert pdf to images. There are fixed size heart-shape QR code as shown in the figure. I make secondary traversal with 10 pixels every picture to find green point(wechat mark), and then replace the square area of a certain size around the green points with white to achieve the purpose of removing the watermark(By observing the document, the content is black, white and gray, except for the watermark, so it can be processed in this way)

![水印](./source/watermark.png)

**其他简单水印去除：**
！！*需要自己改代码的相关部分，*大多数水印都是像素值介于0~255之间（为了不遮盖原文），可以利用这点来遍历每幅图片的每个像素点，进行处理判断（速度会比较慢）。
