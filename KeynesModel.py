print("""Welcome to Keynes Model Program. Now type in the exogen values
      and let the program calculate the endogene values""")

zc = float(input("Other consume: "))
zt = float((input("Other taxes: ")))
zi = float((input("Other investments: ")))
G = float((input("Government spending: ")))
X = float((input("Export: ")))
c = float()
b = float()
a = float()
t = float()

Multiplicator = float()

print("Now give value to parameters: c, b, a and t")

while 0 >= Multiplicator or Multiplicator >= 1:
    c = float((input("Consumption propensity (c): ")))
    while 0 > c or c > 1:
        print("The c has to be between 0 and 1.")
        c = float((input("Consumption propensity (c): ")))
    b = float((input("Investment propensity (b): ")))
    while 0 > b or b > 1:
        print("The b has to be between 0 and 1.")
        b = float((input("Investment propensity (b): ")))
    a = float((input("Import sludge (a): ")))
    while 0 > a or a > 1:
        print("The a has to be between 0 and 1.")
        a = float((input("Import sludge (a): ")))
    t = float((input("Tax rates (t): ")))
    while 0 > t or t > 1:
        print("The t has to be between 0 and 1.")
        t = float((input("Tax rates (t): ")))
    Multiplicator = (1 - c*(1-t) - b + a)
    if 0 < Multiplicator < 1:
        None
    else:
        print("""The multiplicator must be between 0 and 1.
                Currently it's at""", Multiplicator)

Y = (1/(1 - c*(1-t)-b+a)) * (zc - c*zt + zi + G + X)
T = zt + t*Y
I = zi + b*Y
C = zc + c*(Y-T)
Q = a*Y

print("The GDP is ", int(Y))
print("The total tax income is ", int(T))
print("The government spending is ", int(G))
print("The balance is: GDP = C + I + G + X - Q")
print("Balance: ",int(Y)," = ",int(C)," + ",int(I)," + ",int(G)," + ",int(X)," - ",int(Q))
print("""\n Now we will see how change in one variable
      affects change in all variables. Type in changes in variables: """)

while True:

    zc += float(input("Other consume: "))
    zt += float((input("Other taxes: ")))
    zi += float((input("Other investments: ")))
    G2 = float((input("Government spending: ")))
    X2 = float((input("Export: ")))

    X = X + X2
    G = G + G2

    Y2 = (1/(1 - c*(1-t)-b+a)) * (zc - c*zt + zi + G + X)
    T2 = zt + t*Y2
    I2 = zi + b*Y2
    C2 = zc + c*(Y2-T2)
    Q2 = a*Y2

    print("The GDP is ", int(Y2))
    print("The total tax income is ", int(T2))
    print("The government spending is ", int(G))
    print("The balance is: GDP = C + I + G + X - Q")
    print("Balance: ",int(Y2)," = ",int(C2)," + ",int(I2)," + ",int(G)," + ",int(X)," - ",int(Q2))
    print("""Change in GDP: """, int(Y2 - Y),
          """\n Change in C: """, int(C2 - C),
          """\n Change in I: """, int(I2 - I),
          """\n Change in G: """, int(G2),
          """\n Change in X: """, int(X2),
          """\n Change in Q: """, int(T2 - T))
