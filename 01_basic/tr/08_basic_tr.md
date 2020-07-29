# トレーニング - データ構造 - セット

## `set_tr1.py`

次のプログラムがあります。

``` python
names = {"Alice", "Bob", "Carlie", "Bob"}

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Alice Carlie Bob 
```

> 実行結果の出力順序は上記と異なる場合があります。

---

## `set_tr2.py`

次のプログラムがあります。

``` python
name = input("Name: ")
names = {"Alice", "Bob", "Carlie"}

# TODO
```

* キーボードから入力された値が変数 `names` の中に存在する場合は画面に"OK"と出力します。
* キーボードから入力された値が変数 `names` の中に存在しない場合は画面に"NG"と出力します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

* キーボードから `Alice` と入力した場合

``` 
Name: Alice
OK
```

* キーボードから `Daniel` と入力した場合

``` 
Name: Daniel
NG
```

---

## `set_tr3.py`

次のプログラムがあります。

``` python
names = set()
name1 = input("Name1: ")
name2 = input("Name2: ")
name3 = input("Name3: ")

# TODO
```

* キーボードから名前を3つ（ `name1` 、 `name2` 、 `name3` ）入力します。
* 入力された名前について、重複を除いて出力します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 

$ python set_tr3.py
Name1: Alice
Name2: Bob
Name3: Bob
Names: {'Alice', 'Bob'}
```

> 実行結果の出力順序は上記と異なる場合があります。

---

## `set_tr4.py`

次のプログラムがあります。

``` python
names = set()
while True:
    name = input("Name: ")
    if name == "":
        break
    # TODO

print("Names:", names)
```

* キーボードから名前を繰り返し入力します。
        + キーボードから入力された値が空文字の場合、繰り返しを終了します。
* 入力された名前について、重複を除いて出力します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
Name: Alice
Name: Bob
Name: Bob
Name: Charlie
Name: 
Names: {'Charlie', 'Bob', 'Alice'}
```

> 実行結果の出力順序は上記と異なる場合があります。

---

## `set_tr5.py`

次のプログラムがあります。

``` python
number_list = [10, 20, 30, 10]
number_set = set()

# TODO

print("Number Set:", number_set)
```

+ `number_list`変数の重複要素を排除して、結果を出力します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
Number Set: {10, 20, 30}
```

---

## `set_tr6.py`

次のプログラムがあります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Lemon": 100}
price_set = set()

# TODO

print("Price Set:", price_set)
```

+ `fruits`変数の値の重複を排除して、結果を出力します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
Price Set: {200, 100} 
```
---

### テキスト

* [テキスト - データ構造 - セット](../text/08_basic.md)
