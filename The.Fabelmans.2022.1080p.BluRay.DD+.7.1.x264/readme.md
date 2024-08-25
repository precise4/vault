# The.Fabelmans.2022.1080p.BluRay.DD+.7.1.x264-💎

## Motovation

There was not curculating remux or high quality encode for this movie

## Method

1. VapourSynth - vspipe
2. Piped to x264
```
x264 --level 4.1 --preset veryslow --min-keyint 24 --vbv-bufsize 78125 --vbv-maxrate 62500 --rc-lookahead 250 --me umh --merange 48 --direct auto --subme 11 --no-dct-decimate --no-fast-pskip --deblock -3:-3 --qcomp .6 --aq-mode 3 --aq-strength 1 --ipratio 1.4 --pbratio 1.3 --no-mbtree --psy-rd 1 --bframes 16 --crf 18.3 -o enc.h264 --demuxer y4m -
```
3. Mux with MKVToolsNix
