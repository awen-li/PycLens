# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ExceptionContextTestCase_test_get_extended_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    parser.read_string('\n        [Paths]\n        home_dir: /Users\n        my_dir: ${home_dir1}/lumberjack\n        my_pictures: ${my_dir}/Pictures\n        ')
    cm = self.assertRaises(configparser.InterpolationMissingOptionError)
    with cm:
        parser.get('Paths', 'my_dir')
    self.assertIs(cm.exception.__suppress_context__, True)
