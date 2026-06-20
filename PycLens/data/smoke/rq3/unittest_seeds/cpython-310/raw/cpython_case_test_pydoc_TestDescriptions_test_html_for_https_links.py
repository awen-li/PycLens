# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_html_for_https_links

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def a_fn_with_https_link():
        """a link https://localhost/"""
        pass
    html = pydoc.HTMLDoc().document(a_fn_with_https_link)
    self.assertIn('<a href="https://localhost/">https://localhost/</a>', html)
