# 組み込み型 - list型

## list型

### `list1.py`

``` py
my_list = ["A", "B", "D"]
my_list.insert(2, "C")
print(my_list)
my_list.append("E")
print(my_list)
```

### 実行結果

``` 
$ python list1.py 
['A', 'B', 'C', 'D']
['A', 'B', 'C', 'D', 'E']
```

### 解説

* `list` 型の `insert` メソッドはリストの指定した位置に要素を追加する
* `list` 型の `append` メソッドはリストの終端に要素を追加する

---

### `list2.py`

``` py
my_list = ["A", "B", "C", "D", "E"]
print(my_list)

my_list.pop()
print(my_list)

del my_list[1]
print(my_list)

my_list.remove("C")
print(my_list)

my_list.clear()
print(my_list)
```

### 実行結果

``` 
$ python list2.py
['A', 'B', 'C', 'D', 'E']
['A', 'B', 'C', 'D']
['A', 'C', 'D']
['A', 'D']
[]
```

### 解説

* `list` 型の `pop` メソッドはリストの終端の要素を取り出す（取り出した要素はリストから削除される）
* `del` 文によってリストの要素を削除できる
* `remove` メソッドはリストから指定した要素を削除し、 `clear` メソッドはリスト内のすべての要素を削除する

---

### `list3.py`

``` py
my_list1 = [1, 3, 3, 2, 3, 2]
print(3 in my_list1)
print(my_list1.count(3))
```

### 実行結果

``` 
$ python list3.py
True
3
```

### 解説

* リストの中に指定した要素が含まれているかを判定するには `in` キーワードを使う
* `list` 型の `count` メソッドは引数に指定した要素が、リスト内に存在する個数を返却する

---

### `list4.py`

``` py
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
print(my_list1 + my_list2)
print(my_list1 * 3)
```

### 実行結果

``` 
$ python list4.py
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 解説

* Pythonのリストは `+` 演算子で連結できる
* Pythonのリストは `*` 演算子で繰り返し連結できる

---

### `list5.py`

``` py
my_list = ["D", "B", "A", "E", "C"]
print(my_list)

copy_my_list = my_list.copy()
print(copy_my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)
```

### 実行結果

``` 
$ python list5.py
['D', 'B', 'A', 'E', 'C']
['D', 'B', 'A', 'E', 'C']
['A', 'B', 'C', 'D', 'E']
['E', 'D', 'C', 'B', 'A']
```

### 解説

* `list` 型の `copy` メソッドはリストをコピーする（浅いコピー：Shallow Copy）
* `list` 型の `sort` メソッドはリストオブジェクトそのものをソートする
* `list` 型の `reverse` メソッドはリストオブジェクトそのものを反転する

---

## 演習

* [エクササイズ - list型](../ex/23_list_ex.md)
