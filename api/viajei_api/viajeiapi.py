from fastapi import FastAPI
from fastapi.responses import HTMLRespons

app = FastAPI()

@app.get('/', response_class=HTMLRespons)
def reed_root():
    return """
    <html>
      <head>
      </head>
      <body>
      <h1> olá mundo</h1>
      </body>
     </html>
       """