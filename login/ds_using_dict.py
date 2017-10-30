ab = {
	"Swaroop":"swaroop@swaroopch.com",
	"Larry":"larry@wall.org",
	"Matsumoto":"matz@ruby-lang.org",
	"Spammer":"sparmmer@hotmail.com"
}

print ("Swaroop's address is",ab["Swaroop"])

del ab["Spammer"]

print ("There are {} contacts in the address-book".format(len(ab)))

for name,address in ab.items():
	print ("Contact {} at {}".format(name,address))

ab["Guido"] = "quido@python.org"

if "Guido" in ab:
	print ("Guido's address is",ab["Guido"])
