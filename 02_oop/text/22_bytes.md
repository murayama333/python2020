# 組み込み型 - bytes型

## bytes型

### `bytes1.py`

``` py
i = 15
b = i.to_bytes(1, byteorder="big")
print(b)

bit_length = i.bit_length()
print(bit_length)
```

### 実行結果

``` 
$ python bytes1.py 
b'\x0f'
4
```

### 解説

* `int` 型の `to_bytes` メソッドは数値をバイト列に変換する
* `int` 型の `bit_length` メソッドは数値のビット長を取得する
* Pythonのバイト列は `b'\x01'` のように16進数で表記する

> バイトオーダー（ `byteorder` ）にはビッグエンディアン（ `big` ）、リトルエンディアン（ `little` ）２つの並び順がある

---

### `bytes2.py`

``` py
for i in range(256):
    print(i.to_bytes(1, byteorder="big"))
```

### 実行結果

``` 
$ python bytes2.py
b'\x00'
b'\x01'
b'\x02'
b'\x03'
b'\x04'
...省略
b'\xf8'
b'\xf9'
b'\xfa'
b'\xfb'
b'\xfc'
b'\xfd'
b'\xfe'
b'\xff'
```

### 解説

* 0〜255までの数値は1バイト（8bit）で表現できる

---

### `bytes3.py`

``` py
blist = bytes([1, 0])
print(blist)
print(int.from_bytes(blist, byteorder="big"))
```

### 実行結果

``` 
$ python bytes3.py
b'\x01\x00'
256
```

### 解説

* `int` 型の `from_bytes` メソッドはバイト列から数値を作成する
* `from_bytes`メソッドはクラスメソッドである
* バイト列は `bytes` 関数（コンストラクタ）でも生成できる

---

### `bytes4.py`

``` py
str = "Apple"
for s in str:
    print(s, s.encode("UTF-8").hex())
```

### 実行結果

``` 
$ python bytes4.py
A 41
p 70
p 70
l 6c
e 65
```

### 解説

* `str` 型の `encode` メソッドは指定した文字コードでバイト列（ `bytes` 型）に変換する
* `bytes` 型の `hex` メソッドは16進表記の文字列に変換する
* 文字ごとのコード値を確認できる

> 参考： https://ja.wikipedia.org/wiki/ASCII

---

### `bytes5.py`

``` py
blist = [0x41, 0x70, 0x70, 0x6c, 0x65]
bytes_data = bytes(blist)
# bytes_data = b"\x41\x70\x70\x6c\x65"
str = bytes_data.decode("UTF-8")
print(str)
```

### 実行結果

``` 
$ python bytes5.py
Apple
```

### 解説

* `bytes` 型の `decode` メソッドは指定した文字コードで文字列（ `str` 型）に変換する
* エンコードとは、データを元に戻せる形式で変換すること（符号化）
* デコードとは、符号化されたデータを復元すること

> Pythonの数値データは先頭に `0x` を付けることで16進数として処理できます。同様に2進数の場合は `0b` 、8進数の場合は `0o` を数値に先頭に記述します。

---

### `bytes6.py`

``` py
blist = [0x41, 0x70, 0x70, 0x6c, 0x65]
bytearray_data = bytearray(blist)

bytearray_data[0] = 0x61
str = bytearray_data.decode("UTF-8")
print(str)
```

### 実行結果

``` 
$ python bytes6.py 
apple
```

### 解説

* 変更可能なバイト列として `bytearray` 型が用意されている
* バイト列は要素番号でアクセスできる
* `bytes` 型はイミュターブル、 `bytearray` 型はミュータブルである

---

## 演習

* [エクササイズ - bytes型](../ex/22_bytes_ex.md)
