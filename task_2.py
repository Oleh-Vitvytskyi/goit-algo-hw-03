import random

def get_numbers_ticket(min_num, max_num, quantity):
    if quantity > (max_num - min_num + 1):
        raise ValueError("Кількість чисел перевищує діапазон унікальних значень")

    return random.sample(range(min_num, max_num + 1), quantity)

min_num = 1
max_num = 36
quantity = 5

ticket_numbers = get_numbers_ticket(min_num, max_num, quantity)
print(ticket_numbers)
