var tg = window.Telegram.WebApp;

tg.expand();
tg.MainButton.text = 'Замовити';
tg.MainButton.color = '#76bb40';


// Скрытие кнопки MainButton при загрузке страницы
// tg.MainButton.hide();

//Telegram.WebApp.onEvent('mainButtonClicked', function() {
Telegram.WebApp.onEvent('mainButtonClicked', function() {
  var cartData = cart.map(function(item) {
    return item.name + ' (x' + item.count + ') ' + item.count * item.price + ' рублей';
  }).join('\n');

  var total = cart.reduce(function(sum, item) {
    return sum + item.price * item.count;
  }, 0);

  var data = 'Ваш заказ:\n' + cartData + '\nИтого: ' + total.toString() + ' грн.';
  // tg.sendData(data);
  // tg.showPopup();
});

var products = [
  { id: 1, name: "Товар 1", price: 100, image: "https://picsum.photos/200", count: 0 },
  { id: 2, name: "Товар 2", price: 200, image: "https://picsum.photos/200", count: 0 },
  { id: 3, name: "Товар 3", price: 300, image: "https://picsum.photos/200", count: 0 },
  { id: 4, name: "Товар 4", price: 400, image: "https://picsum.photos/200", count: 0 },
  { id: 5, name: "Товар 5", price: 500, image: "https://picsum.photos/200", count: 0 },
  { id: 6, name: "Товар 6", price: 600, image: "https://picsum.photos/200", count: 0 },
  { id: 7, name: "Товар 7", price: 700, image: "https://picsum.photos/200", count: 0 },
  { id: 8, name: "Товар 8", price: 800, image: "https://picsum.photos/200", count: 0 },
  { id: 9, name: "Товар 9", price: 900, image: "https://picsum.photos/200", count: 0 },
  { id: 10, name: "Товар 10", price: 1000, image: "https://picsum.photos/200", count: 0 },
  { id: 11, name: "Товар 11", price: 1100, image: "https://picsum.photos/200", count: 0 },
  { id: 12, name: "Товар 12", price: 1200, image: "https://picsum.photos/200", count: 0 }
];

var cart = [];

var productList = document.querySelector('.product-list');

function renderProducts() {
  productList.innerHTML = '';

  products.forEach(function(product) {
    var productElement = document.createElement('div');
    productElement.classList.add('product');

    productElement.innerHTML = `
      <div>
        <img class="product-image" src="${product.image}" alt="${product.name}">
        ${
          product.count > 0
            ? `<div class="count-badge">${product.count}</div>`
            : ''
        }
      </div>
      <div class="product-name">${product.name}</div>
      <div class="product-price">${product.price} рублей</div>
      <div class="quantity-buttons">
        ${
          product.count > 0
            ? `
              <button class="quantity-button remove-button" onclick="updateQuantity(${product.id}, -1)">-</button>
              <div class="count-badge">${product.count}</div>
              <button class="quantity-button" onclick="updateQuantity(${product.id}, 1)">+</button>
            `
            : `<button class="add-to-cart-button" onclick="updateQuantity(${product.id}, 1)">В корзину</button>`
        }
      </div>
    `;

    productList.appendChild(productElement);
  });

  if (cart.length > 0) {
    tg.MainButton.show();
    // tg.MainButton.onClick('callback');
  } else {
    tg.MainButton.hide();
  }
}

function updateQuantity(id, amount) {
  var product = products.find(function(p) {
    return p.id === id;
  });

  if (product) {
    product.count += amount;

    if (product.count < 0) {
      product.count = 0;
    }

    if (product.count === 0) {
      var productIndex = cart.indexOf(product);

      if (productIndex !== -1) {
        cart.splice(productIndex, 1);
      }
    } else if (cart.indexOf(product) === -1) {
      cart.push(product);
    }

    renderProducts();
    updateCartPopup();
  }
}

function updateCartPopup() {
  var cartItemsPopup = document.getElementById('cart-items-popup');
  var cartTotalPopup = document.getElementById('cart-total-popup');

  var cartItemsContent = cart
    .map(function (item) {
      return `${item.name} (x${item.count}) - ${item.count * item.price} рублей`;
    })
    .join('<br>');

  var totalAmount = cart.reduce(function (sum, item) {
    return sum + item.price * item.count;
  }, 0);

  cartItemsPopup.innerHTML = cartItemsContent;
  cartTotalPopup.innerHTML = `Итого: ${totalAmount} рублей`;
}

function toggleCartPopup() {
  var cartPopup = document.getElementById('cart-popup');
  var cartButton = document.getElementById('cart-container');

  cartButton.style.display = 'none';

  if (cartPopup.classList.contains('show')) {
    cartPopup.classList.remove('show');
    tg.MainButton.hide();
  } else {
    updateCartPopup();
    cartPopup.classList.add('show');

    if (cart.length > 0) {
      tg.MainButton.show();
    }
  }
}

function closeCartPopup() {
  var cartPopup = document.getElementById('cart-popup');
  cartPopup.classList.remove('show');
  tg.MainButton.hide();

  var cartButton = document.querySelector('.cart-container');

  if (cart.length > 0) {
    cartButton.style.display = 'block';
  } else {
    cartButton.style.display = 'none';
  }
}

renderProducts();
