# the_multikeyboard
A custom keyboard that does it all. Standard keyboard, steno keyboard and macropad.

## About the project

I am actually someone that is currently learning steno myself and I already have a matching keyboard for that. Besides I also have a Macropad and of course a normal keyboard. You counted right I have three keyboards on my desk and this is bothering me. Thats why I decided to build my first own custom keyboard that combines all three. **THE MULTIKEYBOARD** is a keyboard that consists of a macropad (on the right side), a full sized keyboard (everything else :]) and a section in the middle that can be used for stenography typing. 

## The project

### Option 1 (normal version)

The standard version of the Keyboard consists mainly out of the two PCBs and a 3D printed case.

### Renders

### PCB and schematics

### CAD

### Option 2 (if you dont have a 3D printer with a large buildvolume)

Instead of printing a case for the keyboard this version uses multiple PCBs so oyu are able to builad a sminimalistic and slick version of the keyboard witgout needing to print parts.

### Renders

### PCB and schematics

### CAD

## BOM

### BOM Option 1 (normal)

| part name | amount | price | link | note |
| --------- | ------ | ----- | ---- | ---- |
| Rotary encoder EC24 | 2 | 1.32 USD | https://de.aliexpress.com/item/1005006894514858.html?spm=a2g0o.productlist.main.2.7f3151dbLgFP04&algo_pvid=9129263f-29b5-45c7-9270-6505827be216&pdp_ext_f=%7B%22order%22%3A%2212%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | look out for the EC numer it is importent for the resolution of the encoder 
| Keyswitches | 120 (54+66) | 21.12 USD | https://de.aliexpress.com/item/1005006091988869.html?spm=a2g0o.productlist.main.11.54f5116676VXSy&algo_pvid=5683f259-8333-46de-8018-3bd4b785d0da&pdp_ext_f=%7B%22order%22%3A%22205%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A
| Keycaps | 120 (54+66) | 7.88 USD| https://de.aliexpress.com/item/32842379355.html?spm=a2g0o.productlist.main.13.19dd3939CSNGEC&algo_pvid=53737e4f-6131-4c20-955c-c0b48daf2625&pdp_ext_f=%7B%22order%22%3A%2286%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | please look where you can buy matching quantities 120 Keys is larger than normal keyboard size
| hotswap socets | 120 (54+66) | 12.92 USD | https://de.aliexpress.com/item/1005007476614771.html?gatewayAdapt=glo2deu | ---- |
| diodes SOD-123 | 120 (54+66) | 2.74 USD | https://de.aliexpress.com/item/1005004664827360.html?spm=a2g0o.productlist.main.2.730d3027Xsqwva&algo_pvid=82ad0fed-5a2a-47ba-b2ca-b1062569d1e1&pdp_ext_f=%7B%22order%22%3A%2215%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | ---- |
| ESP32-S3 | 2 | 15.12 USD | https://de.aliexpress.com/item/1005008209644199.html?spm=a2g0o.productlist.main.2.450b6619Wqsygq&algo_pvid=b6d6b6cd-dfe1-4b51-a066-5df1bfd08fe2&pdp_ext_f=%7B%22order%22%3A%2263%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | ---- |
| PCB LEFT Main | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB RIGHT BACK | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |

<br>

### BOM Option 2 (without 3D printing)

| part name | amount | price | link | note |
| --------- | ------ | ----- | ---- | ---- |
| Rotary encoder EC24 | 2 | 1.32 USD | https://de.aliexpress.com/item/1005006894514858.html?spm=a2g0o.productlist.main.2.7f3151dbLgFP04&algo_pvid=9129263f-29b5-45c7-9270-6505827be216&pdp_ext_f=%7B%22order%22%3A%2212%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | look out for the EC numer it is importent for the resolution of the encoder 
| Keyswitches | 120 (54+66) | 21.12 USD | https://de.aliexpress.com/item/1005006091988869.html?spm=a2g0o.productlist.main.11.54f5116676VXSy&algo_pvid=5683f259-8333-46de-8018-3bd4b785d0da&pdp_ext_f=%7B%22order%22%3A%22205%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A
| Keycaps | 120 (54+66) | 7.88 USD| https://de.aliexpress.com/item/32842379355.html?spm=a2g0o.productlist.main.13.19dd3939CSNGEC&algo_pvid=53737e4f-6131-4c20-955c-c0b48daf2625&pdp_ext_f=%7B%22order%22%3A%2286%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | please look where you can buy matching quantities 120 Keys is larger than normal keyboard size
| hotswap socets | 120 (54+66) | 12.92 USD | https://de.aliexpress.com/item/1005007476614771.html?gatewayAdapt=glo2deu | ---- |
| diodes SOD-123 | 120 (54+66) | 2.74 USD | https://de.aliexpress.com/item/1005004664827360.html?spm=a2g0o.productlist.main.2.730d3027Xsqwva&algo_pvid=82ad0fed-5a2a-47ba-b2ca-b1062569d1e1&pdp_ext_f=%7B%22order%22%3A%2215%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | ---- |
| ESP32-S3 | 2 | 15.12 USD | https://de.aliexpress.com/item/1005008209644199.html?spm=a2g0o.productlist.main.2.450b6619Wqsygq&algo_pvid=b6d6b6cd-dfe1-4b51-a066-5df1bfd08fe2&pdp_ext_f=%7B%22order%22%3A%2263%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | ---- |
| M3 Standofs/Spacers 4mm | 20 | 1.17 USD | https://de.aliexpress.com/item/1005004818052787.html?spm=a2g0o.productlist.main.8.4a7b4f352twTGj&aem_p4p_detail=2025073014352518455665963560002602915&algo_pvid=a9922ca1-e556-4d76-92f7-36b56bf0b6c7&pdp_ext_f=%7B%22order%22%3A%22227%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=2025073014352518455665963560002602915_2 | ---- |
| M3 flathead screws | 20 | 1.17 USD | https://de.aliexpress.com/item/1005007593793297.html?spm=a2g0o.productlist.main.10.540267208LetqA&algo_pvid=0ff48590-2032-4a10-964f-19ffd751115e&pdp_ext_f=%7B%22order%22%3A%2257%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | ---- | 
| PCB LEFT TOP | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB LEFT Main | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB LEFT BACK | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB RIGHT TOP | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB RIGHT Main | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |
| PCB RIGHT BACK | 1 | ~ 5 USD |  https://jlcpcb.com/ | price is subject to JLCs review |

## Credits

**Thanks for the detailed 3D models!**

Gateron keyswitch 3D model: https://www.gateron.com/pages/3d

Keycap 3D model: https://grabcad.com/library/dsa-keycap-for-cherry-mx-switches-1

ESP32-S3 (before I modified it): https://grabcad.com/library/esp32-s3-module-for-pcb-preview-1