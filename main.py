from flask import Flask,request,render_template,redirect,url_for
from flask import jsonify
import json
import sqlite3

#=======================change the path of template folder ===================

app = Flask(__name__ , template_folder = "C:/Users/Owner/Desktop/BASEKETBAL/template/")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route("/")
def index():

	return render_template('index.html')


@app.route("/basketball" , methods=['GET', 'POST'])
def func():
	skill = request.form['skill']
	print(skill)

	#return jsonify({'res' : 'done'})
	if skill == 'Best Paid Sport':

		return redirect(url_for('best_paid_sport'))

	elif skill == 'Athletes & Comparing Their Salary':

		return redirect(url_for('Athletes_and_comparing_their_salary'))

	elif skill == 'Endorsement & Salary By Players':

		return redirect(url_for('endorsement_and_salary_by_players'))
		

	elif skill == 'Highest Paid League':

		return redirect(url_for('highest_paid_league'))






# ===================== API's ============================================================


@app.route("/best_paid_sport")
def best_paid_sport():
	with sqlite3.connect("C:/Users/Owner/Desktop/BASEKETBAL/MONEY_IN_SPORTS.db") as conn:
		cur = conn.cursor()
		cur.execute(
			"select t2.Sport_Top_teams_Payroll_List,avg(t2.Average_Annual_pay_per_player) as Annual_Pay from TAS2_V1 as t2 Group BY t2.Sport_Top_teams_Payroll_List ORDER BY avg(t2.Average_Annual_pay_per_player) DESC"
			)
		res = cur.fetchall()
		conn.commit()
		print(res)
		Sport=[]
		Annual_Pay=[]
		
		for i in range (len (res)):
			Sport.append(res[i][0])
			Annual_Pay.append(res[i][1])
		print(Sport) 
		print(Annual_Pay)
		return jsonify({'Sport' : Sport , 'Annual_Pay' : Annual_Pay })


@app.route("/Athletes_and_comparing_their_salary")
def Athletes_and_comparing_their_salary():
	with sqlite3.connect("C:/Users/Owner/Desktop/BASEKETBAL/MONEY_IN_SPORTS.db") as conn:
		cur = conn.cursor()
		cur.execute(
			"select t1.Athlete, t1.Salary_Winnings_millions from TAS1_V1 as t1 Group By t1.Athlete ORDER BY t1.Salary_Winnings_millions DESC"
			)
		res = cur.fetchall()
		conn.commit()
		print(res)
		Sport=[]
		Annual_Pay=[]
		
		for i in range (len (res)):
			Sport.append(res[i][0])
			Annual_Pay.append(res[i][1])
		print(Annual_Pay) 
		return jsonify({'Annual_Pay' : Annual_Pay , 'Sport' : Sport   })

@app.route("/endorsement_and_salary_by_players")
def endorsement_and_salary_by_players():
	with sqlite3.connect("C:/Users/Owner/Desktop/BASEKETBAL/MONEY_IN_SPORTS.db") as conn:
		cur = conn.cursor()
		cur.execute(
			"select t1.Athlete , t1.Endorsements_Millions , t1.Salary_Winnings_millions from TAS1_V1 as t1 Group By t1.Athlete ORDER BY t1.Salary_Winnings_millions DESC "
			)
		res = cur.fetchall()
		conn.commit()
		print(res)
		Athlete=[]
		Annual_Pay=[]
		Sport = []
		
		for i in range (len (res)):
			Athlete.append(res[i][0])
			Annual_Pay.append(res[i][1])
			Sport.append(res[i][2])
		print(Athlete) 
		return jsonify({'Athlete' : Athlete , 'Annual_Pay' : Annual_Pay , 'Sport' : Sport})

@app.route("/highest_paid_league")
def highest_paid_league():
	with sqlite3.connect("C:/Users/Owner/Desktop/BASEKETBAL/MONEY_IN_SPORTS.db") as conn:
		cur = conn.cursor()
		cur.execute(
			"Select T2.League , T2.Total_Payroll from TAS2_V1 as T2 GROUP BY League Order By T2.Total_Payroll DESC"
			)
		res = cur.fetchall()
		conn.commit()
		print(res)
		Sport=[]
		Annual_Pay=[]
		
		for i in range (len (res)):
			Sport.append(res[i][0])
			Annual_Pay.append(res[i][1])
		print(Sport) 
		return jsonify({'Sport' : Sport , 'Annual_Pay' : Annual_Pay })

# ===============================================================================================

if __name__ == '__main__':
	app.run(debug = True)