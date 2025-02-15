from flask import Flask, render_template, request

app = Flask(__name__)

# Hesaplama işlemleri
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Kullanıcıdan gelen değerleri al
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        
        # İşleme göre hesaplama yap
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
    
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
