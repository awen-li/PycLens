# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_name_error_suggestions_do_not_trigger_for_long_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        somethingverywronghehehehehehe = None
        print(somethingverywronghe)
    try:
        f()
    except NameError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertNotIn('somethingverywronghehe', err.getvalue())
