num1 = 0 #582097494459230781640628620899862803482534211706798214808651328230
num2 = 0#664709384460955058223172535940812848111745028410270193852110555964
num3 = 0#462294895493038196442881097566593344612847564823378678316527120190
num4 = 0#914564856692346034861045432664821339360726024914127372458700660631
num5 = 0#558817488152092096282925409171536436789259036001133053054882046652
num6 = 0#138414695194151160943305727036575959195309218611738193261179310511
num7 = 0#854807446237996274956735188575272489122793818301194912983367336244
num8 = 0#6566430860213949463952247371907021798
sums = 0
while num1 > 0:
    sums = sums + num1 % 10
    num1 = num1 // 10
while num2 > 0:
    sums = sums + num2 % 10
    num2 = num2 // 10
while num3 > 0:
    sums = sums + num3 % 10
    num3 = num3 // 10
while num4 > 0:
    sums = sums + num4 % 10
    num4 = num4 // 10
while num5 > 0:
    sums = sums + num5 % 10
    num5 = num5 // 10
while num6 > 0:
    sums = sums + num6 % 10
    num6 = num6 // 10
while num7 > 0:
    sums = sums + num7 % 10
    num7 = num7 // 10
while num8 > 0:
    sums = sums + num8 % 10
    num8 = num8 // 10
print(sums)

