# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_instance_docs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cm_docstring = mycontext.__doc__
    obj = mycontext()
    self.assertEqual(obj.__doc__, cm_docstring)
