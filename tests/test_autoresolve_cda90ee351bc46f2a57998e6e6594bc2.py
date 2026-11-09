import runpy
import io
from contextlib import redirect_stdout

def test_bug_2_prints_a():
    f = io.StringIO()
    with redirect_stdout(f):
        runpy.run_path('bug_2.py')
    assert f.getvalue().strip() == 'A'