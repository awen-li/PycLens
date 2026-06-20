# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_single_parent_mutex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_mutex_ab(self.ab_mutex_parent.parse_args)
    parser = ErrorRaisingArgumentParser(parents=[self.ab_mutex_parent])
    self._test_mutex_ab(parser.parse_args)
