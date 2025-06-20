import cv2 #استدعاء المكتبة
PH1 = cv2.imread('basic.jpg')
PH2 = cv2.imread('images/d.jpg')

if PH1.shape == PH2.shape :
    #print('The image have same size and channels')
    diff = cv2.subtract(PH1,PH2)
    b ,g ,r  = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) and cv2.countNonZero(r):
        print('The images are completly Equal')
else:
    print('the images are not Equal')