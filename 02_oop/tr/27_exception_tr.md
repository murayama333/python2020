# トレーニング - 例外処理

## `ex_tr1.py`

``` python
# TODO try - except
x = int(input("x: "))
y = int(input("y: "))
z = x + y
print(f"{x}+{y}={z}")
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`x` と `y` に数値を入力した場合

``` 
x: 10
y: 20
10+20=30
```

`x` と `y` のいずれかに文字を入力した場合

``` 
x: 10
y: A
ERROR
```

---

## `ex_tr2.py`

``` python
# TODO try - except
target_key = input("Key: ")
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
print(my_dict[target_key])
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`Key` に `key1` に数値を入力した場合

``` 
Key: key1
1
```

`Key` に `key9` に数値を入力した場合

``` 
Key: key9
key9 is not found.
```

---

## `ex_tr3.py`

``` python
target_key = input("Key: ")
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`Key` に `key1` に数値を入力した場合

``` 
Key: key1
1
```

`Key` に `key9` に数値を入力した場合

``` 
Key: key9
0
```

> 存在しないキー（ `key9` ）を指定した場合は0を表示するものとします。

---

## `ex_tr4.py`

``` python
# TODO try - except
filename = input("File Name: ")
with open(filename, "r") as f:
    print(f.read())
print(f"{filename} is not found.")
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`File Name: ` に存在するファイル名（ `ex_tr1.py` ）を指定した場合

``` 
File Name: ex_tr1.py
try:
    x = int(input("x: "))
    y = int(input("y: "))
    z = x + y
    print(f"{x}+{y}={z}")
except ValueError as e:
    print("ERROR")
```

`File Name: ` に存在しないファイル名（ `not_exist.txt` ）を指定した場合

``` 
File Name: not_exist.txt
not_exist.txt is not found.
```

---

## `ex_tr5.py`

``` python
# TODO class LoginError

# TODO def login

try:
    id = input("ID: ")
    password = input("PASSWORD: ")
    if login(id, password):
        print("LOGIN OK")
except LoginError as e:
    print("LOGIN ERROR")
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`ID: ` に `alice` 、 `PASSWORD: ` に `secret` を指定した場合

``` 
ID: alice
PASSWORD: secret
LOGIN OK
```

> `ID: ` が `alice` 、 `PASSWORD: ` が `secret` の場合のみ `LOGIN OK` と表示します。

`ID: ` に `alice` 、 `PASSWORD: ` に `hello` を指定した場合

``` 
ID: alice
PASSWORD: hello
LOGIN ERROR
```

> `ID: ` が `alice` 、 `PASSWORD: ` が `secret` でない場合は `LOGIN ERROR` と表示します。

---

## `ex_tr6.py`

``` python
class DuplicateInput(Exception):
    pass

input_list = []
while True:
    value = input("Input: ")
    # TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

重複した値を検出するまで入力を繰り返します。重複を検出した場合は、これまでに入力した値を表示します。

``` 
Input: 1
Input: 2
Input: 3
Input: 3
['1', '2', '3']
```

---

## `ex_tr7.py`

``` python
# TODO class MyRequiredError

# TODO class MyLengthError

# TODO def validate

try:
    value = input("Input: ")
    validate(value, 5)
    print(value)
except MyRequiredError as e:
    print("MyRequiredError")
except MyLengthError as e:
    print("MyLengthError")

```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

`Input: ` に空文字を指定した場合

``` 
Input: 
MyRequiredError 
```

`Input: ` に6文字以上（ `123456` ）を指定した場合

``` 
Input: 123456
MyLengthError
```

`Input: ` にそれ以外（1文字以上、5文字以下（ `12345` ））を指定した場合

``` 
Input: 12345
12345
```

---

### テキスト

* [テキスト - 例外処理](../text/27_exception.md)
