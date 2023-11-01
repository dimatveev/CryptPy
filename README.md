<h1>CryptPy</h1>

<p>CryptPy - это мощный инструмент командной строки для шифрования, дешифрования и взлома файлов с использованием различных криптографических алгоритмов.</p>

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
python crypt.py encrypt  input-file
</pre>

<h3>Расшифровка файла</h3>

<pre>
python crypt.py decrypt input-file
</pre>

<h3>Взлом файла</h3>

<pre>
python crypt.py crack input-file
</pre>

<h2>Доступные методы шифрования</h2>

<ol>
    <li><code>caesar</code>: Шифр Цезаря</li>
    <li><code>vigenere</code>: Шифр Виженера</li>
    <li><code>vernam</code>: Шифр Вернама</li>
    ...
</ol>

<h2>Поддержка</h2>

<p>Если у вас возникли вопросы или проблемы, создайте <a href="https://github.com/dimatveev/cryptpy/issues">issue</a> на GitHub.</p>
