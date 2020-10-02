# エクササイズ - オブジェクトの関連（処理の委譲）

## 課題 5.1 - オブジェクトの関連（処理の委譲）

`Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex15
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py

2 directories, 6 files
```

> `main.py` は完成しているので、 `sale.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py`

``` py
from mysales.sale import Sale, Customer, CustomerSale

customer = Customer("Customer A")
sale = Sale(800, 10)
customer_sale = CustomerSale(customer, sale)
customer_sale.print()
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


class Customer:
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(f"{self.__name}")

# TODO
```

> プログラムが動作するように `CustomerSale` クラスを作成してください。

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
Customer A
8,000
```

---

### テキスト

* [テキスト - オブジェクトの関連（処理の委譲）](../text/05_delegate.md)
