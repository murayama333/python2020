# エクササイズ - ファイルオブジェクト

## `file_ex1.py`

``` py
import datetime

file = "datetime.txt"
now = datetime.datetime.now()

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex1.py
```

> 画面には何も表示しません。以下のファイルを生成します。

#### `datetime.txt`

``` 
2020-10-12 16:31:10.873455
```

> 日時の部分は実行時間によって変化します。

---

## `file_ex2.py`

``` py
import datetime

file = "datetime2.txt"
now = datetime.datetime.now()

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex2.py
$ python file_ex2.py
$ python file_ex2.py
```

> 3回実行します。画面には何も表示しません。以下のファイルを生成します。

#### `datetime2.txt`

``` 
2020-10-12 16:33:57.340406
2020-10-12 16:33:59.731824
2020-10-12 16:34:02.270921
```

> 実行する度に日時をファイルに追記するようにします。

---

## `file_ex3.py`

``` py
cities = [{"index": 1, "name": "Tokyo", "population": 927},
          {"index": 2, "name": "London", "population":  898},
          {"index": 3, "name": "New York", "population": 834}]
file = "cities.csv"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex3.py
```

> 画面には何も表示しません。以下のファイルを生成します。

#### `cities.csv`

``` 
1,Tokyo,927
2,London,898
3,New York,834
```

---

## `file_ex4.py`

``` py
file = "cities.csv"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex4.py
1,Tokyo,927
2,London,898
3,New York,834
```

---

## `file_ex5.py`

``` py
file = "cities.csv"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex5.py
Tokyo
London
New York
```

---

## `file_ex6.py`

``` py
search_index = input("Input index: ")
file = "cities.csv"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex6.py
Input index: 1
Tokyo
$ python file_ex6.py
Input index: 2
London
$ python file_ex6.py
Input index: 10
```

> 存在しない `index` が入力された場合は何も表示しません。

---

## `file_ex7.py`

``` py
file = "cities.csv"

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python file_ex7.py
Total: 2659
Max: 927
```

> `cities.csv` の3列目の合計値と最大値を表示します。

---

### テキスト

* [テキスト - ファイルオブジェクト](../text/26_fileobject.md)
