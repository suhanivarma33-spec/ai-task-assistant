const form = document.querySelector("#suggestion-form");
const input = document.querySelector("#suggestion-task");
const result = document.querySelector("#suggestion-result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const task = input.value.trim();
  if (!task) return;
  result.textContent = "Making a simple plan…";
  try {
    const response = await fetch("/api/suggestion", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({task})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.suggestion || "Could not make a plan.");
    result.textContent = data.suggestion;
  } catch (error) {
    result.textContent = "Could not reach the app. Please try again.";
  }
});
