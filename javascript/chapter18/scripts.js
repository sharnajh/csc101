// Sharna Hossain
// Chapter 18
// Grocery List

// Instructions:
// Write an HTML program to Display and Add a list of grocery items.
// (use JavaScript and HTML coding in class to assist you) see below.
// Display subtotal and Grand total with tax.

// Tax is 8.65%
const tax = 0.0865;

// Storing all of the dom elements in vars
let groceryList = document.getElementById("grocery-list"),
  addForm = document.getElementById("add-form"),
  nameInput = document.getElementById("name-input"),
  priceInput = document.getElementById("price-input"),
  qtyInput = document.getElementById("qty-input"),
  submitBtn = document.getElementById("submit-btn"),
  subtotalEl = document.getElementById("subtotal"),
  grandtotalEl = document.getElementById("grandtotal");

// Initializing array to store all items
let groceryItems = [];

// Calculate subtotal and grand total and display in HTML
const calcTotals = () => {
  subtotal = groceryItems.reduce(
    (subtotal, item) => (subtotal += item.subtotal),
    0
  );
  subtotalEl.innerHTML = `$${subtotal.toFixed(2)}`;
  grandtotal = subtotal + subtotal * tax;
  grandtotalEl.innerHTML = `$${grandtotal.toFixed(2)}`;
};

// Initializing class to create items
class Item {
  constructor(name, price, qty) {
    this.name = name;
    this.price = parseFloat(price);
    this.qty = parseInt(qty);
    this.subtotal = this.price * this.qty;
    this.init = () => {
      let row = document.createElement("div");
      row.setAttribute("class", "row");
      row.insertAdjacentHTML(
        "afterbegin",
        `
      <span class="name">${this.name}</span>
      <span class="qty">${this.qty}</span>
      <span class="price">$${this.price.toFixed(2)}</span>
      <span class="subtotal">$${this.subtotal.toFixed(2)}</span>
    `
      );

      let rmBtn = document.createElement("span");
      rmBtn.innerHTML = "✖";
      rmBtn.setAttribute("class", "delete");
      rmBtn.addEventListener("click", () => {
        row.remove();
        groceryItems = groceryItems.filter((item) => item !== this);
        calcTotals();
      });
      row.append(rmBtn);

      groceryList.append(row);
      groceryItems.push(this);
    };
    this.init();
    calcTotals();
  }
}

// Creating beginning data
new Item("Almond Milk", 5, 2);
new Item("Bananas", 2.7, 3);
new Item("Nutella", 7, 1);
new Item("Bread", 3.6, 2);
calcTotals();

// Add new item by submitting form
submitBtn.addEventListener("click", () => {
  name = nameInput.value;
  price = priceInput.value;
  qty = qtyInput.value;
  newItem = new Item(name, price, qty);
  // Reset input values
  nameInput.value = "";
  priceInput.value = "";
  qtyInput.value = "";
});
