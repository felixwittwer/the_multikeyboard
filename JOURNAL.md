---
title: "The Multikeyboard"
author: "Felix Wittwer (fegolix)"
description: "A split keyboard that can be a keyboard, macropad and steno keyboard at the same time"
created_at: "2024-07-29"
---

# Journal

Here you can see a documentation of the entire development process.

**Total hours spent: 2h**

## July 29th (2h)

### Session 1 (2h)

As a starting point for my custom split keyboard I decided to take some rough measurements of my hand an arrange the keys over it inside Inkscape. I decided on going with a full sized layout with the addition of a macropad and two rotary encoders on the left side. As someone who is coding on a daily bases it was important for me to have a full sized Layout and all the functions keys. If I decide that I do not need the numpad on the right side it can be easealy turned into a second macropad as on the left. For the microcontroler I decided on going with two ESP32-S3s because I use them a lot and they are relatively cheap. Besides that most dev boards also provide two USB ports so I can link them together in teh future via a simple USB C cable. I mean the plan is wireless but to make it futureproof. Pesides that I have lots of GPIO and enough computational power for running the firmware. (Plover for Steno might not be that easy to integrate)

<p float="left">
  <img src="./journal%20files/2025-07-29/LEFT.png" width=49% />
  <img src="./journal%20files/2025-07-29/RIGHT.png" width=49% />
</p>