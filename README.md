# sitemap-generator
📜 Скрипт, заносящий все найденые ссылки с переданного URL в базу данных.

# Установка
Перед началом работы со скриптом необходимо установить виртуальное окружение командой:<br>
<b>MacOS/Linux:</b>
```bash
python3 -m virtualenv -p python3 venv
```
<b>Windows:</b>
```bash
python -m venv venv
```

Активируем виртуальное окружение командой:<br>
<b>MacOS/Linux</b>
```bash
source venv/bin/activate
```

<b>Windows</b>
```bash
.\venv\Scripts\activate
```

Устанавливаем все зависимости из файла <code>requirements.txt</code>
```bash
pip install -r requirements.txt
```

# Запуск скрипта

Для запуска скрипта необходимо выполнить команду :
```bash
python src/sitemap_gen.py
```

После выполнения скрипта, карта-сайта каждого сайта будет находиться в соответствующих файлах формата: <code>"\<url\>.xml"</code>
Также информация касательно времени обработки, кол-ва найденных ссылок и т.д будет записана в базу данных, в таблицу <code>sitemap</code>
