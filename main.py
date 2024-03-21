def calculate_discount(sale_amount):
    if sale_amount <= 5000:
        return sale_amount * 0.05
    elif sale_amount <= 15000:
        return sale_amount * 0.12
    elif sale_amount <= 25000:
        return sale_amount * 0.20
    else:
        return sale_amount * 0.30

def compute_net_amount(transactions):
    net_amount = 0
    for trans_type, amount in transactions:
        if trans_type == 'D':
            net_amount += amount
        elif trans_type == 'W':
            net_amount -= amount
    return net_amount

def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

def capitalize_characters(input_str):
    output_str = ''
    for char in input_str:
        if 'a' <= char <= 'z':
            output_str += chr(ord(char) - 32)
        else:
            output_str += char
    return output_str

def update_list(my_list):
    my_list.insert(1, "Peter")

    my_list[2] = "Smek"

    del my_list[3]

    num_items = len(my_list)

    return my_list, num_items

choice = int(input("Enter your choice:\n1. Calculate discount\n2. Compute net amount\n3. Check perfect number\n4. Capitalize characters\n5. Update list\n"))

if choice == 1:
    sale_amount = float(input("Enter the sale amount: "))
    print("Discount:", calculate_discount(sale_amount))

elif choice == 2:
    transactions = []
    while True:
        transaction = input("Enter transaction (Enter D for Deposit/W for Withdrawal): ").split()
        transactions.append((transaction[0], int(transaction[1])))
        cont = input("Want to continue (Y for yes/N for No): ")
        if cont.upper() == 'N':
            break
    print("Net amount:", compute_net_amount(transactions))

elif choice == 3:
    number = int(input("Enter a number to check if it's perfect: "))
    if is_perfect_number(number):
        print(number, "is a perfect number.")
    else:
        print(number, "is not a perfect number.")

elif choice == 4:
    input_str = input("Input: ")
    print("Output:", capitalize_characters(input_str))

elif choice == 5:
    my_list = ["Sarka", "Monica", "James", "Victor"]
    updated_list, num_items = update_list(my_list)
    print("Updated list:", updated_list)
    print("Number of items in the list:", num_items)

else:
    print("Invalid choice!")
