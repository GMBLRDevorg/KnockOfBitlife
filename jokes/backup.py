import random
import time
from threading import Thread
from types import GeneratorType
from colorama import Fore,Style
from better_profanity import profanity
#import jokes.printer
import os
import sys
# 1Month = 20mins
#vars
#character stats
age = 1
health = 100
happiness = 100
looks = 100
smarts = 100
money = 0
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


#def
def main():
  print()
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
  print("|9. quit                     |")
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
    quit()
  elif Menuchoice == 9:
    shop()
  else:
    print("Invalid input")
    main()

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
def shop():
  print("placeholder")
  main()

def casino():
  #Fruit Machine
  #Add credits
  #add prizes
  #High Score

  turns= 3

  credit = 100
  spinner1 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 1 list
  spinner2 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 2 list
  spinner3 = ["Cherry","Bell","Lemon","Orange","Star","Skull"]#spinner 3 list
  while True and turns > 0 and age >= 18:
      turns = turns-1
      print(f"{Fore.CYAN}Tokens: {turns}{Style.RESET_ALL}")
      credit = credit - 20
      print(spinner1[random.randint(0,5)])
      print(spinner2[random.randint(0,5)])
      print(spinner3[random.randint(0,5)])
  #create a new list to contain the current spin
      spin = [spinner1[random.randint(0,5)],spinner2[random.randint(0,5)],spinner3[random.randint(0,5)]]
      print(spin)
      print("You have - ",credit)
      input("Continue?")

      if spin[0] == spin[1] and spin[1] == spin[2]:
          credit = credit + 100
      if spin[0] == spin[1] and spin[1] != spin[2]:
          credit = credit + 50
      if spin[0] != spin[1] and spin[1] == spin[2]:
          credit = credit + 50
      if spin[0] != spin[1] and spin[0] == spin[2]:
          credit = credit + 50
  if turns == 0:
      print(f"{Fore.YELLOW} You are out of Tokens {Style.RESET_ALL}")
      main()
  if age <= 18:
    print(f"{Fore.RED}You are too young to play{Style.RESET_ALL}")
    main()


def ageup():
  global age,health,happiness,looks,smarts,money,depresion,dimentia,anxiety,cancer,AIDS,syphilis,clamidiya
  age = age + 1
  print("You are now",age,"years old")
  health = health + random.randint(-15,20)
  happiness = happiness + random.randint(-15,20)
  print("\nYour health is now",health,"% \nyour happiness is now",happiness,"%")
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
  print("Dimentia:",dimentia)
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

if name.lower()=="lewis":
  sexuality="Gay"
  print(f"{Fore.GREEN}{Style.DIM}Your are lewis your now straight heres your values [Name:{name}, Gender:{gender}, Sexuality{sexuality}]{Style.RESET_ALL}")
  print("Hello",name)

if badName or badGender or badSexuality:
  print(f"{Fore.RED}{Style.BRIGHT}YOU HAVE BEEN BANNED!{Style.RESET_ALL}")
  time.sleep(5)
  os.system("clear")

  quit()
main()