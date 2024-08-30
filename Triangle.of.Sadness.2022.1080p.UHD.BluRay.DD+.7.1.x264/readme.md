# Triangle.of.Sadness.2022.1080p.UHD.BluRay.DD+.7.1.x264-💎

## Motovation

Noticed that most encodes for this movie incorrectly crop by removing one line of pixels and base on the FHD BluRay 

The FHD has 4 lines of dirty lines on the top and bottom while the 4k has none so it would be better to fill the border 1 pixel from non dirty lines to gain that extra line on the bottom or top

So 

Crop 1920:804:0:138 -> Fix Border 4 top 3 bottom < Crop 3840:1612:0:274 -> Fill border top 1 -> Resize 1920x806

IMO 

And because the 4K UHD BluRay is SDR this makes this a walk in the park

Comparing the UHD with the FHD sources are so close psycovisually that the only thing that matters is the stuff stated above

## Method

1. see [./script.vpy](Triangle.of.Sadness.2022.1080p.UHD.BluRay.DD+.7.1.x264/script.vpy)
```bash
vspipe enc.vpy -c y4m - | \
x264 - --demuxer y4m -o out.mkv \
--level 4.1 \
--preset veryslow \
--min-keyint 24 \
--vbv-bufsize 78125 \
--vbv-maxrate 62500 \
--rc-lookahead 250 \
--me umh \
--merange 48 \
--direct auto \
--subme 11 \
--no-dct-decimate \
--no-fast-pskip \
--deblock -3:-3 \
--qcomp .65 \
--aq-mode 3 \
--aq-strength 0.8 \
--ipratio 1.4 \
--pbratio 1.3 \
--no-mbtree \
--psy-rd 1.05 \
--bframes 16 \
--crf 16 \
--zone 205254,211598,q=20 \
--sar 1:1
```
2. Encode audio with DEE/DEEW
3. Rip WEB subs
4. Sync WEB subs
5. Mux with MKToolsNix
