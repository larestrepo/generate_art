from PIL import Image
im = Image.open("./image_to_svg/MoxieGalleryFondos_0009_Capa-1.png").convert('L')
width, height = im.size
colortuples = Image.Image.getcolors(im)
mycolor1 = min(colortuples)[1]
mycolor2 = max(colortuples)[1]
pix = im.load()
for x in range(0, width):
    for y in range(0, height):
        #if pix[x,y] == mycolor1:
        im.putpixel((x, y), (127))
im.save('MyImage.png')