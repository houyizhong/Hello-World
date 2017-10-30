#-*- coding:utf-8 -*-
#version3.0
#owner:houyizhong

import getpass
#create the list and dict
admin_passwd={}
blacklist=[]

#read admin file
admin_file=open("admin.txt","r")
admin_list=admin_file.readlines()
admin_file.close()

#read admin username and password
for i in range(len(admin_list)):
	admin_parts=admin_list[i]
	admin_raw=admin_parts.strip()
	admin_part=admin_raw.split(':')
	name=admin_part[0]
	passwd=admin_part[1]
	admin_passwd[name]=passwd


#read blacklist file
blacklist_file=open("blacklist.txt","r")
blacklist_raw=blacklist_file.readlines()
blacklist_file.close()

#read blacklist username
for i in range(len(blacklist_raw)):
	blacklist_value=blacklist_raw[i]
	blacklist.append(blacklist_value.strip())

count=0
old_name=""

while count < 3:
	username=input("username:")
	if username != old_name:
		count = 0
	passwd=getpass.getpass("passwd:")
	old_name=username
	
	if username not in admin_passwd:
		print ("Sorry ,you account is not exist!")
		continue
	elif username in blacklist:
		print ("Sorry ,you are in the blacklist!")
		exit()
	else:
		if passwd != admin_passwd[username]:
			count += 1
			print("Sorry,you password is wrong.")
		else:
			print ("Welcome!{0}".format(username))
			break
else:
	print ("You are in blacklist now!")
	blacklist_file=open("blacklist.txt","a")
	blacklist_file.write("{0}\n".format(username))
	blacklist_file.close()
	exit()
