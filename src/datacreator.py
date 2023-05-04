import csv
import openai
import os
from helpers.utilities import Topics, RandomFactPrompts, APIKeys

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
    # Create a CSV file for storing the prompt and response data
    with open(os.path.join('..', 'GeneratedData', 'RandomFacts.csv'), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic', 'Random Fact'])

        for topic in topics:
            prompt = RandomFactPrompts(topic).get_random_prompt()
            response = generate_text(prompt)

            # Write the prompt and response data to the CSV file
            writer.writerow([topic, response])


def main():
    prog = MainProgram()
    topics = prog.get_topics()
    prompt_chatgpt(topics)


if __name__ == '__main__':
    main()
