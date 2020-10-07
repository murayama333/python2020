# Python基礎 実力テスト - Part1

## `no01.py`

次のプログラムがあります。

``` py
count = 3
message = "Hello"
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Hello
Hello
Hello
```

---

## `no02.py`

次のプログラムがあります。

``` py
count = 3
message = "Hello"
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
1:Hello
2:Hello
3:Hello
```

---

## `no03.py`

次のプログラムがあります。

``` py
count = 10
message1= "Hello"
message2 = "World"
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Hello
World
Hello
World
Hello
World
Hello
World
Hello
World
```

> `count` に指定した回数分 `message1` と `message2` を交互に繰り返し表示します。

---

## `no04.py`

次のプログラムがあります。

``` 
number1 = 18
number2 = 12
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
GCD: 6
```

> `number1` と `number2` の最大公約数を求めます。

---

## `no05.py`

次のプログラムがあります。

``` 
number1 = 18
number2 = 12
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
LCM: 36
```

> `number1` と `number2` の最小公倍数を求めます。

---

## `no06.py`

次のプログラムがあります。

``` 
names = ["Andy", "Betty", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Carol
Betty
Andy
```

> リストの要素を後ろから順に表示します。

---

## `no07.py`

次のプログラムがあります。

``` 
names = ["Andy", "Betty", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
1:Andy
2:Betty
3:Carol
```

---

## `no08.py`

次のプログラムがあります。

``` py
names = ["Andy", "Betty", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Andy: 4
Betty: 5
Carol: 5
```

> リストの要素の文字数を表示します。

---

## `no09.py`

次のプログラムがあります。

``` py
names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Ellen
Betty
Diana
Fox
Helen
Andy
Ian
Glen
Carol
```

---

## `no10.py`

次のプログラムがあります。

``` py
names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Ellen,Betty,Diana
Fox,Helen,Andy
Ian,Glen,Carol
```

---

## `no11.py`

次のプログラムがあります。

``` py
scores = {"Math": 90, "English": 80, "Science": 70}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Math: 90
English: 80
Science: 70
```

---

## `no12.py`

次のプログラムがあります。

``` py
scores = {"Math": [90, 95, 100],
          "English": [80, 85, 90],
          "Science": [70, 75, 80]}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Math Total: 285
English Total: 255
Science Total: 225
```

---

## `no13.py`

次のプログラムがあります。

``` py
scores = {"Math": [90, 95, 100],
          "English": [80, 85, 90],
          "Science": [70, 75, 80]}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Total Score: 765
```

---

## `no14.py`

次のプログラムがあります。

``` py
scores = {"Math": [90, 95, 100],
          "English": [80, 85, 90],
          "Science": [70, 75, 80]}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
High Score: 100
```

---

## `no15.py`

次のプログラムがあります。

``` py
scores = {"Andy": (80, 90, 90),
          "Betty": (75, 85, 95),
          "Carol": (90, 70, 90),
          "Dave": (90, 90, 80)}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
High Score Andy: 260
High Score Dave: 260
```

> 合計点の最も高いデータを表示します。ただし、同点の場合は複数件表示します。

---

## `no16.py`

次のプログラムがあります。

``` py
students = {"A-class": ["Alice", "Bob"],
            "B-class": ["Andy", "Bob", "Carol"],
            "C-class": ["Carol", "Daniel", "Ellen"]}
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
A-class: 2
B-class: 3
C-class: 3
```

---

## `no17.py`

次のプログラムがあります。

``` py
# TODO def repeat function


message = "Hello"
print(repeat(message))
print(repeat(message, 5))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
HelloHello
HelloHelloHelloHelloHello
```

---

## `no18.py`

次のプログラムがあります。

``` py
# TODO def truncate funtion


messages = ["Hello", "Hello World", "This is a pen."]
for message in messages:
    print(truncate(message, 10))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Hello
Hello W...
This is...
```

> 文字列はリストのようにスライス指定で部分文字列を取得できます。

---

## `no19.py`

次のプログラムがあります。

``` py
# TODO def pad_left function


names = ["Andy", "Bob"]
for name in names:
    print(pad_left(name, 5))
    print(pad_left(name, 5, "*"))

```

実行結果のとおり出力してください。

＜実行結果＞

``` 
 Andy
*Andy
  Bob
**Bob
```

> 指定した文字数分、左側に空白や指定した記号を埋めます。

---

## `no20.py`

次のプログラムがあります。

``` py
# TODO def pair_list function


names1 = ["Andy", "Bob", "Carol"]
names2 = ["Alice", "Betty", "Charlie"]
print(pair_list(names1, names2))
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
[('Andy', 'Alice'), ('Bob', 'Betty'), ('Carol', 'Charlie')]
```
