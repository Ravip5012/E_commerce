document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const suggestionsList = document.getElementById("suggestions-list");

  searchInput.addEventListener("keyup", function () {
    const query = searchInput.value.trim();
    if (query.length === 0) {
      suggestionsList.innerHTML = "";
      return;
    }

    fetch(`/search-suggestions/?q=${query}`)
      .then(response => response.json())
      .then(data => {
        suggestionsList.innerHTML = "";
        data.suggestions.forEach(item => {
          const li = document.createElement("li");
          li.className = "list-group-item list-group-item-action";
          li.textContent = item;

          li.addEventListener("click", function () {
            searchInput.value = item;
            suggestionsList.innerHTML = "";
          });

          suggestionsList.appendChild(li);
        });
      });
  });
});
