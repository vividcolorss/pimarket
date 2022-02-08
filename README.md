# PiMarket
App Store For The Raspberry Pi.
## Compatibility List
Debian-based: supported.

Arch-based: Not supported.

Not ARM, Gentoo, etc: Not supported.

## Installing and updating
To install, use this command:

```bash
wget -qO- https://raw.githubusercontent.com/MakePie/pimarket/main/install | bash
```

To update, use these commands:
```bash
sudo rm -rf /usr/bin/pimarket
rm -rf ~/pimarket
wget -qO- https://raw.githubusercontent.com/MakePie/pimarket/main/install | bash
```
## Licensing
PiMarket is is licensed under GPLv3. view the LICENSE file for more info.
