from flask import Flask, render_template, request

app = Flask(__name__)

# Simple quiz data
quiz = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
]

@app.route('/quiz', methods=['GET', 'POST'])
def take_quiz():
    if request.method == 'POST':
        score = sum(1 for i, q in enumerate(quiz) if request.form.get(f'question-{i}') == q['answer'])
        return f'Your score: {score} out of {len(quiz)}'

    return render_template('quiz.html', questions=quiz)

if __name__ == '__main__':
    app.run(debug=True)
