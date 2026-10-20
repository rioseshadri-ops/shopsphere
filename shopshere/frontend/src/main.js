const button = document.querySelector("#load-products");
const list = document.querySelector("#products");

button.addEventListener("click", async () => {
  list.replaceChildren();
  try {
    const response = await fetch("/api/products");
    if (!response.ok) throw new Error(`Request failed: ${response.status}`);
    const products = await response.json();
    for (const product of products) {
      const item = document.createElement("li");
      item.textContent = `${product.name} — ₹${product.price}`;
      list.appendChild(item);
    }
  } catch (error) {
    const item = document.createElement("li");
    item.textContent = `Could not load products: ${error.message}`;
    list.appendChild(item);
  }
});
