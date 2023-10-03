import mlflow
import sqlite3
import os

from optuna.integration import MLflowCallback

# バックエンドの準備
def backend(db_path):
    # 親ディレクトリなければ作成
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # バックエンド用DBファイルの作成
    sqlite3.connect(db_path)

    # トラッキングサーバの（バックエンドの）場所を指定
    tracking_uri = f'sqlite:///{db_path}'
    mlflow.set_tracking_uri(tracking_uri)

    # tracking_uriが設定できていることを確認
    tracking_uri = mlflow.get_tracking_uri()
    
    return tracking_uri


# experiment作成用関数
def create_experiment(experiment_name, artifact_loc):
    """    
    parameters
    =======
    * experiment : experimentの名前
    * artifact : artifactを保存する場所のパス
    """
    # Experimentの生成
    experiment = mlflow.get_experiment_by_name(experiment_name)
    # 当該Experiment存在しないとき、新たに作成
    if experiment is None:
        experiment_id = mlflow.create_experiment(
                                name=experiment_name,
                                artifact_location=artifact_loc)
    # 当該Experiment存在するとき、IDを取得
    else:
        experiment_id = experiment.experiment_id
    
    return experiment_id


def mlflow_callback(tracking_uri, experiment_id):
    # optunaのmlflow integrationを利用
    mlflc = MLflowCallback(
        tracking_uri=tracking_uri,   
        metric_name="accuracy",
        create_experiment=False,
        mlflow_kwargs = {"experiment_id" : experiment_id}
    )
    return mlflc
