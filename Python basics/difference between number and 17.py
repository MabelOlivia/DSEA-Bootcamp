def difference():
    a = int(input("Enter a number : "))
    if a < 17:
        diff = 17 - a
        print("Difference is :", diff)

    elif a > 17:
        absolute = (a - 17)*2
        print("Double the absolute is :", absolute)


difference()

