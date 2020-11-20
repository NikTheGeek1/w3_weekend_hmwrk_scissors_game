from flask import Flask, render_template, redirect
from app import app


@app.route('/game')
def game():
    return redirect('/game/hum_vs_hum')

@app.route('/game/hum_vs_hum')
def game_hh():
    return render_template('/game/human_vs_human.html', title = 'Game', selected = 'hh')

@app.route('/game/hum_vs_comp')
def game_hc():
    return render_template('/game/pc_vs_human.html', title = 'Game', selected = 'hc')

@app.route('/game/comp_vs_comp')   
def game_cc():
    return render_template('/game/pc_vs_pc.html', title = 'Game', selected = 'cc')
