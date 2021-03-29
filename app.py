from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'bgo91eueshnzkrwavn8p-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uk6dwsvwdfzec5x0'
app.config['MYSQL_PASSWORD'] = 'IzaMsAdvJFQ3qajN0vXD'
app.config['MYSQL_DB'] = 'bgo91eueshnzkrwavn8p'

mysql = MySQL(app)

@app.route('/')
def home(): 
    return 'services ready!'

@app.route('/roles', methods=['GET'])
def roles():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM bgo91eueshnzkrwavn8p.rol; ''')
    rv = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return jsonify({
        "db_result": rv
    })
   

@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    newEmployee = {
        "idpropietario": request.json['idpropietario'],
        "nombre": request.json['nombre'],
        "apellido": request.json['apellido'],
        "email": request.json['email'],
        "fecha_nacimiento": request.json['fecha_nacimiento'],
        "celular": request.json['celular'],
        "contrasena": request.json['contrasena'],
        "rol_idrol": request.json['rol_idrol']
    }
    print(newEmployee)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO `bgo91eueshnzkrwavn8p`.`empleado` (`idpropietario`, `nombre`, `apellido`, `email`, `fecha_nacimiento`, `celular`, `contrasena`, `rol_idrol`) VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s)
    ''', (newEmployee['idpropietario'], newEmployee['nombre'], newEmployee['apellido'], newEmployee['email'], newEmployee['fecha_nacimiento'], newEmployee['celular'], newEmployee['contrasena'], newEmployee['rol_idrol']))
    
    mysql.connection.commit()
    cursor.close()
    return jsonify({
        "result": 'added correctly to database'
    })
    

if __name__ == '__main__': 
    app.run(debug=True, port=8080)