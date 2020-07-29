# トレーニング - 関数 - 組み込み関数

## `func_tr1.py`

次のプログラムがあります。

``` python
number_list = [70, -45, -80, 75]

# TODO
```

組み込み関数を使って、次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Sum: 20
Max: 75
Min: -80
Avg: 5
```

---

## `func_tr2.py`

次のプログラムがあります。

``` python
price1 = "100"
price2 = "200"
price3 = "300"

# TODO
```

* 変数 `price1` 、 `price2` 、 `price3` には文字列型（`str`型）のデータが代入されています。
* 変数 `price1` 、 `price2` 、 `price3`を整数型（`int`型）に変換して合計値を求めます。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Sum: 600
```

---

## `func_tr3.py`

次のプログラムがあります。

``` python
number_list = [70, -45, -80, 75]

# TODO
```

* 変数 `number_list` の要素の絶対値について合計を求めます。

組み込み関数を使って、次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Abs Max: 80
```

---

## `func_tr4.py`

次のプログラムがあります。

``` python
numbers_tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))

# TODO
```

* 変数 `number_tuple` の要素の合計値を求めます。

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
450
```

---


## `func_tr5.py`

次のプログラムがあります。

``` python
alphabets = ["A", "B", "C", "D", "E"]
r_alphabets = [a for a in ???(alphabets)]
print(r_alphabets)
```

+ 組み込みを使って、リスト型の変数`alphabets`の要素の並びを逆順にします。
+ ここでは以下のいずれかの組み込み関数を使います。
  + abs()
  + set()
  + sum()
  + range()
  + reversed()


次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
['E', 'D', 'C', 'B', 'A'] 
```

---

## `func_tr6.py`

次のプログラムがあります。

``` python
number = int(input("Number: "))
print(???(number))
print(???(number))
print(???(number))
```

+ 組み込みを使って、変数`number`の値を2進数、8進数、16進数表記で出力します。
+ ここでは以下のいずれかの組み込み関数を使います。
  + abs()
  + bin()
  + hex()
  + max()
  + oct()

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

+ `15`を入力した場合

```
Number: 15
0b1111
0o17
0xf
```

+ `16`を入力した場合

```
Number: 16
0b10000
0o20
0x10
```

+ `17`を入力した場合

```
Number: 17
0b10001
0o21
0x11
```

---

### テキスト

* [テキスト - 関数 - 組み込み関数](../text/11_basic.md)
