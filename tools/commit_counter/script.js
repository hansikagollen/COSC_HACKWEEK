let count = 0;
const counterDisplay = document.getElementById('counter');

document.getElementById('increment').addEventListener('click', () => {
  count++;
  updateDisplay();
});

document.getElementById('decrement').addEventListener('click', () => {
  if (count > 0) {
    count--;
    updateDisplay();
  }
});

document.getElementById('reset').addEventListener('click', () => {
  count = 0;
  updateDisplay();
});

function updateDisplay() {
  counterDisplay.textContent = count;
}
