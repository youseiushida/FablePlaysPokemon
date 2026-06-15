あなたには任天堂スイッチのゲームをクリアしてもらいます。

latest.pngには常に更新される最新の任天堂スイッチの画面があります。
magichidというcliツールによって操作を行えます（使用するポートは COM5です）
durationの調整や連続入力を工夫してゲームに合わせて効率的に操作することを心がけてください。
操作と画面確認を繰り返して全クリを目指してください。必要に応じて効率的な攻略のために操作用のマクロを組んでもOKです。コマンド実行時には　Get-Date　で前後を囲って、時刻を取得ことを強く推奨します。ゲーム内の特定の操作を効率よく行えているかを測定するのには時刻の把握が必須であり、クリアにかかる時間は短いほど良いからです。


# 操作方法

まずニュートラル送信:

```powershell
magichid --port COM5 --json horipad release-all
```

Aボタンを押す:

```powershell
magichid --port COM5 --json horipad hold --button a --duration-ms 100
```

短すぎて反応しない場合は長めに:

```powershell
magichid --port COM5 --json horipad hold --button a --duration-ms 500
```

十字キー右を200ms:

```powershell
magichid --port COM5 --json horipad dpad --direction right --duration-ms 200
```

左スティックを右に500ms:

```powershell
magichid --port COM5 --json horipad stick-left --x 1.0 --y 0.0 --duration-ms 500
```

使えるボタン名は小文字です:

```text
y b a x l r zl zr minus plus l_stick r_stick home capture
```

十字キー方向:

```text
up up_right right down_right down down_left left up_left center
```

注意点: `--json` はこのCLIではグローバルオプションなので、`horipad` の前に置くのが安全です。また、CLIは終了時に `release-all` を送る実装なので、押しっぱなし用途は `press` より `hold --duration-ms ...` を使ってください。

Universalに戻す場合:

```powershell
magichid --port COM5 --json identity set --profile universal
```

`device not ready` や `not responding` が出る場合は、COM違い、シリアルを他アプリが掴んでいる、USB HID側がSwitch/PCに挿さっていない、Switchがスリープ中、プロファイル切替後にCOM番号が変わった、の順で確認してください。