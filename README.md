hmmTagging
==========

useage:
python ./src/main.py < ./data/entrain

(今までに正解した単語数):(今までの全単語数) 精度
の列が出力されます

既知の問題点
・entestの末尾が###/###になっているため、###/###で区切ると最後の文が空文字列になってしまい、コケる

・学習のためのファイルentrainが可変、評価のためのentestが固定されている。entrainを固定してentestを可変にしないといけない
