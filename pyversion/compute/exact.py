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
        result=int(remainder/d)
        ret = str(result)
        remainder=int(remainder)-int(result*d)
        first=True
        while (remainder > 0):
            if first:
                ret=ret+"."
                first=False
            remainder=remainder*10
            result=int(remainder/d)
            ret = ret+str(result)
            remainder=int(remainder)-int(result*d)
            repeat = self.check_for_repeat(ret)
            if repeat != '':
                return { 'repeat': True, 'value': ret, 'repeat_value': repeat }
        return { 'repeat': False, 'value': ret }