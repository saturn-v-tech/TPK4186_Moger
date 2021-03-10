"""
Practical Python: Factory Design Pattern
https://www.youtube.com/watch?v=6owDuFFXjQU
"""

import random 
from abc import ABC, abstractmethod

class Character(ABC): 
    @abstractmethod
    def __init__(self):
        self.__hit_points = None # Private attributes which we can access by setters and getters 
        self.__health_points = None

    @abstractmethod
    def set_hit_points(self):
        pass 

    @abstractmethod
    def set_health_points(self):
        pass 

    @abstractmethod
    def get_info(self):
        pass 


class Hero: 
    heroes = ['Iron Man', ' Captain America']

    power_bonus = {
        'laser': 10 
        'punches and kicks': 5
        
    }

