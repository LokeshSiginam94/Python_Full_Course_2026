original_price = 1000
discount=250

final_price=original_price-discount
print("The final Price after discount is:",final_price)

cost_of_ticket=150
no_of_peoples=4

total_cost=cost_of_ticket*no_of_peoples
print("The total cost of ticket for",no_of_peoples,"peoples is:",total_cost)

print(17%5) #2

print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10%5)
print(10//5)
print(10**5)

#operators are used to perform operations between two or more operands.% is used to find the remainder after division of two numbers.

#comparison
age=22
print(age>=18)
print(age<=18)
print(age==18)
print(age!=18)
print(age>18)
print(age<18)

#logical
age=21
has_ticket=True

print(age>=18 and has_ticket)
print(age>=18 or has_ticket)
print(not has_ticket)
print(not age>=18)

#assignment
money=1000
money+=500
print(money)

spent=250
money-=spent

print(money)


#identity
x=[1,2,3]
y=[1,2,3]
z=x

print(x is y)
print(x is z)
print(x==y)

#membership
print(1 in x)
print(5 not in x)