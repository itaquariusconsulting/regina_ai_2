from regina_db import get_connection


def obtener_ordenes_pago(
    cod_empresa: str,
    cod_sucursal: str,
    ano_periodo: str,
    cod_periodo: str,
    cod_auxiliar: str
):

    cn = get_connection()
    try:
        cur = cn.cursor()

        sql = """
        SELECT COD_EMPRESA, COD_SUCURSAL, ANO_PERIODO, COD_PERIODO, NUM_ORDEN, FEC_ORDEN,
               COD_MONEDA, TIP_CAMBIO, IMP_SOLES, IMP_DOLARES, GLOSA, TIP_ESTADO, COD_AUXILIAR,
               COD_PERIODO_VOU, ANO_PERIODO_VOU, COD_TIPO_COMPROBANTE, NUM_FILE, NUM_VOUCHER, COD_RUBRO,
               COD_TIPO_GASTO, COD_USUARIO, FEC_ACTUALIZA, NRO_REFERENCIA, NUM_VER_PLAN_CUENTAS, COD_CUENTA,
               FEC_RENDICION, NUM_DIAS_RENDICION, IMP_ORD_PAGO, IMP_LIQ_BASE, IMP_LIQ_SECUN,
               (SELECT DES_ABREVIATURA
                  FROM MAE_MONEDAS
                 WHERE COD_MONEDA = CXP_ORDEN_PAGO.COD_MONEDA) AS C_DES_MONEDA,
               (SELECT DES_AUXILIAR
                  FROM MAE_AUXILIAR
                 WHERE COD_EMPRESA = CXP_ORDEN_PAGO.COD_EMPRESA
                   AND COD_AUXILIAR = CXP_ORDEN_PAGO.COD_AUXILIAR) AS C_DES_AUXILIAR,
               (SELECT DES_TIPO_GASTO
                  FROM MAE_TIPO_GASTO
                 WHERE COD_EMPRESA = CXP_ORDEN_PAGO.COD_EMPRESA
                   AND COD_RUBRO = CXP_ORDEN_PAGO.COD_RUBRO
                   AND COD_TIPO_GASTO = CXP_ORDEN_PAGO.COD_TIPO_GASTO) AS C_DES_TIPO_GASTO
          FROM CXP_ORDEN_PAGO
         WHERE COD_EMPRESA  = ?
           AND COD_SUCURSAL = ?
           AND ANO_PERIODO  = ?
           AND COD_PERIODO  = ?
           AND COD_AUXILIAR = ?
        """

        cur.execute(
            sql,
            (
                cod_empresa,
                cod_sucursal,
                ano_periodo,
                cod_periodo,
                cod_auxiliar
            )
        )

        columnas = [c[0] for c in cur.description]

        data = []
        for row in cur.fetchall():
            data.append(dict(zip(columnas, row)))

        return data

    finally:
        cur.close()
        cn.close()


# ---------------------------------------------------------
# el resto de funciones se mantienen igual
# ---------------------------------------------------------

def obtener_monto_rendido_por_orden(id_orden: str):

    cn = get_connection()
    try:
        cur = cn.cursor()

        cur.execute("""
            SELECT ISNULL(SUM(monto_rendido), 0)
            FROM rendicion
            WHERE id_orden_pago = ?
        """, (id_orden,))

        row = cur.fetchone()
        return float(row[0] or 0)

    finally:
        cur.close()
        cn.close()


def contar_ordenes_por_estado(estado: str):

    cn = get_connection()
    try:
        cur = cn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM orden_pago
            WHERE estado = ?
        """, (estado,))

        return int(cur.fetchone()[0])

    finally:
        cur.close()
        cn.close()


def contar_ordenes_totales():

    cn = get_connection()
    try:
        cur = cn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM orden_pago
        """)

        return int(cur.fetchone()[0])

    finally:
        cur.close()
        cn.close()


def obtener_resumen_rendicion():

    cn = get_connection()
    try:
        cur = cn.cursor()

        cur.execute("""
            SELECT
                COUNT(*),
                ISNULL(SUM(monto_total), 0)
            FROM orden_pago
        """)

        row = cur.fetchone()

        total_ordenes = int(row[0] or 0)
        total_ordenado = float(row[1] or 0)

        cur.execute("""
            SELECT ISNULL(SUM(monto_rendido), 0)
            FROM rendicion
        """)

        total_rendido = float(cur.fetchone()[0] or 0)

        cur.execute("""
            SELECT COUNT(*)
            FROM orden_pago
            WHERE estado = 'ACTIVA'
        """)
        activas = int(cur.fetchone()[0] or 0)

        cur.execute("""
            SELECT COUNT(*)
            FROM orden_pago
            WHERE estado = 'CERRADA'
        """)
        cerradas = int(cur.fetchone()[0] or 0)

        pendiente = total_ordenado - total_rendido

        porcentaje = 0.0
        if total_ordenado > 0:
            porcentaje = round((total_rendido * 100) / total_ordenado, 2)

        return {
            "totalOrdenes": total_ordenes,
            "ordenesActivas": activas,
            "ordenesCerradas": cerradas,
            "totalOrdenado": total_ordenado,
            "totalRendido": total_rendido,
            "totalPendiente": pendiente,
            "porcentajeAvance": porcentaje
        }

    finally:
        cur.close()
        cn.close()
