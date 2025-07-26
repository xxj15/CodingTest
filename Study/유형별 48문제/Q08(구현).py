# 문자열 재졍렬
chars = []
nums = []
for x in input():
  if x.isalpha(): 
    chars.append(x)
  else : 
    nums.append(int(x))

chars.sort()
sum_nums = sum(nums)

chars.append(str(sum_nums))
print(''.join(chars))

