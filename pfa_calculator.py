print("""
Freelancer Net Income Calculator (Romanian Tax Model)

""")

def main():
    gross_income = get_input_float("Enter gross income (in RON): ")
    revenue=get_input_timeline("Is this annual or monthly? ", gross_income)
    deductible=get_input_float("Enter expense value (or 0 if none): ")

    revenue=revenue-deductible
    if revenue<0:
        print("The business is operating at a loss, there is no net income.")
        return
    
    CAS, CASS = calculate_pfa_taxes(revenue)
    income_tax=(revenue-CAS-CASS)*0.1
    net_income=revenue-CAS-CASS-income_tax

    print("Net annual income is:", f"{net_income:,.0f} RON".replace(",", "."))
    print("Net monthly income is:", f"{net_income/12:,.0f} RON".replace(",", "."))

def calculate_pfa_taxes(revenue):
    if revenue<48600:
        CAS=0
    elif 48600<=revenue<97200:
        CAS=12150
    else:
        CAS=24300

    if revenue<24300:
        CASS=2430
    elif 24300<=revenue<291600:
        CASS=0.1*revenue
    else:
        CASS=29160

    return CAS,CASS

def get_input_float(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value<0:
                print("Please enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_input_timeline(prompt, gross_income):
        while True:
            timeline=input(prompt).lower().strip()
            if timeline=="monthly":
                return gross_income*12
            elif timeline=="annual":
                return gross_income
            else:
                print("Please enter 'annual' or 'monthly'.")

main()