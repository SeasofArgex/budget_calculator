def main():
    
    print("Welcome to the Budget Calculator!")
    
    # Get user inputs
    income = float(input("Enter your total monthly income: "))
    housing = float(input("Enter your monthly rent/mortgage payment: "))
    utilities = float(input("Enter your total monthly utilities cost: "))
    groceries = float(input("Enter your total monthly groceries cost: "))
    transportation = float(input("Enter your total monthly transportation cost: "))
    entertainment = float(input("Enter your total monthly entertainment cost: "))
    debt_payments = float(input("Enter your total monthly debt payments: "))
    childcare = float(input("Enter your total monthly childcare cost (if any, else enter 0): "))
    savings_goal = float(input("Enter your monthly savings goal: "))
    
    # Calculate total expenses
    total_expenses = housing + utilities + groceries + transportation + entertainment 
    + debt_payments + childcare
    
    # Calculate remaining budget
    remaining_budget = income - total_expenses - savings_goal
    
    # Display results
    print("\n--- Budget Summary ---")
    print(f"Total Monthly Income: ${income:.2f}")
    print(f"Total Monthly Expenses: ${total_expenses:.2f}")
    print(f"Monthly Savings Goal: ${savings_goal:.2f}")
    
    if remaining_budget > 0:
        print(f"You are within your budget! You have ${remaining_budget:.2f} left after expenses and savings.")
    elif remaining_budget < 0:
        print(f"You are over budget by ${-remaining_budget:.2f}.")
    else:
        print("You have exactly balanced your budget with no money left over.")

if __name__ == "__main__":
    main()