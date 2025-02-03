import calendar

def crear_calendario(año):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calendario = cal.formatyear(año)
    print(calendario)

# Uso del script
crear_calendario(2025)
