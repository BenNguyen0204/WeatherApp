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