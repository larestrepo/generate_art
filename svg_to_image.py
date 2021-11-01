#!/usr/bin/env python

"""Convert an SVG file to a PNG file."""

from argparse import ArgumentParser
import subprocess
import os.path
import svgwrite
from svgwrite.extensions import Inkscape


def main():
    # args = parse_args()
    # if not args.out:
    # args.out = os.path.splitext(args.file)[0] + '.png'
    file = '/home/cexplorer/generate_art/results_svg/1_84f9e649e6f0851db03b8d3846da373cc61f6e5a.svg'
    convert_with_cairosvg_sizes(file,1000,1000)


def convert_with_cairosvg_simple(file):
    # import cairocffi as cairo
    from cairosvg import svg2png
    svg2png(open(file, 'rb').read(), write_to=open('test_output', 'wb'))


def convert_with_cairosvg_sizes(file, width, height):
    from cairosvg.surface import PNGSurface
    # width, height = args.size.split('x')
    with open(file, 'rb') as svg_file:
        PNGSurface.convert(
            bytestring=svg_file.read(),
            width=width,
            height=height,
            write_to=open('test_output'+'.png', 'wb')
            )

def convert_with_rsvg(file,width,height):
    import cairo
    import rsvg

    #width, height = args.size.split('x')
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, int(width), int(height))
    ctx = cairo.Context(img)
    handler= rsvg.Handle(file)
    handler.render_cairo(ctx)
    img.write_to_png('test_output')


def convert_with_inkscape(file,export_width,export_height):
    try:
        inkscape_path = subprocess.check_output(["which", "inkscape"]).strip()
    except subprocess.CalledProcessError:
        print("ERROR: You need inkscape installed to use this script.")
        exit(1)

    # export_width, export_height = args.size.split('x')

    args = [
        inkscape_path,
        "--without-gui",
        "-f", file,
        "--export-area-page",
        "-w", str(export_width),
        "-h", str(export_height),
        "--export-png=" + 'test_output'
    ]
    print(args)
    subprocess.check_call(args)


# def parse_args():
#     parser = ArgumentParser()
#     parser.add_argument('-f', '--file', required=True, help="SVG file to open")
#     parser.add_argument('-s', '--size', required=True, help="target size to render")
#     parser.add_argument('-o', '--out', help="Destination file")
#     return parser.parse_args()


if __name__ == '__main__':
    main()