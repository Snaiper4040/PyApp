from flask import Flask, render_template, request

app = Flask(__name__)

def Determinant(num11, num12, num21, num22):
    return num11 * num22 - num12 * num21

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            result = Determinant(float(request.form['num11']), float(request.form['num12']), float(request.form['num21']), float(request.form['num22']))
        except ValueError:
            result = "Ошибка: Ожидается число!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')