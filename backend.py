from flask import Flask, request, jsonify, render_template
import google.generativeai as genai


genai.configure(api_key="AIzaSyAcFinpP0bU8C3b6mEEV4gYm9GL44zwyak")

model = genai.GenerativeModel("gemini-2.5-flash")
model.generate_content('You are really good translator of slangs and different ways of speeches, with a good understanding of how different groups of people speak')

def brt(g, t): 


    if g == 'x':
        prompt = f'Translate this sentence in quotations gen x slang, output only one option: \"{t}\"'
    elif g == 'm':
        prompt = f'Translate this sentence in quotations millenial slang, output only one option:\"{t}\"'
    elif g == 'z':
        prompt = f'Translate this sentence in quotations gen z slang, output only one option. : \"{t}\"'
    elif g == 'a':
        prompt = f'Using words such as \"gyat\", \"skibidi\", \"ohio\", \"fanum tax\", \"rizz\", \"mewing\", \"sigma\", \"cooking\", \"aura\", \"mogging\" Translate this sentence in quotations into gen a slang, output only one option. : \"{t}\"'
    elif g == 'e':
        prompt = f'Translate this sentence in quotations clear, proper formal/casual english, without any slangs, output only one option. : \"{t}\"'
    else:
        return "Invalid generation."

    response = model.generate_content(prompt)

    o = response.text
    return o

app = Flask(__name__)

@app.route('/')
def showing():
    return render_template('website.html')


@app.route('/translate', methods = ['POST'])
def translate():

    data = request.get_json()
    inputs = data.get('input', '')
    lang = data.get('options', '')

    translated = ''

    #translation here
    translated = brt(lang, inputs)

    return jsonify({'translated': translated})



if __name__ == '__main__':
    app.run(debug=True)
