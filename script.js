var tg = window.Telegram.WebApp;

tg.expand();
tg.MainButton.text = 'Замовити';
tg.MainButton.color = '#008000';


// Скрытие кнопки MainButton при загрузке страницы
// tg.MainButton.hide();

Telegram.WebApp.onEvent('mainButtonClicked', function() {
  var cartPopup = document.getElementById('cart-popup');

  if (cartPopup.classList.contains('show')) {
    // Всплывающее окно открыто, отправляем данные
    var cartData = cart.map(function(item) {
      return item.name + ' (x' + item.count + ') ' + item.count * item.price + ' рублей';
    }).join('\n');
    
    var total = cart.reduce(function(sum, item) {
      return sum + item.price * item.count;
    }, 0);

    var orderComment = document.getElementById('order-comment').value;
    var commentText = orderComment ? 'Коментар: ' + orderComment + '\n' : ''; // Проверка наличия комментария
    
    var data = 'Ваш заказ:\n' + cartData + '\n' + commentText + 'Итого: ' + total.toString() + ' рублей.';
    tg.sendData(data);
  
  } else {
    // Всплывающее окно закрыто, открываем его
    toggleCartPopup();
  }
});

Telegram.WebApp.onEvent('backButtonClicked', closeCartPopup) 


// Загрузка данных из offers.json
var products = []; // Здесь будут храниться товары

// Функция для загрузки данных из offers.json
function loadProducts() {
  fetch('offers.json')
    .then(response => response.json())
    .then(data => {
      if (data.length === 0) {
        console.warn('No products available.');
        document.getElementById('no-products-message').style.display = 'block';
      } else {
        products = data.map(item => ({
          id: item.id,
          name: item.name,
          description: item.description,
          price: item.price,
          image: item.image,
          count: 0
        }));
        renderProducts();
      }
    })
    .catch(error => console.error('Error loading products:', error));
}

var cart = [];

var productList = document.querySelector('.product-list');

function renderProducts() {
  productList.innerHTML = '';

  products.forEach(function(product) {
    var productElement = document.createElement('div');
    productElement.classList.add('product');

    productElement.innerHTML = `
      <div class="product-image-container">
        <img class="product-image" src="${product.image}" alt="${product.name}">
        ${
          product.count > 0
            ? `<div class="count-badge">${product.count}</div>`
            : ''
        }
      </div>
      <div class="product-name">${product.name}</div>
      <div class="product-price">${product.price} ₴</div>
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

    // Добавь следующий код для добавления обработчика события на картинку товара
    var productImage = productElement.querySelector('.product-image');
    productImage.addEventListener('click', function() {
      toggleCartPopup();
    });

    productList.appendChild(productElement);
  });

  if (cart.length > 0) {
    tg.MainButton.show();
  } else {
    tg.MainButton.hide();
  }
}

function openProductModal(product) {
  var productModal = document.createElement('div');
  productModal.classList.add('product-modal');
  
  var modalContent = document.createElement('div');
  modalContent.classList.add('product-modal-content');
  
  var closeButton = document.createElement('span');
  closeButton.classList.add('close-button');
  closeButton.textContent = '×';
  closeButton.addEventListener('click', closeProductModal);
  
  var modalProductImage = document.createElement('img');
  modalProductImage.classList.add('modal-product-image');
  modalProductImage.src = product.image;
  modalProductImage.alt = product.name;
  
  var modalProductDescription = document.createElement('div');
  modalProductDescription.classList.add('modal-product-description');
  modalProductDescription.textContent = product.description;
  
  modalContent.appendChild(closeButton);
  modalContent.appendChild(modalProductImage);
  modalContent.appendChild(modalProductDescription);
  
  productModal.appendChild(modalContent);
  document.body.appendChild(productModal);
  
  productModal.style.display = 'block';
}

function closeProductModal() {
  var productModal = document.querySelector('.product-modal');
  if (productModal) {
    productModal.style.display = 'none';
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
  var cartPopupContent = document.querySelector('.cart-popup-content');
  cartPopupContent.innerHTML = ''; // Очищаем содержимое перед заполнением

  var cartPopupHeader = document.createElement('div');
  cartPopupHeader.classList.add('cart-popup-header');
  cartPopupHeader.innerHTML = `
    <div class="cart-popup-title">Кошик</div>
    <div class="edit-button" onclick="closeCartPopup()">Ред.</div>
  `;

  cartPopupContent.appendChild(cartPopupHeader);

  cart.forEach(function (item) {
    var itemBlock = document.createElement('div');
    itemBlock.classList.add('cart-item');

    itemBlock.innerHTML = `
      <div class="cart-item-image">
        <img src="${item.image}" alt="${item.name}">
      </div>
      <div class="cart-item-name">${item.name}</div>
      <div class="cart-item-count">${item.count}x</div>
      <div class="cart-item-price">${item.price * item.count}₴</div>
    `;

    cartPopupContent.appendChild(itemBlock);
  });

  // Добавляем блок с комментарием под товарами
  var commentBlock = document.createElement('div');
  commentBlock.classList.add('comment-block');
  commentBlock.innerHTML = `
    <textarea id="order-comment" placeholder="Введите комментарий к заказу"></textarea>
  `;

  cartPopupContent.appendChild(commentBlock);
}



function toggleCartPopup() {
  tg.BackButton.show();
  var cartPopup = document.getElementById('cart-popup');

  updateCartPopup();
  cartPopup.classList.add('show');

  var totalAmount = cart.reduce(function (sum, item) {
    return sum + item.price * item.count;
  }, 0);

  tg.MainButton.setText(`Підтвердити ${totalAmount}₴`);
}

function closeCartPopup() {
  var cartPopup = document.getElementById('cart-popup');
  cartPopup.classList.remove('show');
  tg.MainButton.setText("Замовити");
  tg.BackButton.hide();
}


function toggleDescription () {
  tg.BackButton.show();
}
  

loadProducts();
