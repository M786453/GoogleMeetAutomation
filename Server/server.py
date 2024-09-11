from __future__ import print_function
from flask import Flask, request, jsonify
from Meeting import Meeting

meetings_list = []

server = Flask(__name__)

@server.route('/create-meeting')
def create_meeting():
    meeting = Meeting()
    meeting.create()
    meetings_list.append(meeting)
    return jsonify({"id": len(meetings_list), "link": meeting.link})

@server.route('/meeting-details', methods=['POST'])
def get_meeting_details():

    if request.is_json:

        data = request.get_json()

        print("Data:", data)

        if "id" in data:

            try:

                meeting_id = data["id"]

                if meeting_id > 0 and meeting_id <= len(meetings_list): 

                    meeting = meetings_list[meeting_id - 1]

                    return jsonify(meeting.details())
                
                else:

                    return jsonify({"msg": "Invalid Parameter."})

            
            except:

                return jsonify({"msg": "Invalid id."})

        else:

            return jsonify({"msg": "Missing parameters."})
        
    else:

        return jsonify({"msg": "Request must be JSON."})

@server.route('/get-meeting-link', methods=['POST'])
def get_meeting_link():
    
    if request.is_json:

        data = request.get_json()

        if "id" in data:

            try:

                meeting_id = data["id"]

                if meeting_id > 0 and meeting_id <= len(meetings_list): 

                    meeting = meetings_list[meeting_id - 1]

                    return jsonify({"id": meeting_id, "link": meeting.link})
                
                else:

                    return jsonify({"msg": "Invalid Parameter."})

            except:

                return jsonify({"msg": "Invalid id."})

        else:

            return jsonify({"msg": "Missing parameters."})            

    else:

        return jsonify({"msg": "Request must be JSON."})
    
@server.route('/clear-meetings')
def clear_meetings():

    meetings_list.clear()

    return jsonify({"msg": "Meetings cleared."})


if __name__ == '__main__':
    
    server.run(host= '0.0.0.0')