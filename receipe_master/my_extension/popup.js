document.getElementById('searchBtn').addEventListener('click', async () => {
    const query = document.getElementById('queryInput').value;
    
    const response = await fetch('http://127.0.0.1:8000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    });
  
    const data = await response.json();
  
    const resultDiv = document.getElementById('result');
    if (data.text && data.url) {
      resultDiv.innerHTML = `<p>${data.text}</p><a href="${data.url}" target="_blank">View Recipe</a>`;
    } else {
      resultDiv.innerHTML = "<p>No recipe found.</p>";
    }
  });
  