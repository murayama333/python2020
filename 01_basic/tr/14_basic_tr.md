# トレーニング - パッケージ

## tr01

次の `mystats` パッケージがあります。

``` 
tr01
├── main.py
└── mystats
    ├── __init__.py
    ├── calc.py
    └── stats.py
```

#### `tr01/mystats/calc.py`

``` py
def add(x, y):
    return ???

def subtract(x, y):
    return ???
```

#### `tr01/mystats/stats.py`

``` py
def mean(*args):
    return ???
```

#### `tr01/mystats/__init__.py`

> ファイルの中身は空とします。

#### `tr01/main.py`

``` py
import mystats.calc
import mystats.stats

x = 100
y = 50
print(mystats.calc.add(x, y))
print(mystats.calc.subtract(x, y))
print(mystats.stats.mean(x, y))
```

次の実行結果となるようにPythonプログラム（ `calc.py` 、 `stats.py` ）を作成してください。

### 実行結果

``` 
$ cd tr01
$ python main.py
150
50
75.0
```

---

## tr02

次の `mystats` パッケージがあります。（tr01をコピーして作成します）

``` 
tr02
├── main.py
└── mystats
    ├── __init__.py
    ├── calc.py
    └── stats.py
```

> `__init__.py` 、 `calc.py` 、 `stats.py` に変更はありません。

#### `tr02/main.py`

``` py
???
???

x = 100
y = 50
print(cl.add(x, y))
print(cl.subtract(x, y))
print(st.mean(x, y))
```

次の実行結果となるようにPythonプログラム（ `main.py` ）を作成してください。

### 実行結果

``` 
$ cd tr02
$ python main.py
150
50
75.0
```

---

## tr03

次の `mystats` パッケージがあります。（tr02をコピーして作成します）

``` 
tr03
├── main.py
└── mystats
    ├── __init__.py
    ├── calc.py
    └── stats.py
```

> `__init__.py` 、 `calc.py` 、 `stats.py` に変更はありません。

#### `tr03/main.py`

``` py
???
???

x = 100
y = 50
print(add(x, y))
print(subtract(x, y))
print(mean(x, y))
```

次の実行結果となるようにPythonプログラム（ `main.py` ）を作成してください。

### 実行結果

``` 
$ cd tr03
$ python main.py
150
50
75.0
```

---

## tr04

次の `mystats` パッケージがあります。（tr03をコピーして作成します）

``` 
tr04
├── main.py
└── mystats
    ├── __init__.py
    ├── calc.py
    └── stats.py

1 directory, 4 files
```

> `__init__.py` 、 `main.py` を修正します。 `calc.py` 、 `stats.py` に変更はありません。

#### `tr04/mystats/__init__.py`

``` 
???
???
```

#### `tr04/main.py`

``` py
import mystats

x = 100
y = 50
print(mystats.calc.add(x, y))
print(mystats.calc.subtract(x, y))
print(mystats.stats.mean(x, y))
```

> `import mystats` と記述します。

次の実行結果となるようにPythonプログラム（ `__init__.py` ）を作成してください。

### 実行結果

``` 
$ cd tr04
$ python main.py
150
50
75.0
```

---

## tr05

次の `mystats` パッケージがあります。（tr04をコピーして作成します）

``` 
tr05
├── main.py
└── mystats
    ├── __init__.py
    ├── calc.py
    ├── report
    │   ├── __init__.py
    │   └── stats.py
    └── stats.py

2 directories, 6 files
```

> `report` フォルダ以下を追加し、 `mystats/__init__.py`  `mystats/main.py` を修正します。

#### `tr05/mystats/report/stats.py`

``` py
from .. import stats

def report(*args):
    ???
    ???
    ???
```

> `from .. import stats` と記述することで `mystats/stats.py` を `import` しています。

#### `tr05/mystats/report/__init__.py`

``` 
???
```

#### `tr05/mystats/__init__.py`

``` py
import mystats.calc
import mystats.stats
import mystats.report
```

> `import mystats.report` を追記します。

#### `tr05/main.py`

``` py
import mystats

x = 200
y = 100
print(mystats.calc.add(x, y))
print(mystats.calc.subtract(x, y))
print(mystats.stats.mean(x, y))
mystats.report.stats.report(x, y)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ cd tr05
$ python main.py
300
100
150.0
SUM: 300
CNT: 2
MEAN: 150.0
```

---

### テキスト

* [テキスト - パッケージ](../text/14_basic.md)
