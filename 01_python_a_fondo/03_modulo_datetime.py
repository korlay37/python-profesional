from datetime import datetime

# fecha_hora: datetime = datetime(2025, 1, 24, 10, 30)
# print(fecha_hora)

# Fecha actual
actual: datetime = datetime.now()
print(actual)

# Formatear fechas y horas
formato: str = "%d/%m/%Y"
fecha_formateada: str = actual.strftime(formato)
print(fecha_formateada)

# Calcular diferencia entre fechas
fecha_futura: datetime = datetime(2025, 12, 31)
diferencia: int = (fecha_futura - actual).days
print(diferencia)

cadena_fecha: str = "2025-01-24"
formato: str = "%Y-%m-%d"
fecha_convertida: datetime = datetime.strptime(cadena_fecha, formato)
print(fecha_convertida)