from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
imageList = []      # Contains the list of all images to be converted to PDF.

''' setting '''
folder = "../dir"   # Folder containing all the images.
name = "res.pdf"    # Name of the output PDF file.

# ------------- ADD ALL THE IMAGES IN A LIST ------------- #
for dirPath, dirNames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        full_path = os.path.join(dirPath, filename)
        imageList.append(full_path)

imageList.sort()                                # Sort the images by name.
for i in range(0, len(imageList)):
    print(imageList[i])

# --------------- ROTATE ANY LANDSCAPE MODE IMAGE IF PRESENT ----------------- #
for i in range(0, len(imageList)):
    im1 = Image.open(imageList[i])              # Open the image.
    width, height = im1.size                    # Get the width and height of that image.
    if width > height:
        im2 = im1.transpose(Image.ROTATE_270)   # If width > height, rotate the image.
        os.remove(imageList[i])                 # Delete the previous image.
        im2.save(imageList[i])                  # Save the rotated image.

print("\nFound " + str(len(imageList)) + " image files. Converting to PDF....\n")


# -------------- CONVERT TO PDF ------------ #
for image in imageList:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)                           # 210 and 297 are the dimensions of an A4 size sheet.

pdf.output(folder + name, "F")                                 # Save the PDF.

print("PDF generated successfully!")
