#from PIL import Image
import os
from itertools import product


def create_svg(filename, height, width):
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
    
    for combination in product(*list_items):
        section_file = []
        for i in list(range(0,j-1)):
            path_to_file = combination[i]
            # item = combination[i].strip('.txt').split('_')
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

        svg_file = open(filename + ".svg","w")
        svg_file.write(content_svg)
        svg_file.close

if __name__ == '__main__':
    create_svg("test_svg_1",1000,1000)
