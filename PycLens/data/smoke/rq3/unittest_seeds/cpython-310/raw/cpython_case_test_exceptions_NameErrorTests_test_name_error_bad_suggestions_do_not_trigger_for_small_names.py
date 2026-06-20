# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_name_error_bad_suggestions_do_not_trigger_for_small_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vvv = mom = w = id = pytho = None
    with self.subTest(name='b'):
        try:
            b
        except NameError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertNotIn('you mean', err.getvalue())
        self.assertNotIn('vvv', err.getvalue())
        self.assertNotIn('mom', err.getvalue())
        self.assertNotIn("'id'", err.getvalue())
        self.assertNotIn("'w'", err.getvalue())
        self.assertNotIn("'pytho'", err.getvalue())
    with self.subTest(name='v'):
        try:
            v
        except NameError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertNotIn('you mean', err.getvalue())
        self.assertNotIn('vvv', err.getvalue())
        self.assertNotIn('mom', err.getvalue())
        self.assertNotIn("'id'", err.getvalue())
        self.assertNotIn("'w'", err.getvalue())
        self.assertNotIn("'pytho'", err.getvalue())
    with self.subTest(name='m'):
        try:
            m
        except NameError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertNotIn('you mean', err.getvalue())
        self.assertNotIn('vvv', err.getvalue())
        self.assertNotIn('mom', err.getvalue())
        self.assertNotIn("'id'", err.getvalue())
        self.assertNotIn("'w'", err.getvalue())
        self.assertNotIn("'pytho'", err.getvalue())
    with self.subTest(name='py'):
        try:
            py
        except NameError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertNotIn('you mean', err.getvalue())
        self.assertNotIn('vvv', err.getvalue())
        self.assertNotIn('mom', err.getvalue())
        self.assertNotIn("'id'", err.getvalue())
        self.assertNotIn("'w'", err.getvalue())
        self.assertNotIn("'pytho'", err.getvalue())
