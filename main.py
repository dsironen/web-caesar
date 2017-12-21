from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method='POST'>
            <label>Rotate by: <input type="text" name="rot" value="0"></label>
            <textarea name="text" >{0}</textarea>
            <input type="submit" value='Submit query' />
        </form>

    </body>
</html>

"""
@app.route("/")
def index():
    return form.format('')

def is_integer(rot):
    try:
        int(rot)
        return True
    except ValueError:
        return False




@app.route("/", methods=['POST','GET'])
def encrypt():

    if not is_integer(request.form['rot']):
        rot_text = 'Not a valid integer'
       
    else:
        var_rot = int(request.form['rot'])
        var_text = request.form['text']
        rot_text = rotate_string(var_text,var_rot)
   
    return form.format(rot_text)

app.run()