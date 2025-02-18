import mysql.connector
"""
mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = ""
)


#print(mydb)

mycursor = mydb.cursor()

#query = "create database mydatabase"
query = "show databases"

mycursor.execute(query)

for db in mycursor:
    print(db)
"""
mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)
mycursor = mydb.cursor()

def creaTabella():
    query ="create table clienti(id int auto_increment primary key, nome varchar(100), indirizzo varchar(100))"
    mycursor.execute(query)

def inserisciValori():
    query = "insert into clienti(nome, indirizzo) values (%s,%s)"
    #val = ("giovanni","via milano")
    val = [("alfredo","via torino"),
    ("antonio","via napoli"),
    ("giovanni","via milano")]
    #mycursor.execute(query,val)
    mycursor.executemany(query,val)
    mydb.commit()
    print(mycursor.rowcount, "righe inserite!")

def leggiValori():
    query = "select * from clienti"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for riga in myresult:
        print(riga)

def leggiValore():
    query = "select * from clienti"
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    print(myresult)

def eliminaValore(val):
    query = "delete from clienti where id = %s"
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "righe eliminate!")

def aggiornaValore(val):
    query = "update clienti set nome = %s where id = %s"
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "righe modificate!")

def aggiornaValori(val):
    query = "update clienti set nome = %s where id = %s"
    mycursor.executemany(query,val)
    mydb.commit()
    print(mycursor.rowcount, "righe modificate!")

#aggiornaValore(("Tommaso",2))
piuValori =[("mimmo",2),("marco",5)]
#aggiornaValori(piuValori)
leggiValori()
