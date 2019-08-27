import smtplib
import re
import os
from datetime import date, timedelta

def sendmail(server, email, password, port, destinatario, data_envio, data_incidente, qtd_faturas_enviadas, qtd_faturas_incidente):
    subject = 'Your subject'
    to = destinatario
    sender = 'noreply@dominio.com.br'
    smtpserver = smtplib.SMTP(server,port)
    user = email
    password = password
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, password)
    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    message = header + f'\n Prezados, \n Faturas enviadas -> Data: {data_envio} | Qtd: {qtd_faturas_enviadas}'
    smtpserver.sendmail(sender, to, message)
    print(message)
    smtpserver.close()
    print('Envio realizado com sucesso !')
    
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

#---------------------------------------------------------------------------------------------------------------------------

def conectar_BD(server, database, username, password):
    import pyodbc
    import re
    
    con1 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    con2 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    
    cursor1 = con1.cursor()
    cursor2 = con2.cursor()
    
    cursores = [cursor1, cursor2]
    
    #print('Conexão realizada com sucesso !')
    return cursores

def formatString2(string):
    import re
    # Usei REGEX para conseguir retirar os caracteres indesejados e criar um elemento válido para comparações futuras
    formatedArray = " ".join(re.findall('[a-zA-Z-.@_]+', str(string)))
    return formatedArray

def formatString(string):
    import re
    # Usei REGEX para conseguir retirar os caracteres indesejados e criar um elemento válido para comparações futuras
    formatedArray = " ".join(re.findall('[a-zA-Z-.@_,,0-9]+,', str(string)))
    return formatedArray

def encontrar_Emails(string):
    import re
    emails = formatString(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", string))
    return emails

cursor = conectar_BD('ServerName','DatabaseName','username','password')

enviados = ("consulta query")


n_enviados = ("consulta query")

cursor[0].execute(enviados)
cursor[1].execute(n_enviados)

emails = ['lista com emails']

enviados = []
n_enviados = []

for row in cursor[0]:
    enviados.append(row)


for row in cursor[1]:
    n_enviados.append(row)

today = date.today() - timedelta(1)
qtd_enviados = enviados[0][0:1]
qtd_n_enviados = n_enviados[0][0:1]

MAIL_USERNAME = ("youremail@dominio.com.br")
MAIL_PASSWORD = ("yourpassword")
MAIL_SERVER = ("smtp.gmail.com")
MAIL_PORT = (587)
MAIL_DATA_ENVIO = today.strftime("%d/%m/%Y")
MAIL_DATA_INCIDENTE = today.strftime("%d/%m/%Y")
MAIL_QTD_FATURAS1 = formatString(qtd_enviados)
MAIL_QTD_FATURAS1 = MAIL_QTD_FATURAS1.replace(',','')
MAIL_QTD_FATURAS2 = formatString(qtd_n_enviados)


sendmail(MAIL_SERVER, MAIL_USERNAME, MAIL_PASSWORD, MAIL_PORT, emails[0], MAIL_DATA_ENVIO, MAIL_DATA_INCIDENTE, MAIL_QTD_FATURAS1, MAIL_QTD_FATURAS2)