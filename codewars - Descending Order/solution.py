def descending_order(num):
    num_dict = {}
    for n in range(10):
        num_dict[n] = 0
    for n in str(num):
        num_dict[int(n)] += 1
    return_num = ""
    for key in range(9, -1, -1):
        return_num += (str(key) * num_dict[key])
    return int(return_num)

def assertEquals(a, b):
    if a != b:
        raise Exception('%s is not equal to %s' % (a, b))

assertEquals(descending_order(0), 0)
assertEquals(descending_order(15), 51)
assertEquals(descending_order(123456789), 987654321)
assertEquals(descending_order(998899), 999988)