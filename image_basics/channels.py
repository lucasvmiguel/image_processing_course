from cv2 import cv2

pic = cv2.imread("test.jpg")

print(pic.shape)

(b, g, r) = cv2.split(pic)

# cv2.imshow("BLUE", b)
# cv2.imshow("GREE", g)
# cv2.imshow("RED", r)

merged_pic = cv2.merge((b, g, r))
cv2.imshow("MERGED", merged_pic)

cv2.waitKey(5000)
