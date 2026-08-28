import calendar
choice = int(input("1.View Month\n2.View Entire Year\n3.Exit\nEnter the Option you want to choose:\n"))
yr = int(input("Enter the Year:\n"))
mm = int(input("Enter the Month:\n"))
match choice:
    case 1:
        print(calendar.month(yr,mm))