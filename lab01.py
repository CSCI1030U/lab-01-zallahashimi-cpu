def main():
    cost_per_item = 19.99
    quantity = 5

    # YOUR CODE FOR PART 1 GOES HERE 
    cost_per_item = 19.99
    quantity = 5 
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # THIS IS THE CODE FOR PART 3
    
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')

if __name__ == "__main__":
    main()
# expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

#After running the code I got a TypeError (line 29) 
#saying "can only concatenate str (not "float") to str"

#A TypeError is is a programming error that occurs when an operation 
#is attenpted on a value of the wrong data type. In this case, I was trying to add a string
#to a number "investment", and Python doesn't convert numbers to strings.
#To fix this issue, I put str() to convert the number



