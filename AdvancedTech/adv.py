import random
import time
from threading import Thread
from types import GeneratorType
from colorama import Fore,Style,Back
from better_profanity import profanity
import argparse

#Copyright @2023 BlossomFoxSoftware in association with TenthSystemsUK
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

turns= 3

class HumanStats(object):
  age = 1
  health = 100
  happiness = 100
  looks = 100
  smarts = 100
  money = 100
  gender = "unknown"

#assets
class assets(object):
  house = False
  housetype = "none"
  houseaddress = "none"
  car = False
  carmake = "none"
#jobs
class Jobs(object):
  job = False
  job_name = "none"
  job_salary = 0
#relationships
class Relationships(object):
  partner = False
  sexuality = "unknown"
  
#other
  married = False
  slide=False
#illnesses 
class Illnesses(object):
  dimentia = False
  depression = False
  anxiety = False
  cancer = False
  AIDS = False
  syphilis = False
  clamidiya= False
  dyslexia = False
#Disabilitys
class disabilitys(object):
  blind = False
  deaf = False
#Inputs

#As Drogas
class Drugs(object):
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

HStats=HumanStats()
Nastys=Illnesses()
Assets=assets()
#def
def main():
  global HumanStats
  Hstats=HumanStats()
  if args.dev:
    Hstats.money=int(9e9)
    Hstats.age=34
    Hstats.smarts=int(9e9)
    Hstats.health=int(9e9)
    Hstats.happiness=int(9e9)
    Hstats.looks=int(9e9)
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
    print("| Amphetamine⮑",Drugs.Amphetamine)
    print("| CannabisFFH⮑",Drugs.CannabisFFH)
    print("| CannabisResin⮑",Drugs.CannabisResin)
    print("| CocaineAdulterated⮑",Drugs.CocaineAdulterated)
    print("| CocaineUnAdulterated⮑",Drugs.CocaineUnAdulterated)
    print("| CrackCocaine⮑",Drugs.CrackCocaine)
    print("| Heroin⮑",Drugs.Heroin)
    print("| Ketamine⮑",Drugs.Ketamine)
    print("| MDMAPowderorCrystal⮑",Drugs.MDMAPowderorCrystal)
    print("| MDMAPills⮑",Drugs.MDMAPills)

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
  if HumanStats.age <= 18:
    print(f"{Fore.RED}You are too young to play{Style.RESET_ALL}")
    os.system("clear")
    main()
  if HumanStats.money <= 0:
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
  global HStats
  global Nastys
  global Assets
  age =HStats.age + 1
  print("You are now",age,"years old")
  HStats.health = HStats.health + random.randint(-15,20)
  happiness = HStats.happiness + random.randint(-15,20)
  print("\nYour health is now",HStats.health," \nyour happiness is now",happiness,"%")
  if HStats.happiness <= -1:
    Nastys.depression = True
    print("You are depressed and have a hapiness of ",happiness,"% as you cant have more than 100%")
  if HStats.happiness >= 100:
    HStats.happiness = 100
    print("You are happy and have a hapiness of ",happiness)
  if HStats.health <= -1:
    print(f"{Fore.RED}{Style.BRIGHT}Game Over!!!{Style.RESET_ALL}")
    quit()
  main()

def passive_income():
  global HStats
  global HumanStats
  while True and HStats.age >= 16:
    min=1000.50
    max=10000.00
    Pay=round(random.uniform(min,max),2)
    HumanStats.money = HumanStats.money + Pay
    print(f"{Fore.GREEN}{Style.BRIGHT}You have been payed {Pay}{Style.RESET_ALL}\n")
    time.sleep(1200)

def start():
  t=Thread(target=passive_income,daemon=True)
  t.start()



def stats():
  global HStats
  print("Age:",HStats.age)
  print("Health:",HStats.health)
  print("Happiness:",HStats.happiness)
  print("Looks:",HStats.looks)
  print("Smarts:",HStats.smarts)
  print("Money:",HStats.money)
  print("Turns:",turns)
  print("House:",Assets.house)
  print("House Type:",Assets.housetype)
  print("House Address:",Assets.houseaddress)
  print("Car:",Assets.car)
  print("Car Make:",Assets.carmake)
  print("Job:",Jobs.job)
  print("Job Name:",Jobs.job_name)
  print("Job Salary:",Jobs.job_salary)
  print("Partner:",Relationships.partner)
  print("Sexuality:",Relationships.sexuality)
  print("Genders:",HStats.gender)
  print("Married:",Relationships.married)
  print("Dementia:",Illnesses.dimentia)
  print("Depression:",Illnesses.depression)
  print("Anxiety:",Illnesses.anxiety)
  print("Cancer:",Illnesses.cancer)
  print("AIDS:",Illnesses.AIDS)
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


main()
#whats next?
#look in the targets.txt
#Where do we start?