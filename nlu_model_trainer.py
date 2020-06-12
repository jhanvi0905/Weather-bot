from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory=trainer.persist(model_dir, fixed_model_name='chatbotnlu')
print("training model")
train_nlu('./data/data.md', 'config_spacy.yml', './models/chatbotnlu')


interpret=Interpreter.load('./models/chatbotnlu/default/chatbotnlu')
def ask_ques(text):
    print(interpret.parse(text))
ask_ques("How is life")
ask_ques("hello")
ask_ques("good bye")
ask_ques('what is the weather in Ahmedabad')