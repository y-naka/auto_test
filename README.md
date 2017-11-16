# Sample Application

## 概要

Flaskを使ったサンプルのアプリケーション

## 使い方

必要なライブラリのインストール

```bash
pip install -r requirements.txt
```

環境変数を通す

```
export FLASK_APP=${PWD}/run.py
```

データベースの構築を行なう(既存の場合は、内容が全てリセットされる)

```bash
flask initdb
```

APIの起動

```bash
flask run
```

## 構成

.
├── README.md
├── config.py
├── requirements.txt
├── run.py
├── techapp
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── bbs.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   └── profile.html
│   └── views.py
└── tests

* config.py: APIの設定を規定
* run.py: コマンドライン用関数を格納
* models.py: データを持つ主体となるクラスなどデータ本体を格納
* views: REST APIへアクセスした際の挙動を規定
* templates: viewの中でレンダリングされるテンプレートを格納
