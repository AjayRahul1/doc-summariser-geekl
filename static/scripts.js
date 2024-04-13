// To adjust the height of text area according to input height.
function ActivateTextareaResizeListener() {
  document.addEventListener('DOMContentLoaded', function () {
    var textarea = document.getElementById('input_for_summarise');
    textarea.addEventListener('input', function () {
      this.style.height = 'auto';
      this.style.height = (this.scrollHeight) + 'px';
    });

    // Trigger input event initially to adjust the height based on initial content
    textarea.dispatchEvent(new Event('input'));
  });
}

// Function to calculate metrics and update the metrics div
function MetricsOfInputDocument() {
  const documentInputDiv = document.getElementById('input_for_summarise');
  const documentText = documentInputDiv.value;
  const wordCount = documentText.split(/\s+/).filter(word => word !== '').length;
  const digitCount = (documentText.match(/[0-9]/g) || []).length;
  const letterCount = (documentText.match(/[A-Za-z]/g) || []).length;
  document.getElementById('input_essay_metrics').innerHTML = `${wordCount} Words | ${letterCount} Letters | ${digitCount} Digits`;
}

function ActivateInputMetricListener(){
  // Updating the input document metrics when the page is loaded.
  window.addEventListener('load', MetricsOfInputDocument);
  // Updating the input document metrics when the textarea input is changed
  document.getElementById('input_for_summarise').addEventListener('input', MetricsOfInputDocument);
}

function MakeLinkActive(event) {
  // Access information about the clicked anchor tag
  var clickedElement = event.target;
  clickedElement.classList.add("active");
}

async function RemoveBackgroundFn() {
  console.log("Removing Background...");
  var fileInput = document.getElementById('removeBgInputImg');
  var file = fileInput.files[0];
  var formData = new FormData();
  formData.append('file', file);
  
  removebgImgDisplayDiv = document.getElementById('removebg-image');
  loadingDiv(removebgImgDisplayDiv, "Removing the background...")
  try{
    const response = await fetch('/remove_bg_process', {
      method: 'POST',
      body: formData
    });
    if (!response.ok) {
      throw new Error('Failed to process image');
    }
    const responseData = await response.json();
    // response looks { "image_path": "the_path_of_the image" }
    const encodedImagePath = encodeURIComponent(responseData.image_path);
    removeBgResponseDiv = `
    <a href="/image_path/${encodedImagePath}" download="Remove_BG">
      <button class="btn btn-outline-primary mx-auto">Download Image</button>
    </a>
    <img class="my-2" src="/image_path/${encodedImagePath}" alt="Image with Removed Background" style="width: 40%;">
    `;
    removebgImgDisplayDiv.innerHTML = removeBgResponseDiv;
    console.log("Removing Background Finished Successfully!");
  } catch (error) {
      console.error('Error:', error);
      removebgImgDisplayDiv.innerHTML = `Failed to remove background for that image. Maybe unsupported type. Try another one :')`
    }
}