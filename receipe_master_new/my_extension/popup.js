document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('query-form');
  const input = document.getElementById('query-input');
  const output = document.getElementById('response');

  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    const query = input.value.trim();

    if (!query) {
      output.textContent = "Please enter a question.";
      return;
    }

    output.textContent = "Searching..."; // Optional: nice UX

    try {
      const res = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();

      // Log the response for debugging
      console.log("Response Data:", data);

      // Check if the answer exists and is in the correct format
      if (data && data.answer && data.answer.text) {
        // Ensure we're displaying only the text field, not the entire object
        const recipeText = data.answer.text.text || "No recipe found.";
        output.innerHTML = recipeText;  // Using innerHTML to render HTML content (e.g., line breaks, bold text)
      } else {
        output.textContent = "No answer found.";
      }

      // Log the trace of actions if available
      if (data.trace && Array.isArray(data.trace)) {
        const traceOutput = data.trace.join(' -> ');
        console.log("Trace of actions:", traceOutput);
        // Start by adding a title and the chef intro
        let formattedResponse = "<h2>I am your Recipe Master, here is a delicious recipe for you!</h2>";
        // Display the trace in the output or console
        output.textContent += `\nTrace: ${traceOutput}`;
      }

    } catch (err) {
      console.error('Error:', err);
      output.textContent = 'Failed to fetch answer.';
    }
  });
});
