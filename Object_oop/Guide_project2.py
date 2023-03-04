class HealthInsurance:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, num_of_employee, num_of_client):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employee = num_of_employee
        self.num_of_client = num_of_client

    def print_report(self):
        print(f"The company {self.company_name} was found in {self.foundation_year}. The founder of the company is {self.founder_name}. company slogan: {self.company_slogan} Number of clients {self.num_of_client}")

    def sup_health_insurance(self, age, chronic_disease, income):
        if age >= 60 and chronic_disease == True and income < 6000:
            print("We are sorry! you are not eligible for supplemental health insurance")
        elif age < 60 and income >= 6000 or chronic_disease == False:
            print("Congratulations! You can get supplement health insurance")
        
    def update_num_clients(self, new_number):
        self.num_of_client = new_number
        print(f"Number of clients has been changed to {self.num_of_client} ")

RI_company1 = HealthInsurance("Healthy", 2012, "Bob Mayer", "we care for you.", 3500, 13230)

RI_company1.sup_health_insurance(45, False, 5000)
RI_company1.update_num_clients(13231)
RI_company1.print_report()


# Company Two

class LogisticData:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, inventory_space):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventory_space = inventory_space

    def print_report(self):
        print(f"The company {self.company_name} was found in {self.foundation_year}. The founder of the company is {self.founder_name}. company slogan: {self.company_slogan} Inventory space of the company {self.inventory_space}")

    def update_inventory_space(self, new_storage_space):
        self.inventory_space = new_storage_space
        print(f"Inventory space has been changed to {self.inventory_space}!")
         
logistic_company1 = LogisticData("LogCom", 1990, "Laura McCartey", "There is no place towe cannot reach.", 2500)

logistic_company1.update_inventory_space(3000)
logistic_company1.print_report()

# Company Three

class Trading:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, sales, expenses, revenue="python"):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.sales = sales
        self.expenses = expenses
        self.revenue = revenue

    def print_report(self):
        print(f"The company {self.company_name} was found in {self.foundation_year}. The founder of the company is {self.founder_name}. company slogan: {self.company_slogan} Total sales:{self.sales} Total expenses: {self.expenses} Total revenue: {self.revenue}")

    def update_sales_and_expenses(self, new_sales, new_expenses):
        self.sales += new_sales
        self.expenses += new_expenses
        print("Sales and expenses are updated")

    def calculate_revenue(self):
        self.revenue = self.sales = self.expenses
        print(f"The revenue of the company is: {self.revenue}")

trading_company = Trading("TraCom", 2005, "chong Wu", "We revolutionize trading.", 3850, 1720, 1838)

trading_company.update_sales_and_expenses(100,50)
trading_company.calculate_revenue()
trading_company.print_report()