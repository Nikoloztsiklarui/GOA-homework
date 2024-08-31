def goa(numbers):
    if not numbers:
        return  None
    total= sum(numbers)
    count= len(numbers)
    return total/count
numbers_list= [3, 4, 5, 6,]
average= goa(numbers_list)
print(average)

