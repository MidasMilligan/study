from flask import Flask
from redis import Redis
import datetime
app = Flask(__name__)
db = Redis (host="redis")

@app.route("/")
def hello():
    visitsCounter = db.incr('visitsCounter')
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    html = "<H1> Hello!!! </H1>" \
	"<p> Current time: {time}<p>"\
    "<b>Visits: </b>{visits}<br>"\
	"</br>"

    return html.format(visits=visitsCounter, time=current_time)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)

