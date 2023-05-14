import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def fetch_topic_dict_from_firestore(service_account_key_path, project_id):
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

# Example usage:
service_account_key_path = 'path/to/serviceAccountKey.json'
project_id = 'your-project-id'
topic_dict = fetch_topic_dict_from_firestore(service_account_key_path, project_id)
print(topic_dict)
