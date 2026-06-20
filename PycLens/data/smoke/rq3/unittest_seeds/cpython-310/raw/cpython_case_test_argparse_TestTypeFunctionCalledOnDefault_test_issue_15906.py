# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestTypeFunctionCalledOnDefault_test_issue_15906

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', dest='test', type=str, default=[], action='append')
    args = parser.parse_args([])
    self.assertEqual(args.test, [])
