# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:19:50 2019

@author: shb59
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

datas = pd.read_csv("st_data_itemChargeFull.tsv", sep='\t' )
datas_goodsForeign = pd.read_csv("st_data_goodsForeign.tsv", sep='\t')
datas_foreignCharge = pd.read_csv("st_data_foreignCharge.tsv", sep='\t')
df = pd.DataFrame(datas)
df_goods=pd.DataFrame(datas_goodsForeign)
df_foreignCharge=pd.DataFrame(datas_foreignCharge)

#donghwa=df[df['itemcode'].isin(['000020'])]
#dh=donghwa[['date','close_val']]
##donghwa=donghwa.drop(0,axis=1)
#print(dh)
#plt.figure(figsize=(24,12))
#plt.plot([dh.date],[dh.close_val])
##plt.gird()
#plt.show()


#kr_motors=df[df['itemcode'].isin(['000040'])]
#
##print(kr_motors)
#plt.figure(figsize=(24,12))
#plt.plot(donghwa['close_val'], label='DongHwa')
#plt.plot(kr_motors['close_val'], label='KR_motors')
##plt.xlim(20150101,20181230)
#plt.legend(loc=2)
#plt.grid()
#plt.show()


#print(df_goods.drop_duplicates(["itemname"]))
#print(df_foreignCharge.drop_duplicates(["itemname"])) #중복없이 itemname 출력
#print(df)
#DataFrame.from_csv('c:/~/trainSetRel3.txt', sep='\t') #tsv 읽어오는법
#dataset = pd.read_csv("train.tsv", delimiter='\t', header=0) #tsv 읽어오는법
#print(datas.head())
#print(df.drop_duplicates(["itemname"])) #중복없이 보는법
#print(df[['itemcode','itemname']]) # itemcode 와 itemname만 따로 빼서 indexing하는것
#df_dh=df[df['itemcode'].isin(['000020', '000040'])] #itemcode가 저거인거만 뽑아서 보기
#print(df_dh)
#df_out = df.drop_duplicates(["itemname"]) #중복없이 보는법
#df_out.to_csv('df_out.csv', encoding='ms949') #csv파일로 내보내기 한글 깨짐 오류 방지
#print(df_out[df_out.market == 'KONEX'])


#df_dh_graph = df_dh['close_val'].plot(figsize=(15,6))
#plt.xticks[["2015","2016","2017"]]
#plt.xlabel("Date")
#plt.legend()
#plt.show()

#plt.figure(figsize=(15,15))
#plt.scatter(df['])

##이렇게 하면 x축 시간인척 하면서 출력가능
#df = pd.DataFrame(datas)
#donghwa=df[df['itemcode'].isin(['000020'])]
#donghwa['close_val'].plot(figsize=(15,6))
#plt.xticks([0,50,100,150,200,250,300],['2015-01-01','2015-06-01','2016-01-01','2016-06-01','2017-01-01','2017-06-01','2018-01-01','2018-06-01'])
#plt.legend()
#plt.show()


#------------------------------시작--------------------------
#대선테마주를 대선주자별로 저장하고 싶지만 사실 필요없어
#왜냐하면 어차피 시각화는 하나이기 떄문에 그냥 이번에 대통령인 문재인것만 하자 그 중에서도 예외가 있다면 그것만 하면 좋을텐데



https://stml.tistory.com/26
https://nittaku.tistory.com/111
https://blessingdev.wordpress.com/2018/11/15/matplotlib-%EC%82%AC%EC%9A%A9%EA%B8%B0-3%EC%B6%95-%ED%8E%B8%EC%A7%91%ED%95%98%EA%B8%B0/
http://pythonstudy.xyz/python/article/407-Matplotlib-%EC%B0%A8%ED%8A%B8-%ED%94%8C%EB%A1%AF-%EA%B7%B8%EB%A6%AC%EA%B8%B0
https://medium.com/@peteryun/python-matplotlib-%EA%B8%B0%EB%B3%B8-6e23e5fd2f16
https://zzsza.github.io/development/2018/08/24/data-visualization-in-python/
