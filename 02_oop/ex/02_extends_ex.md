# エクササイズ - 継承

## 課題 2.1 - 継承

`Sale` クラスを継承した `DailySale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex05
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py

2 directories, 8 files
```

> `main.py` は完成しているので、 `sale.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import DailySale

sale = DailySale(800, 10)
print(sale.get_date())
print(sale.calc())
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
2020-09-29
8000
```

> 出力の日付部分は変化します。

### `mysales/sale.py`

``` py
import datetime

class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")

# TODO DailySale class
```

> `datetime` モジュールを `import` して、 `datetime.date.today()` と呼び出すことでシステム日付（コンピュータから取得する現在の日付）を取得できます。

---

## 課題 2.2 - メソッドのオーバーライド

`Sale` クラスの `print` メソッドを `DailySale` クラスでオーバーライドします。
 
以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex06
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import DailySale

sale = DailySale(800, 10)
sale.print()
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
2020-09-29 8,000
```

### `mysales/sale.py`

``` py
import datetime

class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")

class DailySale(Sale):
    def get_date(self):
        return datetime.date.today()

    def print(self):
        # TODO 
        pass
```

---

## 課題 2.3 - `super()` 呼び出し

 
`DailySale` クラスの `__init__` メソッド追加します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex07
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
import datetime
from mysales.sale import DailySale

sale = DailySale(800, 10)
sale.print()

date = "2020-10-01"
date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
sale = DailySale(1000, 5, date)
sale.print()
```

> `datetime.datetime.strptime(date, "%Y-%m-%d").date()` 呼び出しは `"2020-10-01"` 文字列を `date` 型オブジェクトに変換しています。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
2020-09-29 8,000
2020-10-01 5,000
```

### `mysales/sale.py`

``` py
import datetime

class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")

class DailySale(Sale):
    def __init__(self, price, count, date=None):
        # TODO 
        pass

    def get_date(self):
        return self.date

    def print(self):
        print(f"{self.get_date()} {self.calc():,d}")

```

> `__init__` メソッドでは第4引数の `date` が省略された場合は、 `date` 変数に現在日付を代入します。現在日付は `datetime.date.today()` によって取得できます。

---

### テキスト

* [テキスト - 継承](../text/02_extends.md)
