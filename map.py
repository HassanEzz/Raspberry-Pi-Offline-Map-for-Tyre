import MySQLdb
from Tkinter import*
import os
root=Tk()
def img(pic):
        os.system('xdg-open /home/pi/Desktop/Map/%s'%pic)
root.wm_title('map select')
root.geometry('500x800+0+0')
frame=Frame(root)
frame.pack()
db=MySQLdb.connect('localhost','root','root','map')
curs=db.cursor()
curs.execute("SELECT * FROM tyr")
i=0


r0=curs.fetchone()
bt0=Button(frame,text=str(r0[0]),bg='white' ,command=lambda:img(str(r0[1])))
bt0.grid(row=0,column=0)

r1=curs.fetchone()
bt1=Button(frame,text=str(r1[0]),bg='white' ,command=lambda:img(str(r1[1])))
bt1.grid(row=0,column=1)

r2=curs.fetchone()
bt2=Button(frame,text=str(r2[0]),bg='white' ,command=lambda:img(str(r2[1])))
bt2.grid(row=1,column=0)    

r3=curs.fetchone()
bt3=Button(frame,text=str(r3[0]),bg='white' ,command=lambda:img(str(r3[1])))
bt3.grid(row=1,column=1)

r4=curs.fetchone()
bt4=Button(frame,text=str(r4[0]),bg='white' ,command=lambda:img(str(r4[1])))
bt4.grid(row=2,column=0)

r5=curs.fetchone()
bt5=Button(frame,text=str(r5[0]),bg='white' ,command=lambda:img(str(r5[1])))
bt5.grid(row=2,column=1)

r6=curs.fetchone()
bt6=Button(frame,text=str(r6[0]),bg='white' ,command=lambda:img(str(r6[1])))
bt6.grid(row=3,column=0)

r7=curs.fetchone()
bt7=Button(frame,text=str(r7[0]),bg='white' ,command=lambda:img(str(r7[1])))
bt7.grid(row=3,column=1)

r8=curs.fetchone()
bt8=Button(frame,text=str(r8[0]),bg='white' ,command=lambda:img(str(r8[1])))
bt8.grid(row=4,column=0)

r9=curs.fetchone()
bt9=Button(frame,text=str(r9[0]),bg='white' ,command=lambda:img(str(r9[1])))
bt9.grid(row=4,column=1)

r10=curs.fetchone()
bt10=Button(frame,text=str(r10[0]),bg='white' ,command=lambda:img(str(r10[1])))
bt10.grid(row=5,column=0)

r11=curs.fetchone()
bt11=Button(frame,text=str(r11[0]),bg='white' ,command=lambda:img(str(r11[1])))
bt11.grid(row=5,column=1)

r12=curs.fetchone()
bt12=Button(frame,text=str(r12[0]),bg='white' ,command=lambda:img(str(r12[1])))
bt12.grid(row=6,column=0)

r13=curs.fetchone()
bt13=Button(frame,text=str(r13[0]),bg='white' ,command=lambda:img(str(r13[1])))
bt13.grid(row=6,column=1)

r14=curs.fetchone()
bt14=Button(frame,text=str(r14[0]),bg='white' ,command=lambda:img(str(r14[1])))
bt14.grid(row=7,column=0)

r15=curs.fetchone()
bt15=Button(frame,text=str(r15[0]),bg='white' ,command=lambda:img(str(r15[1])))
bt15.grid(row=7,column=1)

r16=curs.fetchone()
bt16=Button(frame,text=str(r16[0]),bg='white' ,command=lambda:img(str(r16[1])))
bt16.grid(row=8,column=0)

r17=curs.fetchone()
bt17=Button(frame,text=str(r17[0]),bg='white' ,command=lambda:img(str(r17[1])))
bt17.grid(row=8,column=1)

r18=curs.fetchone()
bt18=Button(frame,text=str(r18[0]),bg='white' ,command=lambda:img(str(r18[1])))
bt18.grid(row=9,column=0)

r19=curs.fetchone()
bt19=Button(frame,text=str(r19[0]),bg='white' ,command=lambda:img(str(r19[1])))
bt19.grid(row=9,column=1)

r20=curs.fetchone()
bt20=Button(frame,text=str(r20[0]),bg='white' ,command=lambda:img(str(r20[1])))
bt20.grid(row=10,column=0)

r21=curs.fetchone()
bt21=Button(frame,text=str(r21[0]),bg='white' ,command=lambda:img(str(r21[1])))
bt21.grid(row=10,column=1)

r22=curs.fetchone()
bt22=Button(frame,text=str(r22[0]),bg='white' ,command=lambda:img(str(r22[1])))
bt22.grid(row=11,column=0)

r23=curs.fetchone()
bt23=Button(frame,text=str(r23[0]),bg='white' ,command=lambda:img(str(r23[1])))
bt23.grid(row=11,column=1)


db.close()
root.mainloop()

  
