# sublimeMQL5compile
MetaTrader5 (MQL5) compile for Sublime Text 3

---

sublimeMQL5compile は [MQL5 (MetaTrader)](http://www.metaquotes.net/en/metatrader5) を [Sublime Text 3](https://www.sublimetext.com/3) でコンパイルし、エラー確認ログを自動表示するプラグインです。 

**<スクリーンショット>**

![sublimeMQL5compile](http://cdn-ak.f.st-hatena.com/images/fotolife/m/mofoolog/20160423/20160423192051.gif?1461406887 "sublimeMQL5compile-gif")

MetaEditor64 で扱う全てのファイル (`.mq5` , `.mqh`) がコンパイル可能です。また、`.dll` や `.ex5` を import した場合も動作します。  

&nbsp;

## インストール

clorn してインストールするか、 zip をダウンロード･解凍してできた `sublimeMQL5compile` を `$HOME$\AppData\Roaming\Sublime Text 3\Packages\` ディレクトリ以下 (ご自身の環境に合わせて読み替えてください) に置いてください。  

※ 今のところ Package Control には対応していません。  

&nbsp;

## 設定

`sublimeMQL5compile` ディレクトリ内の `sublimeMQL5compile.sublime-settings` ファイルを開き、`"compiler_path"` 欄にご自身の `metaeditor64.exe` の絶対パスを入力してください。 

初期設定は以下になっています。  

```json
{
    "compiler_path": "C:\\Program Files\\MetaTrader 5\\metaeditor64.exe"
}
```

Mac や Linux で Wine を介した MetaEditor の PATH を入力する場合の例 (未検証)

```json
{
    "compiler_path": "/home/<Your Name>/.wine/drive_c/Program Files/MetaTrader 5/metaeditor64.exe"
}
```

&nbsp;

## 使い方

コンパイルしたいファイルを保存し、以下の操作でコンパイルからエラー確認ログの表示まで自動で行います。  

* ショートカットキー : [ `Ctrl` + `5` ]

または

* コントロールパネルを開き `mql` と入力して表示される `MQL5 Compile` を選択実行

&nbsp;

## その他

`sublimeMQL4compile` は Windows で動作確認済みですが、wine を利用した Mac や Linux 環境での動作確認はしていません。  

`"compiler_path"` に `metaeditor64.exe` の wine を介した絶対パスを入力すれば動作するのではないかと思ってはいますが、wine 環境を持っていないので分かりません。 

どなたか Mac や Linux で使った方が居ましたら、ご一報くださいm(_ _)m

&nbsp;
