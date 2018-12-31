import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03956922'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1308
    
    missing_img = cv2.imread('nothing_here.png',0)
    
    if not os.path.exists('neg_raw'):
        os.makedirs('neg_raw')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg_raw/"+str(pic_num)+".jpg")
            img = cv2.imread("neg_raw/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            if img.shape == missing_img.shape and not(np.bitwise_xor(missing_img, img).any()):
                print('Bad Image')
            else:
                cv2.imwrite("neg_raw/"+str(pic_num)+".jpg",img)
                pic_num += 1
            
        except Exception as e:
            print(str(e))

def resize_imgs_and_create_descriptor_file():
    if not os.path.exists('neg'):
        os.makedirs('neg')
    
    for i in range(1,2001):
        img = cv2.imread('neg_raw/'+str(i)+'.jpg')
        resized_img = cv2.resize(img, (250,250))
        cv2.imwrite('neg/'+str(i)+'.jpg',resized_img)
        
        line = 'neg/'+str(i)+'.jpg\n'
        with open('bg.txt','a') as f:
            f.write(line)
            
#store_raw_images()
resize_imgs_and_create_descriptor_file()