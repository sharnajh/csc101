# print(format(0.2, '%'))
# print(format(0.2, '.0%')) ANSWER
# print(format(0.2 * 100, '.0%'))
# print(format(20, '.0%'))

# price = int(68.549)
# print(price)

# x = 5
# y = 3
# z= 8
# print(not (x < y or z > x) and y < z)

# x = 5
# y = 3
# z = 8
# print(x < y or z > x)

# for num in range(0, 20, 5):
#     num += num
# print(num)

# def test():
#     for i in range(1,5):
#         print(i)
#     print("TEST")

# count = 4
# while count < 12:
#     print("counting")
#     count = count + 2

# for num in range(4):
#     print(num)

    
# for num in range(1, 5):
#     print(num)

# total = 0
# for count in range(1,4):
#   total += count
# print(total)

def main():
    value = 99
    print(f'The value is {value}')
    change_me(value)
    print(f'Back in main the value is {value}')

    def change_me(arg):
        print(f'I am changing the value.')
        arg = 0
        print(f'Now the value is {arg}')


def main2():
    print(f'The sum of 12 and 45 is')
    show_sum(12,45)
    def show_sum(num1,num2):
        result = num1 + num2
        print(result)
        