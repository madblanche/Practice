from datetime import date, timedelta

d = date(1986, 3, 15)
print('Friends B-day is on', d.day, 'of', d.strftime("%B"))
today = date.today()
enddate = today + timedelta(days=7)

if today.month <= d.month <= enddate.month \
        and today.day <= d.day <= enddate.day:
    print("B-day is on current week!Don't forget to buy a present!!!")
else:
    print('B-day is not so soon')