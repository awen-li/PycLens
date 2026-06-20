# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_async_generator_annotation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def an_async_generator():
        yield 1
    text = pydoc.plain(pydoc.plaintext.document(an_async_generator))
    self.assertIn('async an_async_generator', text)
    html = pydoc.HTMLDoc().document(an_async_generator)
    self.assertIn('async <a name="-an_async_generator"><strong>an_async_generator', html)
