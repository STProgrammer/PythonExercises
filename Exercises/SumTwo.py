class PythonSolutions:
    def sum_target(self, listt, target):
        for i in range(0, len(listt)):
            for j in range(0, len(listt)):
                if i == j:
                    continue
                else:
                    test = listt[i] + listt[j]
                    if test == target:
                        return (i+1,j+1)

def input_list():
    print("""type in an integer and press enter to add it
to the list (press any letter to finish), """)
    a = ""
    listt = []
    while True:
        try:
            a = input("Add an integer to the list: ")
            a = int(a)
            listt += [a]
        except ValueError:
            break
    return listt



class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            print(num)
            if target - num in lookup:
                return(lookup[target - num] + 1, i + 1)
            lookup[num] = i
            print(lookup)

            
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

listt = input_list()
print(listt)
target = input("Type in a target number: ")
target = int(target)
print("%d, %d" % PythonSolutions().sum_target(listt, target))
