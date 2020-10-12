# トレーニング - ファイルオブジェクト

## `file_tr1.py`

``` python
my_list = list(range(1, 10))
file = "my_list.txt"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

> 画面には何も表示されません。カレントフォルダに以下のような `my_list.txt` ファイルが生成されます。

``` 
1
2
3
4
5
6
7
8
9
```

---

## `file_tr2.py`

``` python
file = "my_list.txt"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
45
```

> `my_list.txt` の行の合計値を表示します。

---

## `file_tr3.py`

``` python
fruits = {"Apple": 100, "Lemon": 200, "Oragne": 300}
file = "fruits.txt"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

> 画面には何も表示されません。カレントフォルダに以下のような `fruits.txt` ファイルが生成されます。

``` 
Apple 100
Lemon 200
Oragne 300
```

---

## `file_tr4.py`

``` python
file = "fruits.txt"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
600
```

> `fruits.txt` の行の数値部分の合計値を表示します。

---

## `file_tr5.py`

``` python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
file = "numbers.csv"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

> 画面には何も表示されません。カレントフォルダに以下のような `numbers.csv` ファイルが生成されます。

``` 
10,20,30
40,50,60
70,80,90
```

---

## `file_tr6.py`

``` python
file = "numbers.csv"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
450
```

> `numbers.csv` の項目の合計値を表示します。

---

## `file_tr7.py`

``` python
math_reports = [
    {"subject": "math", "name": "Alice", "score": 90},
    {"subject": "math", "name": "Bob", "score": 80},
]
english_reports = [
    {"subject": "english", "name": "Alice", "score": 90},
    {"subject": "english", "name": "Bob", "score": 100},
]
file = "report.csv"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

> 画面には何も表示されません。カレントフォルダに以下のような `report.csv` ファイルが生成されます。

``` 
math,Alice,90
math,Bob,80
english,Alice,90
english,Bob,100
```

---

## `file_tr8.py`

``` python
target = input("Subject: ")
file = "report.csv"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Subject: math
total 170
```

> 入力した `Subject` の合計値を表示します。

---

## `file_tr9.py`

``` python
target = input("Name: ")
file = "report.csv"

# TODO
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Name: Alice
math 90
english 90
total 180
```

> 入力した `Name` の `Subject` ごとの点数と合計値を表示します。

---

### テキスト

* [テキスト - ファイルオブジェクト](../text/26_fileobject.md)
