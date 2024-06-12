import numpy as np


from flask import Flask, render_template

app = Flask(_name_, template_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('tab.html')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000, debug=False)