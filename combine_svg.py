#from PIL import Image
import os
import hashlib
from itertools import product
import json


def create_svg(height, width,output_format,max_combinations):
    #Defining the generic section of the svg file
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"  xmlns:xlink="http://www.w3.org/1999/xlink">\n'
    switch_init = f'<switch>\n'
    switch_end = f'</switch>\n'
    g_init = f'<g>\n'
    g_end = f'</g>\n'
    footer = f'</svg>'

    directory = './layers'
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
    
    file_counter = 1
    for combination in product(*list_items):
        section_file = []
        attributes = []
        for i in list(range(0,j-1)):
            path_to_file = combination[i]
            item = combination[i].strip('.txt').split('_')
            attributes.append(str(item[2]))
            file = open(path_to_file,"r")
            section_file.append(file.read())
        #Assigning variables
        background = section_file[0]
        additional = section_file[1]
        gallery = section_file[2]
        moxie = section_file[3]

        #Building the content
        content_svg = (
            header + 
            switch_init + 
                g_init +
                    background + 
                    additional +
                    g_init + 
                        g_init +
                            gallery +
                        g_end + 
                    g_end + 
                    g_init + 
                        moxie + 
                    g_end +
                g_end +
            switch_end +
            footer
            )

        #Hashing the content
        encoded_content = content_svg.encode()
        hash_content = hashlib.sha1(encoded_content)
        hexa_content = hash_content.hexdigest()

        #Building the metadata info
        metadata = {}
        metadata["ID"] = hexa_content
        metadata["Attributes"] = {
            "Background": attributes[0],
            "Decor": attributes[1],
            "Gallery": attributes[2],
            "Moxie": attributes[3]
        }

        # Saving the picture
        if output_format == 'svg':
            name = './results_svg/' + str(file_counter) + '_' + str(hexa_content)
            svg_file = open(name + ".svg","w")
            svg_file.write(content_svg)
            svg_file.close
        elif output_format == 'png':
            from cairosvg.surface import PNGSurface
            name = './results_png/' + str(file_counter) + '_' + str(hexa_content)
            PNGSurface.convert(
            bytestring=content_svg,
            width=width,
            height=height,
            write_to=open(name + '.png', 'wb')
            )

        # Saving the metadata
        with open(name + ".json","w") as file:
            json.dump(metadata,file, indent=4)
        if max_combinations >=1:
            if file_counter==max_combinations:
                break
        file_counter +=1

if __name__ == '__main__':
    create_svg(1000,1000,'svg',1)
