# sublimeMQL5compile
MetaTrader5 (MQL5) compile for Sublime Text 3

---

sublimeMQL5compile compiles [MQL5(MetaTrader5)](http://www.metaquotes.net/en/metatrader5) by a [SublimeText 3](https://www.sublimetext.com/3). And an error log is indicated automatically.  

**[Screenshot]**

![sublimeMQL5compile](http://cdn-ak.f.st-hatena.com/images/fotolife/m/mofoolog/20160423/20160423192051.gif "sublimeMQL5compile-gif")

All files with which I deal by a MetaEditor (`.mq5` , `.mqh`) can be compiled.  It's also possible to compile the file which imported `.dll` and `.ex5`.  

&nbsp;

## Installation procedure

1. After whether it's installed in gitclorn downloads a zip file, a zip file is defrosted.

2. The place a sublimeMQL5compile folder establishes is in the `<Your>\<setting>\Sublime Text 3\Packages\` directory.

※ It doesn't correspond to Package Control for the moment.  

&nbsp;

## Setting

1. `sublimeMQL5compile.sublime-settings` filing in the `sublimeMQL5compile` directory is held.

2. A complete path of its `metaeditor64.exe` is input to a `"compiler_path"` space.

Initialization is below.  

```json
{
    "compiler_path": "C:\\Program Files\\MetaTrader 5\\metaeditor64.exe"
}
```

The PATH input when using Wine by Mac and Linux. (I'm not inspecting.)

```json
{
    "compiler_path": "/home/<Your Name>/.wine/drive_c/Program Files/MetaTrader 5/metaeditor64.exe"
}
```

&nbsp;

## How to use

* **Shortcutkey : [ `Ctrl` + `5` ]**

or

* A Control Panel is opened. It's input to a Control Panel with `mql`. `MQL5 Compile` shown to a Control Panel is chosen and carried out.

&nbsp;

## Others

日本語のREADMEは[こちら](https://github.com/rchjp/sublimeMQL5compile/blob/master/README(ja).md)です。  

&nbsp;
