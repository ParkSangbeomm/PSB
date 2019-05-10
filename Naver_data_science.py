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


#donghwa=df[df['itemname'].isin(['바른손'])]
#donghwa.to_csv('bareunson.csv', encoding='ms949')
bareunson = pd.DataFrame(pd.read_csv("bareunson.csv",encoding='euc-kr'))
bareunson['close_val'].plot(figsize=(15,6),label='바른손')
#donghwa=df[df['itemname'].isin(['모나리자'])]
#donghwa.to_csv('monarisa.csv', encoding='ms949')
#monarisa = pd.DataFrame(pd.read_csv("monarisa.csv",encoding='euc-kr'))
#monarisa['close_val'].plot(figsize=(15,6),label='모나리자')
#donghwa=df[df['itemname'].isin(['국보'])]
#donghwa.to_csv('gukbo.csv', encoding='ms949')
#gukbo = pd.DataFrame(pd.read_csv("gukbo.csv",encoding='euc-kr'))
#gukbo['close_val'].plot(figsize=(15,6),label='국보')
#donghwa=df[df['itemname'].isin(['조광페인트'])]
#donghwa.to_csv('jkpaint.csv', encoding='ms949')
#jkpaint = pd.DataFrame(pd.read_csv("jkpaint.csv",encoding='euc-kr'))
#jkpaint['close_val'].plot(figsize=(15,6),label='조광페인트')
#donghwa=df[df['itemname'].isin(['우리들휴브레인'])]
#donghwa.to_csv('wurideul.csv', encoding='ms949')
#wurideul = pd.DataFrame(pd.read_csv("wurideul.csv",encoding='euc-kr'))
#wurideul['close_val'].plot(figsize=(15,6),label='우리들휴브레인')
#donghwa=df[df['itemname'].isin(['국일신동'])]
#donghwa.to_csv('gukilsindong.csv', encoding='ms949')
#gukilsindong = pd.DataFrame(pd.read_csv("gukilsindong.csv",encoding='euc-kr'))
#gukilsindong['close_val'].plot(figsize=(15,6),label='국일신동')
#donghwa=df[df['itemname'].isin(['SG세계물산'])]
#donghwa.to_csv('sgmulsan.csv', encoding='ms949')
#sgmulsan = pd.DataFrame(pd.read_csv("sgmulsan.csv",encoding='euc-kr'))
#sgmulsan['close_val'].plot(figsize=(15,6),label='SG세계물산')
#donghwa=df[df['itemname'].isin(['셀루메드'])]
#donghwa.to_csv('selru.csv', encoding='ms949')
#selru = pd.DataFrame(pd.read_csv("selru.csv",encoding='euc-kr'))
#selru['close_val'].plot(figsize=(15,6),label='셀루메드')
#donghwa=df[df['itemname'].isin(['비엠티'])]
#donghwa.to_csv('bmt.csv', encoding='ms949')
#bmt = pd.DataFrame(pd.read_csv("bmt.csv",encoding='euc-kr'))
#bmt['close_val'].plot(figsize=(15,6),label='비엠티')
#donghwa=df[df['itemname'].isin(['우리들제약'])]
#donghwa.to_csv('wurideuljeyak.csv', encoding='ms949')
#wurideuljeyak = pd.DataFrame(pd.read_csv("wurideuljeyak.csv",encoding='euc-kr'))
#wurideuljeyak['close_val'].plot(figsize=(15,6),label='우리들제약')
#donghwa=df[df['itemname'].isin(['이구산업'])]
#donghwa.to_csv('29sanup.csv', encoding='ms949')
#e9sanup = pd.DataFrame(pd.read_csv("29sanup.csv",encoding='euc-kr'))
#e9sanup['close_val'].plot(figsize=(15,6),label='이구산업')
#donghwa=df[df['itemname'].isin(['포비스티앤씨'])]
#donghwa.to_csv('pobisdnc.csv', encoding='ms949')
#pobisdnc = pd.DataFrame(pd.read_csv("pobisdnc.csv",encoding='euc-kr'))
#pobisdnc['close_val'].plot(figsize=(15,6),label='포비스티앤씨')
#donghwa=df[df['itemname'].isin(['화인베스틸'])]
#donghwa.to_csv('hwain.csv', encoding='ms949')
#hwain = pd.DataFrame(pd.read_csv("hwain.csv",encoding='euc-kr'))
#hwain['close_val'].plot(figsize=(15,6),label='화인베스틸')
#donghwa=df[df['itemname'].isin(['서희건설'])]
#donghwa.to_csv('seohi.csv', encoding='ms949')
#seohi = pd.DataFrame(pd.read_csv("seohi.csv",encoding='euc-kr'))
#seohi['close_val'].plot(figsize=(15,6),label='서희건설')
#donghwa=df[df['itemname'].isin(['DSR'])]
#donghwa.to_csv('dsr.csv', encoding='ms949')
#dsr = pd.DataFrame(pd.read_csv("dsr.csv",encoding='euc-kr'))
#dsr['close_val'].plot(figsize=(15,6),label='DSR')
#donghwa=df[df['itemname'].isin(['유성티엔에스'])]
#donghwa.to_csv('yuseongtns.csv', encoding='ms949')
#yuseongtns = pd.DataFrame(pd.read_csv("yuseongtns.csv",encoding='euc-kr'))
#yuseongtns['close_val'].plot(figsize=(15,6),label='유성티엔에스')

#donghwa=df[df['itemname'].isin(['씨아이테크'])]
#donghwa.to_csv('citech.csv', encoding='ms949')
#citech = pd.DataFrame(pd.read_csv("citech.csv",encoding='euc-kr'))
#citech['close_val'].plot(figsize=(15,6),label='씨아이테크')
#donghwa=df[df['itemname'].isin(['남화토건'])]
#donghwa.to_csv('namhwa.csv', encoding='ms949')
#namhwa = pd.DataFrame(pd.read_csv("namhwa.csv",encoding='euc-kr'))
#namhwa['close_val'].plot(figsize=(15,6),label='남화토건')


#donghwa=df[df['itemcode'].isin(['000020'])]
#donghwa['close_val'].plot(figsize=(15,6),label='동화')
#newbotec = pd.DataFrame(pd.read_csv("newbotec.csv",encoding='euc-kr'))
#newbotec['close_val'].plot(figsize=(15,6),label='뉴보텍')
#newbotec['close_val'].plot(figsize=(15,6),label='뉴보텍')
plt.axvspan(190, 194, facecolor='gray', alpha=0.5)
plt.xticks([0,50,100,150,200,250,300],['2015-01-07','2015-08-03','2016-03-10','2016-10-27','2017-06-09','2018-01-25','2018-09-11'])

plt.xlabel("Date")
plt.ylabel("Close_val")
plt.legend()
plt.show()


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
