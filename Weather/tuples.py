def partition(num):
    if num % 2 == 0:
        x = (num, None)
    else:
        x = (None, num)
    return x

def partition_list(list):
    response = []

    for num in list:
        response.append(partition(num))
    return response

listone = [2,6,1,78,9,1,99,34]





print(partition_list(listone))