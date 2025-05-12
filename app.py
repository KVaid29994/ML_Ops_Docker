from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Square Calculator</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    text-align: center;
                }
                input[type="number"] {
                    padding: 10px;
                    width: 200px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    margin-bottom: 20px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    border: none;
                    background-color: #007BFF;
                    color: white;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Square Calculator</h2>
                <form action="/square" method="POST">
                    <input type="number" name="number" step="any" required placeholder="Enter a number"><br>
                    <input type="submit" value="Calculate Square">
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/square', methods=['POST'])
def square():
    try:
        num = float(request.form['number'])
        result = num ** 2
        return f'''
            <html>
            <head>
                <title>Result</title>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f0f0;
                        font-family: Arial, sans-serif;
                    }}
                    .result {{
                        background-color: white;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        text-align: center;
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        text-decoration: none;
                        color: #007BFF;
                    }}
                    a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <div class="result">
                    <h3>The square of {num} is {result}.</h3>
                    <a href="/">Calculate Again</a>
                </div>
            </body>
            </html>
        '''
    except ValueError:
        return "<h3>Invalid input. Please enter a valid number.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Square Calculator</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    text-align: center;
                }
                input[type="number"] {
                    padding: 10px;
                    width: 200px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    margin-bottom: 20px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    border: none;
                    background-color: #007BFF;
                    color: white;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Square Calculator</h2>
                <form action="/square" method="POST">
                    <input type="number" name="number" step="any" required placeholder="Enter a number"><br>
                    <input type="submit" value="Calculate Square">
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/square', methods=['POST'])
def square():
    try:
        num = float(request.form['number'])
        result = num ** 2
        return f'''
            <html>
            <head>
                <title>Result</title>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f0f0;
                        font-family: Arial, sans-serif;
                    }}
                    .result {{
                        background-color: white;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        text-align: center;
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        text-decoration: none;
                        color: #007BFF;
                    }}
                    a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <div class="result">
                    <h3>The square of {num} is {result}.</h3>
                    <a href="/">Calculate Again</a>
                </div>
            </body>
            </html>
        '''
    except ValueError:
        return "<h3>Invalid input. Please enter a valid number.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
