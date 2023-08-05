"""
This is the main windew.py. Use it whenever you want to have Windew in your command line.

Credits:
	Code: #Guigui (@HastagGuigui)
	Original character: KirbyCreep (@kirbycreep)
"""

REVERSE = "\x1b[7m"
NORMAL = "\x1b[0m"

def reverse(string): return REVERSE + string + NORMAL

WINDEW = reverse((" "*32) + "_ □ x ") \
	+ "\n" + reverse(" ") + (" "*36) + reverse(" ") \
	+ "\n" + reverse(" ") + (" "*13) + reverse(" ") + (" "*8) + reverse(" ") + (" "*13) + reverse(" ")\
	+ "\n" + reverse(" ") + (" "*13) + reverse(" ") + (" "*8) + reverse(" ") + (" "*13) + reverse(" ")\
	+ "\n" + reverse(" ") + (" "*36) + reverse(" ") \
	+ "\n" + reverse(" ") + (" "*17) + "\\/" + (" "*17) + reverse(" ") \
	+ "\n" + reverse(" ") + (" "*36) + reverse(" ") \
	+ "\n" + ("▀"*10) + reverse(" "*18) + ("▀"*10) \
	+ "\n" + (" "*8) + "/" + reverse(" "*20) + "\\" + (" "*8) \
	+ "\n" + (" "*7) + "/" + reverse(" "*22) + "\\" + (" "*7) \
	+ "\n" + (" "*5) + "⬤ " + reverse(" "*24) + "⬤" + (" "*6) \
	+ "\n" + (" "*13) + reverse(" ") + (" "*10) + reverse(" ") + (" "*13) \
	+ "\n" + (" "*10) + ("▄"*3) + reverse(" ") + (" "*10) + reverse(" ") + ("▄"*3) + (" "*10) \

print(WINDEW)
