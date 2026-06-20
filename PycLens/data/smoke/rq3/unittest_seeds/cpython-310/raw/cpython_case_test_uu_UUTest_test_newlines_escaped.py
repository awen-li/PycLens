# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_newlines_escaped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inp = io.BytesIO(plaintext)
    out = io.BytesIO()
    filename = 'test.txt\n\roverflow.txt'
    safefilename = b'test.txt\\n\\roverflow.txt'
    uu.encode(inp, out, filename)
    self.assertIn(safefilename, out.getvalue())
