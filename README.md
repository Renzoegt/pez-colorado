# Pez Colorado - Módulo de Gestión de Especies y Veda
Este repositorio contiene el módulo funcional de Consulta de Especies y Temporadas para la aplicación Pez Colorado, orientada a la pesca deportiva en la provincia de Misiones. Este desarrollo por el momento solo forma parte de la Actividad #8 de la asignatura ingeniería de Software III, enfocada en la Gestión de la Configuración e Integración Continua (CI).
### Instrucciones de Ejecución
Para poder clonar el proyecto y ejecutarlo dentro de tu entorno local debes seguir estos pasos:
##### Clonar el Repositorio
```
git clone https://github.com/Renzoegt/pez-colorado.git 
cd pez-colorado-tif
```
##### Configurar el Entorno Virtual
```
python /m venv venv
# en Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```
##### Instalar Dependencias
```
pip install -r requirements.txt
```
##### Ejecutar pruebas de forma local
```
pytest
```
### Integración Continua (CI)
Para poder realizar este proyecto, implementams un pipeline de Github Actions que garantiza la calidad del código en cada `push` o `pull request` hacia a rama principal.
Nuestro pipeline está definido en el siguiente archivo [`.github/workflows/ci.yml`](https://github.com/Renzoegt/pez-colorado/blob/main/.github/workflows/ci.yml)

##### Funcionamiento de nuestro proceso de CI
Cada vez que un integrante del equipo sube código, el pipeline ejecuta automáticamente los siguientes pasos:
1. Entorno de Ejecución: Se crea un contenedor virtual con Ubuntu y Python 3.10.
2. Linter (Flake8): Se verifica que el código cumpla con el estándar PEP 8. Esto va a evitar errores de formato y mantiene la legibilidad del código.
3. Auditoría de Seguridad: Se escanean las dependencias en busca de vulnerabilidades conocidas.
4. Tests Unitarios (Pytest): Se ejecutan 5 (por el momento) pruebas que validan la lógica actual de negocio, como el cálculo de tamaños mínimos para pesca.

### Tecnologías Utilizadas
- Lenguaje: Python 3.10
- Testing: Pytest
- Linting: Flake8
- CI/CD: Github Actions
- Gestión: Repositorio Git bajo flujo de ramas por integrante.

### Equipo de Trabajo
- Gómez Terrussi Renzo
- Szkabrij Basilio Emanuel
- Rivero Ramiro
- Kislo Ariel Matias
- Steinmann Eduardo Luciano
