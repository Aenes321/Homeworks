import cv2 as cv

def resize(width,height):
    global img
    img=cv.resize(img,(width,height),interpolation=cv.INTER_AREA)
    cv.imshow('foto',img)

def rectangle(p1,p2,p3,p4):
    global img
    cv.rectangle(img,(p1,p2),(p1+p3,p2+p4),(0,0,255),2)
    print(p1,p2,p3,p4)
    cropped=img[p2:p2+p4,p1:p1+p3]
    cv.imwrite('cut.jpg',cropped)
    cv.imshow('cropped',cropped)
    cv.imshow('foto',img)
def write(x,y,c1,c2,c3):
    cv.putText(img,'Ahmet Enes',(x,y),cv.FONT_HERSHEY_SIMPLEX,2.0,(int(c1),int(c2),int(c3)),3)
def circle(x,y):
    cv.circle(img,(x,y),25,(0,255,0),2)


def rotate(img,angle,rotpoint=None): 
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
def clickevent(event,x,y,flags,param):
    global img
    c1=img[y,x,0]
    c2=img[y,x,1]
    c3=img[y,x,2]
    
    if  event==cv.EVENT_LBUTTONDOWN and flags==cv.EVENT_FLAG_CTRLKEY + cv.EVENT_FLAG_LBUTTON:
        r=cv.selectROI('rec',img)
        print(r)
        rectangle(r[0],r[1],r[2],r[3])
        cv.imshow('foto',img)

    elif flags==cv.EVENT_FLAG_ALTKEY +cv.EVENT_FLAG_LBUTTON and event==cv.EVENT_LBUTTONDOWN:
        write(x,y,c1,c2,c3)
        cv.imshow('foto',img)
    elif flags==cv.EVENT_FLAG_CTRLKEY + cv.EVENT_FLAG_RBUTTON and event==cv.EVENT_RBUTTONDOWN:
        circle(x,y)
        cv.imshow('foto',img)
    elif flags==cv.EVENT_FLAG_ALTKEY + cv.EVENT_FLAG_RBUTTON and event==cv.EVENT_RBUTTONDOWN:
        print('kaydet')
    elif event == cv.EVENT_LBUTTONDOWN and not(flags & cv.EVENT_FLAG_CTRLKEY) and not(flags & cv.EVENT_FLAG_ALTKEY):
        img=rotate(img,10)
        cv.imshow('foto',img)
        
    elif event == cv.EVENT_RBUTTONDOWN and not(flags & cv.EVENT_FLAG_CTRLKEY) and not(flags & cv.EVENT_FLAG_ALTKEY):
        img=rotate(img,-10)
        cv.imshow('foto',img)
img=cv.imread('finephoto.jpg')
resize(800,800)       
cv.setMouseCallback('foto',clickevent)
cv.waitKey(0)
