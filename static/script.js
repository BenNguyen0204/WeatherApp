const unitToggle = document.getElementById("unit-toggle");
const unitInput = document.getElementById("unit-input");
const weatherForm = document.getElementById("weather-form");

function applyUnit(unit) {
    unitToggle.dataset.unit = unit;
    unitToggle.textContent = unit === "metric" ? "Change to °F" : "Change to °C";
    if (unitInput) unitInput.value = unit;
}

if (unitToggle) {
    const savedUnit = localStorage.getItem("unit");
    if (savedUnit === "metric" || savedUnit === "imperial") {
        applyUnit(savedUnit);
    }

    unitToggle.addEventListener("click", () => {
        const nextUnit = unitToggle.dataset.unit === "metric" ? "imperial" : "metric";
        applyUnit(nextUnit);
        localStorage.setItem("unit", nextUnit);

        const locationField = weatherForm.querySelector('input[name="location"]');
        if (locationField && locationField.value.trim()) {
            weatherForm.submit();
        }
    });
}