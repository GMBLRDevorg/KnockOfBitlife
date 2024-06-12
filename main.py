import random
import time
from threading import Thread
from types import GeneratorType
from colorama import Fore,Style,Back
from better_profanity import profanity
import argparse

#Copyright @2023 BlossomFoxSoftware in association with TenthSystemsUK (all rights reserved for TenthSystemsUK)
#Beans
#import jokes.printer
import os
import sys
# 1Month = 20mins
#vars
#character stats
Parser=argparse.ArgumentParser(description="Cheats")

Parser.add_argument("-d","--dev",help="Boot in devmode",action="store_true")



args = Parser.parse_args()


age = 1
health = 100
happiness = 100
looks = 100
smarts = 100
money = 100
turns= 3
#assets
house = False
housetype = "none"
houseaddress = "none"
car = False
carmake = "none"
#jobs
job = False
job_name = "none"
job_salary = 0
#relationships
partner = False
sexuality = "unknown"
gender = "unknown"
#other
married = False
slide=False
#illnesses 
dimentia = False
depression = False
anxiety = False
cancer = False
AIDS = False
syphilis = False
clamidiya= False
dyslexia = False
#Disabilitys
blind = False
deaf = False
#Inputs

#As Drogas
Amphetamine = 80

CannabisFFH = random.randint(170,220)

CannabisResin=random.randint(80,150)

CocaineAdulterated=random.randint(800,1000)

CocaineUnAdulterated = random.randint(1100,2000)

CrackCocaine=random.randint(800,1400)

Heroin=random.randint(750,1500)

Ketamine=random.randint(350,600)

MDMAPowderorCrystal=random.randint(300,600)

MDMAPills=random.randint(5,10)
#---------

#def
def main():
	global age
	global health
	global happiness
	global looks
	global smarts
	global money
	
	if args.dev == True:
		money=9e9
		age=34
		smarts=9e9
		health=9e9
		happiness=9e9
		looks=9e9
		print(Fore.LIGHTWHITE_EX+Back.YELLOW+Style.BRIGHT)
		
	print()
	print(f"CPU STATS : {round(time.process_time(),2)} ms")
	print("Welcome to the life simulator!")
	print("|----------------------------|")
	print("|1. age up                   |")
	print("|2. check stats              |")
	print("|3. work                     |")
	print("|4. relationships            |")
	print("|5. casino                   |")
	print("|6. surgery                  |")
	print("|7. life options             |")
	print("|8. go shopping              |")
	print("|9. Search dark web          |")
	print("|10. quit                    |")
	print("|----------------------------|")

	Menuchoice = int(input("What would you like to do? > "))
	if Menuchoice == 1:
		ageup()
	elif Menuchoice == 2:
		stats()
	elif Menuchoice == 3:
		work()
	elif Menuchoice == 4:
		relationships()
	elif Menuchoice == 5:
		casino()
	elif Menuchoice == 6:
		surgery()
	elif Menuchoice == 7:
		lifeoptions()
	elif Menuchoice == 8:
		shop()
	elif Menuchoice == 9:
		dweb()
	elif Menuchoice == 10:
		quit()
	else:
		print("Invalid input")
		main()
def dweb():
	print("Welcome to the dark web")
	search=input("| Search Query(Drugs)⮑:")
	if search.lower()=="drugs":
		print(Fore.BLACK+Style.BRIGHT+Back.LIGHTGREEN_EX)
		print("| Amphetamine⮑",Amphetamine)
		print("| CannabisFFH⮑",CannabisFFH)
		print("| CannabisResin⮑",CannabisResin)
		print("| CocaineAdulterated⮑",CocaineAdulterated)
		print("| CocaineUnAdulterated⮑",CocaineUnAdulterated)
		print("| CrackCocaine⮑",CrackCocaine)
		print("| Heroin⮑",Heroin)
		print("| Ketamine⮑",Ketamine)
		print("| MDMAPowderorCrystal⮑",MDMAPowderorCrystal)
		print("| MDMAPills⮑",MDMAPills)
	
def work():
	print("placeholder")
	main()
def relationships():
	print("placeholder")
	main()
def surgery():
	print("placeholder")
	main()
def lifeoptions():
	print("placeholder")
	main()
def shop(): #Alex is doing the shop :)
	print("Welcome to the shop!")
	global money
	Isle1 = ["Sweets","Chocolate","Soda","Candy"]
	Isle2 = ["Bread","Meat","Fruit","Vegetables"]
	Isle3 = ["Toys","Clothes","Shoes","Jewelry"]
	main()

def slots():	
	global money

	spinner1 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 1 list
	spinner2 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 2 list
	spinner3 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 3 list
	while True and turns > 0 and age >= 18:
			money = money- 100
			print(spinner1[random.randint(0,5)])
			print(spinner2[random.randint(0,5)])
			print(spinner3[random.randint(0,5)])
			spin = [spinner1[random.randint(0,5)],spinner2[random.randint(0,5)],spinner3[random.randint(0,5)]]
			print(spin)
			print("You have ",money)
			print("leave continue blank to stay, type 'no' to leave")
			qwit=input("Continue?")


			if spin[0] == spin[1] and spin[1] == spin[2]:
					money = money + 100
			if spin[0] == spin[1] and spin[1] != spin[2]:
					money = money + 50
			if spin[0] != spin[1] and spin[1] == spin[2]:
					money = money + 50
			if spin[0] != spin[1] and spin[0] == spin[2]:
				money = money + 50
	if turns == 0:
			print(f"{Fore.YELLOW} You are out of Tokens {Style.RESET_ALL}")
			main()
	if age <= 18:
		print(f"{Fore.RED}You are too young to play{Style.RESET_ALL}")
		os.system("clear")
		main()()
	if money <= 0:
		print("You need more money to play")
		main()

def roullete():
	print("work in progress")
def blackjack():
	print("work in progress")
def casino():
	print("|----welcome to the casino----|")
	print("|-----------------------------|")
	print("|1. Fruit Machine/slots       |")
	print("|2. Roulette                  |")
	print("|3. Blackjack                 |")
	print("|4. Back                      |")
	print("|-----------------------------|")

	cas1 = int(input("What would you like to do? > "))
	if cas1 == 1:
		slots()
	if cas1 == 2:
		roulette()
	if cas1 == 3:
		blackjack()
	if cas1 == 4:
		main()
	

			
def ageup():
	global age,health,happiness,looks,smarts,money,depresion,dementia,anxiety,cancer,AIDS,syphilis,clamidiya
	age = age + 1
	print("You are now",age,"years old")
	health = health + random.randint(-15,20)
	happiness = happiness + random.randint(-15,20)
	print("\nYour health is now",health," \nyour happiness is now",happiness,"%")
	if happiness <= -1:
		depression = True
		print("You are depressed and have a hapiness of ",happiness,"% as you cant have more than 100%")
	if happiness >= 100:
		happiness = 100
		print("You are happy and have a hapiness of ",happiness)
	if health <= -1:
		print(f"{Fore.RED}{Style.BRIGHT}Game Over!!!{Style.RESET_ALL}")
		quit()
	main()

def passive_income():
	global money
	while True and age >= 16:
		min=1000.50
		max=10000.00
		Pay=round(random.uniform(min,max),2)
		money = money + Pay
		print(f"{Fore.GREEN}{Style.BRIGHT}You have been payed {Pay}{Style.RESET_ALL}\n")
		time.sleep(1200)

def start():
	t=Thread(target=passive_income,daemon=True)
	t.start()
		
	

def stats():
	print("Age:",age)
	print("Health:",health)
	print("Happiness:",happiness)
	print("Looks:",looks)
	print("Smarts:",smarts)
	print("Money:",money)
	print("Turns:",turns)
	print("House:",house)
	print("House Type:",housetype)
	print("House Address:",houseaddress)
	print("Car:",car)
	print("Car Make:",carmake)
	print("Job:",job)
	print("Job Name:",job_name)
	print("Job Salary:",job_salary)
	print("Partner:",partner)
	print("Sexuality:",sexuality)
	print("Genders:",gender)
	print("Married:",married)
	print("Dementia:",dementia)
	print("Depression:",depression)
	print("Anxiety:",anxiety)
	print("Cancer:",cancer)
	print("AIDS:",AIDS)
	print("")
	main()
	



name=str(input("choose a name:"))
gender=str(input("choose a gender:"))
sexuality=str(input("choose a sexuality:"))

badName= profanity.contains_profanity(name)
badGender= profanity.contains_profanity(gender)
badSexuality= profanity.contains_profanity(sexuality)

if name.lower()=="6e2dd":
	age = 19
	money = 9e40
	turns = 9e40
	happinesss = 9e40
	health = 9e40
	print(f"Dev Mode Enabled | Age: {int(age)} | Money: {int(money)} | Turns: {int(turns)}")





if badName or badGender or badSexuality and not args.dev:
	print(f"{Fore.RED}{Style.BRIGHT}YOU HAVE BEEN BANNED!{Style.RESET_ALL}")
	time.sleep(5)
	os.system("clear")

	quit()


def __init__():
	User=input('Username:')
	Passw=input('Password:')

	
#whats next?
#look in the targets.txt
#Where do we start?