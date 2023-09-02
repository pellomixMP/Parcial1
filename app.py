from flask import Flask, render_template
import pymysql

#app = Flask(__name__)

app=Flask(__name__, template_folder='template')

@app.route('/')
def main():
    return render_template('index.html')

app.run(debug=True)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'TallerDB'


def conectar_bd():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
    )



@app.route('/estudiantes')
def listar_estudiantes():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudiantes")
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/cursos')
def listar_cursos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cursos")
    cursos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('cursos.html', cursos=cursos)

if __name__ == '__main__':
    app.run(debug=True)

