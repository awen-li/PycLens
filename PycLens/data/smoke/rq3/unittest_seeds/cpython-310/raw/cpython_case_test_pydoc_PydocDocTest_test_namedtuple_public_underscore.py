# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_namedtuple_public_underscore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NT = namedtuple('NT', ['abc', 'def'], rename=True)
    with captured_stdout() as help_io:
        pydoc.help(NT)
    helptext = help_io.getvalue()
    self.assertIn('_1', helptext)
    self.assertIn('_replace', helptext)
    self.assertIn('_asdict', helptext)
