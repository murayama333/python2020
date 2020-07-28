# モジュール

### `calculator.py`, `mod1.py`

#### `calculator.py`

``` python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y
```

#### `mod1.py`

``` python
import calculator

x = 20
y = 5
z = calculator.add(x, y)
print("Add:", z)

z = calculator.subtract(x, y)
print("Sub:", z)

z = calculator.multiply(x, y)
print("Mul:", z)

z = calculator.divide(x, y)
print("Div:", z)
```

### 実行

``` 
$ python mod1.py
Add: 25
Sub: 15
Mul: 100
Div: 4
```

> モジュールを扱うプログラムを実行するとカレントディレクトリに `__pycache__` ディレクトリが生成されます。 `__pycache__` ディレクトリにはコンパイル済みのモジュールが格納されます。これにより同じプログラムを複数回実行するとき、コンパイル作業を省略できるためプログラムの実行速度を改善できます。

### 解説

* Pythonプログラムは複数のファイルに分割して作成できる
* Pythonプログラムの1つのファイルをモジュールと呼ぶ
* Pythonのモジュールは `import` 文で読み込むことができる


---

### `mod2.py`

``` python
import calculator as calc

x = 20
y = 5
z = calc.add(x, y)
print("Add:", z)

z = calc.subtract(x, y)
print("Sub:", z)

z = calc.multiply(x, y)
print("Mul:", z)

z = calc.divide(x, y)
print("Div:", z)
```

> 戻り値を返さない関数を定義できます。

### 実行

``` 
$ python mod2.py
Add: 25
Sub: 15
Mul: 100
Div: 4
```

### 解説

* `import` 文にはファイル名（拡張子を除く）を指定する
* デフォルトでは `import` 文で指定したファイル名がモジュール名になる
* `import` 文に `as` 句を指定してモジュールに別名を指定できる


---

### `mod3.py`

``` python
from calculator import add, subtract

x = 20
y = 5
z = add(x, y)
print("Add:", z)

z = subtract(x, y)
print("Sub:", z)
```

### 実行

``` 
$ python mod3.py
Add: 25
Sub: 15
```

### 解説

* `import` 文に `from` 句を記述することでモジュールの中から特定の関数だけを指定して読み込むことができる
* 複数の関数を指定する場合は `,` で区切る
* ワイルドカード（ `*` ）を指定することもできるが名前が衝突しやすいため、推奨されていない

---

### 演習

* [エクササイズ - モジュール](../ex/13_basic_ex.md)
