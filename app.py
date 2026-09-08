from flask import Flask, render_template, redirect # type: ignore

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

if __name__ == '__main__':
    app.run(debug=True)