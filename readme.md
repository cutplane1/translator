# (Trans)lator
*it's like [pot translator](https://github.com/pot-app/pot-desktop/blob/master/README_EN.md) but more minimalistic (or worse)*
![screenshot](https://github.com/cutplane1/translator/blob/main/Screenshot%202025-08-06%20222623.png)
GUI for translation services

## Config
Put trans.config file into root folder of executable or into %appdata% (this program supposed to be cross-platform, but not right now.)

_config example:_
```
deepl_api_key=aaaaaaaa-1337-1234-abcd-qwertyuiop42:fx
#google_api_is_free_btw

api=deepl
#api=google

window_hide_hotkey=Alt+K
translate_hotkey=Ctrl+Return

languages=en,ja
#languages=bg,da,en
```

## Building from source:
```
pip install -r requirements.txt
python build.py
```
