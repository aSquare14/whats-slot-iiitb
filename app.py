from imports import *
from prof import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
port = int(os.environ.get("PORT", 5000))

script_dir = os.path.dirname(__file__)
minorFileName = 'minor.json'
minorFileName = os.path.join(script_dir, minorFileName)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/search/')
def search():
	query = request.args.get('term')
	results = searchData(query)
	return json.dumps( [ course['Name'] for course in results ] )

@app.route('/ajax/', methods=['POST'])
def getCourse():
	query = request.form.get('query')
	results = searchData(query)
	if results:
		return json.dumps( results[0] )
	else:
		return json.dumps( {} )

@app.route('/minor/')
def minor():
	with app.open_resource(minorFileName, 'r') as minorFile:
		data = json.load(minorFile)
	return json.dumps( data )


@app.route('/professor', methods=['POST'])
def result():
	prof = request.form['prof']
	tb, times, dept, website, prof = fetch_results(prof)
	print(prof)
	return render_template('main.html', name=prof, website=website, data=tb, times=times, profs=profs, dept=dept, error=False)

@app.route('/professor', methods=['GET'])
def prof():
	prof = request.args.get('prof')
	if prof:
		tb, times, dept, website, prof = fetch_results(prof)
		return render_template('main.html', name=prof, website=website, data=tb, times=times, profs=profs, dept=dept, error=False)

	else:
		return render_template('main.html', profs=profs) 

class Room(object):
    def __init__(self, date, room):
        self.date = date
        self.room = room

@app.route('/room')
def room():
	with open(os.path.join(script_dir, 'data/data.json'),'r') as f:
		profs_dict = CaseInsensitiveDict(json.load(f))
	room = {}
	for prof in profs_dict:
		fetch_rooms(prof,room)
	
	my_objects = [ ]
	for item in room:
		my_objects.append(Room(item,room[item]))
	return render_template('room.html', my_objects=my_objects)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)