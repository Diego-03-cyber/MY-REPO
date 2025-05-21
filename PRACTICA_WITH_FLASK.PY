"""
flask_app/
│
├── app_basic.py              # App básica que dice "Hola mundo"
├── app_ip_restrict.py        # App que restringe por dirección IP
├── app_interface.py          # App que dice "Holiwis"
├── requirements.txt          # Dependencias
└── README.md                 # Descripción del proyecto
"""

# app_basic.py
# Fecha: 29/04/2025
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'nopuedomas'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# app_ip_restrict.py
from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_IP = '192.168.1.100'  # IP permitida

@app.before_request
def limit_remote_addr():
    if request.remote_addr != ALLOWED_IP:
        abort(403)

@app.route('/')
def hello_world():
    return "Hola Mundo desde IP restringida"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




# app_interface.py
# Fecha: 07/04/2025
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Holiwis'

if __name__ == '__main__':
    app.run(debug=True)
