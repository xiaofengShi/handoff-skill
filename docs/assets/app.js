document.querySelectorAll('[data-mode]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-mode]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    document.querySelectorAll('.sample').forEach(sample => { sample.hidden = sample.id !== `sample-${button.dataset.mode}`; });
  });
});
document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const text = document.getElementById(button.dataset.copy).textContent;
    const original = button.textContent;
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = document.body.dataset.copied;
      document.getElementById('copy-status').textContent = document.body.dataset.copied;
      window.setTimeout(() => { button.textContent = original; }, 1800);
    } catch (error) {
      document.getElementById('copy-status').textContent = document.body.dataset.copyFailed;
    }
  });
});
