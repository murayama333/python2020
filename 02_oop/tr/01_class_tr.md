# トレーニング - Monster Battle Game

2匹のモンスターがバトルするゲームを作成します。

# 課題 1.1 - クラスとインスタンス

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
tr01
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
Dragon attacks Golem! damage: 50
Golem  HP: 250
Golem attacks Dragon! damage: 30
Dragon HP: 120
Dragon attacks Golem! damage: 50
Golem  HP: 200
Golem attacks Dragon! damage: 30
Dragon HP: 90
Dragon attacks Golem! damage: 50
Golem  HP: 150
Golem attacks Dragon! damage: 30
Dragon HP: 60
Dragon attacks Golem! damage: 50
Golem  HP: 100
Golem attacks Dragon! damage: 30
Dragon HP: 30
Dragon attacks Golem! damage: 50
Golem  HP: 50
Golem attacks Dragon! damage: 30
Dragon HP: 0
Winner: Golem
```

### `main.py` - 実装済み

``` py
from mymonsters.monster import Monster

dragon = Monster("Dragon", 150, 50)
golem = Monster("Golem", 300, 30)
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

---

## `monster.py`

### `Monster` クラス

#### `Monster` クラス - データ属性

|データ属性名|意味|データ型|
|:--|:--|:--|
| `name` |モンスターの名前 | `str` |
| `hp` | ライフ<br> | `int` |
| `ap` | 攻撃力 | `int` |

#### `Monster` クラス - メソッド

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
        pass

    def attack(self, target):
        pass

    def print_attack_message(self, target, damage):
        pass

    def calc_damage(self):
        pass

    def print_status(self):
        pass

    def is_down(self):
        pass
```

---

## 課題 1.2 - クラスとインスタンス

`calc_damage` メソッドを修正して、与えるダメージにばらつきが出るようにしてください。

> ヒント： `random` モジュールをimportします。

---

## テキスト

* [テキスト - クラスとインスタンス](../text/01_class.md)
