def estado_veda(mes):
    """Devuelve el estado de la pesca según el mes en Misiones."""
    if mes in [11, 12]:
        return "Veda"
    return "Abierta"


def es_talla_permitida(especie, medida):
    """Verifica si el ejemplar cumple con la talla mínima."""
    normativa = {
        "Dorado": 75,
        "Surubí": 85,
        "Pacú": 45
    }
    talla_minima = normativa.get(especie)
    if talla_minima is None:
        return False
    return medida >= talla_minima

