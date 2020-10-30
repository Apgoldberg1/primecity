from flask import Flask, url_for, redirect, render_template, session, request
import math
import random
from primetests import *
app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/d'

def rand():
  #returns a random prime under 100000
  primes = open("primelist.txt")
  primelist = primes.read()
  primelist = primelist.split(",")
  length = (len(primelist))
  choice = random.randint(0, length)
  number = primelist[choice]
  return int(number)






@app.route("/", methods = ["GET", "POST"])
def home():

    if request.method == "GET":
        return render_template('main_page.html')
    n = (request.form['numbercollect'])
    if n == '':
        n = rand()
    else:
        n = int(n)




    return redirect(url_for('result_page', number = n))
@app.route("/number/<number>")
def result_page(number):
    if number == 'random':
        number = rand()
    n = int(number)
    session['number'] = n
    session['prime'] = prime(n)
    session['twin'] = twin(n)
    session['balanced'] = balanced(n)
    session['circular'] = circular(n)
    session['cousin'] = cousin(n)
    session['cuban'] = cuban(n)
    session['dihedral'] = dihedral(n)
    session['emirp'] = emirp(n)
    session['factorial'] = factorial(n)
    session['happy'] = happy(n)
    session['lefttruncatable'] = lefttruncatable(n)
    session['righttruncatable'] = righttruncatable(n)
    session['rightandlefttruncatable'] = rightandlefttruncatable(n)
    session['lucas'] = lucas(n)
    session['lucky'] = lucky(n)
    session['mersene'] = mersene(n)
    session['doublemersene'] = doublemersene(n)
    session['palindromic'] = palindromic(n)
    session['absolute'] = absolute(n)
    session['pierpont1'] = pierpont1(n)
    session['pierpont2'] = pierpont2(n)
    session['sexy'] = sexy(n)
    session['quadruplet'] = quadruplet(n)
    session['triplet'] = triplet(n)
    session['primorial'] = primorial(n)
    session['pythagorean'] = pythagorean(n)
    session['sophiegermain'] = sophiegermain(n)
    session['safe'] = safe(n)
    session['strobogrammatic'] = strobogrammatic(n)
    session['wagstaff'] = wagstaff(n)
    session['superprime'] = superprime(n)
    session['strong'] = strong(n)
    session['weak'] = weak(n)
    return render_template('results.html')

@app.route("/<type>")
def type_page(type):
    return render_template('type.html', type=type)
