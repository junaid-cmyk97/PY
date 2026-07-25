# to call the image function
# import cv2
#
# import plt
#
# #then to place the image in the code copy the location with .imread
# image = cv2.imread("C:/Users/SIC/Desktop/SHHETS/Screenshot 2026-07-22 140636.png")
#
# #then,to size the image  using resize function
# resized = cv2.resize(image,(500,1000))
# plt.imshow(resized)
# plt.show()

# import cv2
# import plt
#
# image = cv2.imread("C:/Users/SIC/Desktop/3.png")
#
# resized = cv2.resize(image,(500,100))
#
#
# plt.imshow(resized)
#
# plt.show()
# print(resized)

# #################
import cv2
import plt
image = cv2.imread("C:/Users/SIC/Desktop/SHHETS/Screenshot 2026-07-22 140636.png")
resized_image = cv2.resize(image, (1500, 500))
plt.imshow(resized_image)
plt.show()


import cv2
import plt

image_path = r"C:/Users/SIC/Desktop/SHHETS/Screenshot 2026-07-22 140636.png"

image = cv2.imread(image_path)

if image is None:
    print("Image Not Found")

resized_image = cv2.resize(image, (1500,500))

resized_image_for_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)      #

plt.imshow(resized_image_for_rgb)

plt.show()
