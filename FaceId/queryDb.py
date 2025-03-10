import mysql.connector
import datetime
from tkinter import messagebox
import time
# ham Connection toi database
def connectdatabase():
    connection=mysql.connector. connect(
    host="localhost",
    database="FaceId",
    user= "root",
    password="123456"
    )
    return connection
# ham insert neu id nhap vao chua co trong database va update neu trong database da co id
def insertOrUpdate(id, name) :
    con=connectdatabase()
    query = "select * from people where id ="+str(id)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor . fetchall()
    isRecordExit = 0
    for row in records:
        isRecorrdExit = 1
    if (isRecorrdExit == 0):
        query = "insert into people (id, name) values (%s.%s)"
        cursor.execute(query,(id, name))
    else:
        query = "update people set name = %s where id = %s"
        cursor.execute(query,(name,id))
    con.commit()
    con.close()
    cursor.close()
# ham su ly checkout and checkIn
def checkInAndCheckOut(idPeople):
    check : bool
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur_date = datetime.datetime.now() .strftime('%Y-Xm-%d')
    con=connectdatabase( )
    # truy van de lay ra data
    query = "select * from attendance where idPeople ="+str(idPeople)+ " and date(timeCheckIn) = '"+cur_date+"'";
    cursor=con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    isRecordExit = 0
    # neu cau query tren co du lieu thi gan isRecorrExit bang 1
    for row in records:
        isRecorrdExit = 1
    # check neu isRecorrdExit -- @ thi tuc la id Ngubi dung trong ngay hian tai chua co trong database thi minh Insert no vao db
    if (isRecorrdExit == 0):
        query - "insert into attendance (idPeople, timeCheckIn, timeCheckout) values (%s,xs,Xs)"
        cursor.execute(query, (idPeople, cur_time, None))
        check - True
    # nou isRecorrdExit - 1 thi minh sa tinh la thoi gian checkout
    else:
        query = "update attendance set timecheckOut = %s where idPeople = %s"
        cursor.execute(query, (cur_time, idPeople))
        check=False
    con.commit ()
    con.close()
    cursor.close()
    return check
