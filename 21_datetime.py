### Datetime ###
from datetime import datetime, date, time, timedelta
print(dir(datetime))

now = datetime.now()
print(now)

day = now.day
month = now.month
year= now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, hour, minute)
print('timestamp', timestamp)
print(f"{day}/{month}/{year}/, {hour}:{minute}")

#metodo strftime
t = now.strftime("%H:%M:%S")
print(t)
time_one = now.strftime("%m/%d/%y, %H,%M,%S")
print("Formato 1:", time_one)

#convertir cadena a fecha
date_string = "27 October, 2026"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

#usar date desde datetime

d = date(2025, 1, 1)
print(d)
print("Fecha actual:", d.today())#Fecha actual

today = date.today() #objeto date de hoy
print("Año actual: ", today.year)
print("Mes actual: ", today.month)
print("Dia actual: ", today.day)

#Representar tiempo con el objeto time
a = time()
print("a = ", a)
b = time(10,30,50, 200555) #horas, min, seg, microsegundos
print("b = ", b)

#calcular la fecha entre dos puntos de tiempo
today = date(year=2026, month=10, day=27)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print("Tiempo hasta ano nuevo: ", time_left_for_newyear)

t1 = datetime(year=2026, month=10, day=27, hour=19, minute=27, second=20)
t2 = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
t3 = t2 - t1
print("T3: ", t3)

#timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, seconds=30)
t3 = t1 - t2
print("t3= ", t3)