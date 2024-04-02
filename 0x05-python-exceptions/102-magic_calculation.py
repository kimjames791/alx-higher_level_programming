def magic_calculation(a, b):
    result = 0

    for k in range(1, 4):
        try:
            if k > a:
                raise Exception('Too far')
            result += (a ** b) / k
        except:
            result += a + b
            break

    return result
