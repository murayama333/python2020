# エクササイズ - モジュール

##  mod_ex1.py

### figure.py

* 図形の面積を求める `figure.py` モジュールを作成します。
  + `triangle` : 三角形の面積を求める
  + `rectangle` : 三角形の面積を求める
  + `circle` : 三角形の面積を求める

``` python
"""
図形の面積を求める
"""

def triangle(width, height):
    """
    三角形の面積を求める
    """
    return int(width * height * 0.5)

def rectangle(width, height):
    """
    矩形の面積を求める
    """
    return width * height

def circle(radius):
    """
    円の面積を求める
    """
    return int(radius * radius * 3.14)
```

> `"""` で囲まれているコメントは `docstring` と呼ばれる特殊なコメントです。モジュールや関数、後で学習するクラスの説明のために記述します。

次の実行結果となるようにPythonプログラムを作成してください。

#### mod_ex1.py

``` python
import figure

x = 10
y = 10

area = ???.???(x, y)
print("Triangle:", area)

area = ???.???(x, y)
print("Rectangle:", area)

area = ???.???(x / 2)
print("Circle:", area)
```

### 実行結果

``` 
Triangle: 50
Rectangle: 100
Circle: 78
```

---

## mod_ex2.py

次の実行結果となるようにPythonプログラムを作成してください。

#### mod_ex2.py

``` python
import figure as ???

x = 10
y = 10

area = fig.triangle(x, y)
print("Triangle:", area)

area = fig.rectangle(x, y)
print("Rectangle:", area)

area = fig.circle(x / 2)
print("Circle:", area)
```

### 実行結果

``` 
Triangle: 50
Rectangle: 100
Circle: 78
```

---

## mod_ex3.py

次の実行結果となるようにPythonプログラムを作成してください。

#### mod_ex3.py

``` python
from figure import triangle, rectangle

x = 10
y = 10

area = ???
print("Triangle:", area)

area = ???
print("Rectangle:", area)
```

### 実行結果

``` 
$ python mod_ex3.py
Triangle: 50
Rectangle: 100
```

---

### テキスト

* [テキスト - モジュール](../text/13_basic.md)
