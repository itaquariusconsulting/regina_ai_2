tools = [
    {
        "type": "function",
        "function": {
            "name": "obtenerMontoRendidoPorOrden",
            "description": "Obtiene el monto total rendido para una orden de pago",
            "parameters": {
                "type": "object",
                "properties": {
                    "idOrdenPago": {"type": "string"}
                },
                "required": ["idOrdenPago"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "contarOrdenesPorEstado",
            "description": "Cuenta órdenes de pago por estado",
            "parameters": {
                "type": "object",
                "properties": {
                    "estado": {
                        "type": "string",
                        "enum": ["ACTIVA", "CERRADA"]
                    }
                },
                "required": ["estado"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "contarOrdenesTotales",
            "description": "Cuenta todas las órdenes de pago",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "obtenerResumenRendicion",
            "description": "Obtiene el resumen general de rendición",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]
