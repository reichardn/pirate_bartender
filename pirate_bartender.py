import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def question_ask():
    answers = {}
    for i in questions:
        n = raw_input(questions[i])
        if n == "y" or n == "yes":
            answers[i] = True
        else:
            answers[i] = False
            
    return answers

 

def create_drink(answers):
    drink = []
    for i in ingredients:
        if answers[i]:
            drink.append(random.choice(ingredients[i]))
    return drink

answers = question_ask() 

drink = create_drink(answers)

print drink