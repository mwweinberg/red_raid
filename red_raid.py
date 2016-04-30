import urllib

core = "http://58.68.146.102/pic/101p/"

#start all of these one below where you want to start because step 1 is +=1

#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year = 2002
month = 0
day = 0
page = "01"



for i in range(0,31):
	day += 1
	#turns day into a string
	day_fixed = str(day).zfill(2)
	
	for i in range(0,12):
		month += 1
		month_fixed = str(month).zfill(2)

		for i in range(0,6):
			
			year += 1
			year_fixed = str(year)

		#this needs to go at the bottom of the nest
			urllib.urlretrieve(core+year_fixed+"/"+month_fixed+"/"+year_fixed+month_fixed+day_fixed+page+".jpg", year_fixed+"-"+month_fixed+"-"+day_fixed+"-"+page+".jpg")

		year = 2002

	#this resets the month to the starting point so it stays in the right 		range	
	month = 0
	
