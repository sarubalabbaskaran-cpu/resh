from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>EduGenie</title>
    </head>
    <body>
        <h1>EduGenie 📚</h1>

        <input id="question" type="text" placeholder="Ask your question">
        <button onclick="askQuestion()">Ask</button>

        <p id="answer"></p>

        <script>
        function askQuestion() {
            let question = document.getElementById("question").value;

            if (question.trim() === "") {
                document.getElementById("answer").innerText =
                    "Please enter a question.";
                return;
            }

            document.getElementById("answer").innerText =
                "You asked: " + question;
        }
        </script>
    </body>
    </html>
    """
