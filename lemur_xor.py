import cv2 

im1=cv2.imread('flag_7ae18c704272532658c10b5faad06d74.png')
im2=cv2.imread('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
im = im1 +im2
cv2.imshow("addition",im)

cv2.waitKey(0)
cv2.destroyAllWindows()
