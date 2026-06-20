# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestMutuallyExclusiveGroupErrors_test_empty_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    with self.assertRaises(ValueError):
        parser.parse_args(['-h'])
