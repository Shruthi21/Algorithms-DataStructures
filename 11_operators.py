def main():
    T = 3
    Meal = []
    totalCost = 0
    while T!= 0:
        T-=1
        Meal.append(float(raw_input()))
    
    mealCost= Meal[0]
    tipPercent = Meal[1]
    taxPercent = Meal[2]
    tip = mealCost * (tipPercent/100)
    tax = mealCost * (taxPercent/100)
    totalCost = mealCost + tip + tax

    
    print 'The total meal cost is ' + str(int(round(totalCost))) + ' dollars.'
    
if __name__ == '__main__':
    main() 
    
