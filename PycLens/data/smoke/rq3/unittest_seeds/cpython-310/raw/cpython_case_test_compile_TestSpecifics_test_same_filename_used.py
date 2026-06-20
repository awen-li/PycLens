# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_same_filename_used

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'def f(): pass\ndef g(): pass'
    c = compile(s, 'myfile', 'exec')
    for obj in c.co_consts:
        if isinstance(obj, types.CodeType):
            self.assertIs(obj.co_filename, c.co_filename)
