// CSC 101
// Sharna Hossain
// Final | PartB

const tax = 0.085;

let saladOptions = {
  size: "",
  toppings: [],
  dressing: "",
};

// Calculate Subtotals
const getPrice = (type) => {
  switch (type) {
    case "size": {
      return saladOptions.size == "Small"
        ? 3.5
        : saladOptions.size == "Large"
        ? 5.75
        : 0;
    }
    case "toppings": {
      return saladOptions.toppings.length * 0.15;
    }
    case "dressing": {
      return 0.15;
    }
    default:
      return 0;
  }
};

const getTotals = () => {
  let gross = getPrice("toppings") + getPrice("size") + getPrice("dressings");
  return {
    gross,
    net: gross + gross * tax,
  };
};

// Sizes
const sizeBtns = document.querySelectorAll(".size"),
  sizeInput = document.getElementById("display-size"),
  sizeSubtotal = document.getElementById("subtotal-size");
for (const button of sizeBtns) {
  button.addEventListener("click", () => {
    saladOptions.size = button.value == "s" ? "Small" : "Large";
    sizeInput.value = saladOptions.size;
    sizeSubtotal.innerHTML = `$${getPrice("size").toFixed(2)}`;
  });
}

// Toppings
const toppingsBtns = document.querySelectorAll(".toppings"),
  toppingsInput = document.getElementById("display-toppings"),
  toppingsSubtotal = document.getElementById("subtotal-toppings");
for (const button of toppingsBtns) {
  button.addEventListener("click", () => {
    if (!saladOptions.toppings.includes(button.value)) {
      saladOptions.toppings.push(button.value);
    }
    toppingsInput.value = saladOptions.toppings.toString();
    toppingsSubtotal.innerHTML = `$${getPrice("toppings").toFixed(2)}`;
  });
}

// Dressings
const dressingBtns = document.querySelectorAll(".dressings"),
  dressingInput = document.getElementById("display-dressings"),
  dressingsSubtotal = document.getElementById("subtotal-dressings");
for (const button of dressingBtns) {
  button.addEventListener("click", () => {
    saladOptions.dressing = button.value;
    dressingInput.value = saladOptions.dressing;
    dressingsSubtotal.innerHTML = `$${getPrice("dressing").toFixed(2)}`;
  });
}

// Totals
const totalBtn = document.getElementById("calculate-total"),
  subtotalEl = document.getElementById("subtotal"),
  totalEl = document.getElementById("total");
totalBtn.addEventListener("click", () => {
  if (size == "") {
    return;
  }
  const totals = getTotals();
  subtotalEl.value = `$${totals.gross.toFixed(2)}`;
  totalEl.value = `$${totals.net.toFixed(2)}`;
});
