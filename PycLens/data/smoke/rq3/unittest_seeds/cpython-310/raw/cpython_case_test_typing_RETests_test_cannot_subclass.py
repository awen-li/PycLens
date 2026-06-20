# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_cannot_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError) as ex:

        class A(typing.Match):
            pass
    self.assertEqual(str(ex.exception), "type 're.Match' is not an acceptable base type")
