#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
import mysql.connector as mysql


req = requests.get("https://es.wikipedia.org/wiki/M%C3%A9xico")
soup = BeautifulSoup(req.content,"html.parser")
tablas = soup.find("table",{"class":"wikitable"})
df = pd.read_html(str(tablas))[0]


df = df.drop(columns=1)
df = df.drop(columns=3)
df = df.drop(columns=5)
df=df.drop([0,1])
df.columns=["Estado","Capital","Poblacion"]

lista = []
slista = []

for i in range (2,34):
  slista.append(df.Estado[i])
  slista.append(df.Capital[i])
  slista.append(df.Poblacion[i].replace(u'\xa0', u''))
  lista.append(slista)
  slista=[]


db = mysql.connect(host="localhost",user="root",passwd="ToroRoso")
print(db)
cursor=db.cursor() 


cursor.execute("SHOW DATABASES")

databases=cursor.fetchall()
print(databases)

#Creamos la base de datos 
#cursor.execute("CREATE DATABASE Estados_CGDA")

db = mysql.connect(host="localhost",user="root",passwd="ToroRoso",database="Estados_CGDA")
cursor=db.cursor()

#cursor.execute("CREATE TABLE ESTADOS4(ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, ESTADO VARCHAR(255),CAPITAL VARCHAR(255), POBLACION VARCHAR(255))")

#MUESTRA TODAS LAS TABLAS 

cursor.execute("SHOW TABLES")
tablas=cursor.fetchall()
for tabla in tablas:
    print(tabla)
    
cursor.execute("DESC ESTADOS4")
print(cursor.fetchall())

#Inserta información 


query="INSERT INTO ESTADOS4 (Estado,Capital,Poblacion) VALUES (%s,%s,%s)"
i=0 #Nos dara iteraciones, no se te olvide
for slista in lista:
    values=[(slista[0],slista[1],slista[2])]
    cursor.executemany(query,values)
    db.commit()
    i+=1
    
print("AGREGUE",i,"DATOS NUEVOS")

#Consultando tabla

query="SELECT * FROM ESTADOS4"
cursor.execute(query)
registros=cursor.fetchall()
for registro in registros:
    print(registro)
    
#Muestra los estados con población mayor a 2 millones de habitantes
    
query="SELECT Estado,Capital FROM ESTADOS4 WHERE Poblacion>2000000"
cursor.execute(query)
registros=cursor.fetchall()
for registro in registros:
    print(registro)















