PERSONAL_ACCOUNT_LINK = ".//p[text()='Личный Кабинет']" #XPATH для перехода по ссылке "Личный кабинет"
REGISTRATION_LINK = ".//a[text()='Зарегистрироваться']" #XPATH для перехода по ссылке "Зарегистрироваться"
NAME_FIELD = ".//label[text()='Имя']/following-sibling::input" #XPATH для поля "Имя" в форме регистрации
EMAIL_FIELD = ".//label[text()='Email']/following-sibling::input" #XPATH для заполнения поля "Email"
PASSWORD_FIELD = ".//label[text()='Пароль']/following-sibling::input" #XPATH для заполнения поля "Пароль"
REGISTRATION_BUTTON = ".//button[text()='Зарегистрироваться']" #XPATH для кнопки "Зарегистрироваться"
ENTER_BUTTON = ".//button[text()='Войти']" #XPATH для кнопки "Войти"
LOGIN_FIELD = ".//input[@name='name']" #XPATH для поля "Логин" в Личном Кабинете
ERROR_STRING = "input__error" #CLASS_NAME для сообщения об ошибке при неправильном пароле
ENTER_ACCOUNT_BUTTON = ".//button[text()='Войти в аккаунт']" #XPATH для кнопки "Войти в аккаунт"
PROFILE_LINK = "Account_link_active__2opc9" #CLASS NAME для ссылки "Профиль" в Личном кабинете
QUIT_BUTTON = ".//button[text()='Выход']" #XPATH для кнопки "Выйти" в Личном кабинете
ENTER_HEADER = ".//div[@class='Auth_login__3hAey']/h2" #XPATH для надписи "Войти" в форме входа
CONSTRUCTOR_LINK = ".//p[text()='Конструктор']" #XPATH для перехода в Конструктор
SAUCE_LINK = ".//span[text()='Соусы']" #XPATH для секции Соусы в Конструкторе
BREAD_LINK = ".//span[text()='Булки']" #XPATH для секции Булки в Конструкторе
FILLER_LINK = ".//span[text()='Начинки']" #XPATH для секции Начинки в Конструкторе
ACTIVE_SECTION = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #XPATH для активной секции в Конструкторе
ENTER_LINK = ".//a[text()='Войти']" #XPATH для ссылки "Войти"
RESTORE_PASSWORD_LINK = ".//a[text()='Восстановить пароль']" #XPATH для ссылки "Восстановить пароль"
MAKE_BURGER_HEADER = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/h1" #XPATH для заголовка Соберите бургер
LOGO_LINK = ".//div[@class='AppHeader_header__logo__2D0X2']/a" #XPATH для логотипа в Личном кабинете