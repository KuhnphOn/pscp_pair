"""BMI"""


def fake_loop(name_list, bmi_list):
    """Fake the loop"""
    if len(name_list) <= 4:
        name = str(input())
        weight = float(input())
        height = float(input()) / 100
        bmi = weight / (height ** 2)
        name_list.append(name)
        bmi_list.append(bmi)
        fake_loop(name_list, bmi_list)
    else:
        print("%s's  BMI = %.2f" % (name_list[0], bmi_list[0]))
        print("%s's  BMI = %.2f" % (name_list[1], bmi_list[1]))
        print("%s's  BMI = %.2f" % (name_list[2], bmi_list[2]))
        print("%s's  BMI = %.2f" % (name_list[3], bmi_list[3]))
        print("%s's  BMI = %.2f" % (name_list[4], bmi_list[4]))


def main():
    """Doc"""
    list_name = []
    list_bmi = []
    fake_loop(list_name, list_bmi)


main()
