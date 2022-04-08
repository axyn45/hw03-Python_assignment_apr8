def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    if(len(str(n))==1):
        if(len(str(seq))!=1):
            return False
        elif str(n)==str(seq):
            return True
        else: return False
    if(len(str(seq))==1):
        if(str(n)[0]==str(seq)[0]):
            return True
        else: return has_subseq(str(n)[1:],str(seq))
    
    if(str(n)[0]==str(seq)[0]):
        return has_subseq(str(n)[1:],str(seq)[1:])
    else:
        return has_subseq(str(n)[1:],str(seq))

# print(has_subseq(144, 12))