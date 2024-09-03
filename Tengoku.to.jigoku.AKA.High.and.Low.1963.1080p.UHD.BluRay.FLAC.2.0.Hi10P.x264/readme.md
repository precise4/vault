# Tengoku.to.jigoku.AKA.High.and.Low.1963.1080p.UHD.BluRay.FLAC.2.0.Hi10P.x264-💎

## Motovation

The current main circulating version is the CiNEFiLE which is based on the CC 1080p release and has super blown out colours and the encode is not optimised as well there is the UHD which is SDR to make it way easier to transfer plus uses the worse audio

### Notes

TOHO is really doing a number with their audio, they are clearly compressing it hard and using a digital version of the audio rather than the magnetic tape used in BFI also has the same effect with Seven Samurai but their psycovisual quality is insane with their remasters

## Method

1.
```sh
vspipe script.vpy -c y4m - | \
x264 - --demuxer y4m  -o out.mkv \
--output-depth 10 \
--no-mbtree \
--input-depth 10 \
--level 4.1 \
--preset veryslow \
--min-keyint 24 \
--vbv-bufsize 78125 \
--vbv-maxrate 62500 \
--rc-lookahead 250 \
--deblock -3:-3 \
--qcomp .6 \
--aq-mode 3 \
--aq-strength 0.8 \
--ipratio 1.4 \
--pbratio 1.3 \
--psy-rd 1.15 \
--bframes 16 \
--crf 16.7 \
--sar 1:1 \
--merange 32 \
--me umh \
--direct auto \
--no-dct-decimate \
--no-fast-pskip \
--subme 11 
```
see [script.vpy](./script.vpy)
2. MKVToolsNix mux
