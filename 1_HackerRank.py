# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

tip =  12 *( float(tipPercent)/100 )
tax =  12 *( float(taxPercent)/100 )
totalCost = mealCost + tip + tax


print 'The total meal cost is ' + str(int(math.ceil(totalCost))) + ' dollars.'
