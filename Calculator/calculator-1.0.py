from tkinter import *
#calculator-1.0
#written by:Sandeep Jha  


class calculator:
	def __init__(self):
		root=Tk()
		root.title("calculator-1.0")
		root.configure(background='black')

		self.var1=StringVar()
		entry= Entry(root, textvariable=self.var1,bd=20,insertwidth=1,font="Times 17 bold",bg="black",fg="white")
		entry.grid(row=0,column=0,columnspan=4)
		entry.bind("<KeyPress>",self.keyPress) #this is keypress event which will block some keyboard input
		entry.focus()
		# keys stores the numbers and some functional symbols which we are gonna display on calculator
		#clr for clearing the screen , del for deleting one by one, off for exting calculator
		keys=["1","2","3","4","5","6","7","8",     
		      "9","0","+","-","clr","*","/","=",
		       "(",")","off","del"]
		i=0
		row=1
		colmn=0
		for key in keys:

			if(i==4):
				row=2
				colmn=0
			if(i==8):
				row=3
				colmn=0
			if(i==12):
				row=4
				colmn=0
			if(i==16):
				row=5
				colmn=0




			if(key=="="):
				button=Button(root,text=key,fg="orange",bg="black",pady=16,padx=16,bd=8,
					command=lambda :self.equals())
				button.grid(row=row,column=colmn,padx=1,pady=1)
			elif(key=="clr"):
				button=Button(root,text=key,fg="orange",bg="black",pady=16,padx=12,bd=6,
					command=lambda :self.clear())
				button.grid(row=row,column=colmn,padx=1,pady=1)
			elif(key=="del"):
				button=Button(root,text=key,fg="orange",bg="black",pady=16,padx=12,bd=6,
					command=lambda: self.delete())
				button.grid(row=row,column=colmn,padx=1,pady=1)
			elif(key=="off"):
				button=Button(root,text=key,fg="orange",bg="black",pady=16,padx=12,bd=6,
					command=quit)
				button.grid(row=row,column=colmn,padx=1,pady=1)
			else:
				button=Button(root,text=key,fg="orange",bg="black",pady=16,padx=16,bd=8,
					command=lambda key=key:self.addChar(key))
				button.grid(row=row,column=colmn,padx=1,pady=1)
			colmn=colmn+1
			i=i+1
		root.mainloop()
	def keyPress(self,event):
		#here we are blocking the entry of unwanted keyboard buttons which are of no use.
		#this will help users avoid unnecessary errors
		#KP is for numeric keynoard buttons
		allowedPress=["KP_0","KP_1","KP_2","KP_3","KP_4","KP_5","KP_6","KP_7","KP_8","KP_9",
		               "1","2","3","4","5","6","7","8","9","0","KP_Divide","slash",
		               "KP_Multiply","KP_Add","KP_Subtract","minus","equal","parenleft",
		               "parenright","period","percent","plus","BackSpace","asterisk","Right",
		               "Left","KP_Decimal"]
		if event.keysym in("Return","KP_Enter"):
			self.equals()
		elif event.keysym not in allowedPress:
			return 'break';
	def clear(self):
		self.var1.set("")
	def equals(self):
		result=""
		try:
			result=eval(self.var1.get())
		except:
			result="error"
		self.var1.set(result)
	def addChar(self,char):
		self.var1.set(self.var1.get()+(str(char)))
	def delete(self):
		self.var1.set(self.var1.get()[0:-1])
	def quit():
		root.quit()

calculator()
