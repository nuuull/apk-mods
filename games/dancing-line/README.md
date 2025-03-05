# Dancing Line Patch

Currently compatible with `Dancing Line v2.7.74.00` from taptap.cn

## Features

- Unlock all levels
- Unlock all skins
- Unlock all props
- Premium unlocked
- Free store
- Remove GDPR

## How to use

Make sure both java and python is installed on your machine.

Decompile apk with [apktool](https://github.com/iBotPeaches/Apktool)

```sh
java -jar apktool.jar d <apkfile> -o base
```

With python, run this command.

```sh
python3 ./patch.py base
```

Recompile it with apktool

```sh
java -jar apktool.jar b base -o base_mod.apk
```

Sign the apk using [uber-apk-singer](https://github.com/patrickfav/uber-apk-signer)

```sh
java -jar uber-apk-signer.jar -a base_mod.apk -o base_mod_debug.apk
```

Then install `base_mod_debug.apk` in your device.