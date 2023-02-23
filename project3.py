salesperson_revenue = {
    "Ben":0,
    "David":0,
    "Goodluck": 0,
    "Sue": 0
}

def enter_revenue(name, revenue):
    global salesperson_revenue
    salesperson_revenue[name] += revenue

while True:
    name = input("Employee name: ")
    if name == "quite":
        break
    revenue = int(input("Enter revenue: "))
    enter_revenue(name, revenue)
    print(f"{name}'s revenue is {salesperson_revenue[name]}")

print(salesperson_revenue)