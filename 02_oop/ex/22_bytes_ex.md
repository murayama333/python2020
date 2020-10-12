# エクササイズ - 組み込み型 - bytes型

## `bytes_ex1.py`

``` py
numbers = [1, 2, 4, 8, 16]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python bytes_ex1.py
[b'\x01', b'\x02', b'\x04', b'\x08', b'\x10']
```

---

## `bytes_ex2.py`

``` py
numbers = ???

number_bytes_list = [number.to_bytes(1, byteorder="big") for number in numbers]
print(number_bytes_list)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python bytes_ex2.py
[b'\x0e', b'\x0f', b'\x10', b'\x11', b'\x12']
```

---

## `bytes_ex3.py`

``` py
message = "abcdef"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python bytes_ex3.py
616263646566
```

> `abcdef` をUTF-8（ASCIIコード）で変換して16進数表記します。

---

## `bytes_ex4.py`

``` py
message = ???
message_bytes = message.encode("UTF-8").hex()
print("Hex String:", message_bytes)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python bytes_ex4.py
Hex String: 736563726574
```

---

## `bytes_ex5.py`

``` py
b_list = [0x50, 0x79, 0x68, 0x74, 0x6f, 0x6e]
message_byte_array = bytearray(b_list)

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python bytes_ex5.py
Python
```

---

### テキスト

* [テキスト - 組み込み型 - bytes型](../text/22_bytes.md)
