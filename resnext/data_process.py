# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:47:20 2021

@author: jinghanxu
"""

import os
import cv2
import numpy as np

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img

path = 'D:/Files/competition/mindspore/all/all/test'
new = 'D:/Files/competition/mindspore/all/all/test2'
filelist = os.listdir(path)
#with open (datafile, 'w') as f:
for i in filelist:
    p = os.path.join(path, i)
    s = os.listdir(p)
    k = 0
    e=os.path.join(new, i)
    if not os.path.exists(e):
        os.mkdir(e)
    print(e)
    o=0
    for j in s:
        t = os.path.join(p, j)
        image = cv_imread(t)
        k = os.path.join(e, str(o)+ '.jpg')
        cv2.imencode(".jpg", image)[1].tofile(k)
        o +=1
        #cv2.imwrite(k, image)
        