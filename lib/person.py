#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Brent', job='Human Resources'):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 25):
            self._name = new_name.title()
        else:
            print('Name must be string between 1 and 25 characters.')

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job
        else:
            print('Job must be in list of approved jobs.')
