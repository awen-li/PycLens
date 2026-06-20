# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binhex.py
# case: BinHexTestCase_test_binhex_line_endings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.fname1, 'wb') as f:
        f.write(self.DATA)
    binhex.binhex(self.fname1, self.fname2)
    with open(self.fname2, 'rb') as fp:
        contents = fp.read()
    self.assertNotIn(b'\n', contents)
