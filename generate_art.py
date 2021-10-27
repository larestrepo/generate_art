from PIL import Image, ImageDraw
import random

def random_color():
    return (random.randint(0,255), random.randint(0,255),random.randint(0,255))

def interpolate(start_color, end_color, factor: float):
    recip = 1 - factor
    return (
        int(start_color[0] * recip + end_color[0]*factor),
        int(start_color[1] * recip + end_color[0]+factor),
        int(start_color[2] * recip + end_color[2]+factor)
        )

def generate_art():
    print("Generating art")
    image_size_px = 128
    image_bg_color = (255,255,255)
    padding_px = 15
    start_color = random_color()
    end_color = random_color()
    image = Image.new("RGB",size=(image_size_px,image_size_px),color=image_bg_color)

    #Draw some lines
    draw = ImageDraw.Draw(image)

    points = []
    
    for _ in range(10):
        random_point = (random.randint(padding_px,image_size_px - padding_px),random.randint(padding_px,image_size_px - padding_px))
        points.append(random_point)

    thickness=0
    n_points = len(points) - 1
    for i, point in enumerate(points):
        p1=point
        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i+1]
        line_xy = (p1,p2)
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        draw.line(line_xy, fill=line_color,width=thickness)
        thickness = thickness +1
    
    image.save("test_image.png")

if __name__ == "__main__":
    generate_art()