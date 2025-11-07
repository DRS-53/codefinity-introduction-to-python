# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekday_count = len(weekdays)
#
for weekday in range(weekday_count):
    print(f"{weekdays[weekday]}: Promotion on {daily_promotions[weekday]}")
#
daycount = 0
for day in weekdays:
    print(f"{day}: Promotion on {daily_promotions[daycount]}")
    daycount+= 1
