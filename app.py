from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    four_art = """
           _____
          / __ |
         / / | |
        / /  | |
       / /   | |
      / /____| |
     /_______  |
             | |
             |_|
""" 
    return render_template_string('<pre>{{ four_art }}</pre>', four_art=four_art)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
