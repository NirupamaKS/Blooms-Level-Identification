from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', level1=None)

@app.route('/qp')
def qp():
    return render_template('qp.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    question1 = request.form.get('question1')
    print("Received question:", question1)  # Debugging line
    if question1:
        level1 = analyze_blooms_taxonomy(question1)
        print("Analyzed level:", level1)  # Debugging line
    else:
        level1 = "No question provided"
    return render_template('index.html', level1=level1)

@app.route('/qpanalyze', methods=['POST'])
def qpanalyze():
    blooms_levels = {}

    for i in range(1, 9):
        for part in ['a', 'b']:
            question_key = f'question{i}{part}'
            bloom_key = f'level{i}{part}'
            if question_key in request.form:
                question = request.form[question_key]
                level = analyze_blooms(question)
                blooms_levels[bloom_key] = level

    return render_template('qp.html', **blooms_levels)

def analyze_blooms_taxonomy(question1):
    keywords_to_levels = {
        'Remembering level 1': ['define', 'describe', 'find', 'how', 'list', 'name', 'what', 'where', 'which', 'why', 'draw', 'write'],
        'Understanding level 2': ['compare', 'demonstrate', 'discuss', 'distinguish', 'explain', 'illustrate', 'outline', 'show', 'summarize'],
        'Applying level 3': ['compute', 'develop','analyse','analyze', 'identify', 'make use of', 'select', 'solve', 'utilize', 'use', 'draw', 'illustrate', 'classify', 'solve', 'categorize'],
        'Analyzing level 4': ['classify', 'characterize', 'categorize', 'compare', 'derive', 'distinguish', 'examine', 'inference', 'organize', 'simplify', 'test for', 'identify', 'investigate'],
        'Evaluating level 5': ['assess', 'choose', 'compare', 'decide', 'determine', 'estimate', 'evaluate', 'explain', 'interpret', 'justify', 'measure', 'prioritize', 'prove', 'rate', 'recommend'],
        'Creating level 6': ['build', 'compose', 'construct', 'create', 'design', 'develop', 'discuss', 'elaborate', 'estimate', 'formulate', 'improve', 'maximize', 'modify', 'predict', 'invent']
    }

    # Normalize the input question
    question_lower = question1.lower()

    # Iterate through each level and its keywords to find a match
    for level1, keywords in keywords_to_levels.items():
        for keyword in keywords:
            if keyword in question_lower:
                return level1

    # If no keywords match, return "Uncategorized"
    return "Uncategorized"






def analyze_blooms(question):
    keywords_to_levels = {
        '1': ['define', 'describe', 'find', 'how', 'list', 'name', 'what', 'where', 'which', 'why', 'draw', 'write'],
        '2': ['compare', 'demonstrate', 'discuss', 'distinguish', 'explain', 'illustrate', 'outline', 'show', 'summarize'],
        '3': ['compute', 'analyse','analyze','develop', 'identify', 'make use of', 'select', 'solve', 'utilize', 'use', 'draw', 'illustrate', 'classify', 'solve', 'categorize'],
        '4': ['classify', 'characterize', 'categorize', 'compare', 'derive', 'distinguish', 'examine', 'inference', 'organize', 'simplify', 'test for', 'identify', 'investigate'],
        '5': ['assess', 'choose', 'compare', 'decide', 'determine', 'estimate', 'evaluate', 'explain', 'interpret', 'justify', 'measure', 'prioritize', 'prove', 'rate', 'recommend'],
        '6': ['build', 'compose', 'construct', 'create', 'design', 'develop', 'discuss', 'elaborate', 'estimate', 'formulate', 'improve', 'maximize', 'modify', 'predict', 'invent']
    }


    question_lower = question.lower()
    for level, keywords in keywords_to_levels.items():
        for keyword in keywords:
            if keyword in question_lower:
                return level

    return 'UK'

if __name__ == '__main__':
    app.run(debug=True)
