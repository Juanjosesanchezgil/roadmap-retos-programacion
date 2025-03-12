from datetime import datetime

date = datetime.today()
now = datetime.strptime(date, "%d-%m-%Y %H:%M")
birth = datetime.strptime("23-05-1984 14:50", "%d-%m-%Y %H:%M")

diff = now - birth
print(diff)