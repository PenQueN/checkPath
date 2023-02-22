import csv                      #เรียกใช้ library csv
import os                       #เรียกใช้ library os
from tkinter import *           #เรียกใช้ library tkinter
from tkinter import ttk         #theme of tk
from tkinter import messagebox  #เรียกใช้ messagebox
from tkinter import filedialog  #เรียกใช้ dialog
from datetime import datetime   #เรียกใช้ library เกี่ยวกับเวลา

#################### Function #######################
def writeCSV(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file: #ต้องใส่ newline  เพราะไม่งั้นแต่ละบรรทัดจะมีเว้นว่าง
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist

def readCSV():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data =list(fr)
    return data


def get_filepaths(directory):
    #credit : https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        FB2 = LabelFrame(GUI,width=700,text='File in Folder') 
        FB2.place(x=10,y=90) #Position LabelFrame

        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.            
            myLabe1 = Label(FB2,width=60,text=filename,fg="red",font=20,bg="yellow").pack()
            


    return file_paths  # Self-explanatory.

def path():
    data = readCSV()

    current_dir = os.getcwd() #get current path
    tempdir = filedialog.askdirectory(parent=GUI, initialdir=current_dir, title='Please select a directory')
    get_filepaths(tempdir)
    et1.delete(0,END) #ทำการเคลีย Textbox ก่อนการรับค่า,  0 หมายถึง index เริ่มต้นที่ตัวแรก end หมายถึงตัวสุดท้าย
    et1.insert(0,tempdir) #insert นำค่าเข้าที่ Textbox
    t = datetime.now().strftime('%Y%m%d-%H:%M:%S') #กำหนด format เวลาเก็บลงตัวแปร t

    if len(data) == 0: 
        cntApp = 0  #ในกรณีที่ไม่มีข้อมูลใน CSV file  กำหนดให้ count app = 0
    elif len(data) > 0:
        cntApp = int(data[-1][0])
        cntApp += 1

    GUI.title("Location Program  ==> จำนวนครั้งที่เลือก Path = " + str(cntApp) + " ครั้ง  <==") 

    text = [cntApp,tempdir,t] #[เวลา,ข้อมูลที่ได้จากการกรอก]
    writeCSV(text) #บันทึกลง CSV

################# Title Program ##################

data = readCSV()

if len(data) > 0:              #กรณีที่มีข้อมูลในไฟล์ CSV ถึงจะทำ
    readPath = data[-1][1]      #อ่านชื่อ path
    cntApp = int(data[-1][0])
if len(data) == 0:       
    cntApp = 0

GUI = Tk() 
GUI.title("Location Program  ==> จำนวนครั้งที่เลือก Path = " + str(cntApp) + " ครั้ง  <==") 
GUI.geometry('630x300+500+200') #size program (600x100) and location windows (+500+200)

FB1 = LabelFrame(GUI,text='Path') 
FB1.place(x=10,y=10) #Position LabelFrame

et1 = ttk.Entry(FB1,width=80) #สร้าง Textbox อยู่ภายใต้ Frame
et1.grid(row=0,column=0,padx=10,pady=10) #grid position โดยใช้ row , column สะดวกในการวางตำแหน่ง

if len(data) >= 1: et1.insert(0,readPath)

B2 = ttk.Button(FB1,text='Browse',command=path) #สร้างปุ่ม Button อยู่ภายใต้ Frame
B2.grid(row=0,column=1,padx=10,pady=10) #padx , pady ใช้สำหรับ frame

GUI.mainloop() #วนทำงานไปเรื่อย ๆ