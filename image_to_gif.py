from PIL import Image
import os

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

directory = './results_png'
list_items = []
num_items = []
j=0
images = []
for root, dirs, files in os.walk(directory):
        items=[]
        for filename in files:
            j +=1
            # items.append(str(filename))
            image = open_image(os.path.join(root,filename))
            images.append(image)
            # items.append(os.path.join(root,filename))
            if j == 10:
                break
# print(items)

gif = []
#first = open_image('./image_to_svg/5687_b8b6d1d8e530c55f169dc2d224efad4875e2249e.png')
#images = [first]#images, just convert it into PIL.Image obj
for image in images:
    gif.append(image)
gif[0].save('temp_result.gif', save_all=True,optimize=False, append_images=gif[1:], loop=0)