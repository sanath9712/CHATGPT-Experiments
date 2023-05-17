import csv
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from src.helpers.credentials import FirebaseAuth


class DataHandler:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def fetch_topic_dict_from_firestore(self, service_account_key_path, project_id):
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred, {
            'projectId': project_id,
        })
        client = firestore.client()

        # Reference the collection containing the topics
        collection_ref = client.collection('topics')

        # Retrieve all documents in the collection
        docs = collection_ref.get()

        # Construct the topic_dict from Firestore data
        topic_dict = {}
        for doc in docs:
            topic_name = doc.id
            facts = doc.to_dict().get('facts', [])
            topic_dict[topic_name] = facts

        return topic_dict

    def write_to_firestore(self, service_account_key_path, project_id, topic_dict):
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred, {
            'projectId': project_id,
        })
        client = firestore.client()

        for topic_name, facts in topic_dict.items():
            topic_ref = client.collection('topics').document(topic_name)
            topic_ref.update({
                'facts': firestore.ArrayUnion(facts)
            })

    def read_csv_file(self):
        topic_dict = {}
        if os.path.isfile(self.file_path):
            with open(self.file_path, 'r') as file_read:
                reader = csv.reader(file_read)
                next(reader)  # skip the header row
                for row in reader:
                    topic_dict[row[0]] = row[1].split('<!!!!>')

        firebasecred = FirebaseAuth()
        servicekeyfilepath = firebasecred.get_service_keyfile()
        project_id = firebasecred.get_project_id()
        self.write_to_firestore(servicekeyfilepath, project_id, topic_dict)
