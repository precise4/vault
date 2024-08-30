# Triangle.of.Sadness.2022.1080p.UHD.BluRay.DD+.7.1.x264-💎

## Motovation

The UHD BluRay is SDR with better quality vs FHD BluRay and can run it at 10bit

## Method

1. see [./script.vpy](./script.vpy)
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
