# Calculadora

Actividad U2: Automatización de pruebas en CI.

## Archivos
- calculator.py: operaciones matemáticas.
- app.py: menú de consola.
- test_calculator.py: nueve pruebas automáticas.
- requirements.txt: dependencias del proyecto.
- .github/workflows/ci.yml: integración continua.

## Ejecutar calculadora
py app.py

## Ejecutar pruebas
py -m unittest discover -v

## Práctica de CI
1. Comprobar el funcionamiento inicial.
2. Provocar un fallo con Python 9.99.
3. Restaurar Python 3.10 y provocar un fallo de dependencias.
4. Restaurar la configuración y verificar las pruebas.
