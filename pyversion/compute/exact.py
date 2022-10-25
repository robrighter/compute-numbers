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
        return {"numerator":int(n), "denominator":int(d)} 
    
    def divide_generator(self, numerator, denominator):
        n=int(numerator)
        d=int(denominator)
        remainder=int(n)
        ret=""
        first=True
        while (remainder > 0):
            result = remainder//d
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


    def count_leading_zeros(self, numerator, denominator):
        n=int(numerator)
        d=int(denominator)
        gen = self.divide_generator(n,d)
        found_decimal = False
        counter = 0
        while True:
            value = next(gen)
            if value == "\n":
                return counter
            
            if found_decimal:
                if value == "0":
                    counter = counter + 1
                else:
                    return counter
            else:
                if value == ".":
                    found_decimal = True


    def factorial(self, n):
        ret = int(1);
        while n > 0:
            ret = ret * int(n)
            n = n - 1
        return ret

    def e_partial_sum(self, n):
        if(n == 0):
            return 1
        if(n == 1):
            return 1
        numerator = int(2)
        denominator = int(1)
        print("Adding Rational Terms ...")
        for i in range(2, n):
            print(str(i)+", ",end='')
            if(i%10 == 0):
                print("\n")
            fact = self.factorial(i)
            next_denominator = fact * denominator
            next_numerator = (numerator * fact) + (denominator * 1)
            numerator = next_numerator
            denominator = next_denominator
        return self.divide_generator(numerator, denominator)
    
    def add_rational(self, r1, r2):
        n=(r1[0]*r2[1])+(r2[0]*r1[1])
        return (int(n), int(r1[1]*r2[1]))
    
    def e_partial_sum_continuing_fraction(self, n):
        ret = (3,1)
        i=n-1
        while(i>1):
            ret = self.add_rational( (1,1), (ret[0],ret[1]*i) )
            i=i-1
        return ret
        
    def e_partial_sum_v2(self, n):
        t = self.e_partial_sum_continuing_fraction(n)
        dgen = self.divide_generator(t[0], t[1])
        #since the continuing fraction gives e-1 lets simulate adding in the 1
        yield("2")
        next(dgen)
        #now continue as normal
        while True:
            yield(next(dgen))
            
    def e_recusive(self, n, i=2):
        if(i == n):
            return (3,1)
        else:
            #a more readable version of below is 1+ (1/i)*self.e_recusive(n,i+1)
            tup = self.e_recusive(n,i+1)
            return self.add_rational((1,1), (tup[0],tup[1]*i) )
    
