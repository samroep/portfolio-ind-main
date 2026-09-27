#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = False
    button_discord = False
    button_html = False
    button_db = False

    if request.method == 'POST':
        if 'button_python' in request.form:
            button_python = True

        elif 'button_discord' in request.form:
            button_discord = True

        elif 'button_html' in request.form:
            button_html = True

        elif 'button_db' in request.form:
            button_db = True

    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )


#Keterampilan Dinamis
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    email = request.form.get('email')
    text = request.form.get('text')

    if email and text:
        print("email:", email)
        print("comment:", text)
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)
