import time
name="sandeep"
class CaseInsensitiveStr(str):
    def __eq__(self, other):
        return str.__eq__(self.lower(), other.lower())
    def __ne__(self, other):
        return str.__ne__(self.lower(), other.lower())
    def __lt__(self, other):
        return str.__lt__(self.lower(), other.lower())
    def __gt__(self, other):
        return str.__gt__(self.lower(), other.lower())
    def __le__(self, other):
        return str.__le__(self.lower(), other.lower())
    def __ge__(self, other):
        return str.__ge__(self.lower(), other.lower())



while 1:
	a = CaseInsensitiveStr(input(""))
	
	local_time=time.asctime(time.localtime(time.time()))
	time_=10*(int(local_time.split()[3][0]))+int(local_time.split()[3][1])


	if(a=='bye'):
		print(">>Bye!")
		if(time_>=6 and time_<=16):
			print(">>Have a good day!")
			print(">>see you next time")
		elif(time_>19 ):
			print(">>Good Night! Nice to talk to you :)")
		elif(time_>16 and time_<=19):
			print(">>Have a pleasant evening")
		break
	if(a=='hi'):
		print(">>Hi!")
		time.sleep(1)
		print(">>how are you?")
	if(a=="what is your name"):
		print(">>tukto")
		print(">>what is your name")
		global name
		name=CaseInsensitiveStr(input(""))
		print('welcome ',name)
	if (a=='i am fine' or a=="fine"):
		print('>>Good!')
	if(a=="fine how are you?" or a=="fine how are you" or a=="fine you say" or a=="fine! you say"):
		print(">>I am fine!")
		time.sleep(0.89)
		print(">>thanks")
	if(a=="how are you" or a=="How do you do" or a=="How you doing" or a=="how are you doing"):
		print(">>I am fine!")
		print(">>thanks")
	if(a=="whats going on" or a=="whats going on"):
		print("nothing much...u say?")
	if(a=="I love you"):
		print(">>thanks! you are so sweet, ",name)
		print(">>i love you too! -:*")
	if(a=="fuck you"):
		print("you know,  you can't!")
		print("shall we talk some good thing or I should leave you alone ",name)
	







