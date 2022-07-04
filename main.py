from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('index.html')


@app.route('/<data>')
def calculadora(data):
  meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  dia = int(data[:2])
  mes = int(data[3:5])
  ano = int(data[6:])
  tempo = 0
  for i in range(mes-1):
      tempo += meses[i]
  if not ano  % 4:
    if not ano % 100 and ano % 400:
      if not (ano / 100) % 4:
        # Bissexto
        tempo += 1
        tempo += dia
        por = (tempo / 366) * 100
    else:
      # Bissexto
      tempo += 1
      tempo += dia
      por = (tempo / 366) * 100
  else:
    tempo += dia
    por = (tempo / 365) * 100
  return jsonify({'Porcentagem de Rotação': f'{por:.2f}%'})

app.run(host='0.0.0.0')