# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:10:15 2019

@author: shb59
"""

import numpy as np

list1=[1,2,3,4,5,6,7,8,9,0]
data=np.array(list1)
print(data.shape)
print(data.dtype) #이거 왜 int32로 나오냠
print(data.size)
print(data)

#datalist=np.arange(0,10,1)
#print(datalist)
#data=np.array(datalist)
#print(data)

#datalist=[[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]]
#data=np.array(datalist)
#print(data.shape)
#print(data.dtype)
#print(data.size)
#print(data)

#np.array np.arange np.ones np.zeros np.empty np.eye np.full

#datalist=[85.5,102.8,155.2,170.7]
#data=np.array(datalist)
#pyunglist=data/3.305
#print(data)
#print(pyunglist) #이거 소수점 자르고싶다ㅠㅠ

#datalist=[0,1,2,3,4,5,6,7,8,9]
#data=np.array(datalist)
#print(data)
#print(data[5])
#print(data[5:8])
#data[3:6]=0
#print(data)

#datalist=[[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]]
#data=np.array(datalist)
#print(data)
#print(data[2])
#print(data[2][1])
#print(data[2,2])
#print(data[:2,1:])
#data[3]=0
#print(data)

#dadtalist=[55,78,96,75,64,85,49,80,77,89]
#data=np.array(dadtalist)
#print(data)
#print(data>=60)
#data[data<60]=60
#print(data)

#kor=np.random.randint(55,100,10)
#eng=np.random.randint(55,100,10)
#mat=np.random.randint(55,100,10)
#print(kor)
#print(eng)
#print(mat)
#avg=(kor+eng+mat)/3
#print(avg)

#datalist=[(86,93,93),(67,90,85),(90,80,70)]
#score=np.array(datalist,dtype=[('kor','i4'),('eng','i4'),('mat','i4')])
#print(score)
#print(score['eng'])
#print(score[1]['kor'])

#numbers1=np.random.randint(1,100,10)
#numbers2=np.random.randint(1,100,10)
#compare=np.array(numbers1>numbers2)
#largers=np.where(compare,numbers1,numbers2)
#print(numbers1)
#print(numbers2)
#print(compare)
#print(largers)

#numbers=np.random.randint(50,100,10)
#score=np.where(numbers>=70,'Pass','Fail')
#print(numbers)
#print(score)

#numbers=np.random.randint(1,100,10)
#print(numbers)
#print(numbers.max())
#print(numbers.min())
#print(numbers.sum())
#print(numbers.mean())
#print(numbers.std())
#print(numbers.cumsum())
#numbers.sort()
#print(numbers)

#d=np.array([5,0])
#e=np.array([-5,3])
#f=d+e
#print(f)

#points=np.arange(-5,5,1)
#print(points)
#points=np.arange(-5,5,0.1)
#print(points)
#points=np.arange(-5,5,0.05)
#print(points)

#points=np.linspace(-5,5,num=11)
#print(points)
#points=np.linspace(-5,5,num=10,endpoint=False)
#print(points)
#points=np.linspace(-5,5,21)
#print(points)

##not complete
#from random import randint,choice
#import string
#f=open("numdata3.txt","w")
#for i in range(100):
#    randomstr=''.join(choice(string.ascii_uppercase) for _ in range(3))
#    f.write("%s,%d,%d,%d\n"%randomstr,randint(50,100),randint(50,100),randint(50,100))
#    #f.write("%d %d %d\n"%(randint(50,100),randint(50,100),randint(50,100)))
#f.close()

##숫자만 존재
#scores=np.genfromtxt('numdata1.txt',names=('KOR','ENG','MAT'))
#print(scores)
#
##숫자+문자
#scores=np.genfromtxt('numdata2.txt',names=('Name','KOR','ENG','MAT'),dtype=None)
#print(scores)
#
##Header 존재
#scores=np.genfromtxt
