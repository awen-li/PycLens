# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_is_reserved

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertIs(False, P('').is_reserved())
    self.assertIs(False, P('/').is_reserved())
    self.assertIs(False, P('/foo/bar').is_reserved())
    self.assertIs(False, P('//my/share/nul/con/aux').is_reserved())
    self.assertIs(True, P('nul').is_reserved())
    self.assertIs(True, P('aux').is_reserved())
    self.assertIs(True, P('prn').is_reserved())
    self.assertIs(True, P('con').is_reserved())
    self.assertIs(True, P('conin$').is_reserved())
    self.assertIs(True, P('conout$').is_reserved())
    self.assertIs(True, P('COM1').is_reserved())
    self.assertIs(True, P('LPT9').is_reserved())
    self.assertIs(True, P('com¹').is_reserved())
    self.assertIs(True, P('com²').is_reserved())
    self.assertIs(True, P('lpt³').is_reserved())
    self.assertIs(True, P('NUL.txt').is_reserved())
    self.assertIs(True, P('PRN  ').is_reserved())
    self.assertIs(True, P('AUX  .txt').is_reserved())
    self.assertIs(True, P('COM1:bar').is_reserved())
    self.assertIs(True, P('LPT9   :bar').is_reserved())
    self.assertIs(False, P('bar.com9').is_reserved())
    self.assertIs(False, P('bar.lpt9').is_reserved())
    self.assertIs(True, P('c:/baz/con/NUL').is_reserved())
    self.assertIs(False, P('c:/NUL/con/baz').is_reserved())
