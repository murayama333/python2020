# トレーニング - Monster Battle Game

# 課題 2.1 - 継承

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
tr02
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
Dragon FIRE!! Golem! damage: 69
Golem  HP: 231
Golem BOOM!! Dragon! damage: 30
Dragon HP: 120
Dragon FIRE!! Golem! damage: 58
Golem  HP: 173
Golem BOOM!! Dragon! damage: 60
Dragon HP: 60
Dragon FIRE!! Golem! damage: 54
Golem  HP: 119
Golem BOOM!! Dragon! damage: 30
Dragon HP: 30
Dragon attacks Golem! damage: 50
Golem  HP: 69
Golem BOOM!! Dragon! damage: 60
Dragon HP: 0
Winner: Golem
```

> 実行する度に数値や結果は変化します。

### `main.py` - 実装済み

``` py
from mymonsters.monster import Monster, Dragon, Golem

dragon = Dragon("Dragon", 150, 50, 3)
golem = Golem("Golem", 300, 30)
dragon.print_status()
golem.print_status()
winner = None
while(True):
    dragon.attack(golem)
    if golem.is_down():
        winner = dragon
        break
    golem.attack(dragon)
    if dragon.is_down():
        winner = golem
        break
print("Winner:", winner.name)
```

課題1からインスタンスを生成する部分を変更しています。

``` py
dragon = Dragon("Dragon", 150, 50, 3)
golem = Golem("Golem", 300, 30)
```

---

## `monster.py`

以下の3つのクラスを作成します。

* `Monster` クラス - 実装済み
* `Dragon` クラス
* `Golem` クラス

> `Dragon` クラス、 `Golem` クラスを新たに作成します。

### `Monster` クラス

#### `Monster` クラス - データ属性 - 実装済み

|データ属性名|意味|データ型|
|:--|:--|:--|
| `name` |モンスターの名前 | `str` |
| `hp` | ライフ<br> | `int` |
| `ap` | 攻撃力 | `int` |

#### `Monster` クラス - メソッド - 実装済み

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `__init__` | `name` モンスターの名前<br> `hp` モンスターのライフ<br> `ap` モンスターの攻撃力|<br>|コンストラクタ<br> `name` 、 `hp` 、 `ap` を初期化する|
| `attack` | `target` 攻撃対象モンスター|なし|自身の `calc_damage` メソッドを呼び出す<br>自身の `print_attack_message` メソッドを呼び出す<br>撃対象モンスターのライフを減らす<br>攻撃対象モンスターの `print_status` メソッドを呼び出す|
| `print_attack_message` | `target` 攻撃対象モンスター<br> `damage` 与えるダメージ|なし|モンスターの名前、攻撃対象モンスターの名前、ダメージを表示する|
| `calc_damage` |なし| `int` | `self.ap` を返却する|
| `print_status` |なし|なし|モンスターの名前とライフを表示する|
| `is_down` |なし| `bool` | `self.hp` が `0` 以下の場合、 `True` <br>それ以外の場合は `False` を返却する|

``` py
class Monster:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def attack(self, target):
        damage = self.calc_damage()
        self.print_attack_message(target, damage)

        target.hp = target.hp - damage
        if target.hp < 0:
            target.hp = 0
        target.print_status()

    def print_attack_message(self, target, damage):
        print(f"{self.name} attacks {target.name}! damage: {damage}")

    def calc_damage(self):
        return self.ap

    def print_status(self):
        print(f"{self.name:6} HP: {self.hp}")

    def is_down(self):
        return self.hp <= 0
```

### `Dragon` クラス

#### `Dragon` クラス - データ属性

|データ属性名|意味|データ型|
|:--|:--|:--|
| `mp` | `FIRE` 可能回数 | `int` |

#### `Dragon` クラス - メソッド

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `__init__` | `name` モンスターの名前<br> `hp` モンスターのライフ<br> `ap` モンスターの攻撃力<br> `mp`  `FIRE` 可能回数|<br>|コンストラクタ<br> `name` 、 `hp` 、 `ap` 、 `mp` を初期化する<br> ※スーパークラスのコンストラクタを使うこと|
| `print_attack_message` | `target` 攻撃対象モンスター<br> `damage` 与えるダメージ|なし|モンスターの名前、攻撃対象モンスターの名前、ダメージを表示する<br> `mp` が `0` より大きい場合、メッセージを以下のように表示する<br>　 `Dragon FIRE!! Golem! damage: 76` <br>　 `mp` をデクリメントする<br>それ以外の場合、スーパークラスの `print_attack_message` を呼び出す |
| `calc_damage` |なし| `int` | `mp` が `0` より大きい場合、 `0` 〜 `self.ap * 2` の値をランダムで返却する<br>それ以外は `self.ap` を返却する|

``` py
class Dragon:
    pass
```

### `Golem` クラス

#### `Golem` クラス - データ属性

データ属性に変更はありません。

#### `Golem` クラス - メソッド

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `print_attack_message` | `target` 攻撃対象モンスター<br> `damage` 与えるダメージ|なし|モンスターの名前、攻撃対象モンスターの名前、ダメージを表示する<br>メッセージを以下のように表示する<br> `Golem BOOM!! Dragon! damage: 60` |
| `calc_damage` |なし| `int` | 50%の確率で `self.ap * 2` を返却する<br>それ以外の場合は `self.ap` を返却する|

``` py
class Golem:
    pass
```

---

## 課題 2.2 - 継承

`Monster` クラスを継承して新たなクラスを作成してください。

---

## テキスト

* [テキスト - 継承](../text/02_extends.md)
