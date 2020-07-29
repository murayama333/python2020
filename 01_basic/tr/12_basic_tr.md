# トレーニング - 関数 - 関数の定義

## `def_tr1.py`

次の仕様に従って `add` 関数を作成してください。

|関数名|add|
|:--|:--|
|処理概要|引数x, y, zを加算した値を返す|
|引数|x, y, z|
|戻り値|引数x, y, zを加算した値|

``` python
def add(x, y, z):
    # TODO

a = 10
b = 20
c = 30
d = add(a, b, c)
print(d)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
60
```

---

## `def_tr2.py`

次の仕様に従って `calc_rect_area` 関数を作成してください。

|関数名|calc_rect_area|
|:--|:--|
|処理概要|引数width, heightから矩形（長方形）の面積を計算して返す|
|引数|width, height|
|戻り値|矩形の面積|

> 矩形とはすべての角が直角の四角形です。

``` python
def calc_rect_area(width, height):
    # TODO


w = 10
h = 10
area = calc_rect_area(w, h)
print(area)

area = calc_rect_area(20, 30)
print(area)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
100
600
``` 

---

## `def_tr3.py`

次の仕様に従って `calc_circle_area` 関数を作成してください。

|関数名|calc_circle_area|
|:--|:--|
|処理概要|引数radiusから円の面積を計算して返す|
|引数|radius 半径|
|戻り値|円の面積|

``` python
def calc_circle_area(radius):
    # TODO


r = 5
area = calc_circle_area(5)
print(area)

r = 10
area = calc_circle_area(10)
print(area)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
78
314
```

---

## `def_tr4.py`

次の仕様に従って `average` 関数を作成してください。

|関数名|average|
|:--|:--|
|処理概要|引数number_listの平均値を返す<br>ただし、引数が空の配列の場合は0を返す|
|引数|number_list|
|戻り値|引数number_listの平均値|

``` python
def average(number_list):
    # TODO


score_list = [70, 60, 90, 80, 100]
avg = average(score_list)
print(avg)

score_list = []
avg = average(score_list)
print(avg)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
80
0
```

---

## `def_tr5.py`

次の仕様に従って `show_list_info` 関数を作成してください。

|関数名|show_list_info|
|:--|:--|
|処理概要|引数number_listについて、要素数、合計値、最大値、最小値を表示する|
|引数|number_list|
|戻り値|なし|

``` python
def show_list_info(number_list):
    # TODO


number_list = [70, -45, -80, 75]
show_list_info(number_list)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
Len: 4
Sum: 20
Max: 75
Min: -80
```

---

## `def_tr6.py`

次の仕様に従って `abs_sum` 関数を作成してください。

|関数名|abs_sum|
|:--|:--|
|処理概要|引数number_listについて、要素の絶対値の合計値を返す|
|引数|x, y, z|
|戻り値|要素の絶対値の合計値|

``` python
def abs_sum(number_list):
    # TODO


numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
print(abs_sum(numbers))
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

```
45
```

---

### テキスト

* [テキスト - 関数 - 関数の定義](../text/12_basic.md)
