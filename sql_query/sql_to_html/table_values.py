import mysql.connector as db
import os
import pandas as pd

conn=db.connect(host="<IP_OF_DB>"
                ,username="python"
                ,password="Python_123"
                ,database="sanctuary")

#Fetch data
cmd="select * from monsters"
cursor=conn.cursor()
cursor.execute(cmd)
data=cursor.fetchall()
# print(data)

#Manipulate data
df=pd.DataFrame()
for x in data:
    df2=pd.DataFrame(list(x)).T
    df=pd.concat([df,df2])

df.to_html('templates/data.html')
