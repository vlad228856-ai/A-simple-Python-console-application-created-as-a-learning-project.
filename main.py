
numberss =[1 , 2 ,4 ,-6 ,7, -9]
def ger_numbers():
    numbers = []
    while True:
        x = int(input("введите число"))
        if x == 0:
            break
        numbers.append(x)
    return numbers
ger_numbers           
def sum_positive(numberss):
    total = 0
    for n in numberss :
        if n > 0 :
            total += n
    return total
def count_even(numberss):
    count = 0
    for n in numberss:
        if n %2 == 0:
            count +=1
    return count
def average(numberss):
    sum = 0
    countt = 0
    for n in numberss:
        countt +=1
        sum +=n
    average  = sum / countt
    return average
def second_max(numberss):
    if numberss[0] > numberss[1]:
        max1 = numberss[0]
        max2 = numberss[1]
    else:
        max1 = numberss[1]
        max2 = numberss[0]
        for n in numberss[2:]:
            if n > max1:          
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return max2
def main():
    numbers = ger_numbers()
    print("numbers", numbers)
    print("sum_positive",sum_positive (numbers))
    print("count_even", count_even (numberss))
    print("average",average (numberss))
    print("second_max", second_max(numberss))
main()