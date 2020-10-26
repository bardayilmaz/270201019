month = input("Type a month: ") #I didn't check for the day counts of that month, so user can type for example ,258'th of february
day = input("type day: ")
month = month.lower()

if month == "december" or month =="january"  or month == "february":
	print("winter")
elif month == "march" or month =="april" or month =="may":
	print("spring")
elif month == "june" or month == "july" or month =="august":
	print("summer")
elif month=="september" or month =="october" or month == "november":
	print("fall")							
else:
	print("there is not a month named", month, "in English!")
