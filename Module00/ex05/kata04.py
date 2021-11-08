from decimal import Decimal

t = (0, 4, 132.42222, 10000, 12345.67)

print("module_{0[0]:02}, ex_{0[1]:02} : {0[2]:.2f}".format(t), end="")
print("{1:.2E}, {2:.2E}".format(float(t[3]), float(t[4])))
