# regina_services_simulado.py
# Servicios simulados para pruebas sin SQL ni OpenAI

def obtener_monto_rendido_por_orden(idOrdenPago):
    # Devuelve un monto fijo simulado
    return 1234.56

def contar_ordenes_por_estado(estado):
    # Devuelve un número fijo simulado
    return 5

def contar_ordenes_totales():
    return 42

def obtener_resumen_rendicion():
    # Devuelve un resumen simulado
    return [
        {"orden": 1, "monto": 100},
        {"orden": 2, "monto": 200},
        {"orden": 3, "monto": 300},
    ]

def obtener_ordenes_pago(cod_empresa=None, cod_sucursal=None, ano_periodo=None,
                         cod_periodo=None, cod_auxiliar=None):
    # Devuelve un listado de órdenes simulado
    return [
        {"id": 1, "empresa": cod_empresa or "001", "monto": 100},
        {"id": 2, "empresa": cod_empresa or "001", "monto": 200},
        {"id": 3, "empresa": cod_empresa or "001", "monto": 300},
    ]
