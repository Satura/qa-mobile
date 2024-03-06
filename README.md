# Тестирование мобильного приложения

### Домашнее задание #1

<details>
  <summary>Написать тест-кейсы для тестирования функциональности приложения</summary>

---

Приложение: _Stepik_

| No  | Приоритет | Название                                                               | Предусловия                                                                                                              | Шаги                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Ожидаемый результат                                                                                                                                                                                                                                  | Комментарий                                                                                          |
|:---:|:---------:|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
|  1  |  высокий  | Регистрация по email                                                   | --                                                                                                                       | 1. Нажать ссылку "Регистрация" внизу экрана.<br>2. Заполнить открывшуюся форму валидными данными ("Вилланель", "testmail@mail.com", "testpass"). <br>3. Нажать "Регистрация"                                                                                                                                                                                                                                                                                                     | Открывается главная страница, появляется приветственное попап-сообщение для настройки уведомления-напоминания.<br>На указанный email приходит сообщение с ссылкой для подтверждения регистрации.                                                     |                                                                                                      |
|  2  |  высокий  | Поиск курса из строки поиска в разделе "Каталог"                       | --                                                                                                                       | 1. Перейти в "Каталог" тапом по иконке на нижней панели.<br>2. Ввести в строку поиска запрос "тестирование"                                                                                                                                                                                                                                                                                                                                                                      | 1. Открывается раздел "Каталог". <br>2. Выводятся карточки курсов, содержащих в названии слово искомое слово и его производные ("тестировании", "тестирования")                                                                                      |                                                                                                      |
|  3  |  высокий  | Фильтрация результатов поиска                                          | --                                                                                                                       | 1. Тапнуть по иконке фильтр.<br>2. Переключить тумблеры фильтров "Только с сертификатом", "Только бесплатные" в активное состояние.<br>3. "Посмотреть результат".                                                                                                                                                                                                                                                                                                                | Остаются только карточки курсов с обозначением "Сертификат" и указанием "Бесплатно" вместо цены                                                                                                                                                      |                                                                                                      |
|  4  |  высокий  | Просмотр страницы курса                                                | Выбран курс в разделе  поиска либо из предложенных на главной (например "Тестирование ПО: Postman для тестирования API") | 1. Тапнуть по карточке курса. <br>2. Последовательно перейти по вкладкам на страннице курса.                                                                                                                                                                                                                                                                                                                                                                                     | 1. Открывается страница курса. <br>2. На каждой вкладке отображается соответствующая информация (либо сообщение, что в данный момент записи отсутствуют); на вкладке "Модули" выводится перечень модулей с уроками, не доступные для взаимодействия. |                                                                                                      |
|  5  |  высокий  | Загрузка материалов урока (Wi-Fi)                                      | 1. Найти желаемый курс.<br>2. Открыть страницу курса. <br>3. Нажать "Поступить на курс".                                 | На вкладке "Модули" тапнуть по иконке загрузки (облачко со стрелкой) у урока                                                                                                                                                                                                                                                                                                                                                                                                     | Во время загрузки иконка меняется на значок загрузки, по окончании - на галочку. <br>При отключении интернета материалы загруженного урока отображаются.                                                                                             |                                                                                                      |
|  6  |  средний  | Отключение интернета в процессе загрузки материалов урока              | 1. Найти желаемый курс.<br>2. Открыть страницу курса. <br>3. Нажать "Поступить на курс".                                 | 1. На вкладке "Модули" тапнуть по иконке загрузки (облачко со стрелкой) у незагруженного урока. <br>2. Перейти в режим "полета" до окончания загрузки.                                                                                                                                                                                                                                                                                                                           | Иконка меняется на значок загрузки, на панели уведомлений появляется запись о файлах в очереди и необходимости включения Wi-Fi. При повторном включении Wi-Fi загрузка продолжается.                                                                 |                                                                                                      |
|  7  |  высокий  | Загрузка материалов урока (мобильный интернет, настройки по умолчанию) | 1. Найти желаемый курс.<br>2. Открыть страницу курса. <br>3. Нажать "Поступить на курс".                                 | На вкладке "Модули" тапнуть по иконке загрузки (облачко со стрелкой) у урока                                                                                                                                                                                                                                                                                                                                                                                                     | Всплывает сообщение о том, что загрузка через мобильный интернет не доступна с ссылкой в "Настройки"                                                                                                                                                 | (в настройках по умолчанию установлено "Загружать только по Wi-Fi")                                  |
|  8  |  средний  | Загрузка материалов урока (авирежим)                                   | 1. Найти желаемый курс.<br>2. Открыть страницу курса. <br>3. Нажать "Поступить на курс".<br>4. Включить режим "полета"   | На вкладке "Модули" тапнуть по иконке загрузки (облачко со стрелкой) у урока                                                                                                                                                                                                                                                                                                                                                                                                     | Всплывает сообщение об отсутствии интернета                                                                                                                                                                                                          | Всплывает сообщение о том, что загрузка через мобильный интернет не доступна с ссылкой в "Настройки" |
|  9  |  средний  | Настройка уведомления с напоминанием о занятиях                        | --                                                                                                                       | 1. Перейти в раздел "Профиль". <br>2. Переключить тумблер "напоминать о занятиях" во включенное состояние.<br>3. Выбрать время напоминания, нажать "Ок".                                                                                                                                                                                                                                                                                                                         | В установленное время на устройстве появляется уведомление с напоминанием о занятиях                                                                                                                                                                 |                                                                                                      |
| 10  |  высокий  | Сворачивание видео в плавающий всплывающий плеер                       | Найти курс "Эффективная презентация проекта" (пример курса с видеоматериалами в уроках).<br>Поступить на курс.           | 1. Перейти к шагу на курсе, в котором материал представлен в видео формате (шаг 3 урока 1.1).<br>2. Запустить видео и нажать иконку плавающего плеера.                                                                                                                                                                                                                                                                                                                           | Видео сворачивается в плавающий плеер, остальная часть экрана доступна для взаимодействия.                                                                                                                                                           |                                                                                                      |
| 11  |  высокий  | Отображение в горизонтальной ориентации экрана планшета                | Выбран для прохождения хотя бы один курс, хотя бы один курс с сертификатом завершен                                      | 1. Запустить приложение и авторизоваться.<br>2. Последовательно перейти в каждый из разделов (Обучение, Каталог, Профиль, Уведомления).<br>3. Открыть страницу  курса из перечня "Мои курсы". Открыть последовательно все вкладки.<br>4. Открыть урок курса. Переключиться по материалам курса. <br>5. Перейти в раздел "Каталог", открыть запись из "сторис".<br>6. Перейти в раздел "Профиль", перейти в подраздел "Достижения", вернуться, перейти в подраздел "Сертификаты". | Все экраны (разделы, страницы курсов, материалы уроков, сторис, подразделы профиля) отображаются в горизонтальный ориентации, элементы (карточки курсов) перераспределяются заполняя пространство экрана.                                            |                                                                                                      |
| 12  |  высокий  | Редактирование профиля                                                 | Пользователь зарегистрирован и авторизован                                                                               | 1. Перейти в раздел "Профиль" на нижней панели.<br>2. Перейти к редактированию профиля (иконка карандаша в верхней части экрана).<br>3. Тапнуть по строке "Персональные данные".<br>4. Заполнить поля корректными данными и принят изменения.                                                                                                                                                                                                                                    | Появляется уведомление "Информация обновлена", на главной странице раздела указаны обновленные данные.                                                                                                                                               |                                                                                                      |

</details>


### Домашнее задание #2

<details>
<summary>
Составить таблицу с устройствами для тестирования вашего выбранного приложения. Выбрать 2-3 тест-кейса, которые мы писали ранее, провести на них тестирование на выбранных устройствах.</summary>

---
 
  ЦА русскоязычные жители стран СНГ, главным образом Россия.

#### Производители

Распределение по [производителям телефонов](https://gs.statcounter.com/vendor-market-share/mobile/russian-federation):

* Apple - 29.51%
* Xiaomi - 23.2%
* Samsung - 17.91%

Распределение по [производителям планшетов](https://gs.statcounter.com/vendor-market-share/tablet/russian-federation)

* Apple - 37.96%
* Samsung - 33.2%
* Xiaomi - 10.07%
* Huawei - 10.03%

#### Версии ОС 

[iOS](https://developer.apple.com/support/app-store/)

- телефоны:
  * iOS 17 - 76% 
  * iOS 16 - 20%

- планшеты: 
  * iOS 17 - 61% 
  * iOS 16 - 29%

[android](https://www.appbrain.com/stats/top-android-sdk-versions)
* Android 13	24.5%	 
* Android 11	20.1%	
* Android 12 16.8%	
* Android 10	12.5%

[Популярные в России устройства:](https://www.appbrain.com/stats/top-android-phones-tablets-by-country?country=ru)
* Redmi 9C NFC
* Huawei HONOR 10i
* Huawei HONOR 9X lite	
* Samsung Galaxy A12
* Samsung Galaxy A51

В перечень устройств для тестирования включены устройства из перечня популярных, различные  устройства лидирующих производителей охватывающие разные версии ОС, размеры и разрешения экрана и годы выпуска. 

Результаты в [таблице](https://docs.google.com/spreadsheets/d/14XCxbBB1T41FU4HJPQQrFOgd2F5Td_aU/edit?usp=sharing&ouid=102514362893231578101&rtpof=true&sd=true)
</details>

### Домашнее задание #3

<details>
<summary>
Дополнить тест-кейсы негативными проверками, когда от сервера приходят неожиданные/ошибочные ответы</summary>

---
 
| No | Приоритет | Название | Предусловия | Шаги | Ожидаемый результат | Комментарий |
| :--: | :--: | :--- | :--- | :--- | :--- | :--- |
| 1 | средний | Добавление в избранное курса с изменённым номером | Открыта страница выбранного курса | 1. Установить правила breakpoints - before requests.<br>2. Нажать значок избранного.<br>3. В RAW запроса " /api/wish-lists" изменить параметр "course" на несуществующий (пр. "123123123")<br>4. Запустить выполнение запроса. | В заголовке ответа: 400 Bad Request; в теле ответа: {"course": ["Invalid pk '123123123' - object does not exist."]}.<br>Значок избранного остался неактивным. |  |
| 2 | средний | Удаление из избранного курса, без токена авторизации | В избранное добавлен курс, открыта страница этого курса | 1. Установить правила breakpoints - before requests.<br>2. Нажать значок избранного.<br>3. В RAW запроса " /api/wish-lists/<#добавления>" удалить значение после "Authorization: Bearer"<br>4. Запустить выполнение запроса. | В заголовке ответа: 401 Unauthorized; в теле ответа: {"detail": "CSRF Failed: Referer checking failed - no Referer."}.<br>Значок избранного остался активным. |  |
| 3 | средний | Получение в результате поиска ответа 404 Not Found | Открыт раздел "Каталог", в поле поиска введено значение (пр. "java") | 1. Установить правила breakpoints - after requests. <br>2. В запросе "/api/search-results?page=1&query=java..." установить ответ 404 Not Found<br>3. Запустить выполнение запроса | На странице раздела отображаются шаблоны карточек курсов без данных. | На странице раздела отображается сообщение «Sorry, the connection is not available. Try again later». |
| 4 | средний | Получение 503 Service Unavailable при переходе к уроку курса | Открыта вкладка "Модули" проходимого курса | 1. Установить правила breakpoints - after requests. <br>2. Открыть доступный урок курса.<br>3. В запросе "/api/progresses?..." установить ответ 503 Service Unavailable <br>3. Запустить выполнение запроса | На странице урока отображается сообщение с кодом и текстом ошибки | На странице урока отображается сообщение «Sorry, the connection is not available. Try again later». |

[Fiddler-sessions](https://github.com/Satura/qa-mobile/blob/main/docs/HW-3.saz)

</details>

### Домашнее задание #4 - Финальный проект

<details>
<summary>Автоматизировать на эмуляторе 5 тест-кейсов используя Appium и UIAutomator2 драйвер</summary>

---

Реализованы тесты:
1. Регистрация нового пользователя по e-mail
2. Редактирование профиля
3. Поиск курса по заданному слову
4. Работа фильтрации курсов  
5. Попытка загрузки материалов курса на мобильном интернете

![Результаты выполнения тестов](https://github.com/Satura/qa-mobile/blob/main/docs/test_results.png)
[Видео прохождения тестов](https://disk.yandex.com/i/lB8xVZ2MT-lvgQ)

</details>
