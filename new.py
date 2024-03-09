# ARGUMENTS are vales in function call and PARAMETERS are variables inside the function.

def hello(name):
  print('Hi, ' + name)
hello('11')

def add_one(number):
  return number + 1
add_one(4)

def pct_of_num(number, pct):  
  return number*(pct/100)

pct_of_num(450,20)