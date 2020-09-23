# パッケージ

* パッケージは複数のモジュールファイルを組み合わせて管理する仕組み
* パッケージフォルダの中に `__init__.py` ファイルを配置する
* `__init__.py` ファイルは空のままでも動作する。またモジュールの `import` を管理することも可能

> python3.3から `__init__.py` ファイルを省略しても動作します。

---

## 01

以下のフォルダ構成に従ってファイルを作成します。

``` 
01
├── main.py
└── mypack
    ├── __init__.py
    ├── myfile1.py
    └── myfile2.py
```

#### `01/mypack/myfile1.py`

``` py
def hello():
    print("Hello")
```

#### `01/mypack/myfile2.py`

``` py
def world():
    print("World")
```

#### `01/mypack/__init__.py`

> ファイルの中身は空としておきます。

#### `01/main.py`

``` py
import mypack.myfile1
import mypack.myfile2

mypack.myfile1.hello()
mypack.myfile2.world()
```

### 実行

``` 
$ cd 01
$ python main.py
Hello
World
```

---

## 02

以下のフォルダ構成に従ってファイルを作成します。（ `01` フォルダをコピーします）

``` 
02
├── main.py
└── mypack
    ├── __init__.py
    ├── myfile1.py
    └── myfile2.py
```

#### `02/main.py`

``` py
import mypack.myfile1 as mf1
import mypack.myfile2 as mf2

mf1.hello()
mf2.world()
```

### 実行

``` 
$ cd ../02
$ python main.py
Hello
World
```

---

## 03

以下のフォルダ構成に従ってファイルを作成します。（ `02` フォルダをコピーします）

``` 
03
├── main.py
└── mypack
    ├── __init__.py
    ├── myfile1.py
    └── myfile2.py
```

#### `03/main.py`

``` py
from mypack.myfile1 import hello
from mypack.myfile2 import world

hello()
world()
```

### 実行

``` 
$ cd ../03
$ python main.py
Hello
World
```

---

## 04

以下のフォルダ構成に従ってファイルを作成します。（ `03` フォルダをコピーします）

``` 
04
├── main.py
└── mypack
    ├── __init__.py
    ├── myfile1.py
    └── myfile2.py
```

#### `04/mypack/__init__.py`

``` py
import mypack.myfile1
import mypack.myfile2
```

#### `04/main.py`

``` py
import mypack

mypack.myfile1.hello()
mypack.myfile2.world()
```

> `__init__.py` ファイルによって `import mypack` とするだけで、 `myfile1` や `myfile2` にアクセスできるようになります。

### 実行

``` 
$ cd ../04
$ python main.py
Hello
World
```

---

### 演習

* [エクササイズ - パッケージ](../ex/14_basic_ex.md)
