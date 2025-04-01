def bill_amt(reqd_gems,reqd_quantity):
    bill = 0
    gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
    price_list=[1760,2119,1599,3920,3999]
    for i in range(len(reqd_gems)):
        if reqd_gems[i] in gems_list:
            index = gems_list.index(reqd_gems[i])
            bill += price_list[index]*reqd_quantity[i]
        else:
            return -1
    
    if bill > 30000:
        bill *=0.95
    
    return round(bill, 2) 



reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]

bill = bill_amt(reqd_gems,reqd_quantity)

if bill == -1:
    print("Total Bill Amount: -1 (Some gems are not available)")
else:
    print(f"Total Bill Amount: {bill}")