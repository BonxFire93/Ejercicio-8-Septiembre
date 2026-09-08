from flask import Flask, render_template, redirect, request #type: ignore

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect('/registro')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return redirect('/lista')

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    registros = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'edad': request.form['edad']
    }
    registro.save(registros)
    return redirect('/lista')

if __name__ == '__main__':
    app.run(debug=True)