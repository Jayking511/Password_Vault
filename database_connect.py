import mysql.connector

def mysql_statement(statement):
    if statement=="create database":
#   Enter the ip address of your database server in "host" field below.
#   Enter the username to login in "user" field below.
#   Enter your database server password in the place of ********** in "passwd" field below.
        try:
            mydb=mysql.connector.connect(host="host", user="user", passwd="**********", database="vault")
            return
        except:
            mydb=mysql.connector.connect(host="host", user="user", passwd="**********")
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE vault")
            print("New Vault created :)")
            mycursor.execute("USE vault")
            mycursor.execute("CREATE table passwords (website varchar(60) PRIMARY KEY, username varchar(60), password varchar(60))")
            return

    mydb=mysql.connector.connect(host="host", user="user", passwd="**********", database="vault")
    mycursor=mydb.cursor()
    statement=statement.replace("table_name", "passwords")
    statement=statement.replace("attribute", "website")
    if statement.startswith("select"):
        mycursor.execute(statement)
        outputstring=""
        for i in mycursor:
            outputstring+=str(i)
        count=0
        l=[]
        site_name=""
        for i in outputstring:
            if i=="\'":
                count+=1
                if count%2==0:
                    l.append(site_name)
                    site_name=""
                continue
            if count%2!=0:
                site_name+=i
        return(l)
    else:
        mycursor.execute(statement)
        mydb.commit()
        return
