
import os
import json

directory = './results_png'
png_list = []
json_list = []
metadata = {}
for root, dirs, files in os.walk(directory):
        
    for filename in files:
        if '.png' in filename:
            filename=filename.strip('.png')
            png_list.append(filename)
        elif '.json' in filename:
            with open (str(directory) + '/' + str(filename),'r') as file:
                metadata_temp = json.load(file)
            metadata[filename.split('_')[0]] = metadata_temp
            filename=filename.strip('.json')
            json_list.append(filename)

print(len(png_list),len(json_list),len(png_list)-len(json_list))
# Removing corrupted files
if len(png_list)!=len(json_list):
    for png in png_list:
        if png not in json_list:
            os.remove(directory + '/' + png + '.png' )

#Saving overall png metadata file

with open(directory + '/' + 'metadata_png.json','w') as file:
    json.dump(metadata,file, indent=4)
        

directory = './results_svg'
png_list = []
json_list = []
metadata = {}
for root, dirs, files in os.walk(directory):
        
    for filename in files:
        if '.svg' in filename:
            filename=filename.strip('.svg')
            png_list.append(filename)
        elif '.json' in filename:
            with open (str(directory) + '/' + str(filename),'r') as file:
                metadata_temp = json.load(file)
            metadata[filename.split('_')[0]] = metadata_temp
            filename=filename.strip('.json')
            json_list.append(filename)
            
with open(directory + '/' + 'metadata_svg.json','w') as file:
    json.dump(metadata,file, indent=4)

print(len(png_list),len(json_list),len(png_list)-len(json_list))
            # items.append(str(filename))
#             items.append(os.path.join(root,filename))
#     if items!=[]:
#         num_items.append(list(range(1,len(items))))
#         list_items.append(items)
#     j+=1
#     print (root, dirs, files)
# print(num_items,j)