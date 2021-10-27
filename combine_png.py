
from PIL import Image
  
def main():
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open("./layers/background/MoxieGalleryFondos_0009_Capa-1.png") 
          
        #Relative Path
        #Image which we want to paste
        img2 = Image.open("./layers/Gallery/Gallery00.png")
        mask_im = Image.open('./layers/Gallery/Gallery00.png').resize(img2.size).convert('RGBA')
        back_im = img.copy()
        back_im.paste(img2, (100, 50), mask_im)
        # img.paste(img2  z, (50, 50))
          
        #Saved in the same relative location
        back_im.save("pasted_picture.png")
          
    except IOError:
        pass
  
if __name__ == "__main__":
    main()