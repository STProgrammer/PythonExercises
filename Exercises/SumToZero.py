def input_list():
    print("""type in an integer and press enter to add it
to the list (press any letter to finish), """)
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
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


class PySolutions:
    def sum_to_zero(self, listt):
        finallist = []
        for i in range(0,len(listt)):
            for j in range(i+1,len(listt)):
                for k in range(j+1, len(listt)):
                    if listt[i] + listt[j] + listt[k] == 0:
                        elements = list()
                        elements = [listt[i], listt[j], listt[k]]
                        elements = sorted(elements)
                        if elements not in finallist:
                            finallist += [elements]
        return finallist

listt = input_list()

print(PySolutions().sum_to_zero(listt))

print(py_solution().threeSum(listt))
