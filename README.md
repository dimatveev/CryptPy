<h1>CryptPy</h1>

<p>CryptPy - это мощный инструмент командной строки для шифрования, дешифрования и взлома файлов с использованием различных криптографических алгоритмов на английском языке.</p>

<h2>Особенности</h2>

<ol>
    <li>Шифрование и дешифрование файлов с использованием нескольких методов.</li>
    <li>Возможность взлома некоторых известных шифров.</li>
    <li>Простой и интуитивно понятный интерфейс командной строки.</li>
</ol>

<h2>Установка</h2>

<pre>
git clone https://github.com/yourusername/cryptpy.git
cd cryptpy
pip install -r requirements.txt
</pre>

<h2>Использование</h2>

<h3>Шифрование файла</h3>

<pre>
python main.py operate (метод шифрования)-encrypt encrypt.txt key

</pre>

<h3>Расшифровка файла</h3>

<pre>
python main.py operate (метод шифрования)-decipher decipher.txt key
</pre>

<h3>Взлом файла зашифрованного шифром Цезаря </h3>

<pre>
python main.py operate caesar-crack encrypt.txt
</pre>

<h2>Доступные методы шифрования</h2>

<ol>
    <li><code>caesar</code>: Шифр Цезаря</li>
    <li><code>vigenere</code>: Шифр Виженера</li>
    <li><code>vernam</code>: Шифр Вернама</li>
    <li><code>atbash</code>: Шифр Атбаш</li>
    <li><code>rsa</code>: Шифр RSA</li>
</ol>

<h2>Юнит-тесты</h2>

<p>Проект включает в себя набор юнит-тестов для проверки корректности работы криптографических алгоритмов. Для запуска тестов используйте следующую команду:</p>

<pre>
python -m unittest unit_tests.py
</pre>

<p>Убедитесь, что вы находитесь в корневой директории проекта перед выполнением команды.</p>

<h2>Поддержка</h2>

<p>Если у вас возникли вопросы или проблемы, создайте <a href="https://github.com/dimatveev/cryptpy/issues">issue</a> на GitHub.</p>

