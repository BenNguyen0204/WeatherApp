const themeToggle = document.getElementById("theme-toggle");

// Load saved theme
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "light") {
    document.body.classList.add("light");
    themeToggle.textContent = "☾ Dark";
} else {
    themeToggle.textContent = "☀ Light";
}

// Toggle theme
themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {
        themeToggle.textContent = "☾ Dark";
        localStorage.setItem("theme", "light");
    } else {
        themeToggle.textContent = "☀ Light";
        localStorage.setItem("theme", "dark");
    }
});

// --- Unit toggle (Celsius / Fahrenheit) ---
const unitToggle = document.getElementById("unit-toggle");
const unitInput = document.getElementById("unit-input");
const weatherForm = document.getElementById("weather-form");

function applyUnit(unit) {
    unitToggle.dataset.unit = unit;
    unitToggle.textContent = unit === "metric" ? "Change to Imperial" : "Change to Metric";
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