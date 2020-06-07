# 変数と演算子

### var1.py

```python
price = 200
count = 5
total = price * count
message = "TOTAL PRICE"

print(message)
print(total)
```

### 実行

```
$ python var1.py
TOTAL PRICE
1000
```

### 解説

+ 変数には整数や文字列といったデータを代入できる
+ 文字列データは`""`あるいは`''`で囲む
+ 算術演算子(`+, - , *, /, %`)が利用できる

---

### var2.py

```python
count = 1
count = count + 1

print(count)
```

### 実行

```
$ python var2.py
2
```

### 解説

+ 1つのステートメントに同じ名前の変数を利用できる
+ 変数の値を1増やすことをインクリメントと呼ぶ
+ Pythonには`++`のインクリメント演算子は用意されていない

---

### var3.py

```
number = 10
p = number > 0
n = number < 0

print(p)
print(n)
```

### 解説

+ 比較演算子（`>, >=, ==, <=, <, !=`）によって2つの値を比較できる
+ 比較演算子の評価結果は真理値型（`True`, `False`）となる
+ 真理値型は後で学習する制御構文で利用する

### 外部リンク

+ [組み込み型 - 比較](https://docs.python.org/ja/3/library/stdtypes.html#comparisons)


---

### 演習

+ [エクササイズ - 変数と演算子](ex/02_basic_ex.md)
