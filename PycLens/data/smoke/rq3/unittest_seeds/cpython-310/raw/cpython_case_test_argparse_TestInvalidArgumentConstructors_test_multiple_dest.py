# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_multiple_dest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='foo')
    with self.assertRaises(ValueError) as cm:
        parser.add_argument('bar', dest='baz')
    self.assertIn('dest supplied twice for positional argument', str(cm.exception))
