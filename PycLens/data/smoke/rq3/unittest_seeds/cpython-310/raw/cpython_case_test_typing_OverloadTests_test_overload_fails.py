# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: OverloadTests_test_overload_fails

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing import overload
    with self.assertRaises(RuntimeError):

        @overload
        def blah():
            pass
        blah()
