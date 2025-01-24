#1_input first number
x = int(input("enter first number: "))
#2_input operation type
a = input("enter operation type: ")
#3_input second number
v = int(input("enter second number: "))
#4_print the result
if a == "-":
  print(x - v)
elif a == "/":
  print(x / v)
elif a == "*":
  print(x * v)
elif a == "+":
  print(x + v)
else:
  print("error")