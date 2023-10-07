const alertDiv = document.getElementById("alert");
const addedEmpAlert = document.getElementById("added-emp-alert");
const addEmpTxt = document.getElementById("add-emp-txt");
const closeAlertBtn = document.getElementById("close-alert-btn");

if (alertDiv) {
    addEmpTxt.style.display = "none";
    setTimeout(() => {
        alertDiv.style.display = "none";
        addEmpTxt.style.display = "block";
    }, 4000)
}

if (addedEmpAlert) {
    setTimeout(() => {
        addedEmpAlert.remove();
    }, 3000)
}

closeAlertBtn.addEventListener("click", () => {
    addEmpTxt.style.display = "block";
})