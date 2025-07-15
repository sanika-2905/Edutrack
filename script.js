function toggleMode() {
  document.body.classList.toggle("dark-mode");
  const icon = document.getElementById("modeIcon");
  if (document.body.classList.contains("dark-mode")) {
    icon.textContent = "☀️";
  } else {
    icon.textContent = "🌙";
  }
}
