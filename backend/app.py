from flask import Flask, request, jsonify
from resume_parser import extract_resume_data
from matcher import match_resume_to_jd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_resume():
    resume = request.files['resume']
    jd = request.form['jd']
    parsed_resume = extract_resume_data(resume)
    match_score = match_resume_to_jd(parsed_resume, jd)
    return jsonify({'resume_data': parsed_resume, 'match_score': match_score})

if __name__ == '__main__':
    app.run(debug=True)
