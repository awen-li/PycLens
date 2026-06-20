# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_check_unused_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CheckAllUsedFormatter(string.Formatter):

        def check_unused_args(self, used_args, args, kwargs):
            unused_args = set(kwargs.keys())
            unused_args.update(range(0, len(args)))
            for arg in used_args:
                unused_args.remove(arg)
            if unused_args:
                raise ValueError('unused arguments')
    fmt = CheckAllUsedFormatter()
    self.assertEqual(fmt.format('{0}', 10), '10')
    self.assertEqual(fmt.format('{0}{i}', 10, i=100), '10100')
    self.assertEqual(fmt.format('{0}{i}{1}', 10, 20, i=100), '1010020')
    self.assertRaises(ValueError, fmt.format, '{0}{i}{1}', 10, 20, i=100, j=0)
    self.assertRaises(ValueError, fmt.format, '{0}', 10, 20)
    self.assertRaises(ValueError, fmt.format, '{0}', 10, 20, i=100)
    self.assertRaises(ValueError, fmt.format, '{i}', 10, 20, i=100)
