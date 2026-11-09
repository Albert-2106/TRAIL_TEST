import runpy
import io
from contextlib import redirect_stdout

def test_bug_3_output():
    f = io.StringIO()
    with redirect_stdout(f):
        runpy.run_path('bug_3.py')
    assert f.getvalue().strip() == '7'