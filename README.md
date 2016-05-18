idec-utils
==========

Набор скриптов для работы с текстовой базой сообщений. Текстовая база ничем не отличается от ii-базы сообщений и потому скрипты поднодят так же и для пользователей ii.

archive.py
----------

Скрипт принимает в качестве аргументов название эхоконференции и дату в формате YYYY.MM.DD, после чего ищет в текущей директории базу (директории echo/ и msg/) и создаёт файл-бандл с сообщениями из указанной эхоконференции, отправленными до указанной даты с именем echoname_date.bundle.

Пример использования:

```bash
$ ./archive.py ii.14 2015.01.01
```

Данная команда создаст бандл со всеми сообщениями из эхоконференции ii.14, отправленными до 2015 года. Файл будет называться ii.14_2015.01.01.bundle.

clean.py
--------

Скрипт принимает в качестве аргументов название эхоконференции и дату в формате YYYY.MM.DD, после чего ищет в текущей директории базу (директории echo/ и msg/) и удаляет из базу все сообщения из указанной эхоконференции, отправленные до указанной даты.

Пример использования:

```bash
$ ./clean.py ii.14 2015.01.01
```

Данная команда удалит из эхоконференции ii.14, отправленные до 2015 года.

debundle.py
-----------

Скрипт разворачивает файл-бандл, созданный утилитой archive.py в базу в текущей директории (наличие директорий echo/ и msg/ не обязательны, так как скрипт сам их создаст в случае отсутсвия).

Пример использования:

```bash
$ ./debundle.py ./ii.14_2015.01.01.bundle
````

rmecho.py
---------

Скрипт удаляет из базы в текущей директории файл индекса эхоконференции и все сообщения из неё.

Пример использования:

```bash
$ ./rmecho.py ii.14
```

txt2sqlite.py
-------------

Скрипт принимает в качестве аргумента имя файла для sqlite-базы и создаёт sqlite-базу копию текстовой базы из текущей директории. Sqlite-база может быть полезна для переноса базы с машины на машину посредством флешки или передачи по сети в автоматическом режиме.

Пример использования:

```bash
$ txt2sqlite.py idec.db
```

sqlite2txt.py
-------------

Скрипт принимает в качестве аргумента имя файла sqlite-базы, созданной с помощью txt2sqlite.py и разворачивает её в текстовую базу в текущей директории. ВНИМАНИЕ: скрипт полностью удаляет текстовую базу перез началом работы, так что не рекомендуется его запуск в директории с рабочей текстовой базой.

Пример использования:

```bash
$ sqlite2txt.py idec.db
```

stat.py
-------

Скрипт генерирует и выводит на экран гистограмму со статистикой по активности в эхоконференциях за указанный период. Возможно два варианта сбора данных: по пользователям и по эхоконференциям. Список проверяемых эхоконференций указывается в конфигурационном файле в формате:

```
echo echo.name
```

Пример использования:

```bash
$ stat.py -c ./stat.cfg -t echoareas -s 2014.01.01 -e 2015.01.01
```

Данная команда выведет на экран гистограмму по активности в эхоконференциях, перечисленных в файле stat.cfg с первого января 2014 года по первое января 2015 года.

freq.py
-------

Скрипт позволяет работать со схемами x/filelist и x/file. Скрипт принимает имя файла-конфига или параметры с адресом ноды, строкой авторизации и именем файла.

Конфигурационный файл имеет всего два параметра:

```
node http://idec.spline-online.tk/
auth <authstr>
```

Примеры использования:

```bash
$ freq.py -c freq.cfg
```

В данном случае скрипт считает данные из конфигурационного файла и выведет список файлов, доступных на ноде.

```bash
$ freq.py -n http://idec.spline-online.tk/ -f filename.ext
```

Скрипт скачает файла filename.ext с ноды, доступной по адресу http://idec.spline-online.tk/.