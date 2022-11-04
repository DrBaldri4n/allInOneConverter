#!/usr/bin/env python3
import os, sys

def pdfunite(args):
    userArguments = ""
    if args[0] == "-h":
        print("--pdf <input.pdf> <output.pdf>")
        sys.exit()
    for arg in args:
        userArguments += (arg + " ") 
    os.system("pdfunite " + userArguments)

def ffmpeg(args):
    userArgument = ""
    if args[0] == "-h":
        print(("\t--audio <input.mp4> <output.mp3>                    \n") + \
                ("\t-r      FRAMERATE                                 \n") + \
                ("\t-s      SIZE                                      \n") + \
                ("\t-aspect ASPECT RATIO                              \n") + \
                ("\tfor more: https://wiki.ubuntuusers.de/FFmpeg/"))
        sys.exit()
    for arg in args:
        userArgument += (arg +" ")
    os.system("ffmpeg -i " + userArgument)

def imageMagick (args):
    userArguments = ""
    if args[0] == "-h":
        print(("\t--img <input.png> <output.pdf>                                                                              \n") + \
                ("\t-gamma 0.8, 0.8, 0.8 (higher gamma = brighter)                                                            \n") + \
                ("\t-resize '1024x1024' (resize the picture to 1024x1024)                                                     \n") + \
                ("\t-normalize (Stretches the histogram so that black is the darkest color and white is the lightest color)   \n") + \
                ("\t-rotate 90 (rotate the picture right)                                                                     \n") + \
                ("\tshow (shows the picture direct)                                                                           \n") + \
                ("\tfor more: https://wiki.ubuntuusers.de/ImageMagick/"))
        sys.exit()
    for arg in args:
        userArguments += (arg + " ") 
    os.system("convert " + userArguments)

def main(args):
    opt = args[0]
    if opt == "-h":
        print(("\t--pdf     -h (combine PDFs)                                \n") + \
                ("\t--audio   -h (edit .mp4/.mkv files or convert to .mp3 )  \n") + \
                ("\t--img     -h (edit .png/jpg files rof convert to pdf"))
        sys.exit()
    if opt == "--pdf":
        pdfunite(args[1:])
        sys.exit()
    if opt == "--audio":
        ffmpeg(args[1:])
        sys.exit()
    if opt == "--img":
        imageMagick(args[1:])
        sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])


#TODO add automat installation for pdfunite, ffmpeg ...