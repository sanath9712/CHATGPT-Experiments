class APIKeys:
    def __init__(self):
        self.openai_key = '<ADD YOUR OPEN AI API KEY HERE>'

    def get_openai_key(self):
        return self.openai_key


class FirebaseAuth:
    def __init__(self):
        self.servicekeyfile = 'firebasecred.json'
        self.project_id = '<Add your firebase project ID here>'

    def get_service_keyfile(self):
        return self.servicekeyfile

    def get_project_id(self):
        return self.project_id
