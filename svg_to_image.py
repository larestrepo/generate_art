#!/usr/bin/env python

"""Convert an SVG file to a PNG file."""

from argparse import ArgumentParser
import subprocess
import os.path


def main():
    # args = parse_args()
    # if not args.out:
    # args.out = os.path.splitext(args.file)[0] + '.png'
    file = '/home/cexplorer/generate_art/results_svg/1_d46e39b4-3731-11ec-81ff-3f263eb9ca6e.svg'
    convert_with_cairosvg_sizes(file,1000,1000)


def convert_with_cairosvg_simple(args):
    # import cairocffi as cairo
    from cairosvg import svg2png
    svg2png(open(args.file, 'rb').read(), write_to=open(args.out, 'wb'))


def convert_with_cairosvg_sizes(file, width, height):
    from cairosvg.surface import PNGSurface
    # width, height = args.size.split('x')
    with open(file, 'rb') as svg_file:
        PNGSurface.convert(
            bytestring=svg_file.read(),
            width=width,
            height=height,
            write_to=open('test_output', 'wb')
            )

def convert_with_rsvg(args):
    import cairo
    import rsvg

    width, height = args.size.split('x')
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, int(width), int(height))
    ctx = cairo.Context(img)
    handler= rsvg.Handle(args.file)
    handler.render_cairo(ctx)
    img.write_to_png(args.out)


def convert_with_inkscape(args):
    try:
        inkscape_path = subprocess.check_output(["which", "inkscape"]).strip()
    except subprocess.CalledProcessError:
        print("ERROR: You need inkscape installed to use this script.")
        exit(1)

    export_width, export_height = args.size.split('x')

    args = [
        inkscape_path,
        "--without-gui",
        "-f", args.file,
        "--export-area-page",
        "-w", export_width,
        "-h", export_height,
        "--export-png=" + args.out
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