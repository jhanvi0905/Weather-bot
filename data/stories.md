## greeting
* greeting
- utter_greeting

## how are you
* how_are_you
- utter_how_i_am

## good bye
* bye
- utter_bye

## my name is
* my_name_is
- utter_its_nice_to_meet_you
## story 1
* greeting
    - utter_greeting
* my_name_is{"PERSON": "jhanvi"}
    - utter_its_nice_to_meet_you
* my_name_is{"PERSON": "Javk"}
    - utter_its_nice_to_meet_you
* my_name_is{"PERSON": "Mark"}
    - slot{"PERSON": "Mark"}
    - utter_its_nice_to_meet_you
* my_name_is{"PERSON": "jhanvi"}
    - utter_its_nice_to_meet_you
* bye
    - utter_bye
    - action_restart

## Generated Story -6796816239023196207
* greeting
    - utter_greeting
* my_name_is{"PERSON": "jhanvi"}
    - slot{"PERSON": "jhanvi"}
    - utter_its_nice_to_meet_you
* greeting
    - utter_greeting
* get_weather{"GPE": "Ahmedabad"}
    - slot{"GPE": "Ahmedabad"}
	- action_get_weather
* get_weather{"GPE": "Ahmedbad"}
    - slot{"GPE": "Ahmedbad"}
    - action_get_weather
* get_weather{"GPE": "Ahmedabad"}
    - slot{"GPE": "Ahmedabad"}
    - action_get_weather

## Generated Story 2677596708763202869
* Hi
    - utter_greeting
* my_name_is{"PERSON": "Jhanvi"}
    - slot{"PERSON": "Jhanvi"}
    - utter_its_nice_to_meet_you
* get_weather{"GPE": "Ahmedabad"}
    - slot{"GPE": "Ahmedabad"}
    - action_get_weather


