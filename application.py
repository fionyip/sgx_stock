from flask import Flask, request, render_template
from simple_crawler import request_stock_p
import time
import pandas as pd
from threading import Timer
application = Flask(__name__)

df = pd.DataFrame(request_stock_p()).to_html()
def show_df(interval):
  Timer(interval, show_df, [interval]).start()      
  global df
  df = pd.DataFrame(request_stock_p()).to_html()

# update data every second
show_df(60)

@application.route("/")
def index():
    return df

# @app.route("/")
# def show_df(interval):
#     Timer(interval, show_df, [interval]).start()      
#     df = request_stock_p()
#     global pd.DataFrame(df).to_html()



if __name__ =="__main__":
    application.run(debug=True)
