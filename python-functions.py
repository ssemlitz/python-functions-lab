# Challenge 1
def sum_to(num):
  sum = 0
  for x in range(1, num + 1):
    sum += x
  return sum

# Challenge 2
def largest(nums):
  return max(nums)

print(largest([10, 4, 2, 231, 91, 54]))

# Challenge 3
def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'e'))

# Challenge 4
def product(*args):
  product = 1
  for x in args:
    product *= x
  return product

print(product(4, 0.5, 5))


