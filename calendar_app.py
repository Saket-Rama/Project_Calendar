import calendar
choice = int(input("1.View Month\n2.View Entire Year\n3.Exit\nEnter the Option you want to choose:\n"))
match choice:
    case 1:
        mm = int(input("Enter the Month:\n"))
        yr = int(input("Enter the Year:\n"))
        print(calendar.month(yr,mm))
    case 2:
        yr = int(input("Enter the Year:\n"))
        print(calendar.calendar(yr))
    case _:
        print("Exit from the app!")