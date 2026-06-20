# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocUrlHandlerTest_test_url_requests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    requests = [('', 'Pydoc: Index of Modules'), ('get?key=', 'Pydoc: Index of Modules'), ('index', 'Pydoc: Index of Modules'), ('topics', 'Pydoc: Topics'), ('keywords', 'Pydoc: Keywords'), ('pydoc', 'Pydoc: module pydoc'), ('get?key=pydoc', 'Pydoc: module pydoc'), ('search?key=pydoc', 'Pydoc: Search Results'), ('topic?key=def', 'Pydoc: KEYWORD def'), ('topic?key=STRINGS', 'Pydoc: TOPIC STRINGS'), ('foobar', 'Pydoc: Error - foobar')]
    with self.restrict_walk_packages():
        for (url, title) in requests:
            self.call_url_handler(url, title)
