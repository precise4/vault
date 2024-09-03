import vapoursynth as vs
core = vs.core
import awsmfunc as awf

clip = core.ffms2.Source("Tengoku.to.jigoku.AKA.High.and.Low.1963.2160p.UHD.Blu-ray.REMUX.SDR.HEVC.DTS-HD.MA.4.0-CiNEPHiLES.mkv")
crp = core.std.Crop(clip,top=262,bottom=262)
hbit = core.fmtc.bitdepth(crp,bits=16)
fb = awf.fb(hbit,top=1,bottom=1)
resize = fb.resize.Spline36(1920, 818, dither_type="error_diffusion")
lbit = resize.fmtc.bitdepth(bits=10)
lbit.set_output(0)
