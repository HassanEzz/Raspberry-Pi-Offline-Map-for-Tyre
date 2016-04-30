from Tkinter import*
import MySQLdb
db=MySQLdb.connect('localhost','root','root','map')
curs=db.cursor()
def insert(name,pic):
    try:
        curs.execute("INSERT INTO tyr VALUES('4',",name,",",pic,")")
        db.commit()
        print "Data committed"
    except:
        print"Error:the database is being rolled back"
        db.rollback()
root=Tk()
frame=LabelFrame(root,text="insert")
frame.pack()
var=StringVar()
panel1=Label(frame,textvariable=var)
var.set("Street name:")
panel1.grid(row=0,column=0)
panel2=Label(frame,text="image name:")
panel2.pack(side=LEFT)
ent1=Entry(frame)
ent1.grid(row=0,column=1)
ent2=Entry(frame)
ent2.grid(row=1,column=1)
button=Button(frame,text="insert in the map",bg="white",
              command=lambda:insert(ent1['text'],ent2['text']))
#button.pack()

button.grid(row=2,column=1)
root.grid(200,100,320,100)

root.mainloop()
