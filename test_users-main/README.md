<h2>Телеграм бот, помогающий сгенерировать тестовые данные</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
* Бот помогает быстро сгенерировать данные для тестовых пользователей
* Бот принимает на входе число N, а на выходе создаёт N пользователей со случайно заполненными полями: имя, почта, адрес, логин, пароль

## 🖼 Скриншоты

Стартовое меню:

<img width="825" height="568" alt="photo_2026-05-09_16-58-05" src="https://github.com/user-attachments/assets/2d499878-d641-4f28-a735-89978089c7ba" />


После выбора количества пользователей:

<img width="827" height="871" alt="photo_2026-05-09_16-57-47" src="https://github.com/user-attachments/assets/0f187c16-2471-4aaf-bac0-205c3bddf412" />


## 💻 Технологии

* Python
* Библиотека `telebot`
* Библиотека `faker`

## ⏬ Установка на локальном компьютере

1. Скачать проект

2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pyTelegramBotAPI
```

``` markdown
python3 -m pip install faker
```

5. Запускаем
``` markdown
python3 test_users_bot.py
```

## Автор

Мухамадеев Тимур ([@Mukhamadeev_Ti](https://t.me/Mukhamadeev_Ti))
