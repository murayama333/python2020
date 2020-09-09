# データ構造 - セット

### `set1.py`

``` python
colors = {"Red", "Blue", "Green", "Red"}
print(colors)
```

### 実行

``` 
$ python set1.py
{'Red', 'Green', 'Blue'}
```

> セットの要素の取り出し順序は一定ではありません。実行結果の出力順序は上記と異なる場合があります。


### 解説

* セットは重複データを許さないコレクション
* Pythonのセットは `{}` の中に要素を並べて記述する
* セットはリストのように要素番号を指定することができない


---

### `set2.py`

``` python
colors = {"Red", "Blue", "Green", "Red"}
length = len(colors)
print(length)
```

### 実行

``` 
$ python set2.py 
3
```

### 解説

* セットの要素数を求めるには `len` 関数を使う

---

### `set3.py`

``` python
colors = {"Red", "Blue", "Green", "Red"}
for color in colors:
    print(color)
```

### 実行

``` 
$ python set3.py
Green
Red
Blue
```

> 出力順序が定義順やアルファベット順でない点に注意してください。

### 解説

* セットは `for` 文で処理することもできる

---

### `set4.py`

``` python
colors = set()
colors.add("Red")
colors.add("Green")
colors.add("Red")
for color in colors:
    print(color)
```

### 実行

``` 
$ python set4.py
Red
Green
Yellow
Blue
```

### 解説

* 空のセット変数は `set` 関数で作成する
* `{}` リテラルは空のディクショナリを意味する
* セット型の変数は `add` メソッドで要素を追加する

---

### `set5.py`

``` python
colors = {"Red", "Blue", "Green"}
if "Blue" in colors:
    print("Found")
else:
    print("Not Found")
```

### 実行

``` 
$ python set5.py
Found
```

### 解説

* `set` 型の変数は `if` 文の `in` 句に指定できる

---

### 演習

* [エクササイズ - データ構造 - セット](../ex/08_basic_ex.md)
