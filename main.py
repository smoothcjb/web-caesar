from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
  <html>
   <head> 
     <style>
       form{

           background-color: #eee;
           padding: 20px;
           margin: 0 auto;
           width: 540px;
           font: 16px sans-serif;
           border-radius: 10px;
       }
   
   textarea{
     margin: 10px 0;
     width: 540px;
     height: 120px;    
   }
     </style>
   </head>
     <body>
       <!--create your form here-->
     <form action="/" method="post">
         <label><strong>Rotate by:</strong><input type="text" name="rot" value="0"/></label> 
         <textarea name="text"></textarea>
        <input type="submit"/>
     </form>
     </body>
   </html)
 
 <input type="submit"/>


"""

@app.route("/")
def index():
    return form


app.run()   
