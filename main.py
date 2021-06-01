from flask import Flask, redirect, url_for, render_template, jsonify, request
import csv 


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


def getGrav(usager, Num_Acc):

	#my_tuple = []

	try:
		
		for rowUser in usager:

			if rowUser[0] == Num_Acc:


				return rowUser[3]

	except:

		print("Erreur de lecture ...")




	

@app.route('/render', methods=['POST'])
def render():

	result = request.form 


	annee = result['an'] # récupérer l'année qu'on veut étudier
	jour = result['jour']
	mois = result['mois']
	lum = result['lum']
	dep = result['dep']
	inter = result['inter']
	atm = result['atm']
	





	# ouverture des fichiers csv 
	fileCarac = open(f"data/caracteristiques/caracteristiques_{annee}.csv", "r", errors="ignore")
	fileUsager = open(f"data/usagers/usagers_{annee}.csv", "r", errors="ignore")


	

	


	try:
		caracteristique = csv.reader(fileCarac)
		usager = csv.reader(fileUsager)


		coord = {}
		coord_child = []



		for row in caracteristique:

			try:
				coord_child.append({
						"Num_Acc": row[0],
						"an": row[1],
						"mois" : row[2],
						"jour" : row[3],
						"lum": row[5],
						"agg": row[6],
						"inter": row[7],
						"atm": row[8],
						"col": row[9],
						"com": row[10],
						"gps": row[12],
						"lat": row[13],
						"lng": row[14],
						"dep": row[15],
						"grav": getGrav(usager, row[0])
						
				})

				

			except:

				continue
		


		coord["location"] = coord_child


	finally: 
		fileCarac.close()
		fileUsager.close()


	return render_template("render.html", coord = coord, annee = annee, jour = jour, mois = mois, lum = lum, dep = dep, inter = inter, atm = atm)

if __name__ == "__main__":
    app.run()
