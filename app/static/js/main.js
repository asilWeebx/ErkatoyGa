let media = document.querySelector(".media_button");
items = document.querySelectorAll(".block_item");

function filter() {
  media.addEventListener("click", (event) => {
    const targetId = event.target.dataset.id;
    console.log(targetId);
    switch (targetId) {
      case "all":
        items.forEach((items) => {
          if (items.classList.contains("all")) {
            items.style.display = "block";
          } else {
            items.style.display = "none";
          }
        });
        break;

      case "boy":
        items.forEach((items) => {
          if (items.classList.contains("boy")) {
            items.style.display = "block";
          } else {
            items.style.display = "none";
          }
        });
        break;
      case "gril":
        items.forEach((items) => {
          if (items.classList.contains("gril")) {
            items.style.display = "block";
          } else {
            items.style.display = "none";
          }
        });
        break;
    }
  });
}

filter();

let icon = document.querySelector('ion-icon');
icon.onclick = function(){
  icon.classList.toggle('active');
}