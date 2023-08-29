import os
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_cors import CORS

app = Flask(
    __name__
)
CORS(app)

@app.route('/form/contact', methods=['POST'])
def contactform():
    print(request.form)
    return jsonify(request.form)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
