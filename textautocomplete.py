# import systemcheck
from flask import Flask, jsonify, request, redirect, render_template
import GRU  


lexicon = {}
app = Flask(__name__)
app.secret_key = "secret key"


import os, json
 
	
@app.route('/')
def upload_form():
	 
	return render_template('index.html')

@app.route('/search', methods=['POST',"GET"])
def search():
	term = request.form['q'] 
 
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__)) 
	json_url = os.path.join(SITE_ROOT, "data", "subject_lines.json")
	json_data = json.loads(open(json_url).read()) 
 
	if(term.endswith(" ")):
		term_last_index = len(term.split())-1
		filtered_dict = [v.split()[term_last_index+1] for v in json_data if v.lower().startswith(term.lower()) and len(v.split())>len(term.split()) ]
	else:
		term_last_index = len(term.split())-1
		filtered_dict = [v.split()[term_last_index] for v in json_data if ( term.lower() in (v.lower()) and v.lower().startswith(term.lower()))  ]

	filtered_dict = list(set(filtered_dict))

	print(filtered_dict)
	
	resp = jsonify(filtered_dict)
	resp.status_code = 200
	return resp

@app.route('/autocomplete_text', methods=['POST',"GET"])
def autocomplete_text():
	term = request.form['q'] 
 
	with open('data/english_data.txt') as f:
		contents = f.read() 

	json_data = contents.splitlines() 

	filtered_dict = []

	for v in json_data:
		if term.lower() in v:
			filtered_dict.append(v)
			print(v)
 
	print(filtered_dict)
	
	resp = jsonify(filtered_dict)
	resp.status_code = 200
	return resp

@app.route('/result', methods=['POST',"GET"])
def result():
	result_term = request.form['input_text']
	# print ('Result: ', result_term)
	

	output_result = GRU.GRU(result_term)
	# print(output_result)

	result_resp = jsonify(output_result)

	 
	result_resp.status_code = 200

	print("result_resp : " , result_resp)
	return result_resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080) 


