# ссылка на тест кейсы  https://docs.google.com/spreadsheets/d/1xkKzx2Z3AwmXoZn5DcIoyzXLXYnOikGJv1e3JDzhAHw/edit?usp=sharing

valid_user_email = "nick_dj@mail.ru"
valid_user_password = "Валидный пароль"
valid_user_phone = "Валидный телефон"
invalid_email = "mail@mail.foo"
invalid_password = "@s98FtрBRe9@YD1"

# данные для 1,2,3,4 test
data_for_tab_tests = (("t-btn-tab-ls", "Лицевой счёт"),
                      ("t-btn-tab-login", "Логин"),
                      ("t-btn-tab-mail", "Электронная почта"),
                      ("t-btn-tab-phone", "Мобильный телефон"))

# данные для 5,6,7,8 test
data_for_automatic_change_tests = (("t-btn-tab-mail", "89511926033", 'Мобильный телефон'),
                                   ("t-btn-tab-ls", "nick_dj@mail.ru", "Электронная почта"),
                                   ("t-btn-tab-phone", "Фотон", "Логин"),
                                   ("t-btn-tab-mail", "123456789012", "Лицевой счёт"))

# 10 test
data_button_whith_unfilled_fields = (("t-btn-tab-phone", "Введите номер телефона"),
                                     ("t-btn-tab-mail", "Введите адрес, указанный при регистрации"),
                                     ("t-btn-tab-login", "Введите логин, указанный при регистрации"),
                                     ("t-btn-tab-ls", "Введите номер вашего лицевого счета"))
# данные для 16, 17, 18, 19 test
password_correct_input_check = (('1234567', 'Длина пароля должна быть не менее 8 символов'),
                                ('12345678', 'Пароль должен содержать хотя бы одну заглавную букву'),
                                ('12345678A', 'Пароль должен содержать хотя бы одну прописную букву'),
                                ('12345678a', 'Пароль должен содержать хотя бы одну заглавную букву'))
