<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="MobileOptimized" content="176" />
  <meta name="HandheldFriendly" content="True" />
  <meta name="robots" content="noindex,nofollow" />
  
  <!-- light, regular, medium, semibold, bold  шрифт ROBOTO -->
  <link rel="preconnect" href="https://fonts.googleapis.com"> 
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
  
  <!-- шрифт Dela Gothic-->
  <link href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&display=swap" rel="stylesheet">
  
  <!-- Подключение Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <script src="https://telegram.org/js/telegram-web-app.js?1"></script>
  <script>
    function setThemeClass() {
      document.documentElement.className = Telegram.WebApp.colorScheme;
    }
    Telegram.WebApp.onEvent('themeChanged', setThemeClass);
    setThemeClass();
  </script>
  <style>
    body {
      font-family: "Roboto", serif;
      font-weight: 500; /* regular */
      font-style: normal;
      font-size: 14px;
      background-color: var(--tg-theme-bg-color);
      color: var(--tg-theme-text-color);
      margin: 0;
      padding: 0;
      color-scheme: var(--tg-color-scheme);
    }

    /* Анимация плавной смены видимости */
    
    @keyframes animate-out-left {
      0% {
        transform: translateX(0);
        opacity: 1;
      }
      100% {
        transform: translateX(-100%);
        opacity: 0;
      }
    }

    @keyframes animate-out-right {
      0% {
        transform: translateX(0);
        opacity: 1;
      }
      100% {
        transform: translateX(100%);
        opacity: 0;
      }
    }
    
    .animate-out-right {
        animation: animate-out-right 0.5s ease forwards;
    }
    
    .animate-out-left {
        animation: animate-out-left 0.5s ease forwards;
    }
    
    @keyframes animate-on-left {
      0% {
        transform: translateX(-100%);
        opacity: 0;
      }
      100% {
        transform: translateX(0);
        opacity: 1;
      }
    }

    .animate-on-left {
      animation: animate-on-left 0.3s ease forwards;
    }
    
    /* Анимация плавного появления справа */
    @keyframes animate-on-right {
      0% {
        transform: translateX(100%);
        opacity: 0;
      }
      100% {
        transform: translateX(0);
        opacity: 1;
      }
    }

    .animate-on-right {
      animation: animate-on-right 0.3s ease forwards;
    }

    .product-list { /* главный контейнер товара */
        display: flex;
        flex-wrap: wrap; /* Это свойство позволяет элементам переноситься на следующую строку */
        margin-top: 10px; /* Отступ для учета navbar */
        margin: 10px; /* Отступ по краям */
    }

    .product { /* контейнер товара в главном контейнере состоящий из product-image, product-name, product-price, quantity-buttons. */
        width: calc(33.33% - 10px);
        margin: 5px;
        text-align: center;
        position: relative;
    }

    .product-image { /* картинка товара */
        width: 100%;
        border-radius: 10px;
    }

    .product-name { /* название товара */
        margin-top: 5px;
    }

    .product-price { /* цена товара */
        color: #31B545;
        margin-top: 5px;
    }

    .count-badge { /* значок количества на картинке */
        position: absolute;
        color: var(--tg-theme-text-color);
        top: 10px;
        right: 10px;
        background-color: #F8A917;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 65%;
    }

    .quantity-buttons { /* контейнер с кнопками товара */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
}

    .quantity-button { /* кнопки + и - */
        background-color: #F8A917;
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 14px;
        color: var(--tg-theme-text-color);
        border: none;
        padding: 10px;
        cursor: pointer;
        width: 50%;
        margin: 0 5px;
        border-radius: 10px;
        text-align: center;
    }

    .remove-button { /* доп. стиль для кнопки - */
        background-color: #E64D45;
    }

    .add-to-cart-button { /* кнопка В КОРЗИНУ */
        background-color: #F8A917;
        color: var(--tg-theme-text-color);
        border: none;
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 12px;
        padding: 10px;
        cursor: pointer;
        width: 100%;
        margin: 0 auto;
        display: block;
        border-radius: 10px;
        text-align: center;
    }

    /* Стили для всплывающего окна description */
    .description-popup {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%; /* Здесь используется 100vh для высоты экрана */
        /*overflow: hidden;*/
        transition: transform 0.3s; /* Мы используем transform для анимации появления/скрытия */
        transform: translateY(100%);
    }
    
    .description-popup.show { /* показ окна description */
        transform: translateY(0); /* Показать всплывающее окно */
    }


    .description-popup-content {
        align-items: center; /*Центрируем контент по вертикали */
        margin-top: 10px; /* Отступ для учета navbar */
        margin: 10px; /* Отступ по краям */
        padding: 20px;
        text-align: center;
        /*overflow: hidden;*/
        background-color: var(--tg-theme-bg-color);
        
    }

    .product-image-container {
        position: relative;
    }
    
    .product-description {
        background-color: var(--tg-theme-secondary-bg-color);
        font-size: 14px;
        color: var(--tg-theme-text-color); /* Цвет текста */
        line-height: 1.5; /* Межстрочное расстояние */
        margin-top: 10px;
        padding: 10px;
        margin: 10px;
        width: calc(100% - 10px);
        border-radius: 10px;
    }
    
    .product-description p { 
        margin: 0 0 10px; /* Отступ между параграфами */
    }

    .prev-product-button,
    .next-product-button {
        position: absolute;
        top: 40%; /* Разместите по вертикали в центре контейнера  тогда top: 50%*/
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 18px;
        cursor: pointer;
        background-color: var(--tg-theme-secondary-bg-color);
        border-radius: 30%;
        width: 40px;
        height: 40px;
        opacity: 50%;
        display: flex;
        position: fixed;
        align-items: center;
        justify-content: center;
        text-align: center;
        vertical-align: middle;
    }

    .prev-product-button {
        left: 10px; /* Разместите кнопку "назад" слева от картинки */
    }
    .next-product-button {
        right: 10px; /* Разместите кнопку "вперед" справа от картинки */
    } 
    
    .prev-product-button i,
    .next-product-button i {
        line-height: 40px;
        margin-top: 
    } /* Разместите кнопки назад и вперед по центру контейнера кнопки */


    .close-description-button {
        position: absolute;
        top: 10px;
        right: 10px;
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 16px;
        cursor: pointer;
        background-color: var(--tg-theme-secondary-bg-color);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        opacity: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .close-description-button i {
        line-height: 40px;
    } /* Разместите кнопки по центру контейнера кнопки */
    
    .cart-popup { /* окно корзины */
        position: fixed;
        background-color: var(--tg-theme-secondary-bg-color);
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%; /* Здесь используется 100vh для высоты экрана */
        transition: transform 0.3s; /* Мы используем transform для анимации появления/скрытия */
        transform: translateY(100%); /* Начальное положение за пределами экрана */
    }

    .cart-popup.show { /* показ окна корзины */
        transform: translateY(0); /* Показать всплывающее окно */
    }
    
    .cart-popup-header { /* контейнер Заголовка окна корзины */
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: var(--tg-theme-bg-color);
        /*overflow-y: auto;*/
    }

    .cart-popup-title { /* текст заголовка окна корзины */
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 16px;
        color: var(--tg-theme-text-color);
        
    }

    .edit-button { /* кликабельное слово в заголовке окна корзины */
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 16px;
        color: #31B545;
        cursor: pointer;
    }

    .cart-popup-content {
        display: flex;
        background-color: var(--tg-theme-secondary-bg-color);
        flex-direction: column;
        align-items: stretch;
        overflow-y: auto;
    }
        
        

    .cart-item {
        display: flex;
        color: var(--tg-theme-text-color);
        background-color: var(--tg-theme-bg-color);
        align-items: center;
        padding: 10px 20px;
    }

    .cart-item-image {
        width: 40px;
        height: 40px;
        margin-right: 10px;
        border-radius: 10px; /* Закруглённые углы */
        overflow: hidden; /* Обрезаем изображение по границам */
    }

    .cart-item-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .cart-item-name {
        color: var(--tg-theme-text-color);
        
    }

    .cart-item-count {
        color: #F8A917; /* Зелёный цвет для количества */
        margin-left: 10px;
    }

    .cart-item-price {
        color: var(--tg-theme-text-color);
        margin-left: auto; /* Выравнивание цены по правому краю */
    }

    .comment-block {
        background-color: var(--tg-theme-secondary-bg-color);
        padding: 10px 0;
    }

    .comment-input {
        background-color: var(--tg-theme-bg-color);
        width: 100%;
        padding: 10px 20px;
        border: none;
        outline: none;
        font-family: "Roboto", serif;
        font-weight: 400; /* regular */
        font-style: normal;
        font-size: 14px;
        resize: none;
        overflow: hidden; /* Предотвращаем появление полос прокрутки */
        box-sizing: border-box;
        border-radius: 0;
    }

    .comment-helper-text {
        color: var(--tg-theme-hint-color); /* Серый цвет текста */
        font-family: "Roboto", serif;
        font-weight: 500; /* regular */
        font-style: normal;
        font-size: 14px;
        margin-top: 5px; /* Отступ от поля ввода */
        margin-left: 20px;
    }
        
  </style>
</head>
<body>
  <div id="product-list" class='product-list'></div>
  <p id="no-products-message" style="display: none;">Товари відсутні.</p>
  <div id="cart-popup" class="cart-popup">
    <div class="cart-popup-content">
    </div>
  </div>
  <div id="description-popup" class="description-popup">
    <div class="description-popup-content">
    </div>
  </div>
  <!-- <button class="add-to-cart-button" onclick="toggleCartPopup()">В корзину</button>  -->
  <script>
    var tg = window.Telegram.WebApp;
    
    
    tg.disableVerticalSwipes() //отключить вертикальные свайпы webapp
    tg.expand(); // растянуть webapp
    tg.MainButton.text = 'Замовити';
    tg.MainButton.color = '#31B545';
    
    Telegram.WebApp.onEvent('mainButtonClicked', function() {
      var cartPopup = document.getElementById('cart-popup');

      if (cartPopup.classList.contains('show')) {
        // Всплывающее окно открыто, отправляем данные
        var cartData = cart.map(function(item) {
          return item.name + ' (x' + item.count + ') ' + item.count * item.price + '₴';
        }).join('\n');
    
        var total = cart.reduce(function(sum, item) {
          return sum + item.price * item.count;
        }, 0);

        var orderComment = document.querySelector('.comment-input').value;
        var commentText = orderComment ? 'Коментар: ' + orderComment + '\n' : ''; // Проверка наличия комментария
    
        var data = 'Замовлення:\n' + cartData + '\n' + commentText + 'Сума: ' + total.toString() + '₴.';
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
      } else if (descriptionPopup.classList.contains('show')) {
        closeDescriptionPopup();
      }
    }); 
    
    // Загрузка данных из offers.json
    var products = []; // Здесь будут храниться товары
    var currentOpenProductIndex = -1;

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
          <div class="product-price">${product.price}₴</div>
          <div class="quantity-buttons">
            ${
              product.count > 0
                ? `
                  <button class="quantity-button remove-button" onclick="updateQuantity(${product.id}, -1)">-</button>
                  <div class="count-badge">${product.count}</div>
                  <button class="quantity-button" onclick="updateQuantity(${product.id}, 1)">+</button>
                `
                : `<button class="add-to-cart-button" onclick="updateQuantity(${product.id}, 1)">До кошику</button>`
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

    var descriptionPopup = document.getElementById('description-popup');
    var descriptionPopupContent = document.querySelector('.description-popup-content');
    
    function toggleDescriptionPopup(productId, animationDirection) {
      console.log('Animation Direction:', animationDirection); // Вывод значения animationDirection
      var product = products.find(function(p) {
        return p.id === productId;
      });

      if (product) {
        descriptionPopupContent.innerHTML = `
          <div class="product-image-container">
            <img class="product-image" src="${product.image}" alt="${product.name}">
            
            
            <!-- иконки на кнопках  -->
            <div class="prev-product-button" onclick="showProduct('right')">
              <i class="fas fa-chevron-left"></i>
            </div>
            <div class="next-product-button" onclick="showProduct('left')">
              <i class="fas fa-chevron-right"></i>
            </div>
          
          </div>
          <div class="product-name">${product.name}</div>
          <div class="product-description">${product.description}</div>
          
          
          <!-- задан стиль для кнопки закрыть.  -->
          <div class="close-description-button" onclick="closeDescriptionPopup()">
            <i class="fas fa-times"></i> <!-- Иконка для закрытия -->
          </div>
        `;
        currentOpenProductIndex = products.findIndex(function(p) {
          return p.id === productId;
        });

        var prevButton = document.querySelector('.prev-product-button');
        var nextButton = document.querySelector('.next-product-button');

        if (prevButton && nextButton) {
          prevButton.style.display = currentOpenProductIndex > 0 ? 'block' : 'none';
          nextButton.style.display = currentOpenProductIndex < products.length - 1 ? 'block' : 'none';
        }
        
        descriptionPopup.classList.add('show');
        tg.BackButton.show();
        tg.MainButton.hide();
        
        
        setTimeout(function() {
          productList.style.display = 'none';
          descriptionPopup.style.position = 'relative'; // Показываем описание товара
          descriptionPopupContent.classList.remove('animate-out-left', 'animate-out-right');
          
          // Добавляем анимацию в зависимости от направления
          if (animationDirection === 'left') {
          descriptionPopupContent.classList.add('animate-on-right');
          } else if (animationDirection === 'right') {
          descriptionPopupContent.classList.add('animate-on-left');
          }
          
          console.log('Adding animation class:', animationDirection); // Вывод значения animationDirection после добавления класса
        }, 300); // Задержка в миллисекундах
      }
    }

    

    function closeDescriptionPopup() {
  
      descriptionPopup.classList.remove('show');
      descriptionPopup.style.position = 'fixed';
      productList.style.display = 'flex';
      currentOpenProductIndex = -1;
  
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
      }
    }

    function showProduct(direction) {
      if (currentOpenProductIndex !== -1) {
        descriptionPopupContent.classList.remove('animate-on-left', 'animate-on-right');
        var animationClass = direction === 'left' ? 'animate-out-left' : 'animate-out-right';
        descriptionPopupContent.classList.add(animationClass);

        if (direction === 'left' && currentOpenProductIndex < products.length - 1) {
          currentOpenProductIndex += 1;
        } else if (direction === 'right' && currentOpenProductIndex > 0) {
          currentOpenProductIndex -= 1;
        }

        toggleDescriptionPopup(products[currentOpenProductIndex].id, direction);
      }
    }

    
    //СВАЙПЫ
    var startX;
    var startY;
    
    
    descriptionPopupContent.addEventListener('touchstart', function(event) {
      startX = event.touches[0].clientX;
      startY = event.touches[0].clientY;
    });
    
    var minSwipeDistance = 80; // Минимальное расстояние свайпа в пикселях

    descriptionPopupContent.addEventListener('touchmove', function(event) {
      var deltaX = event.touches[0].clientX - startX;
      var deltaY = event.touches[0].clientY - startY;

      if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance) {
        event.preventDefault(); // Предотвращаем прокрутку страницы в случае горизонтального свайпа

        if (deltaX > 0 && currentOpenProductIndex > 0) {
          // Свайп вправо, если не первый продукт
          showProduct('right');
        } else if (deltaX < 0 && currentOpenProductIndex < products.length - 1) {
          // Свайп влево, если не последний продукт
          showProduct('left');
        }
      }
    });
    
    
    

    
    var cartPopup = document.getElementById('cart-popup');
    var body = document.body;
    
    function toggleCartPopup() {
      
      Telegram.WebApp.setHeaderColor('bg_color');
      Telegram.WebApp.setBackgroundColor('secondary_bg_color');
      
      tg.BackButton.show();
      updateCartPopup();
      cartPopup.classList.add('show');
      
      
      setTimeout(function() {
        body.style.backgroundColor = 'var(--tg-theme-secondary-bg-color)';
        productList.style.display = 'none';
        cartPopup.style.position = 'relative';
        scrollToTop();
        
      }, 300);

      var totalAmount = cart.reduce(function (sum, item) {
        return sum + item.price * item.count;
      }, 0);
      tg.MainButton.setText(`Підтвердити ${totalAmount}₴`);
    }

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' }); // Плавно переместить фокус вверх
    }
    
      
    function closeCartPopup() {

      //Telegram.WebApp.setHeaderColor('bg_color');
      body.style.backgroundColor = 'var(--tg-theme-bg-color)';
      Telegram.WebApp.setBackgroundColor('bg_color');
      cartPopup.classList.remove('show');
      cartPopup.style.position = 'fixed';
      productList.style.display = 'flex';
      tg.MainButton.setText("Замовити");
      tg.BackButton.hide();
    }
    
    function updateCartPopup() {
      
      var cartPopupContent = document.querySelector('.cart-popup-content');
      cartPopupContent.innerHTML = ''; // Очищаем содержимое перед заполнением

      var cartPopupHeader = document.createElement('div');
      cartPopupHeader.classList.add('cart-popup-header');
      cartPopupHeader.innerHTML = `
        <div class="cart-popup-title">Ваше замовлення</div>
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
        addSwipeToDeleteHandler(itemBlock, item); //Передаем блок и обьект на обрабутку свайпов.
      });

      // Добавляем блок с комментарием под товарами
      var commentBlock = document.createElement('div');
      commentBlock.classList.add('comment-block');
      commentBlock.innerHTML = `
        <textarea class="comment-input" rows="1" placeholder="Коментар..."></textarea>
        <div class="comment-helper-text">Додайте коментар за потреби.</div> <!-- Добавляем элемент .comment-helper-text -->
      `;

      cartPopupContent.appendChild(commentBlock);
      
      var commentInput = document.querySelector('.comment-input');
      
      // Обработчик события для скрытия клавиатуры
      document.addEventListener('click', function(event) {
        if (!event.target.closest('.comment-input')) {
          commentInput.blur(); // Убирает фокус с текстового поля, скрывая клавиатуру
        }
      });
      
      // Предотвращение распространения события click внутри comment-input
      commentInput.addEventListener('click', function(event) {
        event.stopPropagation();
      });

      commentInput.addEventListener('input', function () {
        this.style.height = 'auto'; // Сначала сбросим высоту
        this.style.height = (this.scrollHeight) + 'px'; // Установим высоту равной высоте контента
      });
      
      commentInput.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
          const lines = this.value.split('\n');
          const currentLine = lines[lines.length - 1];
          if (currentLine.trim() === '') {
            e.preventDefault(); // Предотвращаем переход на новую строку, если текущая строка пуста
          }
        }
      });
    };

    // Обработчик касания для элемента товара в корзине
    function addSwipeToDeleteHandler(item, product) {
      var itemBlock = item;
      var startX;
      var itemWidth = item.offsetWidth;
      var isSwiping = false;

      item.addEventListener('touchstart', function (event) {
        startX = event.touches[0].clientX;
        isSwiping = false;
      });

      item.addEventListener('touchmove', function (event) {
        var deltaX = event.touches[0].clientX - startX;
    
        // Если перемещение происходит влево и касание началось у правого края блока 
        if (deltaX < 0 && startX >= itemWidth * 0.8) {
          isSwiping = true;
      
          // Отменяем стандартное поведение браузера
          event.preventDefault();
      
          // Перемещаем элемент влево
          item.style.transform = `translateX(${deltaX}px)`;
          item.style.borderRadius = '10px';
        }
      });

      item.addEventListener('touchend', function () {
        if (isSwiping) {
          // Если пользователь завершил свайп (перетаскивание)

          // Проверяем, насколько далеко сдвинулся элемент
          var currentX = parseInt(getComputedStyle(item).transform.split(',')[4]);

          if (Math.abs(currentX) >= itemWidth * 0.9) {
            // Если элемент сдвинулся на 90% от своей ширины или больше,
            // выполняем удаление
            removeItemFromCartById(product.id, itemBlock);
          } else {
            // В противном случае возвращаем элемент на место
            item.style.transition = 'transform 0.3s'; // Добавляем анимацию только для возврата
            item.style.transform = 'translateX(0)';
            setTimeout(function() {
              item.style.transform = '';
              item.style.transition = ''; // Сбрасываем анимацию
              item.style.borderRadius = '';
            }, 300);
          }
        }
      });
    }

    // Функция для удаления товара из корзины по его идентификатору
    function removeItemFromCartById(productId, itemBlock) {
      var currentTotalAmount = calculateTotalAmount();
      var index = cart.findIndex(function (item) {
        return item.id === productId;
      });

      if (index !== -1) {
        var removedItem = cart[index];
        cart.splice(index, 1);
        updateQuantity(productId, -removedItem.count);
        var newTotalAmount = calculateTotalAmount();

        // Задаем анимацию плавного исчезновения элемента
        itemBlock.style.transition = 'opacity 0.3s ease';
        itemBlock.style.opacity = 0;

        // Вычисляем высоту элемента корзины и присваиваем ее переменной
        var fixedItemHeight = itemBlock.offsetHeight;

        // Смещаем все элементы ниже удаляемого элемента вверх
        var elementsBelow = Array.from(itemBlock.parentNode.children).slice(index + 1);
        elementsBelow.forEach(function (element) {
          element.style.transition = 'transform 0.3s ease';
          element.style.transform = `translateY(-${fixedItemHeight}px)`;
        });

        updateCartAndButtonAnimation(currentTotalAmount, newTotalAmount);

        setTimeout(function () {
          // После окончания анимации смещения элементов, удаляем элемент из DOM
          itemBlock.parentNode.removeChild(itemBlock);

          // Возвращаем элементам исходное местоположение
          elementsBelow.forEach(function (element) {
            element.style.transform = '';
            element.style.transition = '';
          });

          //tg.MainButton.setText(`Підтвердити ${totalAmount}₴`);
          
          
          updateCartPopup();

          if (cart.length === 0) {
            closeCartPopup();
          }
        }, 300); // Задержка равная времени анимации
      }
    }

    // Функция для анимации уменьшения суммы
    function updateCartAndButtonAnimation(currentTotalAmount, newTotalAmount) {
      // Устанавливаем начальный текст кнопки с текущей суммой
      //tg.MainButton.setText(`Підтвердити ${currentTotalAmount}₴`);

      // Создаем анимацию для изменения текста кнопки
      var animationStep = (newTotalAmount - currentTotalAmount) / 10; // Разницу делим на 10 шагов
      var currentAmount = currentTotalAmount;

      var animationInterval = setInterval(function () {
        currentAmount += animationStep;

        // Останавливаем анимацию, когда достигнута новая сумма
        if ((animationStep > 0 && currentAmount >= newTotalAmount) || (animationStep < 0 && currentAmount <= newTotalAmount)) {
          clearInterval(animationInterval);
          currentAmount = newTotalAmount;
        }

        // Обновляем текст кнопки с текущим значением
        tg.MainButton.setText(`Підтвердити ${Math.round(currentAmount)}₴`);
      }, 10); // Задержка между шагами (миллисекунды)
    }

    function calculateTotalAmount() {
      return cart.reduce(function (sum, item) {
        return sum + item.price * item.count;
      }, 0);
    }
  
    loadProducts();
  </script>
</body>
</html>
