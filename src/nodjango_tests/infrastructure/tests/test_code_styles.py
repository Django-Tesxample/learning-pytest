import io
import pytest
from flake8.api.legacy import get_style_guide
from pathlib import Path
from unittest.mock import patch

CODE_PATHS = [Path('.') / 'src']


@pytest.fixture
def python_filepaths():
    """Helper to retrieve paths of Python files.
    TODO: filter files into migrations folders
    """
    python_paths = []
    for folder in CODE_PATHS:
        python_paths += [python_file for python_file in folder.rglob("*.py")]
    return python_paths


def test_flake8(python_filepaths):
    style_guide = get_style_guide(
        select=['E', 'W', 'F', 'C', 'N'],
        max_line_length=120
    )
    fake_stdout = io.StringIO()
    with patch('sys.stdout', fake_stdout):
        report = style_guide.check_files(python_filepaths)
    if (report.total_errors):
        print("There are issues!\n" + fake_stdout.getvalue())

    assert report.total_errors == 0
