let drink = "latte";
(ounce = 12), (shots = 2), (taxRate = 0.88), (price = 0);

if (drink.toLowerCase() == "espresso") {
  price = 1.4;
} else if (
  drink.toLowerCase() == "latte" ||
  drink.toLowerCase() == "cappuccino"
) {
  if (ounce == 8) {
    price = 1.95;
  } else if (ounce == 12) {
    price = 2.35;
  } else if (ounce == 16) {
    price = 2.75;
  }
} else if (drink.toLowerCase() == "americano") {
  price = 1.2 + 0.3 * (ounce / 8);
}

price += (shots - 1) * 0.5;
price += price * taxRate;

document.getElementById("price").innerHTML = `Price: $${price.toFixed(2)}`;
