document.getElementById('uploadForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const formData = new FormData();
  const resumeFile = document.getElementById('resume').files[0];
  const jdText = document.getElementById('jd').value;

  formData.append('resume', resumeFile);
  formData.append('jd', jdText);

  const response = await fetch('http://127.0.0.1:5000/upload', {
    method: 'POST',
    body: formData
  });

  const result = await response.json();
  document.getElementById('result').innerText = 
    `Match Score: ${result.match_score}%\nCandidate Name: ${result.resume_data.name}`;
});
