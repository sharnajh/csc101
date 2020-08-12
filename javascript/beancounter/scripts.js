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

// Calculate Function
const totalBtn = document.getElementById("total-btn");
const priceInput = document.getElementById("price-input");
const calcPrice = () => {
  // Set up all values necessary to calculate price
  const taxRate = 0.88;
  let drink = typeInput.value.toLowerCase();
  let shots = shotInput.value;
  let ounce =
    // ES6 Shorthand for if-else statements
    sizeInput.value == "S"
      ? 8
      : sizeInput.value == "T"
      ? 12
      : sizeInput.value == "G"
      ? 16
      : 0;
  let price;

  // Calculate function with nested if-else statements
  if (drink == "espresso") {
    price = 1.4;
  } else if (drink == "latte" || drink == "cappuccino") {
    if (ounce == 8) {
      price = 1.95;
    } else if (ounce == 12) {
      price = 2.35;
    } else if (ounce == 16) {
      price = 2.75;
    }
  } else if (drink == "americano") {
    price = 1.2 + 0.3 * (ounce / 8);
  }
  price += (shots - 1) * 0.5;
  price += price * taxRate;
  priceInput.value = price.toFixed(2);
};

totalBtn.addEventListener("click", () => {
  // Check if all input fields have been entered
  if (typeInput.value == "" || sizeInput.value == "" || shotInput.value == "") {
    return;
  }
  calcPrice();
});
