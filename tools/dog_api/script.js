const gallery = document.getElementById("dogGallery");
const refreshBtn = document.getElementById("refreshBtn");
const searchBtn = document.getElementById("searchBtn");
const breedInput = document.getElementById("breedInput");

// Fetch 5 random dogs
async function fetchRandomDogs() {
  gallery.innerHTML = "Loading...";
  const res = await fetch("https://dog.ceo/api/breeds/image/random/5");
  const data = await res.json();
  displayImages(data.message);
}

// Fetch 5 dogs of specific breed
async function fetchBreedDogs(breed) {
  gallery.innerHTML = "Loading...";
  try {
    const res = await fetch(`https://dog.ceo/api/breed/${breed}/images/random/5`);
    const data = await res.json();
    if (data.status !== "success") throw new Error("Invalid breed");
    displayImages(data.message);
  } catch (err) {
    gallery.innerHTML = `<p style="color: red;">❌ Breed not found. Try something like "retriever/golden".</p>`;
  }
}

// Display images in the gallery
function displayImages(images) {
  gallery.innerHTML = "";
  images.forEach(url => {
    const img = document.createElement("img");
    img.src = url;
    gallery.appendChild(img);
  });
}

// Event listeners
refreshBtn.addEventListener("click", fetchRandomDogs);
searchBtn.addEventListener("click", () => {
  const breed = breedInput.value.trim().toLowerCase();
  if (breed) fetchBreedDogs(breed);
});

// Load initial random dogs
fetchRandomDogs();
