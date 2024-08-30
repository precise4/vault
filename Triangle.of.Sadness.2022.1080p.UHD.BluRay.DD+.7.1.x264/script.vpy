import vapoursynth as vs
core = vs.core
import awsmfunc as awf

clip = core.ffms2.Source("Triangle.of.Sadness.2022.UHD.BluRay.2160p.TrueHD.Atmos.7.1.SDR.HEVC.HYBRID.REMUX-FraMeSToR.mkv")
crp = core.std.Crop(clip,top=276,bottom=276)
bit16 = core.fmtc.bitdepth(crp, bits=16)
fb = awf.fb(bit16,bottom=1)
resize = fb.resize.Spline36(1920, 804, dither_type="error_diffusion")
bit8 = core.fmtc.bitdepth(resize,bits=10)
bit8.set_output(0)
