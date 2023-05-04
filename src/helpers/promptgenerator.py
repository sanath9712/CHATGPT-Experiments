import random


class Topics:
    def __init__(self):
        self.topics = ['Technology', 'Rain', 'Basket', 'Drama', 'Hope', 'Innovation', 'Circus', 'Gymnastics', 'Prison',
                       'Fitness',
                       'Universe', 'Bacteria', 'Tiger', 'Loneliness', 'Wave', 'Carnival', 'Comet', 'Sleep', 'Winter',
                       'Robot',
                       'Melody', 'Cinema', 'Waterfall', 'Sculpture', 'Safari', 'Bridge', 'Cosmos', 'City', 'Horse',
                       'Adventure',
                       'Wildfire', 'Journalism', 'Disaster', 'Astronomy', 'Thunderstorm', 'Nostalgia', 'Electricity',
                       'Flower',
                       'Jungle', 'Chaos', 'Eclipse', 'Harmony', 'Rainforest', 'Autumn', 'Wrestling', 'Gravity',
                       'Furniture',
                       'Mountains', 'Democracy', 'Pyramid', 'Chocolate', 'Robotics', 'Tornado', 'Freedom',
                       'Celebration',
                       'Insect', 'Ballet', 'Galaxy', 'Faith', 'Oasis', 'Mushroom', 'Engineering', 'Cactus', 'Justice',
                       'Fantasy',
                       'Fashion', 'Snow', 'Culture', 'Blossom', 'Summer', 'Mystery', 'Bicycle', 'Eagle', 'Heritage',
                       'Water',
                       'Road', 'Disco', 'Sculpture', 'Origami', 'Environment', 'Creativity', 'Desert', 'Robot',
                       'Nightmare',
                       'Bee', 'Meditation', 'Secret', 'Bangalore']

        # Randomly select 50 topics from the list, ensuring that Bangalore is one of them
        self.topics = ['Bangalore'] + random.sample(set(self.topics) - {'Bangalore'}, 49)

        random.shuffle(self.topics)

    def get_topics(self):
        return self.topics


class RandomFactPrompts:
    def __init__(self, token):
        self.random_prompt = "In about 100 words, Give me a random fact about: " + token

    def get_random_prompt(self):
        return self.random_prompt

