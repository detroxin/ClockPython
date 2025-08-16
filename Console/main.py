from datetime import datetime  

current_time = datetime.now()

current_hour = current_time.hour
current_minute = current_time.minute

if current_hour < 10:
    current_hour = "0" + str(current_hour)
if current_minute < 10:
    current_minute = "0" + str(current_minute)

current_time_text = str(current_hour) + ":" + str(current_minute)

print(f"---------Clock----------\n|        {current_time_text}         |\n------------------------")
