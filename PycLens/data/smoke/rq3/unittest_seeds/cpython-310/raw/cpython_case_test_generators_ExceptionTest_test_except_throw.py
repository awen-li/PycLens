# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_except_throw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def store_raise_exc_generator():
        try:
            self.assertEqual(sys.exc_info()[0], None)
            yield
        except Exception as exc:
            self.assertEqual(sys.exc_info()[0], ValueError)
            self.assertIsNone(exc.__context__)
            yield
            self.assertEqual(sys.exc_info()[0], ValueError)
            yield
            raise
    make = store_raise_exc_generator()
    next(make)
    try:
        raise ValueError()
    except Exception as exc:
        try:
            make.throw(exc)
        except Exception:
            pass
    next(make)
    with self.assertRaises(ValueError) as cm:
        next(make)
    self.assertIsNone(cm.exception.__context__)
    self.assertEqual(sys.exc_info(), (None, None, None))
