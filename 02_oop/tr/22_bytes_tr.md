# トレーニング - 組み込み型 - bytes型

## `bytes_tr1.py`

``` python
number = 65535

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
b'\xff\xff'
```

> 数値をバイト列（2バイト）に変換します。

---

## `bytes_tr2.py`

``` python
number = ???
print(number.to_bytes(2, byteorder="big"))
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
b'\x01\x00'
```

---

## `bytes_tr3.py`

``` python
numbers = ???
for number in numbers:
    print(number.to_bytes(2, byteorder="big"))
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
b'\x01\x00'
b'\x02\x00'
b'\x04\x00'
b'\x08\x00'
b'\x10\x00'
```

---

## `bytes_tr4.py`

``` python
number = 15
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Bin: 0b1111
Oct: 0o17
Hex: 0xf
```

> 組み込み関数で変換します。 https://docs.python.org/ja/3.7/library/functions.html

---

## `bytes_tr5.py`

``` python
str = "Hello"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
H 48
e 65
l 6c
l 6c
o 6f
```

---

## `bytes_tr6.py`

``` python
b_str = b"\x41\x42\x43"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
ABC
```

---

## `bytes_tr7.py`

``` python
b_list = [0x48, 0x61, 0x6c, 0x6c, 0x6f]
b_array = bytearray(b_list)

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Hello
```

---

### テキスト

* [テキスト - 組み込み型 - bytes型](../text/22_bytes.md)
