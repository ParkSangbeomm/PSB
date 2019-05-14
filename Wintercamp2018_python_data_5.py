# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:12:31 2019

@author: shb59
"""
##맨땅에 파이썬 . 이거 쓰명...음 힘듬
#input_file="p_20180930.csv"
#output_file="p_20180930.txt"
#
#filereader=open(input_file,'r',newline='')
#filewriter=open(output_file,'w',newline='')
#
#header=filereader.readline()
#header=header.strip()
#header_list=header.split(',')
#print(header_list)
#filewriter.write('/'.join(header_list)+'\n')
#for row in filereader:
#    row = row.strip()
#    row_list = row.split(',')
#    print(row_list)
#    filewriter.write('/'.join(row_list)+'\n')
#filereader.close()
#filewriter.close()



##csv로 ㅇㅇ
#import csv
#
#input_file="p_20180930.csv"
#output_file="p_20180930_2.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader=csv.reader(csv_in_file,delimiter=',')
#filewriter=csv.writer(csv_out_file,delimiter='/')
#for row_list in filereader:
#    filewriter.writerow(row_list)
#csv_in_file.close()
#csv_out_file.close()



##pandas로 ㅇㅇ
#import pandas as pd
#
#input_file="rep_20180930.txt"
#output_file="p_20180930_3.txt"
#
#data_frame=pd.read_csv(input_file)
#print(data_frame)
#data_frame.to_csv(output_file, index=False)



##csv로하는데 엑셀로치면 필터링하는법
#import csv
#
#input_file="p_20180930.csv"
#output_file="p_20180930_4.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader=csv.reader(csv_in_file,delimiter=',')
#filewriter=csv.writer(csv_out_file,delimiter='/')
#header=next(filereader)
#filewriter.writerow(header)
#for row_list in filereader:
#    ptype=str(row_list[3]).strip() #빈칸없애는거임 strip()
#    psize=str(row_list[6]).replace(',','')
#    if ptype=='노상' and int(psize)>30:
#        filewriter.writerow(row_list)
#csv_in_file.close()
#csv_out_file.close()



##pandas에서 처리할때 엑셀로치면 필터링하는법
#import pandas as pd
#
#input_file="rep_20180930.txt"
#output_file="p_20180930_5.txt"
#
#data_frame=pd.read_csv(input_file)
#
#data_frame['주차구획수']=data_frame['주차구획수'].astype(float)
#my_condition=data_frame.loc[(data_frame['주차장유형'].str.contains('노상'))&(data_frame['주차구획수']>30),:]
#my_condition.to_csv(output_file,index=False)



##pandas에서 처리할때 _2
#import pandas as pd
#
#input_file="rep_20180930.txt"
#output_file="p_20180930_6.txt"
#
#data_frame=pd.read_csv(input_file)
#
#my_pattern=data_frame.loc[data_frame['소재지도로명주소'].str.startswith("경상북도 포항시 북구"),:]
#my_pattern.to_csv(output_file,index=False)



####포항시 인구정보 통계
##csv사용해서 필터링
#import csv
#important_dates=['2010.01','2011.01']
#input_file="p_20180630.csv"
#output_file="p_20180630_1.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader=csv.reader(csv_in_file,delimiter=',')
#filewriter=csv.writer(csv_out_file,delimiter='/')
#header=next(filereader)
#filewriter.writerow(header)
#for row_list in filereader:
#    a_date=row_list[0]
#    if a_date in important_dates:
#        filewriter.writerow(row_list)
#csv_in_file.close()
#csv_out_file.close()


##pandas사용해서 필터링
#import pandas as pd
#important_dates=['2010.01','2011.01']
#input_file="rep_20180630.txt"
#output_file="p_20180630_2.txt"
#
#data_frame=pd.read_csv(input_file)
#
#my_set=data_frame.loc[data_frame['년월'].isin(important_dates),:]
#my_set.to_csv(output_file,index=False)


##csv로 한국남녀만 출력
#import csv
#my_columns=[0,1,2]
#input_file="p_20180630.csv"
#output_file="p_20180630_3.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#header=next(filereader)
#for row_list in filereader:
#    row_list_output=[]
#    for index_value in my_columns:
#        row_list_output.append(row_list[index_value])
#    filewriter.writerow(row_list_output)
#csv_in_file.close()
#csv_out_file.close()


##pandas로 한국남녀만 출력
#import pandas as pd
#
#input_file="rep_20180630.txt"
#output_file="p_20180630_4.txt"
#
#data_frame=pd.read_csv(input_file)
#my_columns=[0,1,2]
#my_index=data_frame.iloc[:,my_columns]
#my_index.to_csv(output_file,index=False)


##csv로해서 위에를 012안하고 일일이 부르기
#import csv
#my_columns=['년월',' 한국인남 ',' 한국인여 ']
#my_columns_index=[]
#input_file="p_20180630.csv"
#output_file="p_20180630_5.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#header=next(filereader)
#for index_value in range(len(header)):
#    if header[index_value] in my_columns:
#        my_columns_index.append(index_value)
#filewriter.writerow(my_columns)
#for row_list in filereader:
#    row_list_output=[]
#    for index_value in my_columns_index:
#        row_list_output.append(row_list[index_value])
#    filewriter.writerow(row_list_output)
#csv_in_file.close()
#csv_out_file.close()



#import pandas as pd
#
#input_file="rep_20180630.txt"
#output_file="p_20180630_6.txt"
#
#data_frame=pd.read_csv(input_file)
#my_columns=['년월',' 한국인남 ',' 한국인여 ']
#my_data=data_frame.loc[:,my_columns]
#my_data.to_csv(output_file,index=False)
