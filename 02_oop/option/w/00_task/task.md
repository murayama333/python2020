# タスク管理アプリケーションの開発

## タスク管理アプリケーションの概要

### Taskクラス

* Task
  + id
    - Taskを識別するID
      * 1〜の連番とする
  + title
    - タイトル
  + date
    - 更新日時
      * "%Y-%m-%d %H:%M:%S" 形式で表示する
  + status
    - ステータス
      * 0：未完了のタスク
      * 1：完了したタスク

### TaskBoardクラス

* TaskBoard
  + task_list
    - Taskインスタンスのリスト

### 演習課題

1. Taskクラスの実装
2. TaskBoardクラスの実装
3. タスク管理アプリケーションの開発

---

## 1. Taskクラスの実装

### 1.1 Taskクラスの作成 - task_app.py

`Task` クラスに以下のメソッドを実装します。

* `__init__` メソッド
  + データ属性の `id`, `title`, `date`, `status` を初期化する
* `show` メソッド
  + データ属性の `id`, `title`, `date`, `status` を表示する

``` py
class Task:
    # TODO
    pass

if __name__ == "__main__":
    task1 = Task(1, "Study Python", "2020-11-30 10:00:00", Task.STATUS_CLOSED)
    task2 = Task(2, "Study PHP", "2020-12-01 11:00:00", Task.STATUS_OPENED)
    task3 = Task(3, "Clean the room", "2020-12-02 12:00:00", Task.STATUS_OPENED)

    task1.show()
    task2.show()
    task3.show()
```

次の実行結果となるようにプログラムを作成してください。

#### 実行結果

``` text
$ python task_app.py
1 Study Python 2020-11-30 10:00:00 1
2 Study PHP 2020-12-01 11:00:00 0
3 Clean the room 2020-12-02 12:00:00 0
```

---

## 2. TaskBoardクラスの実装

### 2.1 TaskBoardクラスの作成1 - 作成処理 - task_app.py

`TaskBoard` クラスに以下のメソッドを実装します。

* `__init__` メソッド
  + データ属性 `task_list` を空のリストで初期化する
* `add_task` メソッド
  + データ属性 `task_list` に `Task` インスタンスを追加する
* `show_task_list` メソッド
  + データ属性 `task_list` に追加されている`Task` インスタンスの一覧を表示する

``` py
import datetime

class Task:
    # 省略

class TaskBoard:
    def __init__(self):
        # TODO
        pass

    def add_task(self, title):
        # TODO
        pass

    def show_task_list(self):
        # TODO
        pass

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")
    task_board.show_task_list()
```

次の実行結果となるようにプログラムを作成してください。

``` text
$ python task_app.py
1 Study Python 2020-11-30 13:37:00 0
2 Study PHP 2020-11-30 13:37:00 0
3 Clean the room 2020-11-30 13:37:00 0
```

> タスクの更新日時には、追加した時点の日時を登録するものとします。 

### ヒント：現在日時の取得方法

``` py
import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

---

### 2.2 TaskBoardクラスの作成2 - 更新処理 - task_app.py

`TaskBoard` クラスに以下のメソッドを実装します。

* `edit_task` メソッド - 修正
  + 引数で指定された `id` に該当する `Task` インスタンスを更新する
  + 引数で指定された `id` に該当する `Task` インスタンスが存在しない場合は、`TaskBoardError` 例外をスローする

> `TaskBoardError` クラスの定義を追加します。

``` py
import datetime

class Task:
    # 省略

class TaskBoardError(Exception):
    pass

class TaskBoard:
    def __init__(self):
        # 省略

    def add_task(self, title):
        # 省略

    def show_task_list(self):
        # 省略

    def edit_task(self, id, title, status):
        # TODO
        pass

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")

    try:
        task_board.edit_task(2, "Study PHP8", Task.STATUS_CLOSED)
        task_board.edit_task(10, "Test Excption", Task.STATUS_OPENED)
    except TaskBoardError as e:
        print(e)

    task_board.show_task_list()
```

次の実行結果となるようにプログラムを作成してください。

``` text
$ python task_app.py
Invalid id. 10
1 Study Python 2020-11-30 15:12:42 0
2 Study PHP8 2020-11-30 15:12:42 1
3 Clean the room 2020-11-30 15:12:42 0
```

---


### 2.3 TaskBoardクラスの作成3 - 削除処理 - task_app.py

`TaskBoard` クラスに以下のメソッドを実装します。

* `delete_task` メソッド - 修正
  + 引数で指定された `id` に該当する `Task` インスタンスを更新する
  + 引数で指定された `id` に該当する `Task` インスタンスが存在しない場合は、`TaskBoardError` 例外をスローする


``` py
import datetime

class Task:
    # 省略

class TaskBoardError(Exception):
    pass

class TaskBoard:
    def __init__(self):
        # 省略

    def add_task(self, title):
        # 省略

    def show_task_list(self):
        # 省略

    def edit_task(self, id, title, status):
        # 省略

    def delete_task(self, id):
        # TODO
        pass
    

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")

    try:
        task_board.delete_task(2)
        task_board.delete_task(10)
    except TaskBoardError as e:
        print(e)

    task_board.show_task_list()
```

次の実行結果となるようにプログラムを作成してください。

``` text
$ python task_app.py
Invalid id. 10
1 Study Python 2020-11-30 15:20:47 0
3 Clean the room 2020-11-30 15:20:47 0
```

---

### 2.4 TaskBoardクラスの作成4 - 保存処理 - task_app.py

`TaskBoard` クラスに以下のメソッドを実装します。

* `save_file` メソッド - 修正
  * データ属性 `task_list` に保持されている `Task` インスタンスの一覧を引数 `file_name` で指定されたファイルに保存する
    * ファイル保存時のエンコードはUTF-8、保存形式はCSV形式とする


``` py
import datetime
import csv


class Task:
    # 省略

class TaskBoardError(Exception):
    pass

class TaskBoard:
    def __init__(self):
        # 省略

    def add_task(self, title):
        # 省略

    def show_task_list(self):
        # 省略

    def edit_task(self, id, title, status):
        # 省略

    def delete_task(self, id):
        # 省略

    def save_file(self, file_name):
        # TODO
        pass
    

if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")

    task_board.save_file("task.csv")
```

次の実行結果となるようにプログラムを作成してください。

``` text
$ python task_app.py
```

> カレントフォルダに以下のような `task.csv` ファイルが生成されます。

```csv
1,Study Python,2020-11-30 15:22:49,0
2,Study PHP,2020-11-30 15:22:49,0
3,Clean the room,2020-11-30 15:22:49,0
```

---

### 2.4 TaskBoardクラスの作成4 - 読み込み処理 - task_app.py

`TaskBoard` クラスに以下のメソッドを実装します。

* `load_file` メソッド - 修正
  + 引数 `file_name` で指定されたファイルを読み込み、データ属性 `task_list` に保持する


``` py
import datetime
import csv


class Task:
    # 省略

class TaskBoardError(Exception):
    pass

class TaskBoard:
    def __init__(self):
        # 省略

    def add_task(self, title):
        # 省略

    def show_task_list(self):
        # 省略

    def edit_task(self, id, title, status):
        # 省略

    def delete_task(self, id):
        # 省略

    def save_file(self, file_name):
        # 省略

    def load_file(self, file_name):
        # TODO
        pass


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.load_file("task.csv")
    task_board.show_task_list()
```

またここではカレントフォルダ上に以下の内容で `task.csv` ファイルが存在するものとします。

```csv
1,Study Python,2020-11-30 15:22:49,0
2,Study PHP,2020-11-30 15:22:49,0
3,Clean the room,2020-11-30 15:22:49,0
```

次の実行結果となるようにプログラムを作成してください。

``` text
$ python task_app.py
1 Study Python 2020-11-30 15:22:49 0
2 Study PHP 2020-11-30 15:22:49 0
3 Clean the room 2020-11-30 15:22:49 0
```

---

## 3. タスク管理アプリケーションの開発

`Task` クラス、 `TaskBoard` クラス、`TaskBoardError` クラスを使って、以下のように対話型で動作するタスク管理アプリケーションの開発してください。

> `Task` クラス、 `TaskBoard` クラス、`TaskBoardError` クラスを修正しても構いません。

## 実行結果

### 起動メッセージ

```text
$ python task_app.py
0: show all task list
1: show opened task list
2: add task
3: finish task
4: edit task
5: delete task
6: save file
7: load file
9: quit
```

### 2: add task

```text
operation: 2
title: Study Python
operation: 2
title: Study PHP
operation: 2
title: Clean the room
```

> キーボードから `title:` の入力を受け取ります。

### 0: show all task list

```text
operation: 0
1 Study Python 2020-11-30 15:42:54 0
2 Study PHP 2020-11-30 15:42:58 0
3 Clean the room 2020-11-30 15:43:08 0
```

> タスクの一覧を表示します。

### 3: finish task

```text
operation: 3
id: 3
operation: 0
1 Study Python 2020-11-30 15:42:54 0
2 Study PHP 2020-11-30 15:42:58 0
3 Clean the room 2020-11-30 15:43:23 1
```

> キーボードから `id:` の入力を受け取り、該当する `Task` の `status` を完了（`1`）に更新します。このとき該当する `Task` の `date` は現在日時で更新します。

### 1: show opened task list

```text
operation: 1
1 Study Python 2020-11-30 15:42:54 0
2 Study PHP 2020-11-30 15:42:58 0
```

> 未完了のタスクの一覧を表示します。

### 4: edit task

```text
operation: 4
id: 2
title: Study PHP8
status(0: opened, 1: closed): 0
operation: 0
1 Study Python 2020-11-30 15:42:54 0
2 Study PHP8 2020-11-30 15:43:44 0
3 Clean the room 2020-11-30 15:43:23 1
```

> キーボードから `id:`、 `title:`、 `status(0: opened, 1: closed):` の入力を受け取り、該当する `Task` の `title`、`status` をに更新します。このとき該当する `Task` の `date` は現在日時で更新します。


### 5: delete task

```text
operation: 5
id: 2
operation: 0
1 Study Python 2020-11-30 15:42:54 0
3 Clean the room 2020-11-30 15:43:23 1
```

> キーボードから `id:` の入力を受け取り、該当する `Task` を削除します。


### 6: save file

```text
operation: 6
file name: task.csv
```

> `task.csv` ファイルにタスクの一覧を保存します。

### 7: load file

```text
operation: 7
file name: task.csv
operation: 0
1 Study Python 2020-11-30 15:42:54 0
3 Clean the room 2020-11-30 15:43:23 1
```

> `task.csv` ファイルからタスクの一覧を読み込みます。

### 9: quit

```
operation: 9
```

> アプリケーションを終了します。


### ヒント

```py
import datetime
import csv


class Task:
    # 省略


class TaskBoardError(Exception):
    # 省略


class TaskBoard:
    # 省略

    def show_operation_message(self):
        print("0: show all task list")
        print("1: show opened task list")
        print("2: add task")
        print("3: finish task")
        print("4: edit task")
        print("5: delete task")
        print("6: save file")
        print("7: load file")
        print("9: quit")


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.show_operation_message()
    while True:
      operation = int(input("operation: ").strip())
      # TODO
      pass
```
