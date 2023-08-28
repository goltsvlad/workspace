var tg = window.Telegram.WebApp;

tg.expand();
tg.MainButton.text = 'Замовити';
tg.MainButton.color = '#008000';



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

Telegram.WebApp.onEvent('backButtonClicked', function() {
  var cartPopup = document.getElementById('cart-popup');
  var descriptionPopup = document.getElementById('description-popup');

  if (cartPopup.classList.contains('show')) {
    closeCartPopup();
  } else if (descriptionPopup.style.display === 'block') {
    closeDescriptionPopup();
  }
}); 


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
      toggleDescriptionPopup(product.id);
    });

    productList.appendChild(productElement);
  });

  if (cart.length > 0) {
    tg.MainButton.show();
  } else {
    tg.MainButton.hide();
  }
}

function toggleDescriptionPopup(productId) {
  
  var descriptionPopup = document.getElementById('description-popup');
  // var productListContainer = document.getElementById('product-list');
  var descriptionPopupContent = document.querySelector('.description-popup-content');
  var product = products.find(function(p) {
    return p.id === productId;
  });

  if (product) {
    descriptionPopupContent.innerHTML = `
      <div class="product-image-container">
        <img class="product-image" src="${product.image}" alt="${product.name}">
      </div>
      <div class="product-name">${product.name}</div>
      <div class="product-description">${product.description}</div>
      <div class="close-description-button" onclick="closeDescriptionPopup()">X</div>
    `;
    
    //productListContainer.style.display = 'none'; // Скрываем список товаров
    descriptionPopup.style.display = 'block'; // Показываем описание товара
    descriptionPopup.classList.add('animate-slide-up');
    //productList.style.display = 'none'; // Скрываем список товаров после завершения анимации
    // Добавляем обработчик события animationend
    descriptionPopup.addEventListener('animationend', function() {
      // Этот код выполнится после завершения анимации slide-up
      productList.style.display = 'none'; // Скрываем список товаров
      descriptionPopup.removeEventListener('animationend', arguments.callee); // Удаляем обработчик, чтобы избежать повторного выполнения
    });
    tg.BackButton.show();
    tg.MainButton.hide();
  }
}

//var logOutput = document.getElementById('log-output');
// Перехватываем сообщения из консоли и выводим их в logOutput
//var oldConsoleLog = console.log;
//console.log = function(message) {
  //oldConsoleLog.apply(console, arguments); // Первоначальный вывод в консоль
  //logOutput.innerHTML += message + '<br>'; // Добавляем в logOutput
//};

function closeDescriptionPopup() {
  var descriptionPopup = document.getElementById('description-popup');
  //var productListContainer = document.getElementById('product-list');
  productList.style.display = 'flex';
  descriptionPopup.style.display = 'none';
  descriptionPopup.classList.remove('animate-slide-up');
  tg.BackButton.hide();
  if (cart.length > 0) {
    tg.MainButton.show();
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
  

loadProducts();
