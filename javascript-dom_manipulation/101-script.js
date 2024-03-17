const btnTranslate = document.getElementById('btn_translate');
const languageCode = document.getElementById('language_code');
const hello = document.getElementById('hello');

btnTranslate.addEventListener('click', function() {
  const lang = languageCode.value;
  if (lang) {
    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then(response => response.text())
      .then(data => {
        hello.textContent = data;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});