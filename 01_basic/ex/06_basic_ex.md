# エクササイズ - リスト

## list_ex1.php

次のリストがあります。

```python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex1.py 
22
20
25
20
18
```

### ヒント

```python
ages = [22, 20, 25, 20, 18]
for ??? in ???:
  print(???)
```

---


## list_ex2.php

次のリストがあります。

```python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex2.py
22
20
25
```

> リストのスライス指定を使ってみましょう。

---

## list_ex3.php

次のリストがあります。

```python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex3.py
22
25
18
```

> 要素番号が偶数（0, 2, 4）の要素のみ出力します。

### ヒント

```python
ages = [22, 20, 25, 20, 18]

for i in range(???, ???, ???):
  print(???)

```

---

## list_ex4.php

次のリストがあります。

```python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex4.py
105
```

> リストの要素の合計値を出力します。

### ヒント

```python
ages = [22, 20, 25, 20, 18]

total = 0
for age in ages:
  ??? = ??? + ???

print(total)
```

---

## list_ex5.php

次のリストがあります。

```python
ages = [22, 20, 25, 20, 18]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
> php list_ex4.php
25
```

> リストの要素の最大値を出力します。


### ヒント

```python
ages = [22, 20, 25, 20, 18]

max = 0
for age in ages:
  if ??? < ???:
    ??? = ???

print(max)
```

---

## list_ex6.php

次のリストがあります。

```python
names = ["Alice", "Bob"]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex6.py
['Alice', 'Bob', 'Charlie']
```

> "Charlie"を追加します。


### ヒント

```python
names = ["Alice", "Bob"]

# TODO append "Charlie"

print(names)
```

---

## list_ex7.php

次のリストがあります。

```python
names = ["Alice", "Bob"]
```

次の実行結果となるようにPHPプログラムを作成してください。

### 実行結果

```
$ python list_ex7.py 
['Bob', 'Alice']
```

> "Bob"と"Alice"と入れ替えます。

### ヒント

```python
names = ["Alice", "Bob"]

# TODO change names[0] names[1]

print(names)
```

---
