# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_buffer_artefacts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = [('starttag', 'a', [('b', '<')])]
    self._run_check(["<a b='<'>"], output)
    self._run_check(['<a ', "b='<'>"], output)
    self._run_check(['<a b', "='<'>"], output)
    self._run_check(['<a b=', "'<'>"], output)
    self._run_check(["<a b='<", "'>"], output)
    self._run_check(["<a b='<'", '>'], output)
    output = [('starttag', 'a', [('b', '>')])]
    self._run_check(["<a b='>'>"], output)
    self._run_check(['<a ', "b='>'>"], output)
    self._run_check(['<a b', "='>'>"], output)
    self._run_check(['<a b=', "'>'>"], output)
    self._run_check(["<a b='>", "'>"], output)
    self._run_check(["<a b='>'", '>'], output)
    output = [('comment', 'abc')]
    self._run_check(['', '<!--abc-->'], output)
    self._run_check(['<', '!--abc-->'], output)
    self._run_check(['<!', '--abc-->'], output)
    self._run_check(['<!-', '-abc-->'], output)
    self._run_check(['<!--', 'abc-->'], output)
    self._run_check(['<!--a', 'bc-->'], output)
    self._run_check(['<!--ab', 'c-->'], output)
    self._run_check(['<!--abc', '-->'], output)
    self._run_check(['<!--abc-', '->'], output)
    self._run_check(['<!--abc--', '>'], output)
    self._run_check(['<!--abc-->', ''], output)
