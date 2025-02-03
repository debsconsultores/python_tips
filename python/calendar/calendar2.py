import calendar
import datetime

def crear_calendario(año):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calendario = cal.formatyear(año)
    print(calendario)

# Uso del script
anio_actual = datetime.datetime.now().year
anio = int(input("Indica el Año:") or anio_actual ) 
crear_calendario(anio)
