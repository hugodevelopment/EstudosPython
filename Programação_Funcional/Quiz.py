
# What is the result of this code?
# Aqui temos um conjunto
nums = {1, 2, 3, 4, 5, 6}
# Agora temos outro conjunto que faz intersecção com o 1º, isto é, os elementos em comum {1,2,3}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)

print(len(list(nums)))

# for i in nums:
#     print(i)

