from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LOTR</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                margin: 50px;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>FELLOWSHIP OF THE RING IS BROKEN!</h1>
        <p>Mordor seeks the power of the rings.</p>
        <p>You are in the mines of Moria. Fight the Balrog.</p>
        <img src = "/img.jpeg" />
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
