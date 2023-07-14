def main():
    print("This is a monthly load payment calculator")
    print("")


    principle = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate:  "))
    years = float(input("Enter the amount of years: "))

    monthly_interest = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principle * monthly_interest / (1 - (1 + monthly_interest) ** (-amount_of_months))

    print("The monthly payment : %.2f "  % (monthly_payment))
main()