from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jd(resume_data, jd_text):
    resume_text = ' '.join(resume_data['skills'])
    docs = [jd_text, resume_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)
