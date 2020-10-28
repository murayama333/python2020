# オブジェクトの関連（処理の委譲）

## 処理の委譲

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x.get_value(), self.y.get_value())

class MyX:
    def get_value(self):
        return 10

class MyY:
    def get_value(self):
        return 20

if __name__ == "__main__":
    x = MyX()
    y = MyY()
    instance = MyClass(x, y)
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 10 20
```

### 解説

* データ属性には、文字列や数値だけでなく、異なるクラスのインスタンスを保持できる
* オブジェクト（インスタンス）の中に、別のオブジェクトを持つことを集約や関係、関連などと呼ぶ
* オブジェクトが別のオブジェクトの参照を持ち、処理を委譲することで、クラスごとの責務（役割）が明確になる

---

## 演習

* [エクササイズ - オブジェクトの関連（処理の委譲）](../ex/05_delegate_ex.md)
