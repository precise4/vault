import vapoursynth as vs
core = vs.core

clip = core.ffms2.Source("Cinema.Paradiso.1988.Director's.Cut.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv")
crp = core.std.Crop(clip,left=60,right=60)
crp.set_output(0)
