class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = None
        if numerator * denominator < 0:
            flag = False
        else: flag = True
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer = numerator // denominator
        numerator = numerator % denominator * 10
        decimal = []
        decimal_val = []
        index = -1
        
        while numerator != 0:
            if numerator not in decimal:
                decimal.append(numerator)
                decimal_val.append(str(numerator // denominator))
                numerator = numerator % denominator * 10
            else:
                index = decimal.index(numerator)
                break 
                
        if not decimal_val:
            ans = str(integer)
        else:
            if index == -1:
                ans = str(integer) + "." + "".join(decimal_val[:])
            else:
                d = "".join(decimal_val[:index]) + "(" + "".join(decimal_val[index:]) + ")"
                ans = str(integer) + "." + d
        
        if flag:
            return ans
        else:
            return "-" + ans
