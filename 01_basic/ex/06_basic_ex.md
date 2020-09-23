# エクササイズ - データ構造 - リスト

## list_ex1.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex1.py 
25
```

> 前から3番目の要素を出力します。

---

## list_ex2.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex2.py 
22
20
25
20
18
```

### ヒント

``` python
ages = [22, 20, 25, 20, 18]
for ??? in ???:
    print(???)
```

---

## list_ex3.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex3.py 
5
```

> リストの要素数を出力します。

---

## list_ex4.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex4.py
22
20
25
```

> リストのスライス指定を使ってみましょう。

---

## list_ex5.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex5.py
22
25
18
```

> 要素番号が偶数（0, 2, 4）の要素のみ出力します。

### ヒント

``` python
ages = [22, 20, 25, 20, 18]

for i in range(???, ???, ???):
    print(???)
```

---

## list_ex6.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex6.py
105
```

> リストの要素の合計値を出力します。

### ヒント

``` python
ages = [22, 20, 25, 20, 18]
total = 0
for age in ages:
    ??? = ??? + ???
print(total)
```

---

## list_ex7.py

次のリストがあります。

``` python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex7.py
25
```

> リストの要素の最大値を出力します。

### ヒント

``` python
ages = [22, 20, 25, 20, 18]

max = 0
for age in ages:
    if ??? < ???:
        ??? = ???

print(max)
```

---

## list_ex8.py

次のリストがあります。

``` python
names = ["Alice", "Bob"]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex8.py
['Alice', 'Bob', 'Charlie']
```

> "Charlie"を追加します。

### ヒント

``` python
names = ["Alice", "Bob"]

# TODO append "Charlie"

print(names)
```

---

## list_ex9.py

次のリストがあります。

``` python
names = ["Alice", "Bob"]
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python list_ex9.py 
['Bob', 'Alice']
```

> "Bob"と"Alice"と入れ替えます。

### ヒント

``` python
names = ["Alice", "Bob"]

# TODO change names[0] names[1]

print(names)
```

---

### テキスト

* [テキスト - データ構造 - リスト](../text/06_basic.md)
