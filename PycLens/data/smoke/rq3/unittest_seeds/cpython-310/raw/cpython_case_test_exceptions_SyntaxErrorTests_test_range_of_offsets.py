# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: SyntaxErrorTests_test_range_of_offsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [(('bad.py', 1, 2, 'abcdefg', 1, 7), dedent('\n               File "bad.py", line 1\n                 abcdefg\n                  ^^^^^\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 2, 'abcdefg', 1, 3), dedent('\n               File "bad.py", line 1\n                 abcdefg\n                  ^\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 2, 'abcdefg', 1, -2), dedent('\n               File "bad.py", line 1\n                 abcdefg\n                  ^\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 4, 'abcdefg', 1, 2), dedent('\n               File "bad.py", line 1\n                 abcdefg\n                    ^\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, -4, 'abcdefg', 1, -2), dedent('\n               File "bad.py", line 1\n                 abcdefg\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, -4, 'abcdefg', 1, -5), dedent('\n               File "bad.py", line 1\n                 abcdefg\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 0, 'abcdefg', 1, 0), dedent('\n               File "bad.py", line 1\n                 abcdefg\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 0, 'abcdefg', 1, 5), dedent('\n               File "bad.py", line 1\n                 abcdefg\n             SyntaxError: bad bad\n             ')), (('bad.py', 1, 2, 'abcdefg', 1, 100), dedent('\n               File "bad.py", line 1\n                 abcdefg\n                  ^^^^^^\n             SyntaxError: bad bad\n             '))]
    for (args, expected) in cases:
        with self.subTest(args=args):
            try:
                raise SyntaxError('bad bad', args)
            except SyntaxError as exc:
                with support.captured_stderr() as err:
                    sys.__excepthook__(*sys.exc_info())
                self.assertIn(expected, err.getvalue())
                the_exception = exc
