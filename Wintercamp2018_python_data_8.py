# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:38:47 2019

@author: shb59
"""

# 주식 데이터 가져오기 
from pandas_datareader import data
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf #anaconda prompt에서 pip ㄱㄱ


yf.pdr_override()

start_date = '2000-1-1' 
end_date = '2019-1-31' 
KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
NAVER = data.get_data_yahoo('035420.KS', start_date, end_date)
CJ=data.get_data_yahoo('001040.KS',start_date,end_date)
print(KIA)
#print(NAVER)
print(KIA.columns)

plt.figure(figsize=(24,12))
plt.plot(KIA['Close'], label='KIA')
plt.plot(NAVER['Close'], label='Naver')
plt.plot(CJ['Close'], label='CJ')
plt.legend(loc=2)

plt.grid()
plt.show()
