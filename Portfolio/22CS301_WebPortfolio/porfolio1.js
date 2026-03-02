// Dark Mode Toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

// Quote Generator
const quotes = [
    "The best way to predict the future is to create it.",
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "Programming isn't about what you know; it's about what you can figure out."
];

function generateQuote() {
    const quote = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById('quote').textContent = quote;
}

// Form Validation
function validateForm(event) {
    event.preventDefault();
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (name && email && message) {
        alert('Form submitted successfully!');
        event.target.reset();
    } else {
        alert('Please fill in all fields.');
    }
}