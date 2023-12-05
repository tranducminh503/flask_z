from flask import Flask,render_template,jsonify
app = Flask(__name__)

CHAMPS = [
    {
        'id' : 1,
        'name' : 'leesin'
    },
    {
        'id' : 2,
        'name' : 'akali'
    }
]

@app.route('/')
def home():
    return render_template('home.html',champs = CHAMPS)

@app.route('/api/champ')
def list_champ():
    return jsonify(CHAMPS)

if __name__ :
    app.run(debug=True)