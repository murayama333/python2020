# エクササイズ - データ属性とカプセル化

## 課題 3.1 - データ属性

`Sale` クラスを呼び出す `main.py` ファイルを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex08
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py

2 directories, 8 files
```

> `sale.py` は完成しているので、 `main.py` を作成します。 `__init__.py` は空のファイルです。

### `mysales/sale.py`

``` py
class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")
```

### main.py

``` py
from mysales.sale import Sale

sale = Sale(800, 10)
sale.price = 1000
sale.count = 20
sale.print()
print(sale.???)
print(sale.???)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
20,000
1000
20
```

---

## 課題 3.2 - マングリング

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex09
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

sale = Sale(800, 10)
sale._Sale__price = 1000
sale._Sale__count = 20
sale.print()
print(sale._Sale__price)
print(sale._Sale__count)
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")
```

> プログラムが動作するように `Sale` クラスを修正してください。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
20,000
1000
20
```

---

## 課題 3.3 - Getter/Setter

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex10
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

sale = Sale(800, 10)
sale.set_price(1000)
sale.set_count(20)
sale.print()
print(sale.get_price())
print(sale.get_count())
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:
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
20,000
1000
20
```

---

## 課題 3.4 - プロパティ

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex11
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

sale = Sale(800, 10)
sale.price = 1000
sale.count = 20
sale.print()
print(sale.price)
print(sale.count)
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count
```

> プログラムが動作するように `Sale` クラスを修正してください。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
20,000
1000
20
```

---

## 課題 3.5 - `@property` デコレータ

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex12
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

sale = Sale(800, 10)
sale.price = 1000
sale.count = 20
sale.print()
print(sale.price)
print(sale.count)
```

### `mysales/sale.py`

``` py
# TODO 修正
class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count

    price = property(get_price, set_price)
    count = property(get_count, set_count)
```

> プログラムが動作するように `Sale` クラスを修正してください。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
20,000
1000
20
```

---

### テキスト

* [テキスト - データ属性とカプセル化](../text/03_capsule.md)
