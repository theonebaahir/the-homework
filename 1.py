a = 10
b = 20
c =  30
print(a != b)
print(b != c)
a = "Python"
b = "coding"
if a !=b :
    print(a, "and" , b, "are different")
    
# BMI
Height =(float(input("write your height in CM")))
weight =(float(input("write your weight in kg")))
BMI = weight / (Height/100)**2
print("your BMI",BMI)

if BMI <= 18.4:
  print("your underweight")
elif BMI <= 24.9:
  print("your healthy")
elif BMI <= 29.9:
  print("your overweight")
elif BMI <= 34.9:
  print("your obese")
elif BMI <= 39.9:
  print("your severly obese ")
else:
  print("severly obese")





