# coding=utf-8
import argparse
import CutUI

if __name__ == '__main__':
    # 下面注释的命令行运行方式，有点难用哦
    """parser = argparse.ArgumentParser(prog="Interactive Graph Cut",
                                     description="Interactively segment an image", add_help=True)
    parser.add_argument('-i', '--INFILE', help='Input image file to segment.', required=True)
    parser.add_argument('-o', '--OUTFILE', help='Used to save segmented images.', required=True)

    args = parser.parse_args()"""

    ui = CutUI.CutUI('resource/1.jpg', 'resource/new.jpg')
    ui.run()
