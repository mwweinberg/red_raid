import urllib

core = "http://58.68.146.102/pic/101p/"

#these all have to be numbers not strings - need to change them

year = "2000"
month = 4
day = 2
page = "01"



for i in range(0,6):
	day += 1
	#turns day into a string
	day_fixed = str(day).zfill(2)
	
	for i in range(0,4):
		month += 1
		month_fixed = str(month).zfill(2)

		urllib.urlretrieve(core+year+"/"+month_fixed+"/"+year+month_fixed+day_fixed+page+".jpg", year+"-"+month_fixed+"-"+day_fixed+"-"+page+".jpg")

	month = 4
