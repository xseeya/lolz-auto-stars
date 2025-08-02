<!-- Заголовок первого уровня с эмодзи -->
# LolzTeam Auto Stars :robot:

<!-- Бейджи с динамическими иконками -->
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/)

<!-- Описание -->
Скрипт для раздачи Telegram Stars на форуме lolz.live

<!-- Раздел установки -->
## :gear: Установка

<!-- Блок кода с подсветкой синтаксиса bash -->
```bash
git clone https://github.com/xseeya/lolz-auto-stars.git
cd lolz-auto-stars
pip install -r requirements.txt
```

## :wrench: Конфигурация <!-- Заголовок с эмодзи -->

Перед запуском отредактируйте файл `utils/config.py.example` в `config.py`: <!-- Инлайн-код в тексте -->

```python
# Авторизация в LolzTeam
lolz_token = ''  # API-токен от LolzTeam (обязательно). Получить - https://lzt.market/account/api
thread_id = 0     # ID темы, где будет отправляться сообщение

# Настройки сообщений
text = 'Отправлено!'  # Текст сообщения после отправки звезды
delay = 10            # Задержка между проверкой на новые посты (в секундах)
star = 1              # Количество звёзд для отправки

# Настройка Telegram
api_id = 0           # ID вашего Telegram приложения
api_hash = ''        # Hash вашего Telegram приложения
```

### Описание параметров:

| Параметр       | Тип    | Описание |
|----------------|--------|----------|
| `lolz_token`   | str    | **Обязательно**<br>API-токен [LolzTeam](https://lzt.market/account/api) профиля |
| `thread_id`    | int    | ID темы с раздачей звёзд |
| `text`         | str    | Текст сообщения после отправки звезды |
| `delay`        | int    | Задержка между проверкой на новые посты (По умолчанию: 10 секунд)|
| `star`         | int    | Количество звёзд для каждого пользователя |
| `api_id`       | int    | Получите api_id [my.telegram.org](https://my.telegram.org) |
| `api_hash`     | str    | Получите вместе с api_id |

## :satellite: Создание Telegram сессии

Для корректной работы необходимо создать .session файл:


1. Запустите инициализацию сессии:
   ```bash
   python setup_session.py
   ```

2. Следуйте инструкциям в консоли:
   - Введите номер телефона в международном формате
   - Введите код подтверждения из Telegram
   - При необходимости введите пароль 2FA

3. После успешной аутентификации в папке появится файл `auto_stars.session`

## :rocket: Запуск скрипта

### 1. Создание виртуального окружения (рекомендуется)
Перед запуском создайте [виртуальное окружение](https://docs.python.org/3/tutorial/venv.html):

```bash
python -m venv .venv
```

Активируйте окружение:
- Windows:
  ```bash
  .venv\Scripts\Activate.ps1
  ```
- Linux/MacOS:
  ```bash
  source .venv/bin/activate
  ```

Установите зависимости:
```bash
pip install -r requirements.txt
```

### 2. Запуск скрипта
```bash
python main.py
```

> :bulb: **Совет**  
> Для автоматического запуска можно использовать: `systemd` (Linux)
