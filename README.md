# ansible-role-keepalived [![Build Status](https://www.travis-ci.com/izumimatsuo/ansible-role-keepalived.svg?branch=main)](https://www.travis-ci.com/izumimatsuo/ansible-role-keepalived)

CentOS 7 に導入した haproxy や nginx 等を keepalived を適用してクラスタ化する ansible role です。

- keepalived_cluster_info を設定する事で 1+1 (Active/Standby) クラスタを構成できる

## 設定項目

以下の設定項目は上書き可能。

| 項目名                   | デフォルト値| 説明               |
| ------------------------ | ----------- | ------------------ |
| keepalived_check_process | haproxy     | クラスタ化する対象 |
| keepalived_cluster_info  | None        | クラスタ情報設定 例 {virtual_ipaddr: xxx, check_interface: yyy} |
