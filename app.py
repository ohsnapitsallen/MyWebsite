from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        radius = request.form.get('radius')
        if radius:
            radius = float(radius)
            area = 3.141592653589793238 * radius**2
    return render_template('areaofcircle.html', area=area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        base = request.form.get('base')
        height = request.form.get('height')
        area = 0.5*float(base)*float(height)
    return render_template('areaoftriangle.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == "__main__":
    app.run(debug=True)
