# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Rot13UtilTest_test_rot13_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    infile = io.StringIO('Gb or, be abg gb or, gung vf gur dhrfgvba')
    outfile = io.StringIO()
    encodings.rot_13.rot13(infile, outfile)
    outfile.seek(0)
    plain_text = outfile.read()
    self.assertEqual(plain_text, 'To be, or not to be, that is the question')
