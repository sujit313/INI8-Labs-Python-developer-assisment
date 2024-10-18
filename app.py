from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="assesment"  # Replace with your actual database name
)

mycursor = mydb.cursor()

# CRUD Operations
@app.route('/register', methods=['POST'])
def register_user():
    name = request.form.get('name')
    email = request.form.get('email')
    date_of_birth = request.form.get('date_of_birth')
    gender = request.form.get('gender')
    address = request.form.get('address')
    phone_number = request.form.get('phone_number')
    registration_date = request.form.get('registration_date')

    if not name or not email or not date_of_birth:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        sql = "INSERT INTO Registration (Name, Email, DateOfBirth, Gender, Address, PhoneNumber, RegistrationDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name, email, date_of_birth, gender, address, phone_number, registration_date)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'message': 'User registered successfully'})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        mycursor.execute("SELECT * FROM Registration")
        results = mycursor.fetchall()
        return jsonify(results)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

# ... Implement other CRUD operations (update, delete)

if __name__ == '__main__':
    app.run(debug=True)