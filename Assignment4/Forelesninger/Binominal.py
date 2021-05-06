# Calculation of the binominal (n p)
# binominal(n, p) = n! / p!x(n-p)!

def Factorial(n):
    factorial = 1 
    for i in range(2, n+1):
        factorial = factorial*i
    return factorial

print(Factorial(5))

def Binominal1(n, p):
    return Factorial(n)/(Factorial(p)*Factorial(n-p))

print(Binominal1(10, 2))

def AddResultInBionomialTable(table, n, p, r):
    table[(n, p)] = r 

def LookUpResultInBionomialTable(table, n, p):
    return table.get((n, p), -1)

def Binomial3(table, n, p):
    if n<p: 
        return 0 
    if p == n: 
        return 1 
    if p == 1: 
        return n 
    r = LookUpResultInBionomialTable(table, n, p)
    if r != -1:
        return r
    r = Binomial3(table, n-1, p-1) + Binomial3(table, n-1, p)
    AddResultInBionomialTable(table, n, p, r)
    return r

binomialTable = dict()
print(Binomial3(binomialTable, 10, 2))