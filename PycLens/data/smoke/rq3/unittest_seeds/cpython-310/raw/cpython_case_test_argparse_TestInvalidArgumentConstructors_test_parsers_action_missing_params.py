# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_parsers_action_missing_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTypeError('command', action='parsers')
    self.assertTypeError('command', action='parsers', prog='PROG')
    self.assertTypeError('command', action='parsers', parser_class=argparse.ArgumentParser)
