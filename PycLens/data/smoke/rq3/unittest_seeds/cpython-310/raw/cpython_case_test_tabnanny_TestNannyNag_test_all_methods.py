# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestNannyNag_test_all_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(tabnanny.NannyNag(0, 'foo', 'bar'), {'lineno': 0, 'msg': 'foo', 'line': 'bar'}), (tabnanny.NannyNag(5, 'testmsg', 'testline'), {'lineno': 5, 'msg': 'testmsg', 'line': 'testline'})]
    for (nanny, expected) in tests:
        line_number = nanny.get_lineno()
        msg = nanny.get_msg()
        line = nanny.get_line()
        with self.subTest(line_number=line_number, expected=expected['lineno']):
            self.assertEqual(expected['lineno'], line_number)
        with self.subTest(msg=msg, expected=expected['msg']):
            self.assertEqual(expected['msg'], msg)
        with self.subTest(line=line, expected=expected['line']):
            self.assertEqual(expected['line'], line)
