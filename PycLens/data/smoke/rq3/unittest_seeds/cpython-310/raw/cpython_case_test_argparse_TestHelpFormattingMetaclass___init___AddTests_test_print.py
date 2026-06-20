# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestHelpFormattingMetaclass___init___AddTests_test_print

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(tester)
    print_ = getattr(parser, 'print_%s' % self.func_suffix)
    old_stream = getattr(sys, self.std_name)
    setattr(sys, self.std_name, StdIOBuffer())
    try:
        print_()
        parser_text = getattr(sys, self.std_name).getvalue()
    finally:
        setattr(sys, self.std_name, old_stream)
    self._test(tester, parser_text)
