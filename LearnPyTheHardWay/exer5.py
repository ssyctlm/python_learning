my_name = 'Zed A.shaw'
my_age = 35
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

#this is tricky, try to get it exactly right
print("If I add %d,%d,and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight))


#additional practice
inch_to_cm = 2.54
lbs_to_kg = 0.45359237
print('\n')
print("Let's talk about %s." % my_name)
print("He's %r cm tall." % (my_height*inch_to_cm))

#三种取小数点的方法
print("He's %r kg heavy." % round((my_weight*lbs_to_kg),6))
print("He's %.2f kg heavy." % (my_weight*lbs_to_kg))
print("He's {:.3f} kg heavy." .format(my_weight*lbs_to_kg))
#3 ways to precise digit
print("Actually that's not too heavy")
