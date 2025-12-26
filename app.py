from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Note
from ai_utils import summarize_text

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template("index.html", notes=notes)


@app.route("/create", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        #  AI Summary
        try:
            summary = summarize_text(content)
            print("AI SUMMARY:", summary)
        except Exception as e:
            summary = "AI summary could not be generated."

        note = Note(
            title=title,
            content=content,
            summary=summary
        )

        db.session.add(note)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create_note.html")


@app.route("/note/<int:note_id>")
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template("view_note.html", note=note)


@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
