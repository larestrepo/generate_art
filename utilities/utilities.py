
# Color unit conversions
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def convert_with_cairosvg_sizes(file_path, output_path, width, height):
    from cairosvg.surface import PNGSurface
    # width, height = args.size.split('x')
    with open(file_path, 'rb') as svg_file:
        PNGSurface.convert(
            bytestring=svg_file.read(),
            width=width,
            height=height,
            write_to=open(output_path + '.png', 'wb')
            )