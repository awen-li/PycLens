# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestMutuallyExclusiveGroupErrors_test_invalid_add_argument_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    raises = self.assertRaises
    raises(TypeError, parser.add_mutually_exclusive_group, title='foo')
