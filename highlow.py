def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers_low = min(numbers)
    numbers_high = max(numbers)
    high_and_low_num = "{} {}".format(numbers_high, numbers_low )
    return high_and_low_num
# clever 
def high_and_low_c(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
