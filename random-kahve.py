#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

isimler = ["Oğuzhan 🤬 ","Yasin 😎 "]
taraf = ["sağ", "sol"]

print str(isimler[random.getrandbits(1)]) + " " + str(taraf[random.getrandbits(1)]) + "daki kahveyi içer. ☕️"

