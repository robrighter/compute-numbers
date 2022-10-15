class Compute:
    
    
    def check_for_repeat(self, ret):
        sp = ret.split(".")
        if len(sp) == 0:
            return ""
        s = sp[1]
        if len(s.replace('0','')) == 0:
            return ""
        s1 = s[0:int(len(s)/2)]
        s2 = s[int(len(s)/2):len(s)]
        if (s1 == s2):
            return s1
        else:
            return ""

    def divide(self, numerator, denominator):
        n=int(numerator)
        d=int(denominator)
        remainder=int(n)
        ret=""
        first=True
        while (remainder > 0):
            #print(remainder)
            #print(ret)
            result = int(remainder/d)
            ret = ret+str(result)
            remainder = remainder - (result*d)
            #print(remainder)
            if first:
                if remainder != 0:
                    ret=ret+"."
                first=False
            else:
                repeat = self.check_for_repeat(ret)
                if repeat != '':
                    return { 'repeat': True, 'value': ret, 'repeat_value': repeat }
            remainder=remainder*10
        return { 'repeat': False, 'value': ret }

    def factorial(self, n):
        ret = int(1);
        while n > 0:
            ret = ret * int(n)
            n = n - 1
        return ret

    def e(self):
        numerator = int(2)
        denominator = int(1)
        for i in range(2, 5):
            fact = self.factorial(i)
            next_denominator = fact * denominator
            next_numerator = (numerator * fact) + (denominator * 1)
            numerator = next_numerator
            denominator = next_denominator
            print(i)
        print(str(numerator) + " / " + str(denominator) )
        return self.divide(numerator, denominator)
            
        
