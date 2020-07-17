# 関数 - 関数定義

### func1.py

+ 足し算をする`add`関数を定義します。
+ `add`関数の引数に`10`と`20`を指定して呼び出します。
+ `add`関数の戻り値を`$result`に代入します。

```python
def add(x, y):
  z = x + y
  return z

result = add(10, 20)
print(result)
```

### 実行

```
$ python func1.py
30
```

---


### func2.py

+ 配列の合計値を求める`sum`関数を定義します。
+ `sum`関数の引数に`$prices`を指定して呼び出します。
+ `sum`関数の戻り値を`$result`に代入します。


```python
<?python
function sum($array)
{
  $total = 0;
  for ($i = 0; $i < count($array); $i++) {
    $total += $array[$i];
  }
  return $total;
}

$prices = [1000, 2000, 3000];
$result = sum($prices);
echo $result;
```

### 実行

```
> python func2.py
6000
```

---


### func3.py

+ 指定した回数"Hello"と出力する`hello`関数を定義します。
+ `hello`関数の引数に`5`を指定して呼び出します。
+ `hello`関数の戻り値はありません。


```python
<?python
function hello($repeat)
{
  for ($i = 0; $i < $repeat; $i++) {
    echo "Hello";
  }
}

hello(5);
```

### 実行

```
> python func3.py
HelloHelloHelloHelloHello
```

---

### func4.py

+ 現在の年を取得する`get_year`関数を定義します。
+ `get_year`関数を引数なしで呼び出します。
+ `get_year`関数の戻り値を`$year`に代入します。


```python
<?python
function get_year()
{
  return date('Y');
}

$year = get_year();
echo $year;
```

### 実行

```
> python func4.py
2019
```

---

### func5.py

+ "Hello World!"を出力する`hello_world`関数を定義します。
+ `hello_world`関数を引数なしで呼び出します。
+ `hello_world`関数の戻り値はありません。


```python
<?python
function hello_world()
{
  echo "Hello World!";
}

hello_world();
```

### 実行

```
> python func5.py
Hello World!
```

---

### func6.py

+ 再帰的に値を出力する`recursion`関数を定義します。
+ `recursion`関数の引数に`1`を指定して呼び出します。
+ `recursion`関数の戻り値はありません。

```python
<?python
function recursion($a)
{
    if ($a < 10) {
        echo $a . python_EOL;
        recursion($a + 1);
    }
}

recursion(1);
```

> recursion関数は再帰的な関数です。

### 実行

```
> python func6.py
1
2
3
4
5
6
7
8
9
```

---

### 考察

+ [ユーザ定義ー関数](https://www.py.net/manual/ja/functions.user-defined.py)

---

### 演習

+ [エクササイズ - 関数 - ユーザ定義関数](ex/11_python_ex.md)