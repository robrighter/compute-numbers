class Compute:
    #todo: Write a function that can calculate the accuracy of iteration n (Calculate the n+1 term and count the leading zeros
    #todo: Make an option for the divide function that generates digits up to a given number of decimal places ignoring repeats
    
    def determine_if_repeating_fraction(self, numerator, denominator):
            reduced = self.reduce_fraction(numerator, denominator)
            d=int(reduced['denominator'])
            #the maximum numbers before the repeat is the max of the power of 2 vs the power of 5
            #the maximum period of the repeat is d-1 (https://mathworld.wolfram.com/DecimalPeriod.html)
            power_of_2=0
            power_of_5=0
            while( ( (d%2) == 0 ) or ( (d%5) == 0 ) ): 
                if( (d%2) == 0 ):
                    d=int(d/2)
                    power_of_2=power_of_2+1
                if( (d%5) == 0 ):
                    d=int(d/5)
                    power_of_5=power_of_5+1
            if( d==1 ):
                return {"is_repeating": False }
            else:
                return {"is_repeating": True, "max_nonrepeat": max(power_of_2,power_of_5), "max_repeat": int(reduced['denominator']-1) } 
    
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

    def reduce_fraction(self, numerator, denominator):
        n=int(numerator)
        d=int(denominator)
        i=2
        min_term = min(n,d)
        while( i<=(min_term) ):
            if( (n%i)==0 and (d%i)==0 ):
                n = (n/i)
                d = (d/i)
                i=2
            else:
                if(i==2):
                    i=i+1
                else:
                    i=i+2
                if(i%33333333 == 0):
                    pass
                    #print(i)
                    #print(min_term/i)
        return {"numerator":int(n), "denominator":int(d)} 
    
    def divide_generator(self, numerator, denominator):
        n=int(numerator)
        d=int(denominator)
        remainder=int(n)
        ret=""
        first=True
        while (remainder > 0):
            result = int(remainder/d)
            ret = ret+str(result)
            remainder = remainder - (result*d)
            if first:
                if remainder != 0:
                    ret=ret+"."
                first=False
            remainder=remainder*10
            for i in range(0, len(ret)):
                yield(str(ret[i]))
            ret=""
        yield("\n")


    def divide(self, numerator, denominator):
        reduced = self.reduce_fraction(numerator, denominator)
        n=reduced['numerator']
        d=reduced['denominator']
        is_repeating = self.determine_if_repeating_fraction(n, d)
        remainder=int(n)
        ret=""
        first=True
        i=0
        while (remainder > 0):
            result = int(remainder/d)
            ret = ret+str(result)
            remainder = remainder - (result*d)
            if first:
                if remainder != 0:
                    ret=ret+"."
                first=False
            else:
                if is_repeating['is_repeating']:
                    i=i+1
                    if( (is_repeating['max_nonrepeat']+is_repeating['max_repeat']) < i):
                        return { 'repeat': True, 'value': ret, 'max_nonrepeat': is_repeating['max_nonrepeat'],'max_repeat': is_repeating['max_repeat'] }
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
        for i in range(2, 10):
            print('here '+str(i))
            fact = self.factorial(i)
            next_denominator = fact * denominator
            next_numerator = (numerator * fact) + (denominator * 1)
            numerator = next_numerator
            denominator = next_denominator
        print(str(numerator) + " / " + str(denominator) )
        return self.divide(numerator, denominator)
            
        
