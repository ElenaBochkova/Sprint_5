# Sprint_5
<h1>Тестирование проекта Stellar Burger</h1>
<h2>Папки проекта</h2>
<h3>Папка common:</h3>
Содержит вспомогательные файлы проекта, а именно:

- <b>common_procedures.py</b> - содержит общие функции, а именно:
- - <b>generate_login</b> - функция генерации логина (email)
- - <b>generate_password</b> - функция генерации пароля заданной длины
- <b>common_selectors.py</b> - содержит все селекторы, использующиеся в проекте
- <b>common_user_class.py</b> - содержит класс User с полями login и password

<h3>Папка tests:</h3>
Содержит тесты проекта, а именно:

- <b>test_registration.py</b> - тестирование регистрации в системе, а именно:
- - <b>test_correct_registration</b> - тест совершенно обычной регистрации со всеми корректными данными
- - <b>test_registration_password_shorter_6_symbols_FAIL</b> - тест регистрации с паролем длиной короче 6 символов
- <b>test_quit_account.py</b> - тестирование выхода из аккаунта, а именно:
- - <b>test_open_personal_account_after_login_pass</b> - тест выхода из аккаунта после логина новозарегистрированным пользователем
- <b>test_navigate_constructor.py</b> - тестирование перехода по разделам в Конструкторе, а именно:
- - <b>test_navigate_to_sauces_unlogged_constructor_pass</b> - переход в секцию "Соусы" в Конструкторе без логина
- - <b>test_navigate_to_bread_unlogged_constructor_pass</b> - переход в секцию "Булки" в Конструкторе без логина
- - <b>test_navigate_to_filling_unlogged_constructor_pass</b> - переход в секцию "Начинки" в Конструкторе без логина
- - <b>test_navigate_to_sauces_logged_constructor_pass</b> - переход в секцию "Соусы" в Конструкторе после логина
- - <b>test_navigate_to_bread_logged_constructor_pass</b> - переход в секцию "Булки" в Конструкторе после логина
- - <b>test_navigate_to_filling_logged_constructor_pass</b> - переход в секцию "Начинки" в Конструкторе после логина
- <b>test_login.py</b> - тестирование входа, а именно:
- - <b>test_login_through_main_page_pass</b> - логин через кнопку "Войти в аккаунт" на главной странице
- - <b>test_login_through_personal_account_pass</b> - логин через Личный кабинет
- - <b>test_login_through_link_in_registration_form_pass</b> - логин через кнопку "Войти" на форме регистрации
- - <b>test_login_through_link_in_password_recovery_form_pass</b> - логин через кнопку "Войти" на форме восстановления пароля
- <b>test_go_to_personal_account.py</b> - тестирование перехода в Личный кабинет, а именно:
- - <b>test_open_personal_account_without_login_pass</b> - Вход в Личный кабинет, не логинясь в системе
- - <b>test_open_personal_account_after_login_pass</b> - Вход в Личный кабинет после входа зарегистрированным в фикстуре пользователем
- <b>test_go_from_personal_account</b> - тестирование перехода в конструктор из Личного кабинета, а именно:
- - <b>test_go_from_logged_personal_account_to_constructor_pass</b> - Переходим в Конструктор по ссылке Конструктор из Личного кабинета залогинившегося пользователя
- - <b>test_go_from_logged_personal_account_to_logo_pass</b> - Переходим в Конструктор по клику на логотип из Личного кабинета залогинившегося пользователя
- - <b>test_go_from_unlogged_personal_account_to_constructor_pass</b> - Переходим в Конструктор по ссылке Конструктор из Личного кабинета без логина в системе
- - <b>test_go_from_unlogged_personal_account_to_logo_pass</b> - Переходим в Конструктор по клику на логотип из Личного кабинета без логина в систему
- <b>conftest.py</b> - фикстуры, а именно:
- - <b>driver</b> - фикстура со scope=function. Создает драйвер браузера и выходит из браузера по окончании теста
- - <b>generated_user</b> - фикстура со scope=function. Регистрирует в системе пользователя и передает тесту его данные
- - <b>login</b> - фикстура со scope=function. Логинится в системе под пользователем, созданным фикстурой generated_user
