# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_clean_traceback_from_fields_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = io.StringIO()
    try:
        fields(object)
    except TypeError as exc:
        traceback.print_exception(exc, file=stdout)
    printed_traceback = stdout.getvalue()
    self.assertNotIn('AttributeError', printed_traceback)
    self.assertNotIn('__dataclass_fields__', printed_traceback)
