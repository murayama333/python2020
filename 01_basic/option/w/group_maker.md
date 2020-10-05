# 総合演習：席替えアプリケーションの開発

## 1. メンバー数の表示

次のプログラム（ `group_maker.py` ）があります。

``` py
names = ["Alice", "Alex", "Andy", "Abel", "Albert",
        "Betty", "Bob", "Bella", "Billie", "Benn",
        "Carol", "Connie", "Crysta", "Clara", "Cyndy",
        "Daniel", "David", "Denny", "Diana"]

group_count = int(input("Group Count: "))
member_count = ???
group_member_count = ???
rest_member = ???

print("Member Count:", member_count)
print("Group Member Count:", group_member_count)
print("Rest Member Count:", rest_member)
```

次の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
$ python group_maker.py
Group Count: 5
Member Count: 19
Group Member Count: 3
Rest Member Count: 4
```

> `Group Count` を入力します。メンバー数、グループメンバー数、余りのメンバー数を表示します。

---

## 2. グループメンバー数の表示

先ほどのプログラムを修正して、の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
$ python group_maker.py
Group Count: 5
Member Count: 19
Group Member Count: 3
Rest Member Count: 4
Group Member Counts: [4, 4, 4, 4, 3]
```

> `Group Member Counts: [4, 4, 4, 4, 3]` を追加します。

---

## 3. グループメンバーの表示

先ほどのプログラムを修正して、の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
$ python group_maker.py
Group Count: 4
Member Count: 19
Group Member Count: 4
Rest Member Count: 3
Group Member Counts: [5, 5, 5, 4]
Group1: Abel Albert Alex Alice Andy 
Group2: Bella Benn Betty Billie Bob 
Group3: Carol Clara Connie Crysta Cyndy 
Group4: Daniel David Denny Diana 
```

---

## 4. シャッフル機能の追加

先ほどのプログラムを修正して、の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
Group Count: 4
Shuffle (0: False, 1:True): 1
Member Count: 19
Group Member Count: 4
Rest Member Count: 3
Group Member Counts: [5, 5, 5, 4]
Group1: Denny Daniel Alice Albert Connie 
Group2: Billie Abel Betty Crysta Clara 
Group3: Diana Bob Carol Andy Benn 
Group4: Cyndy Alex David Bella 
```

> `Shuffle (0: False, 1:True): 1` を追加します。ユーザがシャッフルの有無を `0` or `1` で入力するものとします。

---

## ５. ソート機能の追加

先ほどのプログラムを修正して、の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
Group Count: 4
Shuffle (0: False, 1:True): 1
Sort (0: False, 1:True): 1
Member Count: 19
Group Member Count: 4
Rest Member Count: 3
Group Member Counts: [5, 5, 5, 4]
Group1: Abel Alex Crysta Cyndy David 
Group2: Bella Benn Billie Clara Denny 
Group3: Alice Andy Betty Carol Diana 
Group4: Albert Bob Connie Daniel 
```

> `Sort (0: False, 1:True): 1` を追加します。ユーザがグループ内のソートの有無を `0` or `1` で入力するものとします。

---

## 6. 表示の切り替え

先ほどのプログラムを修正して、の実行結果のとおり出力するプログラムを作成してください。

### 実行結果

``` 
Group Count: 4
Shuffle (0: False, 1:True): 1
Sort (0: False, 1:True): 1
Print Mode (0: noraml, 1:table): 1
Member Count: 19
Group Member Count: 4
Rest Member Count: 3
Group Member Counts: [5, 5, 5, 4]
|Abel  |Betty |Crysta|Denny |Diana |
|Albert|Billie|Carol |Cyndy |David |
|Alice |Benn  |Bob   |Clara |Connie|
|Alex  |Andy  |Bella |Daniel|
```

> `Print Mode (0: noraml, 1:table): 1` を追加します。ユーザが出力形式を `0` or `1` で入力するものとします。

### ヒント1

名前の一覧の中から文字数が最大値を求めます。`len` 関数の引数に`str`型のデータを渡すと文字数を取得できます。

### ヒント2

文字列の出力にはフォーマット文字列を使うと便利です。

```py
names = ["Alex", "Alebert"]
for name in names:
    print(f"|{name:10}|")
```

実行結果は次のようになります。

```
|Alex      |
|Alebert   |
```
