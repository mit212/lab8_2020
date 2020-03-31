import cv2

img_lena=cv2.imread('Example_lena_denoise_noisy.jpg',1)
img_flower=cv2.imread('Flower_noisy.jpg',1)
cv2.imshow('image',img_lena)
cv_image=cv2.imread('Flower_noisy.jpg',1)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##
##cv2.imwrite('lena_copy.png',img_lena)
cv2.imshow("Original_Image", cv_image)
cv2.waitKey(3) 
    
# 3. Hough Transform
gray = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)  # Convert to grascale image
cv2.imshow("Gray_Image", gray)
cv2.waitKey(3) 

edges = cv2.Canny(gray,10,500,apertureSize = 3)   # Canny edge detector to make it easier for hough transform to "agree" on lines
cv2.imshow("Canny_Image", edges)
cv2.waitKey(3) 

min_intersections = 200                           # TO DO: Play with this parameter to change sensitivity.
lines = cv2.HoughLines(edges,1,np.pi/180,min_intersections)     # Run Hough Transform
num_lines = 0;
shape = lines.shape
for i in range(shape[0]):                         # Plot lines over original feed
    for rho,theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(cv_image,(x1,y1),(x2,y2),(0,0,255),2)
        num_lines += 1
        
cv2.imshow("Line_Detected_Image", cv_image)
cv2.waitKey(5)
print("Detecting Lines...")
