"""composit"""


def func_f(xxxx):
    """fog"""
    ans = xxxx*2
    return ans


def func_g(xxxx):
    """gof"""
    ans = (xxxx / 2) + 1
    return ans


def main():
    """main"""
    number = int(input())
    f_o_g = func_f(func_g(number))
    g_o_f = func_g(func_f(number))
    print("%.2f" % f_o_g)
    print("%.2f" % g_o_f)


main()
