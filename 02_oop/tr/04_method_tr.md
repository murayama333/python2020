# トレーニング - Monster Battle Game

# 課題 4.1 - メソッド

以下のフォルダ構成に従ってPythonプログラムを作成します。

``` 
tr04
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
Golem BOOM!! Dragon! damage: 60
Dragon HP: 90
Dragon FIRE!! Golem! damage: 78
Golem  HP: 222
Golem BOOM!! Dragon! damage: 30
Dragon HP: 60
Dragon FIRE!! Golem! damage: 58
Golem  HP: 164
Dragon FIRE!! Golem! damage: 60
Golem  HP: 104
Golem BOOM!! Dragon! damage: 30
Dragon HP: 30
Dragon FIRE!! Golem! damage: 77
Golem  HP: 27
Golem BOOM!! Dragon! damage: 30
Dragon HP: 0
Winner: Golem
```

> 先攻後攻が変化するように実装します。

### `main.py` - 実装済み

``` py
from mymonsters.monster import Monster, Dragon, Golem

dragon = Dragon("Dragon", 150, 50)
golem = Golem("Golem", 300, 30)
dragon.print_status()
golem.print_status()
winner = None
while(True):
    monster1, monster2 = Monster.shuffle(dragon, golem)
    monster1.attack(monster2)
    if monster2.is_down:
        winner = monster1
        break
    monster2.attack(monster1)
    if monster1.is_down:
        winner = monster2
        break
print("Winner:", winner.name)
```

> `while` 文の中に `monster1, monster2 = Monster.shuffle(dragon, golem)` を追記しています。

## `monster.py`

以下の3つのクラスを作成します。

* `Monster` クラス - 修正します
* `Dragon` クラス - 実装済み
* `Golem` クラス - 実装済み

> `Monster` クラスのみ修正します。 `Dragon` クラス `Golem` クラスを新たに作成します。

### `Monster` クラス

#### `Monster` クラス - メソッド - 実装済み

以下の `shuffle` メソッドを追加します。

|メソッド名|引数|戻り値|処理|
|:--|:--|:--|:--|
| `shuffle` |モンスター1<br>モンスター2| モンスター1, 2をシャッフルしたタプル | TODO |

> `shuffle` メソッドは、クラスメソッド、あるいはスタティックメソッドとして実装します。

---

# 課題 4.2 - データ属性とカプセル化

`shuffle` メソッドが3匹以上のモンスターを受け取れるようにするにはどうすれば良いか考察してください。

---

## テキスト

* [テキスト - メソッド](../text/04_method.md)
