import json
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import meet_v2

class Meeting:

    def __init__(self):
        
        self.name = ""

        self.code = ""

        self.start_time = ""

        self.expire_time = ""

        self.conference_record = ""

        self.link = ""

        self.participants = []

        self.credentials = None

        self.setup_google_meet_api()

    def setup_google_meet_api(self):
    
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/meetings.space.created']

        creds = None

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.credentials = creds
    
    def create(self):

        try:

            client = meet_v2.SpacesServiceClient(credentials=self.credentials)

            request = meet_v2.CreateSpaceRequest()

            request.space.config.access_type = "OPEN" # Anyone can join the meeting

            response = client.create_space(request=request)
            
            self.name = response.name

            self.code = response.meeting_code

            self.conference_record = response.active_conference.conference_record

            self.link = response.meeting_uri
        
        except Exception as error:
            
            print(f'An error occurred: {error}')
    
    def update_conference_record(self):

        try:

            client = meet_v2.SpacesServiceClient(credentials=self.credentials)

            request = meet_v2.GetSpaceRequest(
                name=self.name
            )

            response = client.get_space(request=request)

            self.conference_record = response.active_conference.conference_record

        except Exception as e:

            print("Error @ update_conference_record:", e)

    def details(self):

        try:

            self.update_conference_record()

            if self.conference_record:

                client = meet_v2.ConferenceRecordsServiceClient(credentials=self.credentials)

                participants = client.list_participants(parent=self.conference_record)
                
                # Retrieve Participants

                participants_list = []

                for p in participants:

                    if p.anonymous_user:
                        participants_list.append(p.anonymous_user.display_name)

                    if p.signedin_user:
                        participants_list.append(p.signedin_user.display_name)

                self.participants = participants_list

                # Retrieve Conference Record

                conference_record = list(client.list_conference_records())[0]

                self.start_time = conference_record.start_time

                self.expire_time = conference_record.expire_time
            
            else:

                self.participants = []

                self.start_time = ""

                self.expire_time = ""

            print("Meeting:",self.jsonfiy())

        except Exception as e:

            print("Error @ get_meeting_details:", e)
        
        return self.jsonfiy()
    
    def jsonfiy(self):
        return json.dumps({"name": self.name, "code": self.code, "start_time": str(self.start_time), 
                           "expire_time": str(self.expire_time), "conference_record": self.conference_record,
                            "link": self.link, "participants": self.participants})