# Template for Python package Project

## Introduction

Pythonパッケージ作成用のcookiecutterテンプレート

## How to use this template

cookiecutterをinstall

```bash
pip install cookiecutter
```

templateを用いてprojectを作成

```bash
cookiecutter https://github.com/oga-a/cct_python

# 適当に入力する
project_name: プロジェクトの名前
package_author: パッケージ管理者名
package_author_email: パッケージ管理者メール
github_username: GitHubアカウント名
repo_name: リポジトリ名
python_package: Pythonパッケージ名
github_fqdn: GitHubがEnterprise版だったら変更
docs_url: パッケージ用ドキュメントURL
```

プロジェクトフォルダに移動
```bash
cd `repo_name`
```

アカウント名`github_username`でリポジトリ名が`repo_name`のGitHubにpush

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin git@`github_fqdn`:`github_username`/`repo_name`.git
git push --set-upstream origin master
```

## How to develop this project

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
