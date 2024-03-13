#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Mr Pup', breed='Mastiff'):
        self.name = name
        self.breed = breed
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 25):
            self._name = new_name
        else:
            print('Name must be string between 1 and 25 characters.')

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if not new_breed in APPROVED_BREEDS:
            print('Breed must be in list of approved breeds.')
        else:
            self._breed = new_breed
