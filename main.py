# print my welcome message
print("Welcome to Og styling line!")
#create menu 
def store_items():
  print("1. crop-tops")
  print("2. oversized shirts/Graphic tshirts")
  print("3. ripped jeans")
  print("4. low-waisted jeans")
  print("5. high-waisted jeans")
  print("6. heels")
  print("7. shoes")
  print("8. flip-flops")
  print("9. sandels")


def exchange_process():
  item_cost = int(input("How much did your item cost?"))
  cropTops = 9
  oversizedTshirts  = 30
  graphicShirts = 30
  rippedJeans = 20
  low_waisted_jeans = 20
  high_waisted_jeans = 25
  heels = 20
  shoes = 35
  flipFlops = 15
  sandels =10
  
  if item_cost <= cropTops:
    print("you can return your item for crop-tops or pay the difference with another item")
    question = input("\nWould you like to see to pay the difference with another item?")
    if question  == "yes":
      print("Here are the items in store")
      store_items()
      userChoice = int(input("\nChoose from the folllowing options(ex. 1,2,3):"))
      if userChoice == 1:
        print(f" your remianing balance is {cropTops - item_cost} dollars")
      elif userChoice == 2:
        print(f"your remianing balance is {oversizedTshirts - item_cost} dollar")
      elif userChoice == 3:
        print(f"your remianing balance is {rippedJeans - item_cost} dollar")
      elif userChoice == 4:
        print(f"your remianing balance is {low_waisted_jeans - item_cost} dollar")
      elif userChoice == 5:
        print(f"your remianing balance is {high_waisted_jeans - item_cost} dollar")
      elif userChoice == 6:
        print(f"your remianing balance is {heels - item_cost} dollar")
      elif userChoice == 7:
        print(f"your remianing balance is {shoes - item_cost} dollar")
      elif userChoice == 8:
        print(f"your remianing balance is {flipFlops - item_cost} dollar")
      elif userChoice == 9:
        print(f"your remianing balance is {sandels - item_cost} dollar")
    elif question == "no":
      print("you have returned this item for a crop top")
    else:
      print("\ntry again with lowercase letters")
      question = input("\nWould you like to see to pay the difference with another item?")
      if question  == "yes":
        print("\nHere are the items in store")
        store_items()
        userChoice = int(input("\nChoose from the folllowing options(ex. 1,2,3):"))
        if userChoice == 1:
          print(f" your remianing balance is {cropTops - item_cost} dollars")
        elif userChoice == 2:
          print(f"your remianing balance is {oversizedTshirts - item_cost} dollar")
        elif userChoice == 3:
          print(f"your remianing balance is {rippedJeans - item_cost} dollar")
        elif userChoice == 4:
          print(f"your remianing balance is {low_waisted_jeans - item_cost} dollar")
        elif userChoice == 5:
          print(f"your remianing balance is {high_waisted_jeans - item_cost} dollar")
        elif userChoice == 6:
          print(f"your remianing balance is {heels - item_cost} dollar")
        elif userChoice == 7:
          print(f"your remianing balance is{shoes - item_cost} dollar")
        elif userChoice == 8:
          print(f"your remianing balance is {flipFlops - item_cost} dollar")
        elif userChoice == 9:
          print(f"your remianing balance is {sandels - item_cost} dollar")
      elif question == "no":
        print("you have returned this item for a crop top")
    
  elif item_cost >= oversizedTshirts and graphicShirts:
    print("you can return your item for a \noversized T shirt\n graphic shirt \nor pay the difference with another item")
    question = input("Would you like to see to pay the difference with another item?")
    if question  == "yes":
      print("Here are the items in store")
      store_items()
    elif question == "no":
      print("we have exchanged  your item for a oversized t-shirt/ graphic shirt")
  elif item_cost >= rippedJeans:
    print("ripped-Jeans")
  elif item_cost >= low_waisted_jeans:
    print("low-waisted-jeans")
  elif item_cost >= high_waisted_jeans:
    print("high-waisted-jeans")
  elif item_cost >= heels:
    print("heels")
  elif item_cost >= shoes:
    print("shoes")
  elif item_cost >= flipFlops:
    print(" flipFlops")
  elif item_cost <= sandels:
    print("sandels")
  
def item_return():
  item = input("What item do you want to return?")
  print(f"\nbefore we can return your {item}, \ntheres a few questions you need to answer")
  return_process()
def displayMenu():
  print("\n1: Returning item")
  print("\n2:Exchaning an item")
def return_process():    
  days = int(input("\nhow many days has it been since you purchased this item?"))
  if days >= 30:
    print("I'm sorry you can not return this item")
    print("its been 30 days or over since you bought this item")
  elif days <= 30:
    print("You can return this item")
    hygenic_concerns = input("\nHave you worn this item yet?")
    if hygenic_concerns == "yes":
      print("\nSorry you can't return this item")
    elif hygenic_concerns == "no":
      print("You can return this item")
      print("here are three options ")
      print("1. Exchange item")
      print("2. store credit")
      print("3. full refund")
      userChoice = int(input("\nChoose from the folllowing options:(ex. 1,2,3)"))
      exchange = 1
      store_credit = 2
      full_refund = 3
      if userChoice == 1:
        exchange_process()
      elif userChoice == 2:
        print("we have refunded your money in store credit ")
      elif userChoice == 3:
        print("we have refunded your money to your bank account ")
    
    
      
      
      
    
    
displayMenu()

def options():

  userChoice = int(input("\nChoose from the folllowing options:"))
  
  if userChoice == 1:
    print("you want to return an item!")
    print("great!")
    name = input("can I get your name?:")
    item_return()
  
  elif userChoice == 2:
    name = input("Great! can I get your name?:")
    item = input("What item do you want to return?")
    print(f"\nbefore we can return your {item}, \ntheres a few questions you need to answer")
    days = int(input("\nhow many days has it been since you purchased this item?(ex. 2,15,5):"))
    if days >= 30:
      print("I'm sorry you can not return this item")
      print("its been 30 days or over since you bought this item")
    elif days <= 30:
      print("You can return this item")
      hygenic_concerns = input("\nHave you worn this item yet?")
      if hygenic_concerns == "yes":
        print("\nSorry you can't exchange this item")
      elif hygenic_concerns == "no":
        print("You can exchange this item")
        exchange_process()
  else:
    print("try again")
    displayMenu()
    options()
  
options()



  
  
  
#create menu 

#give them options to return or exchnage an item