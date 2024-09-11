from GMAutomator import GMAutomator
from flask import Flask, request, jsonify

app = Flask(__name__)

gm_automator = GMAutomator()

@app.route('/join-meeting', methods=['POST'])
def join_meeting():

    if request.is_json:

        data = request.get_json()

        if "link" in data and "name" in data:

            gm_automator.join_meeting(meeting_link=data["link"], username=data["name"])

            return jsonify({"msg": "Meeting joined successfully."})

        else:

            return jsonify({"msg": "Missing parameters."})
    else:
        
        return jsonify({"msg": "Request must be JSON."})

@app.route('/left-meeting')
def left_meeting():

    gm_automator.leave_meeting()

    return jsonify({"msg": "Meeting left successfully."})


if __name__ == "__main__":

    app.run(host='0.0.0.0', port= 80)