from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')



# a simple page that says hello
@app.route('/hello')
def home_page():
    return render_template('home.html')

@app.route('/product')
def product_page():
    return render_template('product.html')