
from PIL import Image
import os
from itertools import product
import json
import hashlib

def save_files(path, name, rgb_im):
    if not os.path.exists(path):
        os.makedirs(path)
    rgb_im.save(name + ".png")
  
def create_png(max_combinations):
    try:
        directory = './layers2'
        list_items = []
        num_items = []
        j=0
        for root, dirs, files in os.walk(directory):
            for _ in enumerate(root):
                
                items=[]
                for filename in files:
                    # items.append(str(filename))
                    items.append(os.path.join(root,filename))
            if items!=[]:
                num_items.append(list(range(1,len(items))))
                list_items.append(items)
            j+=1
        list_items.sort()
        file_counter = 1
        for combination in product(*list_items):
            attributes = []
            item0 = combination[0].strip('.png').split('/')[-1]
            attributes.append(item0)
            com = Image.open(combination[0]).convert('RGBA')
            for i in list(range(1,j-1)):
                img2 = Image.open(combination[i]).convert('RGBA')
                com = Image.alpha_composite(com, img2)
                attributes.append(combination[i].strip('.png').split('/')[-1])
            rgb_im = com.convert('RGB')
            #Hashing the content
            hash_content = hashlib.sha1(str(com.info).encode()).hexdigest()
                
            #Building the metadata info
            metadata = {}
            metadata["ID"] = hash_content
            metadata["Attributes"] = {
                "Background": attributes[0],
                "Cherry": attributes[1],
                "Leaf": attributes[2],
                "Decor": attributes[3]
            }
            path = './results_cherry_png/'
            file_name = path + str(file_counter) + '_' + str(hash_content)
            save_files(path,file_name,rgb_im)

            # Saving the metadata
            with open(file_name + ".json","w") as file:
                json.dump(metadata,file, indent=4)
            if max_combinations >=1:
                if file_counter==max_combinations:
                    break
            file_counter +=1

    except IOError:
        print('error')
  
if __name__ == "__main__":
    create_png(0)
