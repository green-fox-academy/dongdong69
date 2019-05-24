from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    language_John = ["Hello, John!", "你好约翰！", "سلام جان!", "こんにちはジョンさん！"]

    random_index = random.randint(0, len(language_John) - 1)
    return render_template('Random language.html', language = language_John[random_index])

if __name__ == "__main__":
    app.run()