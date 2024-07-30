# zadani sati, minute, sekunde, dan misec i kolko ima sekundi do kraja miseca

#od trenutnog momenta do kraja miseca
import datetime
from datetime import date

today = date.today()

krajMiseca = date(2024,2,1)

razlikaDani = krajMiseca - today

print(razlikaDani.days)

razlikaSati = razlikaDani.days * 24
razlikaMin = razlikaSati * 60
razlikaSek = razlikaMin * 60

print(f"Do kraja miseca ima {razlikaSek} sek.")

# from datetime import datetime

# current_time = datetime(year=2024, month=1, day=8, hour=12, minute=30, second=0)

# future_time = datetime(year=2024, month=1, day=10, hour=15, minute=45, second=30)

# time_difference = future_time - current_time

# days = time_difference.days
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# print(f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
