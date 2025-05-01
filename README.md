# Simple-ETL-Pipeline_Python_SQL_Power-BI
My first ETL Pipeline: dataset from kaggle.com --> Python (pandas, sqlalchemy libraries) -->SQL (Oracle Database) --> Power BI

Dataset (in CSV format) from kaggle.com:  https://www.kaggle.com/datasets/youvolvedata/employee-salary-data

Problem: 
A medium sized pharmaceutical company with little over 500 employees has been missing their yearly profit target for the last 3 years. They want to analyze the workforce structure and salary disbursements to make sure they are not overpaying in salary.

Assumptions:
1) Administrative Departments like HR, Legal, Finance should not have employee count over 5% of the total workforce
2) Q&A and R&D should be 10%-15% of the total workforce 
3) Hight Paid Employee (HPE) limit 15%-20% of the total workforce
4) Medium Paid Employee (MPE) limit 60%-70% of the total workforce

