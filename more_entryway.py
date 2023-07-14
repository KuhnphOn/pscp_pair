"""More entryway"""


def loop_fruad(number):
    """Doc"""
    if number <= 20:
        print("Output_" + str(number))
        number += 1
        loop_fruad(number)
    else:
        pass


def main():
    """Dingstrock"""
    loop_fruad(1)


main()
