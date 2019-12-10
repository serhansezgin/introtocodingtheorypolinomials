


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
def sub(A, B, m, n): 

    size = max(len(A), len(B))
    sum = [0 for i in range(size)] 

    # Initialize the product polynomial 
    
    for i in range(0, len(A), 1): 
        sum[i] = A[i] 

    # Take ever term of first polynomial 
    for i in range(len(B)): 
        sum[i] -= B[i] 

    return sum

# A utility function to print a polynomial 
def printPoly(poly, n): 
    for i in range(0,n): 
        #print(poly[i], end = "")
        return poly[i]
    if (i != 0): 
            #print("x^", i, end = "")
        return ("x^", i)
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


    sum = sub(A, B, m, n) 
                
    size = max(len(A), len(B))

    #print("sum",sum)
    
    mod_sum = []
    for s in sum:
        mod_sum.append(s % p)
        #if mod_sum[-1] == 0:
         #   mod_sum.pop()


    if mod_sum[-1] == 0:
        mod_sum.pop()
    '''
    if m == -1:
        mod_sum = [0]
    if n == -1:
        mod_sum = [0]
    '''
    if all(x == 0 for x in mod_sum):
        size = 0
        mod_sum = [0]
        print(len(mod_sum)-2)
    else:
        print(len(mod_sum)-1)


    Anew = ((A[:])*max(len(A),len(B)))
    #print(Anew)
    #print(A)
    #print(B)
    #print(mod_sum)
    #print("First polynomial is") 
    printPoly(A, len(A)) 
    #print("\n", end = "") 
    #print("Second polynomial is") 
    printPoly(B, len(B)) 
    #print("\n", end = "")     
    
    #print("sum polynomial is") 
    printPoly(mod_sum, len(mod_sum)) 
    
    #print("\n")
    
    #print("\n")
    #print("mod_sum",mod_sum)
    #print("mod_sum_1",mod_sum[-1])
    
        #print("mod_sum2",mod_sum)

        

    #if all(x == 0 for x in mod_sum):
    print (" ".join(map(str,mod_sum))) 

# Driver Code 
if __name__ == '__main__': 
    main()

     



        
