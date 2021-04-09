# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 

# life span of 90 years
life_span = 90 

# Var types
print(type(life_span))
print(type(age))

# Step 1 : (90 - age)
step_1 = life_span - (int(age))

# Step 2 : Multiply Step 1 by 365, 52 and 12 
x = step_1 * 365
y = step_1 * 52
z = step_1 * 12

# Expected output:
print(f"You have {x} days, {y} weeks, and {z} months left.")

