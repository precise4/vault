# Gentlemen.Prefer.Blondes.1953.1080p.BluRay.DD+.5.1.x264-💎

## Motovation

There was no high quality encode for this movie

## Method

1. Av1an
```
docker run --privileged -v "/mnt/library/:/videos" --user $(id -u):$(id -g) -it --rm masterofzen/av1an:master -i Gentlemen.Prefer.Blondes.1953.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv -e x264 -v "--level 4.1 --preset veryslow --min-keyint 24 --vbv-bufsize 78125 --vbv-maxrate 62500 --rc-lookahead 250 --me umh --merange 48 --direct auto --subme 11 --no-dct-decimate --no-fast-pskip --deblock -3:-3 --qcomp .65 --aq-mode 3 --aq-strength 0.8 --ipratio 1.4 --pbratio 1.3 --no-mbtree --psy-rd 1 --bframes 16" --target-quality 97 --ffmpeg "-vf 'crop=1480:1080:0:220'"
```
2. Mux with MKVToolsNix
