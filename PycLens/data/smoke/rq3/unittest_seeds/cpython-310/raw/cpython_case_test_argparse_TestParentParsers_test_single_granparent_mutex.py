# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_single_granparent_mutex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parents = [self.ab_mutex_parent]
    parser = ErrorRaisingArgumentParser(add_help=False, parents=parents)
    parser = ErrorRaisingArgumentParser(parents=[parser])
    self._test_mutex_ab(parser.parse_args)
