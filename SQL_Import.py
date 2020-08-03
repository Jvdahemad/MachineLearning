 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
np.arange(3,5)
import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                          'Server={DESKTOP-P1DC346};'
                          'Database={AdventureWorks};'
                          'Trusted_Connection=yes;')
cursor=conn.cursor()

cursor.execute('''select * from [HumanResources].[Employee] T1
               join [HumanResources].EmployeeDepartmentHistory T2
               on T1.BusinessEntityID=t2.BusinessEntityID
               join [HumanResources].[Department] T3
               on T2.DepartmentID=t3.DepartmentID''')

sql='''select * from [HumanResources].[Employee] T1
               join [HumanResources].EmployeeDepartmentHistory T2
               on T1.BusinessEntityID=t2.BusinessEntityID
               join [HumanResources].[Department] T3
               on T2.DepartmentID=t3.DepartmentID'''
data=[]

for row in cursor:
    data.append(row)
    
data_arr=np.array(data)


Data=pd.read_sql(sql,conn,)
Data.columns

