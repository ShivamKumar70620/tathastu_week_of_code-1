cp=int(input("Enter cost price of the product"))
sp=int(input("Enter selling price of the product"))
if(sp>cp):
    print("Profit gain from this sell is",sp-cp)
else:
    print("NO profit gained")
new_sp=cp+(sp-cp)*((105)/100)
print("New selling price to increase profit by 5% is",new_sp)