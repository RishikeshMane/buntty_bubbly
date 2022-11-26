import tkinter as tk;
#import requests;
#from bs4 import BeautifulSoup;
li=[]

'''
url=''
pagecont=requests.get(url)
soup=BeautifulSoup(pagecont.content,'html.parser')
print(soup)'''

def outfnc(ad):
	return str(ad)

def outfnc2(sb):
	return str(sb)

def outfnc3(ml):
	return str(ml)

def outfnc4(dv):
	return str(dv)

#def errormsg(ms):
#	return str(ms)

def add(ent1,ent2):
	num1=int(ent1)
	num2=int(ent2)
	ad=num1+num2
	lab['text']=outfnc(ad)

def subs(ent1,ent2):
	num1=int(ent1)
	num2=int(ent2)
	sb=num1-num2
	lab['text']=outfnc2(sb)

def mult(ent1,ent2):
	num1=int(ent1)
	num2=int(ent2)
	ml=num1*num2
	lab['text']=outfnc3(ml)

def divi(ent1,ent2):
	num1=int(ent1)
	num2=int(ent2)
	dv=num1/num2
	lab['text']=outfnc4(dv)

'''def outansfuc():
	if add(ent1,ent2)==True:
		outfnc(ad)
		lab['text']=outfnc(ad)'''
	
def out3(st):
	return str(st)


def func3():
	st='3'
	lab['text']=out3(st)

win=tk.Tk()
can=tk.Canvas(win,width=290,height=300)
can.pack()
frm1=tk.Frame(can,bg='black')
frm1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.18)
frm2=tk.Frame(can,bg='black')
frm2.place(relx=0.01,rely=0.2,relwidth=0.98,relheight=0.79)
ent1=tk.Entry(frm1,bg='white')
ent1.place(relx=0.01,rely=0.07,relwidth=0.48,relheight=0.84)
ent2=tk.Entry(frm1,bg='white')
ent2.place(relx=0.5,rely=0.07,relwidth=0.49,relheight=0.84)
but1=tk.Button(frm2,bg='skyblue',bd=7,text='1')
but1.place(relx=0.01,rely=0.02,relwidth=0.24,relheight=0.25)
but2=tk.Button(frm2,bg='skyblue',bd=7,text='2')
but2.place(relx=0.26,rely=0.02,relwidth=0.24,relheight=0.25)
but3=tk.Button(frm2,bg='skyblue',bd=7,text='3',command=lambda:func3())
but3.place(relx=0.51,rely=0.02,relwidth=0.24,relheight=0.25)
but4=tk.Button(frm2,bg='skyblue',bd=7,text='4')
but4.place(relx=0.01,rely=0.28,relwidth=0.24,relheight=0.25)
but5=tk.Button(frm2,bg='skyblue',bd=7,text='5')
but5.place(relx=0.26,rely=0.28,relwidth=0.24,relheight=0.25)
but6=tk.Button(frm2,bg='skyblue',bd=7,text='6')
but6.place(relx=0.51,rely=0.28,relwidth=0.24,relheight=0.25)
but7=tk.Button(frm2,bg='skyblue',bd=7,text='7')
but7.place(relx=0.01,rely=0.55,relwidth=0.24,relheight=0.25)
but8=tk.Button(frm2,bg='skyblue',bd=7,text='8')
but8.place(relx=0.26,rely=0.55,relwidth=0.24,relheight=0.25)
but9=tk.Button(frm2,bg='skyblue',bd=7,text='9')
but9.place(relx=0.51,rely=0.55,relwidth=0.24,relheight=0.25)
but0=tk.Button(frm2,bg='skyblue',bd=7,text='0')
but0.place(relx=0.76,rely=0.02,relwidth=0.23,relheight=0.25)
##for functionality
butpl=tk.Button(frm2,bg='yellow',bd=7,text='+',command=lambda:add(ent1.get(),ent2.get()))
butpl.place(relx=0.76,rely=0.28,relwidth=0.23,relheight=0.12)
butsb=tk.Button(frm2,bg='yellow',bd=7,text='-',command=lambda:subs(ent1.get(),ent2.get()))
butsb.place(relx=0.76,rely=0.41,relwidth=0.23,relheight=0.12)
butml=tk.Button(frm2,bg='yellow',bd=7,text='*',command=lambda:mult(ent1.get(),ent2.get()))
butml.place(relx=0.76,rely=0.55,relwidth=0.23,relheight=0.12)
butdv=tk.Button(frm2,bg='yellow',bd=7,text='/',command=lambda:divi(ent1.get(),ent2.get()))
butdv.place(relx=0.76,rely=0.68,relwidth=0.23,relheight=0.12)
##for final answer functionality
but5=tk.Button(frm2,bg='pink',bd=7,text='=',command=lambda:outansfuc())
but5.place(relx=0.76,rely=0.81,relwidth=0.23,relheight=0.18)
butc=tk.Button(frm2,bg='pink',bd=7,text='C')
butc.place(relx=0.51,rely=0.81,relwidth=0.24,relheight=0.18)
##just labeling
lab=tk.Label(frm2,bg='blue',bd=9)
lab.place(relx=0.01,rely=0.81,relwidth=0.48,relheight=0.16)

win.mainloop()