# エクササイズ - 制御構文 - 分岐構造 - if文

## if_ex1.py

* 認証プログラムを作成します。
  + 入力されたユーザIDによって出力を決定します。
    - ユーザIDが"Alice"の場合、"Success"と表示します。
    - ユーザIDが"Alice"でない場合、"Error"と表示します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### ユーザIDが"Alice"の場合

``` 
$ python if_ex1.py
USER ID: Alice
Success
```

> プログラムを実行後、キーボードからAliceと入力します。

#### ユーザIDが"Alice"でない場合

``` 
$ python if_ex1.py
USER ID: Bob
Error
```

> プログラムを実行後、キーボードからBobと入力します。

### ヒント

``` python
user_id = input("USER ID: ")

# TODO
```

> `input` 関数は標準入力（この場合、キーボードからの入力）を処理します。

---

## if_ex2.py

* 認証プログラムを作成します。
  + 入力されたユーザIDによって出力を決定します。
    - ユーザIDが"Alice"、"Bob"のいずれかの場合、"Success"と表示します。
    - 上記以外の場合は、"Error"と表示します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### ユーザIDが"Alice"、あるいは"Bob"の場合

``` 
$ python if_ex2.py
USER ID: Alice
Success
```

``` 
$ python if_ex2.py
USER ID: Bob
Success
```

#### ユーザIDが"Alice"、"Bob"でない場合

``` 
$ python if_ex2.py
USER ID: John
Error
```

### ヒント

``` python
user_id = input("USER ID: ")

# TODO
```

---

## if_ex3.py

* 認証プログラムを作成します。
  + 入力されたユーザID、パスワードによって出力を決定します。
    - ユーザIDが"Alice"、かつ、パスワードが"pass"の場合、"Success"と表示します。
    - 上記以外の場合は、"Error"と表示します。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### ユーザIDが"Alice"、パスワードが"pass"の場合

``` 
$ python if_ex3.py
USER ID: Alice
PASSWORD: pass
Success
```

#### ユーザIDが"Alice"、パスワードが"test"の場合

``` 
$ python if_ex3.py
USER ID: Alice
PASSWORD: test
Error
```

### ヒント

``` python
user_id = input("USER ID: ")
password = input("PASSWORD: ")

# TODO
```

---

## if_ex4.py

* 買い物の金額とポイントを表示するプログラムを作成します。
  + ポイントは500円以上購入した場合に1ポイント付与するものとします。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### 購入金額が500円の場合

``` 
> python if_ex4.py
PRICE: 500
POINT: 1
```

> プログラムを実行後、キーボードから500と入力します。

#### 購入金額が300円の場合

``` 
> python if_ex4.py
PRICE: 300
```

### ヒント

``` python
price = int(input("PRICE: "))

# TODO
```

> `int` 関数は整数型（ `int` 型）データに変換します。

---

## if_ex5.py

* 買い物の金額とポイントを表示するプログラムを作成します。
  + ポイントは500円毎に1ポイント付与するものとします。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### 購入金額が2000円の場合

``` 
$ python if_ex5.py
PRICE:2000
POINT:4
```

#### 購入金額が300円の場合

``` 
$ python if_ex5.py
PRICE:300
```

### ヒント

``` python
price = int(input("PRICE: "))

# TODO
```

---

## if_ex6.py

* 買い物の金額とポイントを表示するプログラムを作成します。
  + ポイントはGOLD会員と通常会員の2種類によって決定します。
    - GOLD会員の場合、ポイントは500円毎に1ポイント付与するものとします。
    - 通常会員の場合、ポイントは1000円毎に1ポイント付与するものとします。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

#### GOLD会員が3000円購入した場合

``` 
$ python if_ex6.py
PRICE: 3000
MEMBER: GOLD
POINT: 6
```

> プログラムを実行後、キーボードから3000 GOLDと入力します。

#### 通常会員が3000円購入した場合

``` 
$ python if_ex6.py
PRICE: 3000
MEMBER: NORMAL
POINT: 3
```

> プログラムを実行後、キーボードから3000 NORMALと入力します。

#### GOLD会員が500円購入した場合

``` 
$ python if_ex6.py
PRICE: 500
MEMBER: GOLD
POINT: 1
```

> プログラムを実行後、キーボードから500 GOLDと入力します。

#### 通常会員が500円購入した場合

``` 
$ python if_ex6.py
PRICE: 500
MEMBER: NORMAL
```

> プログラムを実行後、キーボードから500 NORMALと入力します。

### ヒント

``` python
price = int(input("PRICE: "))
member = input("MEMBER: ")

# TODO
```

---

### テキスト

* [テキスト - 制御構文 - 分岐構造 - if文](../text/03_basic.md)
