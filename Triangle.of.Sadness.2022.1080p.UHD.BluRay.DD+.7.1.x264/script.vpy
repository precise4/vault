import vapoursynth as vs
core = vs.core
import awsmfunc as awf
  
clip = core.ffms2.Source("Triangle.of.Sadness.2022.UHD.BluRay.2160p.TrueHD.Atmos.7.1.SDR.HEVC.HYBRID.REMUX-FraMeSToR.mkv")
crp = core.std.Crop(clip,top=274,bottom=274)
fb = awf.fb(crp, top=1,bottom=1)
resize = fb.resize.Spline36(1920, 806, dither_type="error_diffusion")
resize.set_output(0)
