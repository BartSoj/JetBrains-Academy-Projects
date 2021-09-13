from math import ceil, floor, log
from sys import argv

payment_type = None
d = None
p = None
n = None
i = None
for arg in [arg.split("=") for arg in argv[1:]]:
    if arg[0] == "--type":
        payment_type = arg[1]
    elif arg[0] == "--payment":
        d = int(arg[1])
    elif arg[0] == "--principal":
        p = int(arg[1])
    elif arg[0] == "--periods":
        n = int(arg[1])
    elif arg[0] == "--interest":
        i = float(arg[1]) / 1200

if len(argv) < 5:
    print("Incorrect parameters")
elif payment_type != "annuity" and payment_type != "diff":
    print("Incorrect parameters")
elif d is None:
    if payment_type == "diff":
        overpayment = 0
        for m in range(1, n + 1):
            d = ceil(p / n + i * (p - ((p * (m - 1)) / n)))
            overpayment += d
            print("Month {}: payment is {}".format(m, d))
        print("\nOverpayment = {}".format(overpayment - p))
    else:
        d = ceil(p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        print("Your annuity payment = {}!".format(d))
        print("Overpayment = {}".format(n * d - p))
elif payment_type == "diff":
    print("Incorrect parameters")
elif p is None:
    p = floor(d / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print("Your loan principal = {}!".format(p))
    print("Overpayment = {}".format(d * n - p))
elif n is None:
    n = ceil(log(d / (d - i * p), 1 + i))
    years = "{} years".format(n // 12) if n // 12 != 0 else ""
    months = "{} months".format(n % 12) if n % 12 != 0 else ""
    years_and_months = years if not months else months if not years else years + " and " + months
    print("It will take {} to repay this loan!".format(years_and_months))
    print("Overpayment = {}".format(d * n - p))
elif i is None:
    print("Incorrect parameters")
