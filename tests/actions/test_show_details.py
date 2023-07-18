import os
from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_inexistent_file(capsys):
    path_mock = {"base_path": "/file/not_exist_file.py"}

    show_details(path_mock)
    captured = capsys.readouterr()

    assert captured.out == "File 'not_exist_file.py' does not exist\n"


def test_show_details(capsys, tmp_path):
    mock_file = tmp_path / "mock_file.txt"
    mock_file.touch()
    path_mock = {
        "base_path": str(mock_file)
    }
    show_details(path_mock)
    captured = capsys.readouterr()
    file_name = "mock_file.txt"
    file_size = os.path.getsize(mock_file)

    expect = (
        f"File name: {file_name}\n"
        f"File size in bytes: {file_size}\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {date.today()}\n"
    )
    assert expect in captured.out


def test_show_details_no_extension(capsys, tmp_path):
    mock_file = tmp_path / "mock_file"
    mock_file.touch()
    path_mock = {
        "base_path": str(mock_file)
    }
    show_details(path_mock)
    file_name = "mock_file"
    file_size = os.path.getsize(mock_file)
    captured = capsys.readouterr()

    expect = (
        f"File name: {file_name}\n"
        f"File size in bytes: {file_size}\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
    assert expect in captured.out
