"""Regulation"""


def main():
    """Doc"""
    a_unit = int(input())
    b_unit = float(input())
    c_unit = str(input())
    print("%30s" % str(a_unit))
    print("%030d" % a_unit)
    print("%.2f" % b_unit)
    print("%.12f" % b_unit)
    print("%40s" % c_unit)


main()
