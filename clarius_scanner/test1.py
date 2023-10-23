import time
import pyclariuscast


# Callback function to receive images
def newProcessedImage(image, width, height, sz, micronsPerPixel, timestamp, angle, imu):
    # Convert the raw image data to a QImage
    bpp = sz / (width * height)
    if bpp == 4:
        img = QtGui.QImage(image, width, height, QtGui.QImage.Format_ARGB32)
    else:
        img = QtGui.QImage(image, width, height, QtGui.QImage.Format_Grayscale8)

    # Save the image to a file
    img.save(f"clarius_image_{int(time.time())}.png")


# Initialize the Clarius Caster
cast = pyclariuscast.Caster(newProcessedImage)

# Connect to the Clarius device (adjust IP and port as needed)
if cast.connect("192.168.1.1", 46673, "research"):
    print("Connected to Clarius device")

# Capture images for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    time.sleep(0.1)  # Adjust the sleep time as needed

# Disconnect from the Clarius device
cast.disconnect()
print("Disconnected from Clarius device")

# Clean up
cast.destroy()
