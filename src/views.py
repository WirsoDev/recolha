from src import app
from flask import render_template, redirect, Blueprint
main_bp = Blueprint('main_bp', __name__)



@app.route('/create-rec')
def creatRec():
    
    return render_template('create-rec.html')


    


#test api
@app.route('/api/value1=<x>value2=<y>', methods=['GET', 'POST'])
def api(x, y):

    x = int(x) + 20
    y = int(y) + 20

    print(x, y)

    obj = {
        'dados':{
            x:y
        }
    }
    return obj