# OtakuHayakuchiYamero
## 概要
人が聞き取りやすいと言われる5文字/秒を超えると怒られるアプリ

## 必要ライブラリ
すべてpipで入ります。
- azure-cognitiveservices-speech
- json
- requests
- PySimpleGUI

## 使用方法
api_keys.jsonを以下の内容でトップディレクトリに作成。
```api_keys.json
{
    "key": "azure speechのサブスクリプションキー",
    "region": "azure 使用リージョン",
    "app_id: "gooラボのひらがな化APIキー"
}
```
<a href="http://www.goo.ne.jp/">
<img src="//u.xgoo.jp/img/sgoo.png" alt="supported by goo"
title="supported by goo">
</a>