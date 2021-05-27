from time import sleep
import random

customer = ['c' + str(i) for i in range(1000)]
quantity = [i for i in range(1, 11)]
product = ['p' + str(i) for i in range(1000)]
price = {i: int(i[1:]) + 17 for i in product}

for i in range(1000):
    t_customer = random.choice(customer)
    t_product = random.choice(product)
    t_quantity = random.choice(quantity)
    t_price = t_quantity * price[t_product]

    t_data = str(t_customer) + ' ' + str(t_product) + ' ' + str(t_quantity) + ' ' + str(t_price) + '\n'
    print(t_data)

    file1 = open("server.log", "a")  # append mode
    file1.write(t_data)
    file1.close()

    sleep(5)