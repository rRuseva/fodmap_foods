from flask import Flask, render_template, request
import processing as pr
import os
import requests
from waitress import serve

foods_dict = {}

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ewrfewr'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', food_results=[], 
                           number_of_results=0)

@app.route('/foods')
def get_food_info():
    food = request.args.get('food')
    print(f"{food=}")

    food_results = pr.look_up_by_food_name(food, foods_dict)

    print(f"found: {len(food_results)}")
    if len(food_results) == 0:
        return render_template('food-not-found.html')
    
    food_results = sorted(food_results, key=lambda food:food.fodmap_type, reverse=True)
    return render_template("index.html",
                           food_results=food_results, 
                           number_of_results=len(food_results) )

if __name__ == "__main__":
    foods_dict = pr.read_food_catalog("food_catalog.csv")
    print(f"foods catalog: {len(foods_dict)} ")

    serve(app, host="0.0.0.0", port=8000)
    print("server started")
    
    # with open("food_catalog.txt") as my_file:
    #     print(my_file.read())