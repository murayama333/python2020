# スコア分析アプリケーションの開発

## スコア分析アプリケーション概要

スコア分析アプリケーションは、数学（`math`）、英語（`english`）、科学（`science`）のテスト結果を分析するアプリケーションです。具体的には、以下のようなデータを取り扱います。

```py
scores = [
    {"name": "Andy", "math": 70, "english": 90, "science": 80},
    {"name": "Betty", "math": 80, "english": 90, "science": 100},
    {"name": "Carol", "math": 40, "english": 90, "science": 90},
    {"name": "Daniel", "math": 80, "english": 100, "science": 40},
    {"name": "Ellen", "math": 90, "english": 70, "science": 90},
]
```

1. スコアのプリント
2. 合計スコアのプリント
3. 科目指定によるスコアのプリント
4. 科目指定による合計スコアのプリント
5. データの保存（JSONフォーマット）
6. データのロード（JSONフォーマット）
7. オリジナル機能の実装1
8. オリジナル機能の実装2
9. オリジナル機能の実装3
---

## 1. スコアのプリント

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.print_scores()
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
- scores -
Andy 70 90 80
Betty 80 90 100
Carol 40 90 90
Daniel 80 100 40
Ellen 90 70 90
```

> `ScoreAnalyzer` クラスに `__init__` メソッド、`print_scores` メソッドを実装します。

---

## 2. 合計スコアのプリント

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # 省略

    def print_total_score(self):
        # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.print_total_score()
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
- total scores -
1200
```

> `ScoreAnalyzer` クラスに `print_total_score` メソッドを実装します。


---

## 3. 科目指定によるスコアのプリント

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # 省略

    def print_scores_by_subject(self, subject, with_name=False):
        # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.print_scores_by_subject("science")
    score_analyzer.print_scores_by_subject("science", with_name=True)
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
- scores by science -
80
100
90
40
90
- scores by science -
Andy 80
Betty 100
Carol 90
Daniel 40
Ellen 90
```

> `ScoreAnalyzer` クラスに `print_scores_by_subject` メソッドを実装します。引数 `with_name` が `True` の場合は学生の名前も表示します。

---

## 4. 科目指定による合計スコアのプリント

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # 省略

    def print_total_score_by_subject(self, subject):
        # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.print_total_score_by_subject("science")
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
- total score by science -
400
```

> `ScoreAnalyzer` クラスに `print_total_score_by_subject` メソッドを実装します。

---

## 5. データの保存（JSONフォーマット）

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # 省略

    def save(self, file_name):
        # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer(scores)
    score_analyzer.save("score.json")
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
```

> `ScoreAnalyzer` クラスに `save` メソッドを実装します。カレントフォルダに以下のような`score.json` ファイルが生成されます。

```json
[
    {
        "name": "Andy",
        "math": 70,
        "english": 90,
        "science": 80
    },
    {
        "name": "Betty",
        "math": 80,
        "english": 90,
        "science": 100
    },
    {
        "name": "Carol",
        "math": 40,
        "english": 90,
        "science": 90
    },
    {
        "name": "Daniel",
        "math": 80,
        "english": 100,
        "science": 40
    },
    {
        "name": "Ellen",
        "math": 90,
        "english": 70,
        "science": 90
    }
]
```

---

## 6. データのロード（JSONフォーマット）

次のプログラム（`score_analyzer.py`）があります。

```py
import json


class ScoreAnalyzer:
    # 省略

    @classmethod
    def load(cls, file_name):
        # TODO


if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]
    score_analyzer = ScoreAnalyzer.load("score.json")
    score_analyzer.print_scores()
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python score_analyzer.py
- scores -
Andy 70 90 80
Betty 80 90 100
Carol 40 90 90
Daniel 80 100 40
Ellen 90 70 90
```

> `ScoreAnalyzer` クラスに `load` メソッドを実装します。このプログラムを動作させるためには、カレントフォルダに以下のような `score.json` ファイルを用意しておく必要があります。

```json
[
    {
        "name": "Andy",
        "math": 70,
        "english": 90,
        "science": 80
    },
    {
        "name": "Betty",
        "math": 80,
        "english": 90,
        "science": 100
    },
    {
        "name": "Carol",
        "math": 40,
        "english": 90,
        "science": 90
    },
    {
        "name": "Daniel",
        "math": 80,
        "english": 100,
        "science": 40
    },
    {
        "name": "Ellen",
        "math": 90,
        "english": 70,
        "science": 90
    }
]
```

---

## 7〜9. オリジナル機能の実装1〜3

以下の機能一覧を参考に、スコア分析アプリケーションに機能を3つ追加してください。

1. スコアの平均点のプリント
1. スコアの標準偏差のプリント
1. 学生指定によるスコアのプリント
1. 学生指定による合計スコアのプリント
1. スコアの高い（低い）順に学生の名前をプリント
1. 科目ごとの最小値、最大値をプリント
1. 100点の学生の名前をプリント
1. 50点以下の点数の学生の名前をプリント
1. データの保存（CSVフォーマット）
1. データのロード（CSVフォーマット）

> 上記以外のアイデアを実装してもOKです。