# エクササイズ - メソッド

## 課題 4.1 - `@classmethod` - クラスメソッド

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex13
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py

2 directories, 8 files
```

> `main.py` は完成しているので、 `sale.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py`

``` py
from mysales.sale import Sale

sale1 = Sale(800, 10)
sale2 = Sale(800, 10)
sale3 = Sale(800, 10)
print("Sale Count:", Sale.get_sale_count())
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:

    sale_count = 0

    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")
```

> プログラムが動作するように `Sale` クラスを修正してください。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
Sale Count: 3
```

---

## 課題 4.2 - `@staticmethod` - スタティックメソッド

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex14
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py

2 directories, 8 files
```

> `main.py` は完成しているので、 `sale.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py`

``` py
from mysales.sale import Sale

sale1 = Sale(800, 10)
sale2 = Sale(800, 10)
sale3 = Sale(800, 10)
print("Sale Count:", Sale.get_sale_count())
print("Now:", Sale.get_now())
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:

    sale_count = 0

    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")
```

> プログラムが動作するように `Sale` クラスを修正してください。現在日時を出力するには `datetime` モジュールをインポートし、 `datetime.datetime.now()` を呼び出します。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
Sale Count: 3
Now: 2020-10-02 10:48:15.079630
```

---

### テキスト

* [テキスト - メソッド](../text/04_method.md)
