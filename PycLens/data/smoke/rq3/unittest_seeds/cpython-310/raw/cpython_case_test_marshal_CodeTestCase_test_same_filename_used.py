# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: CodeTestCase_test_same_filename_used

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'def f(): pass\ndef g(): pass'
    co = compile(s, 'myfile', 'exec')
    co = marshal.loads(marshal.dumps(co))
    for obj in co.co_consts:
        if isinstance(obj, types.CodeType):
            self.assertIs(co.co_filename, obj.co_filename)
