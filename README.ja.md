# 概要

MicroPython 用の SparkFun **moto:bit** ドライバです

# 使い方

```python
motobit = MotoBit()

motobit.enable() # モータードライバを有効にします

l = motobit.left_motor() # モーターオブジェクトを取得します
r = motobit.right_motor(invert=True) # 極性を反転することもできます

l.forward(100) # 順回転します
r.reverse(50)  # 逆回転します

l.forward(0) # モーターを停止します
r.forward(0)

l.forward(-100) # マイナスを付けると逆に回転します
r.reverse(-50)

l.reverse(0) # モーターを停止します
r.reverse(0)

motobit.disable() # モータードライバを無効にします (モーターが回転していた場合は停止します)
```

# License

These codes are licensed under CC0.

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)
