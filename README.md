# Template for Python package Project

## Introduction

Pythonパッケージ作成用のcookiecutterテンプレート

## How to use this template

```bash
# cookiecutterをinstall
pip install cookiecutter

# templateを用いてprojectを作成
cookiecutter https://github.com/oga-a/cct_python

# 適当に入力する
project_name: プロジェクトの名前
package_author: パッケージ管理者名
package_author_email: パッケージ管理者メール
repo_name: レポジトリ名
python_package: パッケージ名
github_username: GitHubユーザー名
github_fqdn: GitHubがEnterprise版だったら変更
docs_url: パッケージ用ドキュメントURL

# プロジェクトフォルダに移動
cd `repo_name`

# GitHubにpush
git init
git add .
git commit -m "initial commit"
git push
```

作成後はpoetryを使ってパッケージ開発

```bash
poetry install
poetry add numpy==1.21.6
```

実行できるか確認

```bash
poetry shell
python
```

```python
import `python_package`
print(`python_package`.__version__)
```
