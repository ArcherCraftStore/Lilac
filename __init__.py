import cmd,sys,os
from datetime import *


class Lilac(cmd.Cmd):
 def __init__(self):
  cmd.Cmd.__init__(self)
  self.prompt="ArcherCraft VM"
 def do_tipcalc(self,line):
  meal = raw_input("Enter the meal cost")
  tax = raw_input("Enter the tax")
  tip = raw_input("enter the Tip")

  meal = meal + meal * tax

  total = meal + meal * tip
  print("%.2f" % total)


if __name__  == "__main__":
  archercraftvmlilac = Lilac()
  archercraftvmlilac.cmdloop()
