# Cinema.Paradiso.1988.Director's.Cut.1080p.BluRay.DD+.5.1.x264

## Motovation

## Method

1. vs
2. x264
3. mkvtoolsnix

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
--aq-mode 2 \
--aq-strength 0.8 \
--ipratio 1.4 \
--pbratio 1.3 \
--no-mbtree \
--psy-rd 1.00:0.15 \
--qpmin 10 \
--bframes 16 \
--crf 22 \
--sar 1:1 \
--zones 246104,249625,qp=27
```
