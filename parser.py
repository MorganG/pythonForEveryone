import re
# Short Quiz print( sum( [ ****** *** * in **********('[0-9]+',regex_sum_6060.txt.read()) ] ) )


numbers = list()
numsum = 0
handler = open('regex_sum_6060.txt')
for line in handler:
    line = line.strip()
    nums = re.findall('([0-9]+)', line)
    if len(nums) <= .5 : continue
    for n in nums:
        ns = n.split()
        for i in ns:
            x = int(i)
        numsum = numsum + x
print(numsum)
