# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_async_annotation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def coro_function(ign) -> int:
        return 1
    text = pydoc.plain(pydoc.plaintext.document(coro_function))
    self.assertIn('async coro_function', text)
    html = pydoc.HTMLDoc().document(coro_function)
    self.assertIn('async <a name="-coro_function"><strong>coro_function', html)
