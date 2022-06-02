from flask import *
import speech_recognition as sr


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('record.html', transcript=transcript)


@app.route("/record/", methods=["GET", "POST"])
def test():
    import SPEECHTOTEXT as s
    s.threading_rec()
    return render_template('record.html')


if __name__ == '__main__':
    app.run(debug=True)