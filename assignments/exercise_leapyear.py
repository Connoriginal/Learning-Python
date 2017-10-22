def isleapyear():
	year = int(input())
	if year < 0:
		print(year,"0")
	elif year % 4 ==0 and (year % 400 ==0 and year % 100 ==0):
		print(year,"True")
	else:
		print(year,"False")

isleapyear()
