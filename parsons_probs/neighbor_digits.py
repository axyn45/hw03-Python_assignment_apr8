def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if prev_digit==-1:
        return neighbor_digits(str(num),0)
    elif len(num)-2==prev_digit:
        if num[prev_digit+1]==num[prev_digit]:
            if prev_digit==0:
                return 2
            elif num[prev_digit]!=num[prev_digit-1]:
                return 2
            else:
                return 1
        else:
            return 0
    else:
        if num[prev_digit+1]==num[prev_digit]:
            if prev_digit==0:
                return 2+neighbor_digits(num,prev_digit+1)
            elif num[prev_digit]!=num[prev_digit-1]:
                return 2+neighbor_digits(num,prev_digit+1)
            else:
                return 1+neighbor_digits(num,prev_digit+1)
        else:
            return neighbor_digits(num,prev_digit+1)

# print(neighbor_digits(112))