# GoogleMeetAutomation

## Project Overview
GoogleMeetAutomation is a simple tool to automate the process of creating, joining, and managing Google Meet sessions. This project provides APIs to automate these tasks, making it ideal for developers looking to integrate Google Meet functionality into their applications.

## Applications

### Client

Offer following endpoints to join and leave google meetings:

- /join-meeting

    Method: POST
    
    Accepts: Json

        Parameters:
        - link
            Link of google meeting.
        - name
            Name to join as google meeting.

        Example:

        {"link" : "GOOGLE_MEET_LINK", "name": "USERNAME"}

    Returns: Json

        Success: {"msg": "Meeting joined successfully."}

        Error: 

            - {"msg": "Missing parameters."}

            - {"msg": "Request must be JSON."}

- /left-meeting

    Method: GET

    Returns: Json

        Success: {"msg": "Meeting left successfully."}

### Server

Offer following endpoints to join and leave google meetings:

- /create-meeting

    Method: GET

    Returns: Json

        Success: {"id": "MEETING_ID", "link": "MEETING_LINK"}

- /meeting-details

    Method: POST

    Accepts: Json

        Parameters:
        - id
            id of google meeting.

        Example:

        {"id" : "GOOGLE_MEETING_ID"}

    Returns: Json

        Success: {"name": self.name, "code": self.code, "start_time": str(self.start_time), 
                           "expire_time": str(self.expire_time), "conference_record": self.conference_record,
                            "link": self.link, "participants": self.participants}

        Error: 

            - {"msg": "Invalid Parameter."}

            - {"msg": "Invalid id."}

            - {"msg": "Missing parameters."}

            - {"msg": "Request must be JSON."}

- /get-meeting-link

    Method: POST

    Accepts: Json

        Parameters:
        - id
            id of google meeting.

        Example:

        {"id" : "GOOGLE_MEETING_ID"}

    Returns: Json

        Success: {"id": "MEETING_ID", "link": "MEETING_LINK"}

        Error: 

            - {"msg": "Invalid Parameter."}

            - {"msg": "Invalid id."}

            - {"msg": "Missing parameters."}

            - {"msg": "Request must be JSON."}

- /clear-meetings

    Method: GET

    Returns: Json

        Success: {"msg": "Meetings cleared."}