num_d = int(input("for how many days do you have sales?"))
with open('sales.txt','w') as sales_file:
    for count in range(1,num_d +1):
        sales = float(input(f'enter the sales for days #{count}: '))
        sales_file.write(str(sales) + '\n')
    print('data writeten to sales.txt')