

def calculate_sum(start, end, str_num):
	sum = 0
	for i in range(start, end):
	 sum += int(str_num[i])
	return sum

def substring_10(num):
  str_num = str(num)
  start = 0
  end = 1
  sum = 0
  pos_set = set()
  while not end == len(str_num)+1:
    sum = calculate_sum(start, end, str_num)
    if sum < 10:
      end += 1
    elif sum > 10:
      if not start in pos_set:
        return False
      start += 1
    elif sum == 10:
      for i in range(start, end):
        pos_set.add(i)
      end += 1
  return pos_set == set(range(0, len(str_num)))

def count_substrings_10(exponent):
  sum = 0
  for i in range(0, 10**exponent):
    if substring_10(i):
      sum += 1
  return sum

print(count_substrings_10(5))