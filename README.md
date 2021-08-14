# Libbeta
RustでPythonのライブラリを作るためのテストベット

## 目的
* [x] `setuptools-rust` で 複数のPythonモジュールを作成する方法を確立する。
* [ ] [nalgebra](https://nalgebra.org) と NumPyを相互理利用する方法を習得する。
* [ ] GitHub Actionsを使って `whl` を作成し、`Release` のところに貼り付ける方法を習得する。

## System Requirements
* macOS Big Sur 11.5.1
* Apple M1
* rustc 1.53.0
* Python 3.8.2 ~

## Building From Source
```shell
$ git clone https://github.com/khirotaka/libbeta.git
$ cd libbeta/
$ python -m venv venv && souce venv/bin/activate
$ python setup.py install
```
