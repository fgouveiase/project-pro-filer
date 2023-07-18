import pytest

from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_files(tmp_path):

    mock_file1 = tmp_path / "mock_file1.txt"
    mock_file1.write_text("same")
    mock_file2 = tmp_path / "mock_file2.txt"
    mock_file2.write_text("same")
    mock_file3 = tmp_path / "mock_file3.txt"
    mock_file3.write_text("diferent")

    context = {
        "all_files": [str(mock_file1), str(mock_file2), str(mock_file3)]
    }

    expect = find_duplicate_files(context)

    assert expect == [(str(mock_file1), str(mock_file2))]


def test_find_duplicate_lenght(tmp_path):
    mock_file1 = tmp_path / "mock_file1.txt"
    mock_file1.write_text('same')
    mock_file2 = tmp_path / "mock_file2.txt"
    mock_file2.write_text('diferent')
    mock_file3 = tmp_path / "mock_file3.txt"
    mock_file3.write_text('same')

    context = {
        "all_files": [str(mock_file1), str(mock_file2), str(mock_file3)]
    }

    assert len(find_duplicate_files(context)) == 1


def test_find_duplicate_without_file(tmp_path):

    mock_file1 = tmp_path / "mock_file1.txt"
    mock_file1.write_text("same")
    inexistent_file = tmp_path / "inexistent_file.py"

    context = {
        "all_files": [str(mock_file1), inexistent_file]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
