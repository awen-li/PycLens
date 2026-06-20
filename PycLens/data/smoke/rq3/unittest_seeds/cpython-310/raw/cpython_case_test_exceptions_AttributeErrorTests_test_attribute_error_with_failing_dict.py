# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_attribute_error_with_failing_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T:
        bluch = 1

        def __dir__(self):
            raise AttributeError('oh no!')
    try:
        T().blich
    except AttributeError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertNotIn('blech', err.getvalue())
    self.assertNotIn('oh no!', err.getvalue())
