# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestHelpFormattingMetaclass___init___AddTests_test_print_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(tester)
    print_ = getattr(parser, 'print_%s' % self.func_suffix)
    sfile = StdIOBuffer()
    print_(sfile)
    parser_text = sfile.getvalue()
    self._test(tester, parser_text)
