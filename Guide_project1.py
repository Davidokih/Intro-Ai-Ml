my_name = "David"
my_surname = "Okih"
my_age = 19
ID_number = 123456789
where_i_live = "Nigeria"
health_insurance = False

# Making use of F strings
print(f"My name is {my_name} {my_surname} I am {str(my_age)} years old, I live in {where_i_live}")

item_list  = ["Laptop", "Headset", "Second monitor", "Mousepad", "USB drive", "External drive"]

print(item_list)

mandatory_item_list = item_list[0:3]
optional_item_list = item_list[3:6]

print(mandatory_item_list)
print(optional_item_list)

price_sheet = {
    "Laptop":1500,
    "Headset":100,
    "Second monitor":200,
    "Mousepad":50,
    "USB drive":70,
    "External drive":250
}

cart = []

def add_to_cart(item,quantity):
    cart.append((item,quantity))
    item_list.remove(item)

def create_invoice():
    total_amount_inc_tax = 0
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.10 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print("Item", item, "\t", "price", price, "\t", "Quantity", quantity, "\t", "Tax", tax, "\t" "Total", total, "\n")
    
    print("After the taxes are applied the total amount is:", "\t", total_amount_inc_tax)

    return total_amount_inc_tax

def checkout():
    global limit
    # limit = -1
    total_amount = create_invoice()
    if limit == 0:
        print("You don't have any budget")
    elif total_amount > limit:
        print("The amount you have to pay is above the apending limit. You have to drop some item")
    else:
        limit -= total_amount
        print(f"The total amount (incl. taxes) you've paid is {total_amount}. You have {limit} dollare left")

add_to_cart("Laptop", 1)
add_to_cart("Headset", 3)
add_to_cart("Second monitor", 2)
add_to_cart("Mousepad", 2)
add_to_cart("USB drive", 1)
add_to_cart("External drive", 1)

checkout()