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
