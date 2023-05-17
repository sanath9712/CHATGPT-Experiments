from helpers.credentials import FirebaseAuth
from helpers.utilities import DataHandler
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(facts):
    #Load the pre-trained model
    model = SentenceTransformer('bert-base-nli-mean-tokens')

    #Encode the facts into fixed-length vectors
    fact_embeddings = model.encode(facts)

    #Compute pairwise cosine similarity between the fact embeddings
    similarity_matrix = cosine_similarity(fact_embeddings)

    #Calculate the average similarity
    overall_similarity = similarity_matrix.mean()

    return overall_similarity

def main():
    data_fetcher = DataHandler()
    firebaseauth = FirebaseAuth()
    topic_dict = data_fetcher.fetch_topic_dict_from_firestore(firebaseauth.get_service_keyfile(),
                                                              firebaseauth.get_project_id())

    for topic in topic_dict:
        sim_score = calculate_similarity(topic_dict[topic])
        print("The similarity for " + topic + " is " + str(sim_score))





if __name__ == '__main__':
    main()
