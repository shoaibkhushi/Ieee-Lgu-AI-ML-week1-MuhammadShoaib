#expenes
def add_expense(expenses):
    print("---Add Expense---")
    title = input("EnterExpense Name: ")
    amount = float(input(f"Enter Amount for {title}: "))
    category = input("Enter Category (Food, Transport, Books, Bills): ")
    expense ={
        "title":title,
        "amount":amount,
        "category":category
    }
    expenses.append(expense)
    print("Item Added Successfully")

expenses = []
#display All Expense
def view_expenses(expenses):
    print("---All Expenses---")

    if not expenses:
        print("Not Any Expenses Yet")
        return
    print(f"{'Title':<20} {'Amount':<15} {'Category':>10}")
    print("-"*50)

    for exp in expenses:
        print(f"{exp['title']:<20} {exp['amount']:<15.2f} {exp['category']: >10}")
#Summary Analysis
def summaru_analysis(expenses):
    print("---------Spending Summary & Analytics--------")
    if not expenses:
        print("No Expensis Show Summary for Anlytics")
        return
    total = sum(exp["amount"] for exp in expenses)
    print("-"*50)
    print(f"Total Spent: {total:.2f}")
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("-"*50)
    print("Spending by Category:")
    for cat, amount in category_totals.items():
        print(f"   • {cat}: {amount:.2f}")
    print("-"*50)
    
    # 3. Highest Expense
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"Highest Expense: {highest['title']} ({highest['category']}) - {highest['amount']:.2f}")
    print("-"*50)
while True:
    print("1.Add Expenses")        
    print("2.View All Expense")        
    print("3.View Spending Summary & Analytics")        
    print("4:Exist")  

    choice = input("Enter Your Choice...")
    match choice:
        case "1" :
            add_expense(expenses)
        case "2":
            view_expenses(expenses)
        case "3":
            summaru_analysis(expenses)    
        case "4":
            print("Goodbye Exist")
            break
        case _:
            print("Invalid Choice Please Enter Valid Choice")

            