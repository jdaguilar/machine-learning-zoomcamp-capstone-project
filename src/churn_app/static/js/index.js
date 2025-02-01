let currentStep = 0;
showStep(currentStep);

function showStep(n) {
  let steps = document.getElementsByClassName("step");
  steps[n].classList.add("active");
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == steps.length - 1) {
    document.getElementById("nextBtn").innerHTML = "Submit";
    document.getElementById("nextBtn").type = "submit";
    showPreview();
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
    document.getElementById("nextBtn").type = "button";
  }
}

function nextPrev(n) {
  let steps = document.getElementsByClassName("step");
  steps[currentStep].classList.remove("active");
  currentStep = currentStep + n;
  if (currentStep >= steps.length) {
    document.getElementById("churnForm").submit();
    return false;
  }
  showStep(currentStep);
}

function showPreview() {
  let preview = document.getElementById("preview");
  let form = document.getElementById("churnForm");
  let formData = new FormData(form);
  let previewHtml = "";
  for (let [key, value] of formData.entries()) {
    let label = form.querySelector(`label[for=${key}]`).innerText;
    previewHtml += `<p><strong>${label}</strong>: ${value}</p>`;
  }
  preview.innerHTML = previewHtml;
}
