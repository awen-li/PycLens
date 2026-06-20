# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_mutability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = zipfile.Path(alpharep)
    (a, b, g) = root.iterdir()
    alpharep.writestr('foo.txt', 'foo')
    alpharep.writestr('bar/baz.txt', 'baz')
    assert any((child.name == 'foo.txt' for child in root.iterdir()))
    assert (root / 'foo.txt').read_text(encoding='utf-8') == 'foo'
    (baz,) = (root / 'bar').iterdir()
    assert baz.read_text(encoding='utf-8') == 'baz'
