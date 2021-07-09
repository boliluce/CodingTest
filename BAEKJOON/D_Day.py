import datetime

year,month,day = list(map(int, input().split(' ')))
today = datetime.date(year,month,day)
out = datetime.date(year+1000,month,day)
year,month,day = list(map(int, input().split(' ')))
d_day = datetime.date(year,month,day)

if(d_day>=out):
    print("gg")
else:
    print("D-"+str((d_day-today).days))

