# エクササイズ - クラスとインスタンス

## 課題 1.1 - クラスとインスタンス

売上を表す `Sale` クラスを作成します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex01
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `sale.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import Sale

sale = Sale()
print(sale)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
<mysales.sale.Sale object at 0x10368d040>
```

### `mysales/sale.py`

``` py
# TODO
```

---

## 課題 1.2 - メソッド

`Sale` クラスには売上額を計算する `calc` メソッド、売上額を出力する `print` メソッド、を定義します。
 
以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex02
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import Sale

sale = Sale()
print(sale.calc())
sale.print()
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
0
0
```

### `mysales/sale.py`

``` py
class Sale:
    # TODO
```

> `0` を返却する `calc` メソッド、 `0` を出力する `print` メソッドの2つを定義します。

---

## 課題 1.3 - データ属性

 
`Sale` クラスに `price` （販売価格） と `count` （販売個数）の２つのデータ属性を定義します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex03
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import Sale

sale = Sale()
print(sale.calc())
sale.print()
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
8000
8,000
```

### `mysales/sale.py`

``` py
class Sale:
    def __init__(self):
        self.price = 800
        self.count = 10

    # TODO

```

> `self.price * self.count` の結果を返却する `calc` メソッド、 `self.price * self.count` の結果を3桁カンマ表示で出力する `print` メソッドの2つを定義します。

---

## 課題 1.4 - `__init__` メソッド

 
`Sale` クラスに `__init__` メソッドを定義します。

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
ex04
├── main.py
└── mysales
    ├── __init__.py
    └── sale.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

### `main.py` - 実装済み

``` py
from mysales.sale import Sale

sale = Sale(800, 10)
print(sale.calc())
sale.print()
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python main.py
8000
8,000
```

### `mysales/sale.py` - 実装済み

``` py
class Sale:
    # TODO
```

---

### テキスト

* [テキスト - クラスとインスタンス](../text/01_class.md)
