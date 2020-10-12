# エクササイズ - 例外処理

## `ex_ex1.py`

``` py
# TODO try - except
x = 10
y = "20"
z = x + y
print(z)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python ex_ex1.py
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

> `try-except` 構文を追加して例外を捕捉するようにします。

---

## `ex_ex2.py`

``` py
while True:
    # TODO try - except
    x = int(input("Input: "))
    print(x)
    break
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python ex_ex2.py
Input: ABC
Input: DEF
Input: 100
100
```

> 数値以外の文字列を入力された場合は再入力できるようにします。

---

## `ex_ex3.py`

``` py
try:
    with open("not_exist.txt", "r") as f:
        print(f.read())
except ??? as e:
    print(e)
???:
    print("end")
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python ex_ex3.py
[Errno 2] No such file or directory: 'not_exist.txt'
end
```

#### `cities.csv`

``` 
1,Tokyo,927
2,London,898
3,New York,834
```

---

## `ex_ex4.py`

``` py
import io

try:
    with open("not_exist.txt", "w") as f:
        print(f.read())
except ??? as e:
    print(e)
???:
    print("end")
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python ex_ex4.py
not readable
end
```

> `w` でオープンしたファイルオブジェクトに対して `read` メソッドを呼び出しています。このようなケースでも例外が発生します。

---

## `ex_ex5.py`

``` py
# TODO class MyNotFoundError


# def search


fruits = ["Lemon", "Orange", "Grape", "Banana", "Peach"]
targets = ["Orange", "Apple", "Lemon"]

for target in targets:
    try:
        print(search(fruits, target))
    except MyNotFoundError as e:
        print(e)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python ex_ex5.py
Orange is found.
Apple is not found.
Lemon is found.
```

---

### テキスト

* [テキスト - 例外処理](../text/27_exception.md)
