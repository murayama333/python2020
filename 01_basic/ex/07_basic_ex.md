# エクササイズ - データ構造 - ディクショナリ

## dict_ex1.py

次の連想配列があります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex1.py
200
```

---

## dict_ex2.py

次の連想配列があります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex2.py
Apple
Banana
Cherry
```

---

## dict_ex3.py

次の連想配列があります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
for key in fruits.values():
    print(key)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex3.py
100
200
300
```

---

## dict_ex4.py

次のディクショナリがあります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex4.py
3
```

> ディクショナリの要素数を出力します。

---

## dict_ex5.py

次のディクショナリがあります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex5.py
600
```

> ディクショナリの要素の合計値を出力します。

---

## dict_ex6.py

次のディクショナリがあります。

``` python
fruits = {"Apple": 100, "Banana": 200, "Cherry": 300}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex6.py
200
```

> ディクショナリの要素の平均値を出力します。小数点以下は切り捨てとします。

---

## dict_ex7.py

次のディクショナリがあります。

``` python
fruits = {
    "Apple": {"price": 100, "color": "Red"},
    "Banana": {"price": 200, "color": "Yellow"},
    "Cherry": {"price": 300, "color": "Red"},
}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex7.py
Apple
Cherry
```

> `color` キーの値が `"Red"` のものだけ出力します。

### ヒント

``` python
fruits = {
    "Apple": {"price": 100, "color": "Red"},
    "Banana": {"price": 200, "color": "Yellow"},
    "Cherry": {"price": 300, "color": "Red"},
}

for key, value in fruits.???:
    if ??? == ???:
        print(key)
```

---

## dict_ex8.py

次のディクショナリがあります。

``` python
fruits = {
    "Apple": {"price": 100, "color": "Red"},
    "Banana": {"price": 200, "color": "Yellow"},
    "Cherry": {"price": 300, "color": "Red"},
}
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex8.py
400
```

> `color` キーの値が `"Red"` の合計値 `400` を出力します。

---

### テキスト

* [テキスト - データ構造 - ディクショナリ](../text/07_basic.md)
