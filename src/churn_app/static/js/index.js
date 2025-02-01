let currentStep = 0;
const steps = document.getElementsByClassName("step");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");
const form = document.getElementById("churnForm");
const previewDiv = document.getElementById("preview");

showStep(currentStep);

function showStep(n) {
  Array.from(steps).forEach(step => step.style.display = "none");
  steps[n].style.display = "block";
  
  prevBtn.style.display = n === 0 ? "none" : "inline";
  
  if (n === steps.length - 2) {
    nextBtn.innerHTML = "Preview";
    nextBtn.style.display = "inline";
    submitBtn.style.display = "none";
  } else if (n === steps.length - 1) {
    nextBtn.style.display = "none";
    submitBtn.style.display = "inline";
  } else {
    nextBtn.innerHTML = "Next";
    nextBtn.style.display = "inline";
    submitBtn.style.display = "none";
  }
}

function nextPrev(n) {
  steps[currentStep].style.display = "none";
  currentStep += n;

  if (currentStep === steps.length - 1) {
    showPreview();
  } else {
    showStep(currentStep);
  }
}

function showPreview() {
  const formData = new FormData(form);
  previewDiv.innerHTML = "";

  formData.forEach((value, key) => {
    const p = document.createElement("p");
    p.textContent = `${key}: ${value}`;
    previewDiv.appendChild(p);
  });

  showStep(currentStep);
}

form.addEventListener("submit", function(event) {
  if (currentStep < steps.length - 1) {
    event.preventDefault();
    nextPrev(1);
  }
});
