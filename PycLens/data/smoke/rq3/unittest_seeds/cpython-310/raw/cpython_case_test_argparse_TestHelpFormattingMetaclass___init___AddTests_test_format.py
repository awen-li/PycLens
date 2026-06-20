# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestHelpFormattingMetaclass___init___AddTests_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(tester)
    format = getattr(parser, 'format_%s' % self.func_suffix)
    self._test(tester, format())
