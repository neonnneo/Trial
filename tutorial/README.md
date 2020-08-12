メモ
====
# ReadMe
|更新日|更新者|更新内容|
|:-----------|:-----------|:-----------|
|2020.06.20|nennneo|新規作成|

本ファイルはDjangoのチュートリアルを行っての備忘録です。
本ファイルはmarkdown形式で作成しているので、mdファイルのプレビューが可能なエディタなどで参照すると良いです。


https://docs.djangoproject.com/ja/3.0/intro/tutorial01/


GoogleスタイルのPythonDocstringを使う。
https://qiita.com/11ohina017/items/118b3b42b612e527dc1d

## Version

開発環境やソフトバージョンは以下の通り。

```bash
OS==Windows10
Python==3.8.3
django-crispy-forms==1.7.2
django-filter==2.0.0
```

## Editer + Package

VSCodeで以下拡張機能インストールしました。

## Package


## Usage

開発するパソコンで以下を行う必要があります。

1. Pythonをインストール（このとき、 インストーラではAdd Python 3.x to PATHにチェックをいれること)
```bash
python -m django --version
```

2. Django、Django用Lint（問題タブのエラーや警告表示）をインストール
```bash
python -m pip install Django
```

```bash
pip install pylint-django
```

VSCodeのsetting.jsonに以下を追加します。
```bash
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
]

```
3. cdでプロジェクトを作成するディレクトリに移動し、プロジェクトを作成(今回はtutorialは任意の名前)します。
```bash
cd /d D:\Git\
```
```bash
$ django-admin startproject tutorial
```

4. コマンドプロンプトを起動し、以降のコマンドでDjango他をアプリケーションの実行に必要なライブラリをインストールします。

5. (今回はPostgreを使うので)PostgreSQLをインストールします。

6. PostgreSQLへの接続に必要なパッケージをインストールします。

```bash
pip install psycopg2 psycopg2-binary
```

7. tutorial\tutorial\settings.pyでDATABASESを以下のように修正します。(インストールしたPostgreSQLにあわせる)

```bash
DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'POST': '5432'
    }
}
```

8. マイグレーションを実行(これでPgAdminでテーブルを参照すると、auth_group等のDjango関連テーブルが作成される)
```bash
python manage.py migrate
```

9. データベースにアプリケーションの管理者ユーザーを作成します。メールアドレスは任意。
```bash
python manage.py createsuperuser
```

10. 管理者ユーザーの登録が完了したら、以下のコマンドを入力してアプリケーションを起動します。
```bash
python manage.py runserver
```

11. 新たなアプリケーションpollsを作成します。
```bash
python manage.py makemigrations polls
```

12. テストコードは以下コマンドで実行します。

```bash
python manage.py test polls
```

## Contribution


## Author

neonnneo
