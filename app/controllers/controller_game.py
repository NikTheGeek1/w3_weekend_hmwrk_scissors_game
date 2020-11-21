from flask import Flask, render_template, redirect, request
from app import app

from app.models.player import Player
from app.models.start_tournament import tournament

@app.route('/game')
def game():
    return redirect('/game/hum_vs_hum')

@app.route('/game/hum_vs_hum')
def game_hh():
    return render_template('/game/human_vs_human.html', title = 'Game', selected = 'hh', matches = tournament.history['hh'])

@app.route('/game/hum_vs_comp')
def game_hc():
    return render_template('/game/pc_vs_human.html', title = 'Game', selected = 'hc', matches = tournament.history['hc'])

@app.route('/game/comp_vs_comp')   
def game_cc():
    return render_template('/game/pc_vs_pc.html', title = 'Game', selected = 'cc', matches = tournament.history['cc'])

@app.route('/game/hum_vs_hum/play', methods = ['POST'])
def hh_play():
    p1_name = request.form.get('p1-name')
    p2_name = request.form.get('p2-name')
    p1_choice = request.form.get('hand-p1')
    p2_choice = request.form.get('hand-p2')
    p1 = Player(p1_name, p1_choice)
    p2 = Player(p2_name, p2_choice)
    winner = tournament.game(p1, p2, 'hh')
    return render_template('/game/who-won.html', title = "Game", selected = 'hh', winner = winner.name, matches = tournament.history['hh'])
