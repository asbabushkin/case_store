# case_store
     Интернет-магазин аксессуаров для сотовых телефонов. В первой версии магазина продаются только чехлы, но бд разработана таким образом, чтобы в дальнейшем можно было легко расширить ассоримент магазина.
     На главной странице пользователь видит доступные категории чехлов (силиконовые, пластиковые, противоударные). По клику на категорию пользователю предлагается выбрать из списка свою марку и модель телефона. После этого выводится список товаров, соответствующих заданным условиям. Список выводится в виде плитки, элементов содержащих изображение товара, наименование, цену, кнопку "подробнее" и кнопку "в корзину". Нажав на кнопку "подробнее" или кликнув по изображению, пользователь переходит в карточку товара, содержащую подробную информацию о товаре (изображение, описание, характеристики) и кнопки "добавить в корзину" и "назад". Клик по кнопке "назад" возвращает пользователя на страницу, с которой он перешел. После того как покупатель поместит товар в корзину, значек пустой корзины в хедере изменится на значек полной корзины. После того, как покупатель закончит покупки он кликает на иконку корзины в хедере и переходит на экран корзины. Там он видит выбранные товары, их цену, количество и общую стоимость. Пользователь может изменить количество товаров или удалить некоторые позиции из заказа. После этого покупатель кликает  кнопку "подтвердить заказ". Если пользователь был авторизован, он переходит на экран ввода данных для доставки. Если покупатель не был авторизован, выпадает всплывающее окно с предложением авторизоваться либо зарегистрироваться. После выполнения предложенной процедуры авторизованный пользователь переходит на экран ввода данных для доставки. Указав адрес и выбрав способ доставки, покупатель нажимает клавишу "далее" и переходит на экран оплаты (cloudi-psp), где вносит данные банковской карты и производит оплату. После оплаты пользователь переходит на экран "спасибо за покупку", а на его электронную почту отправляется письмо с номером и деталями заказа. 
     Стек: Django - основный бекенд фреймворк, Bootstrap4 -верстка и стили,  Postgre SQL - основная бд,  cloudi-psp - сервис для совершения оплаты.
