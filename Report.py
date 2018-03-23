# -*- coding: utf-8 -*-
#你需要改变Datear来进行不同日期查询，共有3处
#结果将保存在F:/DayRerport下
"""在刷新TABLEAU 前你 需要对excel进行简单的整理，步骤如下：
   1.找到“count”列并将其中的‘nan’进行向上填充
   2.第一个字段的名称重新命名为“daytime”
   3.保存文件
   4.打开同一文件夹下的tableau，
"""

"""
Created on Sat Feb  3 17:19:16 2018

@author: Jianping wu 
"""
import pandas as pd
import numpy as np
import pymysql 
import numpy as np
from dateutil.parser import parse
#选择日期范围和STACTSID
Dateqr=20180322
connect = pymysql.connect(host='********',user='root',db='mysql',password='********',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
sql_Stacts="select * from inter_alarm_records where  date_day =%d  "%(Dateqr)
cursor=connect.cursor()
cursor.execute(sql_Stacts)
df_rc=pd.DataFrame(cursor.fetchall())
df_rc['DateTime']=df_rc['date_day']  +" "+df_rc['time_point']
df_rc['DateTime']=df_rc['DateTime'].map(parse)
df_rc.set_index('DateTime',inplace=True)
print("*"*100)
print("数据读取成功")
connect.close()
#=====================================================================================================
#对报警记录进行每两分钟分割
start=parse('20180322'+"000000")
end=parse('20180322'+'235959')
df_dt=pd.DataFrame(data=[],index=pd.date_range(start=start,end=end,freq='2min'))
df=pd.merge(df_dt,df_rc,how='left',left_index=True,right_index=True)
print('*'*200)

grouped = df.groupby(by='scats_id',as_index=False)
df_group_list=[]                        #这是对每个表计数的计数器列表
for key,dfself in grouped:            #dfself 每个scats表
    dfself  = dfself[~dfself.index.duplicated()] 
    df_group = pd.merge(df_dt,dfself,how = 'left',left_index=True,right_index=True)
   
    df_group_list.append(df_group)
result = pd.concat(df_group_list)


l= ['nan']*len(result)
count = 0
for i in range(len(result)):
    if result['delay_value'][i] >0:
        count+=1
      
    else:
        
        l[i-1] = count
        count = 0
print('程序正在运行中....')

result['count']  = l
result.to_excel(r'F:\DayReport\resultalarm.xlsx')    
print('结果已经保存在F盘下')

#开始作图表
#1.连续报警大于15次路口










#2.不同路口连续报警出现的方向统计



    
    


    
       
    

        
    
    
            
            




