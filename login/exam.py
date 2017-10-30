
admin_passwd={
		"houyizhong":"137116010",
		"root":"root"
		}

class Person:
	def __init__(self):
		self.username=input("username--->")
		self.password=input("password--->")

	def judge(self,name,passwd):
			if passwd != admin_passwd[name]:
                                global count
                                count += 1

                                print("passwd-miss")
			else:
                                print("passwd-hit")
                                return 1

count=0


while  count < 3:

	my=Person()
	result=my.judge(my.username,my.password)
	if result == 1:
		break
else:
	print("You are in blacklist!")
