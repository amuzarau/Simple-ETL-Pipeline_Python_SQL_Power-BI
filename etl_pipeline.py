# import kaggle
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files('youvolvedata/employee-salary-data',path='C:/Users/User/Documents/projects/python', unzip=True)

import pandas as pd
import sqlalchemy as odb
from datetime import datetime
df = pd.read_csv("C:/Users/User/Documents/projects/python/emp_salary_data.csv")
#print(df.head(5))
#print(df)
print(df['department'].unique())
df['fna'] = df['first name'].str.isalpha()
df['lna'] = df['last name'].str.isalpha()
df['msn'] = df['monthly salary'].str.isnumeric()
print(df)
print("Raws with alphanumeric data issues")
df2 = df.query('fna == False or lna == False or msn == False')
print(df2)
df['first name'] = df['first name'].str.replace('#','')
df['first name'] = df['first name'].str.replace('$','')
df['last name'] = df['last name'].str.replace('+','')
df['last name'] = df['last name'].str.replace('$','')
df['monthly salary'] = df['monthly salary'].str.replace('&','')
df['monthly salary'] = df['monthly salary'].str.replace(' ','')
df.drop('fna',axis=1,inplace=True)
df.drop('lna',axis=1,inplace=True)
df.drop('msn',axis=1,inplace=True)
print("Raws with alphanumeric data issues fixed")
print("----------------------------------------")
print(df)

#Checking join dates
df['join date2'] = df['join date']
df['join date'] = pd.to_datetime(df['join date'], format="%d-%b-%Y",errors='coerce')
print("Data with invalid join date")
print("----------------------------------------")
df2 = df[df['join date'].isna()]
print(df2)
df = df.dropna()
df.drop('join date2',axis=1,inplace=True)

print("Raws with join date fixed")
print("----------------------------------------")
print(df)

#Checking birth dates
df['birth date2'] = df['birth date']
df['birth date'] = pd.to_datetime(df['birth date'], format="%d-%b-%Y",errors='coerce')
print("Data with invalid birth date")
print("----------------------------------------")
df2 = df[df['birth date'].isna()]
print(df2)
df = df.dropna()
df.drop('birth date2',axis=1,inplace=True)

print("Raws with birth date fixed")
print("----------------------------------------")
print(df)

print("Fix the column headers")
print("----------------------------------------")
df.columns = df.columns.str.replace(' ','_')
print(df)


#Loading the date to Oracle databases
username = "app_user"
password = "appuser12345"
dsn = "localhost:1521/?service_name=xepdb1"
conn_Str = "oracle+cx_oracle://"+username+":"+password+"@"+dsn
print("Connection string used:")
print(conn_Str)
eng = odb.create_engine(conn_Str)
df.to_sql('emp_salary_data', con=eng, if_exists='append', index=False)