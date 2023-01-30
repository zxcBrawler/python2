month_31 = '12345678910111213141516171819202122232425262728293031'
month_30 = '123456789101112131415161718192021222324252627282930'
month_29 = '1234567891011121314151617181920212223242526272829'
month_28 = '12345678910111213141516171819202122232425262728'

def yearType(count):
    array = list(map(int,month_31))
    a = (sum(array))
    array.clear()
    array = list(map(int,month_30))
    b = (sum(array))
    array.clear()

    if (count == 1):
        array = list(map(int,month_29))
    else:
        array = list(map(int,month_28))

    c = (sum(array))
    array.clear()
    print(a * 7 + b * 4 + c)

print('Input year')
year = int(input())

if (year % 4 == 0 or year % 400 == 0):
    print('Leap year')
    yearType(1)
else:
    yearType(0)   