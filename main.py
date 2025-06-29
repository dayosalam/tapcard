from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    with open('tapcard.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
    
