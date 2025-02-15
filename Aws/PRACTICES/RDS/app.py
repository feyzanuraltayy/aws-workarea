from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# RDS bağlantı bilgileri
DB_CONFIG = {
    'dbname': 'xxxxxxxxxxxxxxx',
    'user': 'xxxxxxxxxxxxxxxxxx',
    'password': 'xxxxxxxxxxxxx',
    'host': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'port': '5432'
}

# Veritabanı bağlantısı
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

# Ana sayfa
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students;')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

# Öğrenci ekleme
@app.route('/add', methods=['POST'])
def add_student():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_number = request.form['student_number']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (first_name, last_name, student_number, email) VALUES (%s, %s, %s, %s)',
        (first_name, last_name, student_number, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# Öğrenci silme
@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# Öğrenci güncelleme sayfası
@app.route('/update/<int:id>', methods=['GET'])
def update_student_page(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = %s', (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', student=student)

# Öğrenci güncelleme
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_number = request.form['student_number']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE students SET first_name = %s, last_name = %s, student_number = %s, email = %s WHERE id = %s',
        (first_name, last_name, student_number, email, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)