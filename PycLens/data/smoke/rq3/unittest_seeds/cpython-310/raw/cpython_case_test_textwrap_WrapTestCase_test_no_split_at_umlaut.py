# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_no_split_at_umlaut

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Die Empfänger-Auswahl'
    self.check_wrap(text, 13, ['Die', 'Empfänger-', 'Auswahl'])
