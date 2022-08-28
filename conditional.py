# conditional statement in python
name= input("what is yoru name?\n")
age = int (input("what is your age\n"))

if age<0:
      print(f"dear {name}, your are lying")
elif age==10:
    print(f"dear {name}, your ticekt price is: 100 ")
elif age>10:
    print(f"dear {name}, your tickt price is: 150")
else:
    print(f"dear {name}, your tickt price is: 50")

#physics
mass= int (input("what is your mass?\n"))
g = float (input("whats the acceleration due to gravity around you?"))
weight = int (mass * g)
print(f"your weight is {weight}")








