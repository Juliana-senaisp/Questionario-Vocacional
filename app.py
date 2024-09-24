from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='.')

def mostrar_resultado(respostas):
    # Contar o número de ocorrências de cada letra
    contagem = {
        'a': respostas.count('a'),
        'b': respostas.count('b'),
        'c': respostas.count('c'),
        'd': respostas.count('d'),
        'e': respostas.count('e')
    }

    # Definir o resultado com base nas contagens
    if contagem['a'] > max(contagem['b'], contagem['c'], contagem['d'], contagem['e']):
        return "Você se interessa por logística"
    elif contagem['b'] > max(contagem['a'], contagem['c'], contagem['d'], contagem['e']):
        return "Você gosta de elétrica"
    elif contagem['c'] >= max(contagem['a'], contagem['b'], contagem['d'], contagem['e']):
        return "Você gosta de desenvolvimento de sistemas"
    elif contagem['e'] >= max(contagem['a'], contagem['b'], contagem['d'], contagem['c']):
        return "Você gosta de desenvolvimento de sistemas"
    elif contagem['d'] > max(contagem['a'], contagem['b'], contagem['c'], contagem['e']):
        return "Você gosta de mecânica"
    else:
        return "Empate entre as opções. Tente responder novamente."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    respostas = []
    for i in range(1, 11):
        resposta = request.form.get(f'pergunta{i}')
        respostas.append(resposta)
    resultado_final = mostrar_resultado(respostas)
    return render_template('resultado.html', resultado=resultado_final)

@app.route('/restart')
def restart():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
