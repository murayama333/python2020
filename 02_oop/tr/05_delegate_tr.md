# トレーニング - Monster Battle Game

# 課題 5.1 - オブジェクトの関連（処理の委譲）

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
tr05
├── main.py
└── mymonsters
    ├── __init__.py
    └── monster.py
```

> `main.py` は完成しているので、 `monster.py` を作成します。 `__init__.py` は空のファイルです。

## 実行結果

``` 
$ python main.py
Awesome Monsters
Dragon HP: 150
Golem  HP: 300
```

> 先攻後攻が変化するように実装します。

### `main.py` - 実装済み

``` py
from mymonsters.monster import Monster, Dragon, Golem, MonsterParty

dragon = Dragon("Dragon", 150, 50)
golem = Golem("Golem", 300, 30)
party = MonsterParty("Awesome Monsters")
party.add(dragon)
party.add(golem)
party.print_monsters()
```

## `monster.py`

以下の4つのクラスを作成します。

* `Monster` クラス - 実装済み
* `Dragon` クラス - 実装済み
* `Golem` クラス - 実装済み
* `MonsterParty` クラス - 作成します

### `MonsterParty` クラス

#### `MonsterParty` クラス - データ属性

|データ属性名|意味|データ型|
|:--|:--|:--|
| `monsters` |モンスターのリスト | `list` |

#### `MonsterParty` クラス - メソッド

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `__init__` | `name` パーティの名前 |<br>|データ属性 `monsters` を空のリストで初期化する|
| `add` | `monster` 追加対象のモンスター|なし|データ属性 `monsters` に引数のモンスターを追加する|
| `print_monsters` |なし| なし | パーティの名前を出力する<br>データ属性 `monsters` に存在するモンスターの `print_status` メソッドを呼び出す|

---

## テキスト

* [テキスト - オブジェクトの関連（処理の委譲）](../text/05_delegate.md)
