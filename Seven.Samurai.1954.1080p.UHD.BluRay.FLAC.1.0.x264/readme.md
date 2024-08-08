# Seven.Samurai.1954.1080p.UHD.BluRay.FLAC.1.0.x264

## Motovation

This in perticular has no 1080p version for the new 4k Toho remaster so tried to improve the quality of the other circulating 1080p REMUXs and encodes all mostly from the CC release

## Method

1. VapourSynth - vspipe
2. Piped to x264
```
cabac=1 / ref=5 / deblock=1:-3:-3 / analyse=0x3:0x133 / me=umh / subme=11 / psy=1 / psy_rd=1.00:0.00 / mixed_ref=1 / me_range=48 / chroma_me=1 / trellis=2 / 8x8dct=1 / cqm=0 / deadzone=21,11 / fast_pskip=0 / chroma_qp_offset=-2 / threads=9 / lookahead_threads=2 / sliced_threads=0 / nr=0 / decimate=0 / interlaced=0 / bluray_compat=0 / constrained_intra=0 / bframes=16 / b_pyramid=2 / b_adapt=2 / b_bias=0 / direct=3 / weightb=1 / open_gop=0 / weightp=2 / keyint=250 / keyint_min=24 / scenecut=40 / intra_refresh=0 / rc_lookahead=250 / rc=crf / mbtree=0 / crf=17.0 / qcomp=0.60 / qpmin=0 / qpmax=69 / qpstep=4 / vbv_maxrate=62500 / vbv_bufsize=78125 / crf_max=0.0 / nal_hrd=none / filler=0 / ip_ratio=1.40 / pb_ratio=1.30 / aq=3:0.70
```
3. Mux with MKVToolsNix
