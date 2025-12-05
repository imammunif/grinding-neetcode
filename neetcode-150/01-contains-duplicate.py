nums = [1, 2, 3, 3]

def hasDuplicate(nums: list) -> bool:
    hashMap = set()
    for num in nums:
        print(f'checking {num}')
        if num in hashMap:
            # print("True")
            return True
        else:
            hashMap.add(num)
    # print("False")
    return False  

print(hasDuplicate(nums))