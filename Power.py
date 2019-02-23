class PySolutions:
    def power(x, n):
        z = 1
        if n > 0:
            for i in range(0,n):
                z = z*x
        elif n < 0:
            for i in range(0,-n):
                z = z / x
                print(z)
        return x,n,z

class py_solution:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(4, -1));
print(py_solution().pow(3, 5));
print(py_solution().pow(100, 0));

x = input("Type in a base number: ")
x = int(x)
y = input("Type in exponent: ")
y = int(y)

print("%d^%d = %g" % PySolutions.power(x,y))


r = 1
r = int(r)
r = r/25

print(r)
