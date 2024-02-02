import random
import time

class RabinMiller:

    def __init__(self) -> None:
        pass
    
    def is_prime(self, n):
        if n % 2 == 0 or n < 3:
            return 'Composite'
    
        r, s = 0, n - 1

        while s % 2 == 0:
            r += 1
            s //= 2


        a = random.randint(2, n - 2)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            return 'ProbablyPrime'
        
        for j in range(1,r):
            x = pow(x,2,n)
            #x = pow(a, pow(2, j) * s, n)
            if x == 1:
                return 'Composite'
            if x == n - 1:
                return 'ProbablyPrime' 
        

        return 'Composite'
    
    
    def testRM(self, n):
        s = set()
        while len(s) < 20:
            a = random.randint(2, n - 2)
            s.add(a)
        
        for x in s:
            print("for a:", x,"->", self.is_prime(n, x))

        
        



rabin_miller = RabinMiller()
num = 7223399909167574172743325414693676548326825921666135854056448724070480414758160361022571562690368732168013824985784486717075079212295627526200227158562047888282887211844730490147676518048003289711084227194914361012670986318249514449278985556450486058932343718753559106698633057330231937868208844758233219408845112694405541695669350109895321866545482304377169596621795775943667361216751751838335414124771956246519441217477610102093446316975989333346980859657099599767868627339185186074113599058701960284473895435657641144273311422709961683891403909853678660480390562191809134005697630258782396543741818675463203501763

print(num.bit_length())




    

