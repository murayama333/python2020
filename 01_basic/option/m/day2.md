# Python基礎 実力テスト - Part2

## `no21.py`

次のプログラムがあります。

``` py
start = 5
end = 10
total = 0
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Total: 45
```

> `start` から `end` までの合計値を求めます。

---

## `no22.py`

次のプログラムがあります。

``` py
rows = 5
columns = 9
symbol = "*"
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
*********
*********
*********
*********
*********
```

> `rows` x `columns` の個数分 `symbol` を表示します。

---

## `no23.py`

次のプログラムがあります。

``` py
rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

> 偶数列の出力を空白（ `symbol2` ）にします。

---

## `no24.py`

次のプログラムがあります。

``` py
rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
**** ****
**** ****
**** ****
**** ****

**** ****
**** ****
**** ****
**** ****
```

> 行と列の中央を空白（ `symbol2` ）にします。

---

## `no25.py`

次のプログラムがあります。

``` py
rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
 ******* 
* ***** *
** *** **
*** * ***
**** ****
*** * ***
** *** **
* ***** *
 ******* 
```

`X` の部分を空白（ `symbol2` ）にします。

---

## `no26.py`

次のプログラムがあります。

``` py
names = ["Andy", "Betty", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
And
Bet
Car
```

> 名前を先頭から3文字まで表示します。文字列はリストのようにスライス指定で部分文字列を取得できます。

---

## `no27.py`

次のプログラムがあります。

``` py
names = ["Andy", "Betty", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Andy,Betty,Carol
```

---

## `no28.py`

次のプログラムがあります。

``` py
names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
1:Ellen
2:Betty
3:Diana
4:Fox
5:Helen
6:Andy
7:Ian
8:Glen
9:Carol
```

---

## `no29.py`

次のプログラムがあります。

``` py
names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
end_with = "n"
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Ellen
Helen
Ian
Glen
```

> `names_list` の要素である文字列の末尾が `end_with` で終わっているものだけを表示します。

---

## `no30.py`

次のプログラムがあります。

``` py
names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Andy
Betty
Carol
Diana
Ellen
Fox
Glen
Helen
Ian
```

> 辞書順でソートして表示します。

---

## `no31.py`

次のプログラムがあります。

``` py
scores = {"Math": 90, "English": 80, "Science": 70}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Total: 240
```

---

## `no32.py`

次のプログラムがあります。

``` py
names = ["Andy", "Betty", "Carol"]
scores = [80, 90, 100]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
{'Andy': 80, 'Betty': 90, 'Carol': 100}
```

> `names` リストをキー、 `scores` リストを値に持つディクショナリを作ります。

---

## `no33.py`

次のプログラムがあります。

``` py
names = ["Alice", "Bob", "Andy", "Bob", "Carol", "Carol", "Daniel", "Ellen"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Alice', 'Andy', 'Bob', 'Carol', 'Daniel', 'Ellen']
```

> 重複するデータを除去します。また辞書順で表示します。

---

## `no34.py`

次のプログラムがあります。

``` py
students = {"A-class": ["Alice", "Bob"],
            "B-class": ["Andy", "Bob", "Carol"],
            "C-class": ["Carol", "Daniel", "Ellen"]}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Alice', 'Andy', 'Bob', 'Carol', 'Daniel', 'Ellen']
```

> 重複するデータを除去します。また辞書順で表示します。

---

## `no35.py`

次のプログラムがあります。

``` py
# TODO def palindrome function

messages = ["txt", "html", "level"]
for message in messages:
    print(message, palindrome(message))

```

> `palindrome` とは回文という意味です。

実行結果のとおり出力してください。

＜実行結果＞

``` 
txt True
html False
level True
```

> 文字列の並び順を反転するには `str[::-1]` のようにスライス指定します。

---

## `no36.py`

次のプログラムがあります。

``` py
# TODO def pad_right function

names = ["Andy", "Bob"]
for name in names:
    print(pad_right(name, 5))
    print(pad_right(name, 5, "*"))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Andy 
Andy*
Bob  
Bob**
```

> 指定した文字数分、右側に空白や指定した記号を埋めます。

---

## `no37.py`

次のプログラムがあります。

``` py
# TODO def append_list function

names1 = ["Andy", "Bob", "Carol"]
names2 = ["Alice", "Betty", "Charlie"]
print(append_list(names1, names2))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Andy', 'Bob', 'Carol', 'Alice', 'Betty', 'Charlie']
```

---

## `no38.py`

次のプログラムがあります。

``` py
# TODO def flat_list function

names = [["Andy", "Bob", "Carol"], ["Alice", "Betty", "Charlie"]]
print(flat_list(names))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Andy', 'Bob', 'Carol', 'Alice', 'Betty', 'Charlie']
```

2次元配列を1次元の配列に変換します。

---

## `no39.py`

次のプログラムがあります。

``` py
# TODO def unique_list function

names = ["Andy", "Bob", "Carol", "Bob"]
print(unique_list(names))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Andy', 'Bob', 'Carol']
```

> 重複を除いたリストに変換します。リストの要素は辞書順とします。

---

## `no40.py`

次のプログラムがあります。

``` py
# TODO def contains function

names = ["Andy", "Bob", "Carol"]
print(names)
print("Bob:", contains(names, "Bob"))
print("Dave:", contains(names, "Dave"))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Andy', 'Bob', 'Carol']
Bob: True
Dave: False
```

> 指定した名前が、 `names` リストの中に存在する場合は `True` そうでない場合は `False` を表示します。

---
