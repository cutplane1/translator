# (Trans)lator
*like [pot translator](https://github.com/pot-app/pot-desktop/blob/master/README_EN.md) but more minimalistic (or worse)*
GUI for translation services

## Config
Put trans.config file into root folder of executable or into %appdata% (this program supposed to be cross-platform, but not right now.)

_config example:_
```
deepl_api_key=aaaaaaaa-1337-1234-abcd-qwertyuiop42:fx
google_api_key=whatever

api=deepl
#api=google

window_hide_hotkey=Alt+K
translate_hotkey=Ctrl+Return

languages=en,ja
```

## Installing from source:
```
pip install -r requirements.txt
python build.py
```