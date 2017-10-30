import sys

file=sys.argv[1]
string=raw_input('Enter search string:')
new_string=raw_input('Enter repalce string:')
f=open(file,'r+')
while True:
	x=f.tell()
	data=f.readline()
	if len(data) == 0:
		break
	elif string in data:
		data=data.replace(string,new_string)
	f.seek(x)
	f.write(data)

f.close()
