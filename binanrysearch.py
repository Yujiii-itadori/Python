
# function that takes list and target parameters 
# multiple variables; middle, start, end and amount of time or steps
# can use while or recursion loop

def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0 

    while(start <= end):
        print("Steps ", steps, ":", str(list[start:end+1]))


        steps = steps +1
        middle =( start + end ) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else: #element > list 
            start = middle +1
            
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

binary_search(my_list, target)