import vapoursynth as vs
import awsmfunc as awf
core = vs.core

src = core.ffsm2.Source("The.Terminator.1984.1080p.Blu-ray.Remux.AVC.FLAC1.0-CiNEPHiLES.mkv")
crop = src.core.Crop(top=20,bottom=20)
bb = awf.bb(top=1,bottom=1)
bb.set_output(0)
