# optuna + MLflowを用いてハイパーパラメータ管理の実装

## 概要
ハイパーパラメータ最適化フレームワークである**optuna**と実験管理ツールである"MLflow"を用いて、
fashion_mnistデータを分類する多層ニューラルネットワークモデルを管理する。  
バックエンドにはSQLiteを使用する。  
適宜以下の文献を参考にされたい。  
* MLflow公式ドキュメント  
[MLflow Documentation](https://mlflow.org/docs/latest/index.html)  

* MLflowのバックエンド選定について  
[MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)  
※ 今回は上記の[Scenario 2: MLflow on localhost with SQLite](https://mlflow.org/docs/latest/tracking.html#scenario-2-mlflow-on-localhost-with-sqlite)を参考にしている。  

* optuna公式ドキュメント  
[Optuna: A hyperparameter optimization framework](https://optuna.readthedocs.io/en/stable/index.html)

* 今回使用するfashion_mnistデータについて  
[fashion_mnist - Datasets](https://www.tensorflow.org/datasets/catalog/fashion_mnist?hl=ja)



## リポジトリの構成
* `main.ipynb`
  * 実行用コード。optunaで最適化する対象の目的関数の定義などが書かれている。
* `modules/mlflow.py`
  * mlflowで実験管理するためのバックエンドやコールバックの準備をするためのコード


## 環境構築手順
[ライブラリ/フレームワーク]  
・ numpy  
・ matplotlib  
・ tensorflow  
・ mlflow  
・ optuna  
・ sqlite3  

[手順]  
1. 上記ライブラリ/フレームワークがまだインストールされていない場合は、以下のコマンドを実施。
```
pip install -r requirements.txt
```

2. SQLiteでモデルの情報を管理していくため、DBファイルを作成するためのフォルダとアーティファクト(訓練したモデルや環境情報など)を保管するためのディレクトリをあらかじめ作成しておく。  


3. 今回は特段使う想定はしていないが、SQLiteの可視化ツールをインストールしておくと便利  
[DB Browser for SQLite](https://sqlitebrowser.org/dl/)  

4. main.ipynb を開き順にセルを実行する  

5. 手順4完了後、DBファイルを格納しているディレクトリに移動し以下コマンドを実行。mlflkowのGUIを立ち上げる。  
```
mlflow ui --backend-store-uri sqlite:///mlruns.db
```
