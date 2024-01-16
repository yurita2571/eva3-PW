from flask import Flask, render_template, request

app = Flask(__name__)
# Ruta principal que carga la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el primer ejercicio que carga el formulario
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

# Ruta que procesa el formulario del primer ejercicio
@app.route('/resultado_ejercicio1', methods=['POST'])
def resultado_ejercicio1():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        resultado = 'Aprobado'
    else:
        resultado = 'Reprobado'

    return f'Promedio: {promedio}, Estado: {resultado}'

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/resultado_ejercicio2', methods=['POST'])
def resultado_ejercicio2():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)
    caracter_nombre_mas_largo = len(nombre_mas_largo)

    return f' El nombre más largo: {nombre_mas_largo}, caracter: {caracter_nombre_mas_largo}'

if __name__ == '__main__':
    app.run(debug=True)