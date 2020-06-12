from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.domain import Domain
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer
#from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.run import serve_application
from rasa_core.utils import EndpointConfig
logging.basicConfig(level='INFO')

def train_dialogue():
    training_data_file = './data/stories.md'
    model_path = './models/current/dialogue'

    agent = Agent('chat_domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])
    data = agent.load_data(training_data_file)
    agent.train(data)

    agent.persist(model_path)
    return agent

def run_dialogue():
    interpreter=RasaNLUInterpreter('./models/chatbotnlu/default/chatbotnlu')
    #action_endpoint=EndpointConfig(url='http://localhost:5055/webhook')
    agent = Agent.load('./models/current/dialogue', interpreter=interpreter)
    serve_application(agent, channel='cmdline')
    #do_interactive_learning(cmdline_args=)
    return agent
#weathers.ActionGetWeather()
train_dialogue()
run_dialogue()
