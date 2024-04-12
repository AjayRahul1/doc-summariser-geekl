document.addEventListener('DOMContentLoaded', function () {
  var textarea = document.getElementById('input_for_summarise');
  textarea.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
  });

  // Trigger input event initially to adjust the height based on initial content
  textarea.dispatchEvent(new Event('input'));
});

// Function to calculate metrics and update the metrics div
function metricsOfInputDocument() {
  const documentInputDiv = document.getElementById('input_for_summarise');
  const documentText = documentInputDiv.value;
  const wordCount = documentText.split(/\s+/).filter(word => word !== '').length;
  const digitCount = (documentText.match(/[0-9]/g) || []).length;
  const letterCount = (documentText.match(/[A-Za-z]/g) || []).length;
  document.getElementById('input_essay_metrics').innerHTML = `${wordCount} Words | ${letterCount} Letters | ${digitCount} Digits`;
}

// Updating the input document metrics when the page is loaded.
window.addEventListener('load', metricsOfInputDocument);

// Updating the input document metrics when the textarea input is changed
document.getElementById('input_for_summarise').addEventListener('input', metricsOfInputDocument);