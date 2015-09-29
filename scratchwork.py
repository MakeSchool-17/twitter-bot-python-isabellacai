nums = [5, 2, 8, 4, 9]


def sum():
    total = nums[0]+nums[1]+nums[2]+nums[3]+nums[4]
    print(total)

sum()


# def sumthing():
#     for x in range(nums[0], len(nums)-1):
#
#
#
# sumthing()

def sumthing():
    total = 0
    for x in nums:
        total += x
    print(total)

sumthing()
