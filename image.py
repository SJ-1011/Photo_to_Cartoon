import cv2
import numpy as np
# Load the image
img = cv2.imread('./image_folder/cat_test.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply median blur to reduce noise
# 1로하면 엄청 검은선이 많아지고, 크게하면 그냥 블러 효과가 됨
gray = cv2.medianBlur(gray, 5)
# Detect edges using adaptive thresholding
# 뒤에있는 숫자 값만 조정하기 이거도 블러 효과 되는듯?
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# Convert the image to color
color = cv2.bilateralFilter(img, 9, 300, 300)
# Combine the color image with the edges mask
cartoon = cv2.bitwise_and(color, color, mask=edges)
# Display the cartoon image
cv2.imshow("Cartoon", cartoon)
cv2.imwrite('./image_folder/cartoon_cat2.jpg',cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()