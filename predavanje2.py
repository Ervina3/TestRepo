"""#funkcije koje kvadrira zadati parametri
def square(x):
    return x*x
print(square(4))

#koristimo lambda funkcije

square_lambda = lambda x: x*x
print(square_lambda(4))

#f=a*x*x+b*x+c
def build_quadrtic_function(a,b,c):
    return lambda x: a*x*x+b*x+c

f= build_quadrtic_function(2,3,-5)
print(f(0))
print(f(1))
print(f(2))
print(build_quadrtic_function(3,2,1)(2))
"""

#bez for petlje koristi lambda funkcije 
"""def even_check(num):
    if num%2 ==0:
        return True
    else:
        return False
    
def even_check_short(num):
        return num%2==0
    """
"""
even_check_lambda= lambda num : num %2==0

l=[2,5,7,8,10]
even_elements= list(filter(even_check_lambda,l))
print()
"""
#data je lista za svaki grad koja se sajstoji od torki prvi element je grada a druga temperatura,temperatura ne drugu skalar koja se odredjuju ne drugu formulu
#(9/5 * temp_C+32)
"""
cities_temp_C=[("Podgorica",20), ("Niksic", 18) ,("Budva",21),("Cetinje",15)]
cities_temp_f= map(lambda elem:(elem[0], (9/5)* elem[1]+32), cities_temp_C)
print(list(cities_temp_f))
          """    

#date su dvije liste treba tako da se rezlutat novu lista koji sastoji od zbira elemenata sa odgovarajuci pozicija
#l1=[1,2,3]
#l2=[2,4,5]  l3=[3,6,8]

l1=[1,2,3]
l2=[2,4,5]

l3=list(map(lambda x,y: x+y , l1,l2))
print(l3)

