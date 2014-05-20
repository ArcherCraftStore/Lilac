
import cmd,sys
from datetime import datetime

def hotel_cost(nights):
      return 140 * nights
def plane_ride_cost(city):
     if city == "Charlotte":
        return 183
     elif city == "Tampa":
        return 220
     elif city == "Pittsburgh":
        return 222
     elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
def trip_cost(city, days, spending_money):
    return  rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)+spending_money
    
class Lilac(cmd.Cmd):
  def __init__(self):
   cmd.Cmd.__init__(self)
   self.prompt="ArcherCraft VM"
  def do_tipcalc(self,line):
   meal = input("Enter the meal cost")
   tax = input("Enter the tax")
   tip = input("enter the Tip")
   meal = meal + meal * tax
   total = meal + meal * tip
   print(total)
  def do_time(self,line):
    now = datetime.now()
    print('%s/%s/%s' % (now.month, now.day, now.year))
    print('%s:%s:%s' % (now.hour, now.minute, now.second))
    print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
  def do_EOF(self, line):
   sys.exit()
  def do_pyglatin(self,line):
    pyg = 'ay'

    original = input('Enter a word:')

    if len(original) > 0 and original.isalpha():
     word=original.lower()
     first=word[0]
     new_word = word+first+pyg
     new_word=new_word[1:len(new_word)]
     print(new_word)
    else:
     print('empty')
  def do_vacationmach(self,line):
    print(trip_cost(input("City"), input("Days"), input("Money")))
   
if __name__  == "__main__":
  archercraftvmlilac = Lilac()
  archercraftvmlilac.cmdloop()
