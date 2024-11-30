"""
- You sell lemonade over two weeks, the lists show number of lemonades sold per week
- Profit for each lemonade sold is 1.5$

1. Add another day to week 2 list by capturing a number as input
2. Combine the two lists into the list called 'sales'
3. Calculate and print how much you have earned on 
4. Best day
5. Worst day
6. Seperated and in total
Hints: 3 prints in total
"""

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
sales_w2.append(int(input("Enter the sale of today: ")))
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()
worst_day_sale = sales[0] * 1.5
best_day_sale = sales[-1] * 1.5
print("Sales: ", sales)
print("Best Day Sale: $", best_day_sale)
print("Worst Day Sale: $", worst_day_sale)
print(f"Combined Profit: ${best_day_sale + worst_day_sale}")