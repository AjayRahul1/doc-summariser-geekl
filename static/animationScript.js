// Border Spin Animation
const borderSpinLoadAnimation = `
  <div class="spinner-border spinner-border-sm" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>`;

// Grow Spin Animation
const growSpinLoadAnimation = `
  <div class="spinner-grow spinner-grow-sm" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>`;

// Disable btn if in enabled state. Else enables.
const toggleButton = (buttonElement) => {
  buttonElement.disabled = !buttonElement.disabled;
}

// TODO: take the response data and fill the HTML template with this data.
async function getSummary() {
  var docToSummarise = document.getElementById("input_for_summarise").value;
  try {
    const response = await fetch('/summarise_document', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ data: docToSummarise })
    });

    const responseData = await response.json();    
  } catch (error) { console.error("Error:", error); }

}

function loadingDiv(divElementToAnimate, titleText) {
  // Loads animation
  divElementToAnimate.innerHTML = `
  <div class="card">
  <div class="card-body">
    <h5 class="card-title">${titleText} ${borderSpinLoadAnimation}</h5>
    <p class="card-subtitle mb-2 text-body-secondary placeholder-glow">
      <span class="placeholder col-4"></span>
      </p>
      <p class="card-text placeholder-glow">
      <span class="placeholder col-7"></span><span class="placeholder col-4"></span>
      <span class="placeholder col-4"></span><span class="placeholder col-6"></span>
      <span class="placeholder col-8"></span>
      ${growSpinLoadAnimation}
    </p>
  </div>
  </div>`;
}

// 
function generateSummary() {
  console.log("Generating Summary...");
  // let summariseButton = document.getElementById("generateSummaryBtn");
  // toggleButton(summariseButton);

  let summarisedOutputDiv = document.getElementById("summarised_output");
  loadingDiv(summarisedOutputDiv, titleText="Summary")
  // toggleButton(summariseButton);
}