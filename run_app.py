from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/chatbotnlu/default/chatbotnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/current/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-648575328130-655090052769-QhOthMP9CvFMxvthqyDl5eJv')

agent.handle_channels([input_channel], 5004, serve_forever=True)
