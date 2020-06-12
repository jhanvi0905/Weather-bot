# Weather-bot
A chatbot that updates you of the weather at the place, day and time you ask for.

This Weather showing bot is made using the Rasa Python library which helps building custom Natural Language Understanding Models and Dialogue Generation Models.

# NLU Model of the Bot:
 
To train the model run nlu_model_trainer.py. It takes two things as input, data for training and configuration file.

Data- data.md contains intent and slot related data to train the nlu model 

config_spacy.yml- Rasa module provides support for many existing nlp libraries, hence which backbone library to use for intent classification and for named entity recognition (slot_tagging) is specified through this file.

The trained intent classifier and NER models are saved in models/chatbotnlu folder.

# Dialogue Generation Model:

The model is trained based on the stories.md data, which contains example conversations the bot with the bot to identify intent and slot.
The dialogue generation training takes two things - 

Data- stories.md 

chat_domain.yml- The file consist of list of intents, slots and actions to be performed for a given intent.

The trained dialogue model is persisted to models/current folder.

# Actions

The utter actions are specified directly in the yml file, however for slot based actions or information gathering type actions we write code for tracking the user dialogue.

actions.py - tracks the dialogue with the intent of get_weather and tracks the slots to obtain weather through the OpenWeather API.

Run bot.py to train the dialogue model and obtain a commandline version of the bot.

Run run_app.py - for deploying the bot on slack using rasa's slack input channel.

P.S- Generated stories are the real time stories generated while conversing with the bot and stored in stories.md, which further were used to improve the precision of dialogue generation model.

![running instance of the bot](https://github.com/jhanvi0905/Weather-bot/blob/master/weather-bot-running.png)



