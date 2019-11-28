
def get_don_list(int_a, int_b):
    """get the devided denominator list"""
    int_a = int(int_a)
    int_b = int(int_b)
    don_list = 1
    if int_a == 1:
        return 1
    elif int_a == 2:
        if int_b % int_a == 0:
            return 2
        else:
            return 1
    else:
        for i in range(2, int_a):
            if int_a % i == 0 and int_b % i == 0:
                don_list *= i
                rec_don = get_don_list(int_a/don_list, int_b/don_list)
                return rec_don * don_list
            elif i == int_a - 1:
                return don_list

def get_don_list_2(int_a, int_b):
    """get the devided denominator list"""
    int_a = int(int_a)
    int_b = int(int_b)
    for i in range(1, int_a+1):
        if int_a % i == 0 and int_b % i == 0:
            don_list = i
    return don_list

def get_don_list_3(int_a, int_b):
    if int_a == 0:
        return 0
    while int_b % int_a != 0:
        m = int_b
        n = int_a
        int_b = n
        int_a = m%n
    return int_a

class Fraction:
    """model a fraction data type"""

    def __init__(self, num, den):
        """initialize the instance of fraction"""
        self.num = num
        self.den = den

    def __str__(self):
        """show the slash form"""
        return f"{self.num}/{self.den}"

    def __add__(self, frac):
        """override the add operator"""
        final_num = self.num * frac.den + frac.num * self.den
        final_den = self.den * frac.den
        com_divide = get_don_list_3(final_num, final_den)

        # // get the quotient
        return "%d/%d" % (final_num//com_divide, final_den//com_divide)

    def __eq__(self, frac):
        """
        compare two instances of fraction based on the value, instead of reference
        """
        if self.num * frac.den == self.den * frac.num:
            return True
        else:
            return False

    def __sub__(self, frac):
        """override the minus operator"""
        final_num = self.num * frac.den - frac.num * self.den
        if final_num < 0:
            signal = -1
            final_num *= -1
        else:
            signal = 1
        final_den = self.den * frac.den
        com_divide = get_don_list_3(final_num, final_den)

        # // get the quotient
        if com_divide == 0:
            return 0
        elif final_den//com_divide == 1:
            return signal * final_num//com_divide
        else:
            return "%d/%d" % (signal * final_num//com_divide, signal * final_den//com_divide)

    def __mul__(self, frac):
        """override the multiply operator"""
        final_num = self.num * frac.num
        final_den = self.den * frac.den
        com_divide = get_don_list_3(final_num, final_den)

        # // get the quotient
        return "%d/%d" % (final_num//com_divide, final_den//com_divide)

    def __truediv__(self, frac):
        """override the divide operator"""
        final_num = self.num * frac.den
        final_den = self.den * frac.num
        com_divide = get_don_list_3(final_num, final_den)

        # // get the quotient
        if com_divide == 0:
            return 0
        elif final_den//com_divide == 1:
            return final_num//com_divide
        else:
            return "%d/%d" % (final_num//com_divide, final_den//com_divide)

my_fraction = Fraction(3,4)
my_fraction4 = Fraction(3,4)
my_fraction2 = Fraction(34,84)
my_fraction3 = my_fraction
print(my_fraction)
print(my_fraction + my_fraction2)
print(my_fraction == my_fraction3)
print(my_fraction == my_fraction4)
print(my_fraction * my_fraction4)
print(my_fraction / my_fraction4)
print(my_fraction - my_fraction4)


# Python magic methods or special functions for operator overloading
# Binary Operators:
# Operator 	Magic Method
# + 	__add__(self, other)
# – 	__sub__(self, other)
# * 	__mul__(self, other)
# / 	__truediv__(self, other)
# // 	__floordiv__(self, other)
# % 	__mod__(self, other)
# ** 	__pow__(self, other)
# Comparison Operators :
# Operator 	Magic Method
# < 	__lt__(self, other)
# > 	__gt__(self, other)
# <= 	__le__(self, other)
# >= 	__ge__(self, other)
# == 	__eq__(self, other)
# != 	__ne__(self, other)
# Assignment Operators :
# Operator 	Magic Method
# -= 	__isub__(self, other)
# += 	__iadd__(self, other)
# *= 	__imul__(self, other)
# /= 	__idiv__(self, other)
# //= 	__ifloordiv__(self, other)
# %= 	__imod__(self, other)
# **= 	__ipow__(self, other)
# Unary Operators :
# Operator 	Magic Method
# – 	__neg__(self, other)
# + 	__pos__(self, other)
# ~ 	__invert__(self, other)