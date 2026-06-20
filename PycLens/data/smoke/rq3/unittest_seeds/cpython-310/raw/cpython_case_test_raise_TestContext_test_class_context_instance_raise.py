# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_class_context_instance_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = IndexError
    try:
        try:
            raise context
        except:
            raise OSError()
    except OSError as e:
        self.assertIsNot(e.__context__, context)
        self.assertIsInstance(e.__context__, context)
    else:
        self.fail('No exception raised')
