# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimetypesCliTestCase_test_guess_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    type_info = self.mimetypes_cmd('-l', 'foo.pic')
    eq(type_info, 'type: image/pict encoding: None')
    type_info = self.mimetypes_cmd('foo.pic')
    eq(type_info, "I don't know anything about type foo.pic")
