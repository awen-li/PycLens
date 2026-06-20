# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestActionsReturned_test_misc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    action = parser.add_argument('--foo', nargs='?', const=42, default=84, type=int, choices=[1, 2], help='FOO', metavar='BAR', dest='baz')
    self.assertEqual(action.nargs, '?')
    self.assertEqual(action.const, 42)
    self.assertEqual(action.default, 84)
    self.assertEqual(action.type, int)
    self.assertEqual(action.choices, [1, 2])
    self.assertEqual(action.help, 'FOO')
    self.assertEqual(action.metavar, 'BAR')
    self.assertEqual(action.dest, 'baz')
