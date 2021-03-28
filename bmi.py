#This is a python program that calculates a person's BMI#
#input person's height in centimetre and weight in kilograms#
#output is weight divided by height in metres squared#

print ("This person's BMI is")

metre = cm * 0.01    #converts height in cm to m
m_square = metre * metre

weight = int(input(65))
height = int(input(1.8))

bmi = weight/(height*height)
print (bmi) 
