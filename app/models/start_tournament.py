from app.models.tournament import Tournament
import random as rd
tournament = Tournament()

def simulate_pc_choice():
    CHOICES = ['rock', 'paper', 'scissors']
    weights = [.3, .3, .3]
    return rd.choices(CHOICES, weights)[0]