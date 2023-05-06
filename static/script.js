async function process() {
  const inputString = document.getElementById('input_string').value;
  const prefix = document.getElementById('prefix').value;
  const ar = document.getElementById('ar').value;

  const resultsDiv = document.getElementById('results');

  if (inputString.length === 0) {
    alert('Please enter a string to process.');
    return;
  }

  if (resultsDiv) {
    resultsDiv.remove();
  }

  const response = await fetch('/process', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({input_string: inputString, prefix: prefix, ar: ar}),
  });

  const result = await response.text();

  console.log(result);

  const resultTitle = document.createElement('h2');
  resultTitle.innerText = 'Result:';
  resultsDiv.appendChild(resultTitle);

  const resultTextArea = document.createElement('textarea');
  resultTextArea.value = result;
  resultTextArea.rows = 20;
  resultTextArea.cols = 100;
  resultsDiv.appendChild(resultTextArea);

  console.log(resultsDiv);
}

function copyResult() {
  const resultsDiv = document.getElementById('resultsDiv');
  if (!resultsDiv) {
    alert('No results to copy.');
    return;
  }
  const resultTextArea = document.createElement('textarea');
  resultTextArea.value = document.getElementById('resultsDiv').innerText;
  document.body.appendChild(resultTextArea);
  resultTextArea.select();
  document.execCommand('copy');
  document.body.removeChild(resultTextArea);
}

function clearInput() {
  document.getElementById('input_string').value = '';
}
