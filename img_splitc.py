import cv2

# https://note.nkmk.me/en/python-opencv-pillow-image-size/

print("Welcome to ImageSplitter2000")
print("We have two options for splitting your image:")
print("#1. Key-in   a    for split by rows and columns")
print("#2. Key-in   b    for split by square pixels")
optioncheckcheck = str(input("How do you want to split your image ('a' or 'b')? : "))


# https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
nameofimage = (
    askopenfilename()
)  # show an "Open" dialog box and return the path to the selected file
# print(filename)

# nameofimage = input("What's the name of the file you want to split (e.g. test.jpg): ")

# path = pathlib.Path(nameofimage)
# path.exists()

im = cv2.imread(nameofimage)

# print(type(im))
# print(im.shape)
# print(type(im.shape))

if optioncheckcheck == "a":
    h, w, c = im.shape
    print("width:  ", w)
    print("height: ", h)
    print("channel:", c)

    # https://stackoverflow.com/questions/53755910/how-can-i-split-a-large-image-into-small-pieces-in-python

    splpixel2 = int(
        input("How many times would you like to split this image (columns)? = ")
    )
    splpixel2 = int(w / splpixel2)

    splpixel = int(
        input("How many times would you like to split this image (rows)? = ")
    )
    splpixel = int(h / splpixel)

    img = cv2.imread("test.jpg")
    for r in range(0, img.shape[0], splpixel):
        for c in range(0, img.shape[1], splpixel2):
            cv2.imwrite(f"img{r}_{c}.png", img[r : r + splpixel, c : c + splpixel2, :])

elif optioncheckcheck == "b":

    splpixel = int(input("Size of each crop -- by square pixels? = "))

    img = cv2.imread(nameofimage)
    for r in range(0, img.shape[0], splpixel):
        for c in range(0, img.shape[1], splpixel):
            cv2.imwrite(f"img{r}_{c}.png", img[r : r + splpixel, c : c + splpixel, :])

else:
    sys.exit()