


def isPrime(p) : 
    
  
    # Corner cases 
        if (p <= 1) : 
            return False
        if (p <= 3) : 
            return True
        if (p > 100) :
            return False
        # This is checked so that we can skip  
        # middle five numbers in below loop 
        if (p % 2 == 0 or p % 3 == 0) : 
            
            return False
                
        i = 5
        while(i * i <= p) : 
            if (p % i == 0 or p % (i + 2) == 0) : 
                
                return False
                
            i = i + 6
    
        return True


def is_correct_(A,B,m,n):
    return len(A)-1 == m and len(B)-1 == n
    
def is_correct___(A,B,m,n):
    if m == -1:
        return A[:] == [0] * max(len(A),len(B))   
    
    if n == -1:
        return B[:] == [0] * max(len(A),len(B))      

    
     
                    
#is_correct_(A,B,m,n)
    
def is_correct(n,m):
    return (m > -1 and n <= 100)
               

           
                    

def is_correct__(A,B,n,m):
    if (m >= 0):
        return A[-1] != 0
    
    if (n >= 0):
        return B[-1] != 0  
     




        
      
# Driver Program
#isPrime(p)

    #print(" true")
   


    
            

            


        




# Simple Python 3 program to add two 
# polynomials 
  
# A utility function to return maximum  
# of two integers 
  
# A[] represents coefficients of first polynomial 
# B[] represents coefficients of second polynomial 
# m and n are sizes of A[] and B[] respectively

def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)

def div(A, B,m,n):

    A = A[:]
    normalize(A)
    B = B[:]
    normalize(B)

    if len(A) >= len(B):
        shiftlen = len(A) - len(B)
        B = [0] * shiftlen + B
    else:
        return [0], A


    quot = []
    divisor = (B[-1])
    for i in range(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = A[-1] / divisor
        quot = [mult] + quot

        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in B]
            A = [u - v for u, v in zip(A, d)]

        A.pop()
        B.pop(0)

    normalize(A)
    return quot, A


    # Multiply two polynomials term by term 
      
    # Take ever term of first polynomial 
    '''
    for i in range(len(A)): 
          
        # Multiply the current term of first  
        # polynomial with every term of  
        # second polynomial. 
        for j in range(len(B)): 
            prod[i + j] += A[i] * B[j]
  
    return prod
'''
# A utility function to print a polynomial 
def printPoly(poly, n): 
  
    for i in range(n): 
        #print(poly[i], end = "")
        return poly[i]
    if (i != 0): 
            #print("x^", i, end = "")
        return("x^", i)
    if (i != n - 1): 
            #print(" + ", end = "")
        return (" + ")



                    

                    
                    
                    


def main():
    p = int(input())
    
    if not isPrime(p):
        #print("-1\n0")
        #print("INVALID")
        return False
    # The following array represents 
    # polynomial 5 + 10x^2 + 6x^3 
    #A = [5, 0, 10, 6]
    m = int(input())
    



    A=list(map(int,input().split()))
    


    
    # The following array represents 
    # polynomial 1 + 2x + 4x^2 
    #B = [1, 2, 4]
    n= int(input())
    

    B=list(map(int,input().split()))
    

    m = len(A)-1
    n = len(B)-1


    if m == -1:
        A[:] == [0] * max(len(A),len(B))   
    
    if n == -1:
        B[:] == [0] * max(len(A),len(B))      
    

    #if not is_correct_(A,B,m,n):
        #print("-1\n0")
        #print("INVALID")
     #   return False

    #m = len(A)-1
    #n = len(B)-1
    #print("m",m)
    #print("lenA",len(A))
    #print("lenB",len(B))
    #print("n",n)

    #if not is_correct(m,n):
        #print("-1\n0")
        #print("INVALID")
        #return False


    #if not is_correct__(A,B,n,m):
        #print("-1\n0")
        #print("INVALID")
        #return False

    #if not is_correct___(A,B,m,n):
     #   return False


   




    Anew = ((A[:])*max(len(A),len(B)))
    #print(Anew)
    #print(A)
    #print(B)
    #print(mod_sum)
    #print("First polynomial is") 
    printPoly(A, len(A)) 
    #print("\n", end = "") 
    #print("Second polynomial is") 
    printPoly(B, len(A)) 
    #print("\n", end = "")     
    
    #print("sum polynomial is") 
    printPoly(quot, len(quot)) 
    
    #print("\n")
    
    #print("\n")
    #print("mod_sum",mod_sum)
    #print("mod_sum_1",mod_sum[-1])
    
        #print("mod_sum2",mod_sum)

        

    #if all(x == 0 for x in mod_sum):
    print (" ".join(map(str,quot))) 

# Driver Code 
if __name__ == '__main__': 
    main()

     



        
