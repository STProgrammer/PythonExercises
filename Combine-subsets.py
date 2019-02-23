class Numbers():
    def number_sets(nums):
        nums = sorted(nums)

        x = len(nums)-1
        y = 0

        for i in range(0,x+1):
            y += 2**i

        sets = [0]*(y+1)
        sets[0] = []

        j = 1
        i = 0
        k = int()
        while j <= y:
            if j == 2**i:
                sets[j] = [nums[x - i]]
                i += 1
                j += 1
                k = 1
            else:
                sets[j] = sets[2**(i-1)] + sets[k]
                k += 1
                j += 1

        return sets

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6,2,4,6,7]))

print("""Make a list of integers and the program will get all
possible unique subsets from a set of distinct integers n\.""")

repeat = True  
repeat2 = True

nums = list()

while repeat == True:   
    while repeat == True:
        try:
            number = int(input("""Type in a number and press enter
    to add to the list (press a letter to finish):"""))        
            nums.append(number)
            print(nums)
        except ValueError:
            repeat = False
    sets = Numbers.number_sets(nums)
    print("\n The integer set is: \n",nums,
          "\n all the unique subsets aresets are: \n",sets)
    repeat = True
    nums = list()
    sets = list()
    answer = input("""Press "q" to quit, or any key to continue:""")
    if answer == "q":
        repeat = False
    

    
