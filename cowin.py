try:
	import time
	import datetime
	import requests 
	from playsound import playsound
	#from colorama import Fore, Back, Style
except ImportError as e:
	print("Import Error Has Occured and Please Check all Modules and Library are installed Properly or Not!")

"""
AUTHOR: VISHVESH BHAVSAR
DATE:09-06-2021

Definition: Used Public Cowin API to get the Details if the slots are available or not based on the pincode you provide and U can see the slots 
for the current date...
"""
"""
def colored(r, g, b, text):
	return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
	"""
pincode=int(input("\n              Enter the Pincode: "))

#typ=str(input("\n   Please Provide Fee Type(Paid/Free): "))
if (len(str(pincode))!=6):
	exit("Please Enter the Valid Pincode and try again");
else:
	vaccinetype=input("\n Enter the Vaccine Name (Covishield/Covaxin/Sputnik V):  ")
	#cc=int(input("\n Enter the No of centers (At Least) You Want to see detail of: " ))
	dat=datetime.date.today().strftime('%d-%m-%Y')
	print("\n")
	print("**************Today's Date: {}".format(dat))
	print("\n")
	URL_GET='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,dat)
	header = {'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
	count=0

	def findCowinAvail():
		global count
		res=requests.get(URL_GET,header).json()
		data=res["sessions"]
		for x in data:
			if((x["vaccine"]==(vaccinetype.upper())) and (x["available_capacity"] > 0) and (x["min_age_limit"] == 18) and ((x["fee_type"]=="Paid") or (x["fee_type"]=="Free"))):
				count += 1
				#print(count,end="\n")
				print("\n")
				print(" Name of Center  : {}".format(x["name"]))
				print(" Address         : {}".format(x["address"]))
				print(" State           : {}".format(x["state_name"]))
				print(" District/City   : {}".format(x["district_name"]))
				#print(" Block Name      : {}".format(x["block_name"]))
				print(" Pincode         : {}".format(x["pincode"]))
				print(" Vaccine Name    : {}".format(x["vaccine"]))
				print(" Fee Type        : {}.".format(x["fee_type"]))
				print(" Available Slots : {}".format(x["available_capacity"]))
				print(" Slots (Dose:1)  : {}".format(x["available_capacity_dose1"]))
				print(" Slots (Dose:2)  : {}".format(x["available_capacity_dose2"]))
				playsound('C:/Users/vishvesh/Desktop/Cowinpython/ding-sound-effect_2.mp3')
				print("\n")
			if (count==3):
				return True
		if(count == 0):
			print(' No Slots Available!...')
			return False
	while(findCowinAvail() != True):
		time.sleep(1)
		findCowinAvail()
