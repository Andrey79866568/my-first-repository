import sys


def is_correct_mobile_phone_number_ru(number):
    try:
        assert number
        number = ''.join(''.join(number.split(' ')).split('-'))
        if not(number[0] == '8' or number[:2] == '+7'):
            raise ValueError
        elif number[0] == '8':
            number = number[1:]
        else:
            number = number[2:]
        number = number.split('(')
        w = len(number)
        assert (w == 2 or w == 1) and ')' not in number[0]
        number = ''.join(number)
        number = number.split(')')
        assert len(number) == w
        number = ''.join(number)
        assert number.isdigit()
        number = number[3:]
        assert len(number) == 7
        return True
    except (ValueError, AssertionError):
        return False


def test_funk(func):
    test_list = [
        ("8 960 527-88-36", True),
        ("+7(931) 4234559", True),
        ("+7-(931)-666-222-2", True),
        ("-79315283333", False),
        ("9(228)333-6764", False),
        ("+7(2345)22-22-222", False),
        ("8 960 527-88-366", False),
        ("8!960!444|44|44", False),
        ("-7(9800)222332233", False)
    ]
    for test in test_list:
        if func(test[0]) != test[1]:
            print('NO')
            return
    print('YES')


numb = sys.stdin.readline()
if numb:
    if is_correct_mobile_phone_number_ru(numb):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
