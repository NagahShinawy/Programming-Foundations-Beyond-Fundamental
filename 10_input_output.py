"""
created by Nagaj at 17/06/2021
"""

with open("values.txt", "rt") as inf:
    lines = [line.strip() for line in inf.readlines()]

outfile = open("total.txt", "wt")

for line in lines:
    print(line, file=outfile)  # print line not to console but to file obj

total = sum([int(num) for num in lines])
print(f"{'#' * 30}\nTotal: {total}", file=outfile)
outfile.close()
