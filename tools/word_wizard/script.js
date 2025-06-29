function getDefinition() {
  const word = document.getElementById("wordInput").value.trim().toLowerCase();
  const resultDiv = document.getElementById("result");

  if (word === "") {
    resultDiv.innerHTML = "❗ Please enter a word.";
    return;
  }

  resultDiv.innerHTML = "🔍 Searching...";

  fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`)
    .then((response) => response.json())
    .then((data) => {
      if (Array.isArray(data)) {
        const entry = data[0];
        const phonetics = entry.phonetics[0]?.text || "";
        const audio = entry.phonetics[0]?.audio || "";
        const meaning = entry.meanings[0]?.definitions[0]?.definition || "No definition available.";
        const example = entry.meanings[0]?.definitions[0]?.example || "";

        let output = `<h2>${entry.word}</h2>`;
        if (phonetics) output += `<p><em>Phonetic:</em> ${phonetics}</p>`;
        output += `<p><strong>Definition:</strong> ${meaning}</p>`;
        if (example) output += `<p><em>Example:</em> "${example}"</p>`;
        if (audio) {
          output += `<p><audio controls src="${audio}">Audio not supported</audio></p>`;
        }

        resultDiv.innerHTML = output;
      } else {
        resultDiv.innerHTML = `❌ No definition found for "<strong>${word}</strong>"`;
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      resultDiv.innerHTML = "⚠️ Error fetching definition. Please try again later.";
    });
}
