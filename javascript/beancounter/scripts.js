// let drink = "latte";
// (ounce = 12), (shots = 2), (taxRate = 0.88), (price = 0);

// if (drink.toLowerCase() == "espresso") {
//   price = 1.4;
// } else if (
//   drink.toLowerCase() == "latte" ||
//   drink.toLowerCase() == "cappuccino"
// ) {
//   if (ounce == 8) {
//     price = 1.95;
//   } else if (ounce == 12) {
//     price = 2.35;
//   } else if (ounce == 16) {
//     price = 2.75;
//   }
// } else if (drink.toLowerCase() == "americano") {
//   price = 1.2 + 0.3 * (ounce / 8);
// }

// price += (shots - 1) * 0.5;
// price += price * taxRate;

// Shots
const shotInput = document.getElementById("shot-input");
const shotBtns = document.querySelectorAll(".shots");
for (const button of shotBtns) {
  button.addEventListener("click", () => {
    shotInput.value = button.value;
  });
}

// Sizes
const sizeInput = document.getElementById("size-input");
const sizeBtns = document.querySelectorAll(".size");
for (const button of sizeBtns) {
  button.addEventListener("click", () => {
    sizeInput.value = button.value;
  });
}

// Types
const typeInput = document.getElementById("type-input");
const typeBtns = document.querySelectorAll(".type");
for (const button of typeBtns) {
  button.addEventListener("click", () => {
    typeInput.value = button.value;
  });
}

// Clear function
const clearBtn = document.getElementById("clear");
const clear = () => {
  typeInput.value = "";
  shotInput.value = "";
  sizeInput.value = "";
};
clearBtn.addEventListener("click", () => {
  clear();
});

