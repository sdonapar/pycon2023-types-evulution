from typing import TypedDict

conference = {'name': "Pycon India", 'year': 2023, 'location': 'Hyderabad'}

class Conference(TypedDict, total=True): # By default total=True
    name: str
    year: int
    location: str

pycon_india: Conference = {'name': "Pycon India", 'year': 2023, 'location': 'Hyderabad'}
pycon_india_workshop: Conference = {'name': "Pycon India Workshop", 'year': 2023}