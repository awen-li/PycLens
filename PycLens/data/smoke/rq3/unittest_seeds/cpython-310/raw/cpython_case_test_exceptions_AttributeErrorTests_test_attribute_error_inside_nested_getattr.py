# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_attribute_error_inside_nested_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        bluch = 1

    class B:

        def __getattribute__(self, attr):
            a = A()
            return a.blich
    try:
        B().something
    except AttributeError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn('Did you mean', err.getvalue())
    self.assertIn('bluch', err.getvalue())
