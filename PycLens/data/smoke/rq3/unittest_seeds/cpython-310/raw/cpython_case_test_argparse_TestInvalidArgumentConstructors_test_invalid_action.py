# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_invalid_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertValueError('-x', action='foo')
    self.assertValueError('foo', action='baz')
    self.assertValueError('--foo', action=('store', 'append'))
    parser = argparse.ArgumentParser()
    with self.assertRaises(ValueError) as cm:
        parser.add_argument('--foo', action='store-true')
    self.assertIn('unknown action', str(cm.exception))
