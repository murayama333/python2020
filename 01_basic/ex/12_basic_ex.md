# エクササイズ - 関数 - 関数の定義

## def_ex1.py

次の仕様に従って `subtract` 関数を作成してください。

|関数名|subtract|
|:--|:--|
|処理概要|引数xからyを減算した値を返す|
|引数|x, y|
|戻り値|xからy減算した値|

``` python
def subtract(x, y):
    # TODO

a = 100
b = 10
c = subtract(a, b)
print(c)

```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python def_ex1.py 
90
```

> subtractは"引き算"という意味です。

---

## def_ex2.py

次の仕様に従って `exclaim` 関数を作成してください。

|関数名|exclaim|
|:--|:--|
|処理概要|引数messageに"!!"を付けた値を出力する|
|引数|message|
|戻り値|なし|

``` python
def exclaim(message):
    # TODO

exclaim("Hello");

```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python def_ex2.py   
Hello!!
```

---

## def_ex3.py

次の仕様に従って `double` 関数を作成してください。

|関数名|double|
|:--|:--|
|処理概要|引数xを2倍した値を返す|
|引数|x|
|戻り値|xを2倍した値|

``` python
# TODO define double function

value = 100
result = double(value)
print(result)
```

次の実行結果となるようにpythonプログラムを作成してください。

### 実行結果

``` 
$ python def_ex3.py
200
```

---

## def_ex4.py

次の仕様に従って `array_double` 関数を作成してください。

|関数名|array_double|
|:--|:--|
|処理概要|引数arrayの要素を2倍にした配列を返す|
|引数|array 配列データとする|
|戻り値|arrayの要素を2倍にした配列|

``` python
# TODO array_double function

prices = [100, 200, 300]
result = array_double(prices)
print(result)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python def_ex4.py
[200, 400, 600]
```

---

## def_ex5.py

次の仕様に従って `factorial` 関数を作成してください。

|関数名|factorial|
|:--|:--|
|処理概要|引数xの階乗を返す|
|引数|x|
|戻り値|引数xの階乗|

> x = 5のときの階乗は5 x 4 x 3 x 2 x 1 = 120

``` python
# TODO define facorial function

x = 5
y = factorial(x)
print(y)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
$ python def_ex5.py
120
```

---

### テキスト

* [テキスト - 関数 - 関数の定義](../text/12_basic.md)
