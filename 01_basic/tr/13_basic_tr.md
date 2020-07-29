# トレーニング - モジュール

### `greeting.py` , `mod_tr1.py`

以下の `greeting.py` ファイルを作成します。

#### `greeting.py`

``` python
def hello(name):
    return "Hello " + name

def bonjour(name):
    return "Bonjour " + name
```

#### `mod_tr1.py`

``` python
import greeting

name = "Alice"
print(greeting.???(name))
print(greeting.???(name))
```

* `mod_tr1.py` から `greeting.py` モジュールを参照できるようにします。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Hello Alice
Bonjour Alice
```

---

### `mod_tr2.py`

次のプログラム（ `mod_tr2.py` ）があります。

``` python
import greeting

name = "Alice"
print(greeting.hello(name))
print(greeting.bonjour(name))
print(greetings.ciao(name))
```

次の実行結果となるようにPythonプログラム（ `greeting.py` ）を修正してください。

### 実行結果

``` 
Hello Alice
Bonjour Alice
Ciao Alice
```

---

### `mod_tr3.py`

次のプログラム（ `mod_tr3.py` ）があります。

``` python
import greeting as greet

name = "Alice"

# TODO
```

次の実行結果となるようにPythonプログラム（ `mod_tr3.py` ）を作成してください。

### 実行結果

``` 
Bonjour Alice
```

---

### `mod_tr4.py`

次のプログラム（ `mod_tr4.py` ）があります。

``` python
from greeting import bonjour

name = "Alice"

# TODO
```

次の実行結果となるようにPythonプログラム（ `mod_tr4.py` ）を作成してください。

### 実行結果

``` 
Bonjour Alice
```

---

### `mod_tr5.py`

次のプログラム（ `mod_tr5.py` ）があります。

``` python
# TODO

name = "Alice"
print(bonjour(name))
print(ciao(name))
```

次の実行結果となるようにPythonプログラム（ `mod_tr5.py` ）を作成してください。

### 実行結果

``` 
Bonjour Alice
Ciao Alice
```

---

### `mod_tr6.py`

次のプログラム（ `mod_tr6.py` ）があります。

``` python
# TODO

name = "Alice"
print(h(name))
print(b(name))
print(c(name))
```

次の実行結果となるようにPythonプログラム（ `mod_tr6.py` ）を作成してください。

### 実行結果

``` 
Hello Alice
Bonjour Alice
Ciao Alice
```

---

### テキスト

* [テキスト - モジュール](../text/13_basic.md)
