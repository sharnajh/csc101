// Shots
const shotInput = document.getElementById("shot-input");
const shotBtns = document.querySelectorAll(".shots");
for (const button of shotBtns) {
  button.addEventListener("click", () => {
    shotInput.value = button.value;
  });
}

// Sizes
const typeInput = document.getElementById("type-input");
const sizeInput = document.getElementById("size-input");
const sizeBtns = document.querySelectorAll(".size");
for (const button of sizeBtns) {
  button.addEventListener("click", () => {
    sizeInput.value = button.value;
    sizeInput.disabled = false;
    if (typeInput.value === "espresso") {
      typeInput.value = "";
    }
  });
}

// Types
const typeBtns = document.querySelectorAll(".type");
for (const button of typeBtns) {
  button.addEventListener("click", () => {
    typeInput.value = button.value;
    sizeInput.disabled = false;
    if (button.value === "espresso") {
      sizeInput.value = "";
      sizeInput.disabled = true;
    }
  });
}

// Calculate Function
const totalBtn = document.getElementById("total-btn");
const priceInput = document.getElementById("price-input");
const calcPrice = () => {
  // Set up all values necessary to calculate price
  const taxRate = 0.88,
    drink = typeInput.value.toLowerCase(),
    shots = shotInput.value,
    ounce =
      // ES6 Shorthand for if-else statements
      sizeInput.value == "S"
        ? 8
        : sizeInput.value == "T"
        ? 12
        : sizeInput.value == "G"
        ? 16
        : 0;
  let price;

  // Calculate by drink type and size
  // Using a switch function instead of if/else because
  // it is faster.
  switch (drink) {
    case "espresso": {
      price = 1.4;
      break;
    }
    case "latte":
    case "cappuccino": {
      switch (ounce) {
        case 8: {
          price = 1.95;
          break;
        }
        case 12: {
          price = 2.35;
          break;
        }
        case 16: {
          price = 2.75;
          break;
        }
      }
      break;
    }
    case "americano": {
      price = 1.2 + 0.3 * (ounce / 8);
      break;
    }
  }
  // Calculate shots
  price += (shots - 1) * 0.5;
  // Calculate tax
  price += price * taxRate;
  // Display price
  priceInput.value = price.toFixed(2);
};

totalBtn.addEventListener("click", () => {
  // Check if all input fields have been entered
  if (typeInput.value == "espresso" && shotInput.value !== "") {
    calcPrice();
  }
  if (typeInput.value == "" || sizeInput.value == "" || shotInput.value == "") {
    return;
  }
  calcPrice();
});

// Clear function
const clearBtn = document.getElementById("clear");
const clear = () => {
  typeInput.value = "";
  shotInput.value = "";
  sizeInput.value = "";
  priceInput.value = "";
};
clearBtn.addEventListener("click", () => {
  clear();
});
