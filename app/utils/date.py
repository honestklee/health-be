from datetime import datetime
import pytz

months_in_indonesia = {
  1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
  7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}


def get_date_milisecond():
  return int(datetime.now().timestamp() * 1000)


def jakarta_now():
  jakarta_timezone = pytz.timezone('Asia/Jakarta')
  return datetime.now(jakarta_timezone)

def get_date_formatted_indonesia(value: datetime):
  day = value.day  
  month = value.month  
  year = value.year  
    
  month_name = months_in_indonesia.get(month, "")  
  formatted_date = f"{day} {month_name} {year}"  
  return formatted_date  
