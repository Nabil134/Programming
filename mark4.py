print("-------------Marksheet-----------------")
name=input("Enter Your Name:")
roll=int(input("Enter Your Roll NO:"))
dt=int(input("Enter Your Data Mining Marks:"))
ds=int(input("Enter Your Data Science Marks:"))
ai=int(input("Enter Your AI Marks:"))
total=dt+ds+ai
per=total/300*100
print("Name:",name)
print("Roll NO:",roll)
print("Total:",total)
print("Percentage:",per)
if  per >= 80:
  print("You got A+ Grade")
elif per >= 70:
  print("You got A Grade")
elif per >= 60:
  print("You got B Grade")
elif per >= 50:
  print("You got C Grade")
else:
  print("You are fail")
print("Subject\t\t\t\t\tTotal Marks\t\t\t\t\tObtained Marks")
print("**************************************************************************")
print("Data Mining\t\t\t100\t\t\t\t\t\t\t\t\t",dt)
print("Data Science\t\t\t100\t\t\t\t\t\t\t\t\t",ds)
print("AI           \t\t\t100\t\t\t\t\t\t\t\t\t",ai)
print("Name:",name)
print("Roll NO:",roll)
print("Total:",total)
print("Percentage:",per)
if  per >= 80:
  print("You got A+ Grade")
elif per >= 70:
  print("You got A Grade")
elif per >= 60:
  print("You got B Grade")
elif per >= 50:
  print("You got C Grade")
else:
  print("You are fail")


