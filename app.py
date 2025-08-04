from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contacts = []

@app.route('/')
def home():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    contacts.append({'name': name, 'phone': phone})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect('/')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)