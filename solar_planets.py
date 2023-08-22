import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,  
           "Sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (100, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (200, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (300, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (400, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (500, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (800, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (1000, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (1100, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.imshow("output",img)

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)
