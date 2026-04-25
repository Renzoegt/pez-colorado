from especies import estado_veda, es_talla_permitida


def test_veda_noviembre():
    # En noviembre debe estar en veda
    assert estado_veda(11) == "Veda"


def test_pesca_abierta_mayo():
    # En mayo la pesca debe estar abierta
    assert estado_veda(5) == "Abierta"


def test_dorado_talla_legal():
    # Un dorado de 80cm es legal (mínimo 75cm)
    assert es_talla_permitida("Dorado", 80) is True


def test_dorado_talla_ilegal():
    # Un dorado de 60cm es ilegal
    assert es_talla_permitida("Dorado", 60) is False


def test_especie_no_registrada():
    # Si la especie no está en la normativa, debe rechazar por seguridad
    assert es_talla_permitida("Mojarra", 10) is False

def test_veda_noviembre():
    # Simulamos un error: Decimos que en noviembre debería estar "Abierta" 
    # cuando la lógica del programa dice que es "Veda"
    assert estado_veda(11) == "Abierta"