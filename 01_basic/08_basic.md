# データ構造 - セット

### set1.py

+ セットは重複データを許さないコレクション
+ Pythonのセットは`{}`の中に要素を並べて記述する
+ セットはリストのように要素番号を指定することができない

```python
cities = {"Red", "Blue", "Green", "Red"}
print(cities)
```

### 実行

```
$ python set1.py
{'Red', 'Green', 'Blue'}
```

---

### set2.py

+ セットの要素数を求めるには`len`関数を使う

```python
cities = {"Red", "Blue", "Green", "Red"}
length = len(cities)
print(length)
```

### 実行

```
$ python set2.py 
3
```

---


### set3.py

+ セットは`for`文で処理することもできる

```python
cities = {"Red", "Blue", "Green", "Red"}
for city in cities:
    print(city)
```

### 実行

```
$ python set3.py
Green
Red
Blue
```

> 出力順序が定義順やアルファベット順でない点に注意してください。

---

### set4.py

+ 空のセット変数は`set`関数で作成する
+ `{}`リテラルは空のディクショナリを意味する
+ セット型の変数は`add`メソッドで要素を追加する

```python
cities = set()
cities.add("Red")
cities.add("Green")
cities.add("Red")
for city in cities:
    print(city)
```

### 実行

```
$ python set4.py
Red
Green
Yellow
Blue
```

---

### set5.py

+ `set`型の変数は`if`文の`in`句に指定できる

```python
cities = {"Red", "Blue", "Green"}
if "Blue" in cities:
    print("Found")
else:
    print("Not Found")
```

### 実行

```
$ python set5.py
Found
```

---

### 演習

+ [エクササイズ - データ構造 - セット](ex/08_basic_ex.md)
