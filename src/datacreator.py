import csv
import openai
import os
from helpers.promptgenerator import Topics, RandomFactPrompts
from helpers.utilities import DataInterpreter
from helpers.creds import APIKeys

# set up ChatGPT API credentials
openaikey = APIKeys()
openai.api_key = openaikey.get_openai_key()


class MainProgram:
    def __init__(self):
        self.topics = Topics()

    def print_topics(self):
        topic_list = self.topics.get_topics()
        print(topic_list)

    def get_topics(self):
        topic_list = self.topics.get_topics()
        return topic_list


def generate_text(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    message = response.choices[0].text.strip()

    return message


def prompt_chatgpt(topics):
    file_path = os.path.join('..', 'GeneratedData', 'RandomFacts.csv')

    # Create a dictionary to hold the topics and their random facts
    topic_dict = {}

    # Check if file exists
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file_read:
            reader = csv.reader(file_read)
            next(reader)  # skip the header row
            for row in reader:
                topic_dict[row[0]] = row[1]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic', 'Random Fact'])

        for topic in topics:
            prompt = RandomFactPrompts(topic).get_random_prompt()
            response = generate_text(prompt)

            if topic in topic_dict:
                topic_dict[topic] += '<!!!!>' + response
            else:
                topic_dict[topic] = response

        # Write the data to the CSV file
        for topic, fact in topic_dict.items():
            writer.writerow([topic, fact])

        return file_path


def main():
    prog = MainProgram()
    topics = prog.get_topics()
    file_path = prompt_chatgpt(topics)
    filereader = DataInterpreter(file_path)
    filereader.read_csv_file()


if __name__ == '__main__':
    main()
