# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestBooleanOptionalAction_test_const

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    with self.assertRaises(TypeError) as cm:
        parser.add_argument('--foo', const=True, action=argparse.BooleanOptionalAction)
    self.assertIn("got an unexpected keyword argument 'const'", str(cm.exception))
