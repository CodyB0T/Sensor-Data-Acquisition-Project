import sys
import pyclariuscast
from PIL import Image
import os

# image will be 640x480

# print(help(pyclariuscast))

printStream = True


## called when a new processed image is streamed
# @param image the scan-converted image data
# @param width width of the image in pixels
# @param height height of the image in pixels
# @param sz full size of image
# @param micronsPerPixel microns per pixel
# @param timestamp the image timestamp in nanoseconds
# @param angle acquisition angle for volumetric data
# @param imu inertial data tagged with the frame
def newProcessedImage(image, width, height, sz, micronsPerPixel, timestamp, angle, imu):
    bpp = sz / (width * height)
    if printStream:
        print(
            "image: {0}, {1}x{2} @ {3} bpp, {4:.2f} um/px, imu: {5} pts".format(
                timestamp, width, height, bpp, micronsPerPixel, len(imu)
            ),
            end="\r",
        )
    if bpp == 4:
        img = Image.frombytes("RGBA", (width, height), image)
    else:
        img = Image.frombytes("L", (width, height), image)
    # img.save("processed_image.png")
    return


## called when a new raw image is streamed
# @param image the raw pre scan-converted image data, uncompressed 8-bit or jpeg compressed
# @param lines number of lines in the data
# @param samples number of samples in the data
# @param bps bits per sample
# @param axial microns per sample
# @param lateral microns per line
# @param timestamp the image timestamp in nanoseconds
# @param jpg jpeg compression size if the data is in jpeg format
# @param rf flag for if the image received is radiofrequency data
# @param angle acquisition angle for volumetric data
def newRawImage(image, lines, samples, bps, axial, lateral, timestamp, jpg, rf, angle):
    # check the rf flag for radiofrequency data vs raw grayscale
    # raw grayscale data is non scan-converted and in polar co-ordinates
    # print(
    #    "raw image: {0}, {1}x{2} @ {3} bps, {4:.2f} um/s, {5:.2f} um/l, rf: {6}".format(
    #        timestamp, lines, samples, bps, axial, lateral, rf
    #    ), end = "\r"
    # )
    # if jpg == 0:
    #    img = Image.frombytes("L", (samples, lines), image, "raw")
    # else:
    #    # note! this probably won't work unless a proper decoder is written
    #    img = Image.frombytes("L", (samples, lines), image, "jpg")
    # img.save("raw_image.jpg")
    return


## called when a new spectrum image is streamed
# @param image the spectral image
# @param lines number of lines in the spectrum
# @param samples number of samples per line
# @param bps bits per sample
# @param period line repetition period of spectrum
# @param micronsPerSample microns per sample for an m spectrum
# @param velocityPerSample velocity per sample for a pw spectrum
# @param pw flag that is true for a pw spectrum, false for an m spectrum
def newSpectrumImage(
    image, lines, samples, bps, period, micronsPerSample, velocityPerSample, pw
):
    return


## called when freeze state changes
# @param frozen the freeze state
def freezeFn(frozen):
    if frozen:
        print("\nimaging frozen")
    else:
        print("imaging running")
    return


## called when a button is pressed
# @param button the button that was pressed
# @param clicks number of clicks performed
def buttonsFn(button, clicks):
    print("button pressed: {0}, clicks: {1}".format(button, clicks))
    return


## main function
def main():
    ip = "192.168.1.1"
    port = 46673
    width = 640
    height = 480

    # uncomment to get documentation for pyclariuscast module
    # print(help(pyclariuscast))

    # get home path
    path = os.path.expanduser("~/")

    # initialize
    cast = pyclariuscast.Caster(
        newProcessedImage, newRawImage, newSpectrumImage, freezeFn, buttonsFn
    )
    ret = cast.init(path, width, height)
    if ret:
        print("initialization succeeded")
        ret = cast.connect(ip, port, "research")
        if ret:
            print("connected to {0} on port {1}".format(ip, port))
        else:
            print("connection failed")
            cast.destroy()
            return
    else:
        print("initialization failed")
        return


if __name__ == "__main__":
    main()
