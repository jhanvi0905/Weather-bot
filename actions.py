from pyowm import OWM
from rasa_core.actions.action import Action
from rasa_core.domain import Domain
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json
from rasa_core.trackers import DialogueStateTracker
class ActionGetWeather(Action):
    
    def name(self):
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain):
        from pyowm import OWM
        API_key = 'API KEY'
        owm = OWM(API_key)
        city = tracker.get_slot('GPE')
        dispatcher.utter_message('Retreieved location: '+str(city))
        #city="Berlin"
        #print(city)
        obs = owm.weather_at_place(city)
        
        w = obs.get_weather()
        s = w.get_temperature()
        t = w.get_status()
        #t = obs.get_status()
        dispatcher.utter_message("The temperature is: " +str(s)+" Status: "+ str(t))
        return[]
     

#+'Status:'+str(t)"
