import re
import docx2txt
from PyPDF2 import PdfReader

def extract_text(file):
    if file.filename.endswith('.pdf'):
        reader = PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    elif file.filename.endswith('.docx'):
        text = docx2txt.process(file)
    else:
        text = file.read().decode('utf-8')
    return text

def extract_resume_data(file):
    text = extract_text(file)
    name = re.findall(r'[A-Z][a-z]+\s[A-Z][a-z]+', text)[:1]
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    skills = re.findall(r'(Python|Java|Node\.js|C\+\+|SQL|ML|AI)', text, re.IGNORECASE)
    return {
        'name': name[0] if name else 'N/A',
        'email': email[0] if email else 'N/A',
        'skills': list(set([s.lower() for s in skills]))
    }
