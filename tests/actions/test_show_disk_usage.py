from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage_context_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage(capsys, tmp_path):

    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("primeiro arquivo de teste.")
    file2.write_text("")
    context = {
        "all_files": [
            str(file1),
            str(file2),
        ]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()

    message1 = f"'{_get_printable_file_path(str(file1))}':".ljust(70)
    message2 = f"'{_get_printable_file_path(str(file2))}':".ljust(70)

    assert (
        captured.out
        == f"{message1} 26 (100%)\n{message2} 0 (0%)\nTotal size: 26\n"
    )
