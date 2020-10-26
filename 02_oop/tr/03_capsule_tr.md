# トレーニング - Monster Battle Game

# 課題 3.1 - データ属性とカプセル化

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
tr03
├── main.py
└── mymonsters
    ├── __init__.py
    └── monster.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

## 実行結果

``` 
$ python main.py
Dragon HP: 150
Golem  HP: 300
Dragon FIRE!! Golem! damage: 78
Golem  HP: 222
Golem BOOM!! Dragon! damage: 30
Dragon HP: 120
Dragon FIRE!! Golem! damage: 58
Golem  HP: 164
Golem BOOM!! Dragon! damage: 30
Dragon HP: 90
Dragon FIRE!! Golem! damage: 53
Golem  HP: 111
Golem BOOM!! Dragon! damage: 30
Dragon HP: 60
Dragon FIRE!! Golem! damage: 75
Golem  HP: 36
Golem BOOM!! Dragon! damage: 60
Dragon HP: 0
Winner: Golem
```

> 実行する度に数値や結果は変化します。

### `main.py` - 実装済み

``` py
from mymonsters.monster import Monster, Dragon, Golem

dragon = Dragon("Dragon", 150, 50)
golem = Golem("Golem", 300, 30)
dragon.print_status()
golem.print_status()
winner = None
while(True):
    dragon.attack(golem)
    if golem.is_down:
        winner = dragon
        break
    golem.attack(dragon)
    if dragon.is_down:
        winner = golem
        break
print("Winner:", winner.name)
```


> `if golem.is_down:` のように条件式を変更しています。

## `monster.py`

以下の3つのクラスを作成します。

* `Monster` クラス - 修正します
* `Dragon` クラス - 実装済み
* `Golem` クラス - 実装済み

> `Monster` クラスのみ修正します。 `Dragon` クラス `Golem` クラスを新たに作成します。

### `Monster` クラス

#### `Monster` クラス - データ属性

|データ属性名|意味|データ型|プロパティ|
|:--|:--|:--|:--|
| `__name` |モンスターの名前 | `str` |Getterのみ|
| `__hp` | ライフ<br> | `int` |Getter/Setter|
| `__ap` | 攻撃力 | `int` |Getterのみ|


#### `Monster` クラス - メソッド

以下の `is_down` メソッドをプロパティに変更します。

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `is_down` |なし| `bool` | `self.hp` が `0` 以下の場合、 `True` <br>それ以外の場合は `False` を返却する|

> データ属性の追加は不要です。`is_down`メソッドに `@property` デコレータを付与してください。


---

# 課題 3.2 - データ属性とカプセル化

`__hp` にSetterプロパティを定義しない場合、どのようなエラーが発生するか確認してください。またその原因を考察してください。

---

## テキスト

* [テキスト - データ属性とカプセル化](../text/03_capsule.md)
