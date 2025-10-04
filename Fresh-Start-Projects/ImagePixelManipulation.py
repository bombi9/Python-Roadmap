import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = np.array(mpimg.imread('/Users/Racem/Documents/bbl/myFiles/Learning_Python/Git/Python-Roadmap/Fresh-Start-Projects/myStolenFiles/myImage.png'))

# If the image is a float32, convert it to a uint8
if image.dtype == np.float32:
    image = (image * 255).astype(np.uint8)

bright_image = np.clip(image + 50, 0, 255) #clipping the image to the range of 0 to 255 which when we add 50 to the image it will not exceed the range of 0 to 255 then clip will take the value and set it to 255 if it exceeds the range of 0 to 255
inverted_image = 255 - image #inverting the pixels by substracting 255 from them
thresholded = np.where(image < 128, 0, 255) #threshold when an image's pixel is less than 128 it goes 0 'black' else it goes 255 'white'

plt.imshow(image)
plt.title("The World's Best Image :o")
plt.axis(None)
plt.show()

plt.imshow(bright_image)
plt.title("The World's Best bright image :o")
plt.axis(None)
plt.show()

plt.imshow(thresholded)
plt.title("The World's Best inverted image :o")
plt.axis(None)
plt.show()
