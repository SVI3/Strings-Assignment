# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

discount_percentage = 30

sum_one_each = (broccoli + leek + potato + brussel_sprout)

print ('total price =',sum_one_each)

avg_price = (sum_one_each / 4)

print ('average price =', avg_price)

sum_total = ((num_potatoes * potato) + (num_broccolis * broccoli) + (num_leeks * leek) + (num_brussel_sprouts * brussel_sprout))

print ('new total price =', sum_total)

discounted_sum_total = round((sum_total - (sum_total * (discount_percentage/100))), 2)

print('discounted total price =', "{:.2f}".format(discounted_sum_total))
