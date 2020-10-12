# ファイルオブジェクト

## ファイルオブジェクト

> Pythonでは `open` 関数によって返却されるオブジェクトをファイルオブジェクトと呼びます。Python3の場合、open関数の戻り値の実体は `<class '_io.TextIOWrapper'>` です。

### `file1.py`

``` py
names = ["Alice", "Bob", "Charlie"]
f = open("names.txt", mode="w")
for name in names:
    f.write(name + "\n")
f.close()
```

### 実行結果

``` 
$ python file1.py
```

> 画面には何も表示されません。カレントフォルダ上に以下のような `names.txt` ファイルが生成されます。

``` 
Alice
Bob
Charlie
```

### 解説

* `open` 関数によってファイルオブジェクトを生成する
* ファイルオブジェクトの `write` メソッドは引数に指定したデータをファイルに書き込む
* ファイルオブジェクトの `close` メソッドはオープンしたファイルを解放する

> `open` 関数は第1引数にファイル名、第2引数にモード（ `"r"：読み込みモード` 、 `"w"` ：書き込みモードなど）を指定します。

---

### `file2.py`

``` py
f = open("names.txt", mode="r")
str = f.read()
f.close()
print(str)
```

### 実行結果

``` 
$ python file2.py
Alice
Bob
Charlie

```

### 解説

* ファイルオブジェクトの `read` メソッドはファイルの中身を全て読み込む
* `read` メソッドはファイルの内容を `str` 型で返却する

> OSの中でオープン可能なファイル数には上限があります。不要になったファイルは `close` メソッドで閉じるようにします。

---

### `file3.py`

``` py
f = open("names.txt", mode="r")
lines = f.readlines()
f.close()
for line in lines:
    print(line)
```

### 実行結果

``` 
$ python file3.py
Alice

Bob

Charlie

```

### 解説

* ファイルオブジェクトの `readlines` メソッドはファイルの中の各行を `list` 型で取得する
* ファイルの各行の末端の改行コードも取得する点に注意する
* 同様にファイルオブジェクトの `readline` メソッドはファイルの中の1行を `str` 型で取得する

> 行の終端改行コードを除去する場合は `str` 型の `rstrip` メソッドなどを使います。

---

### `file4.py`

``` py
f = open("names.txt", mode="r")
print(f.read(1))
f.seek(6)
print(f.read(1))
f.seek(10)
print(f.read(1))
f.close()
```

### 実行結果

``` 
$ python file4.py
A
B
C
```

### 解説

* ファイルオブジェクトの `read` メソッドは現在のファイルオブジェクトの位置から1文字を読み込む
* ファイルオブジェクトの `seek` メソッドはファイルオブジェクトの位置を移動する

> ファイルオブジェクトは内部にファイル内のデータを指し示す位置情報を保持しています。 `read` メソッドや `readline` メソッドは呼び出す度にファイルオブジェクト内の位置情報が移動するようになっています。

---

### `file5.py`

``` py
with open("names.txt", mode="r") as f:
    print(f.read())
```

### 実行結果

``` 
$ python file5.py
Alice
Bob
Charlie
```

### 解説

* `with` キーワードでファイルオブジェクトのクローズ処理を自動化できる
* `with` ブロック内で例外が発生した場合もファイルはクローズされる

---

## 演習

* [エクササイズ - ファイルオブジェクト](../ex/26_fileobject_ex.md)
