from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('students.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']

         rows = [(name,addr,city,pin)]
         print rows
         
         with sql.connect('student.db') as con:
            cur = con.cursor()
            print "Opened database successfully"
            cur.execute("INSERT INTO STUDENTS VALUES (?,?,?,?)",(name,addr,city,pin))
            print "Insert Successfully"
            con.commit()
            msg = "Record successfully added"
      except:
          con.rollback()
          msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect('student.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from STUDENTS")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)