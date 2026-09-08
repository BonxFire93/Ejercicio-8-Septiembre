from flask import Flask, render_template, redirect # type: ignore

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect('/registro')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

if __name__ == '__main__':
    app.run(debug=True)