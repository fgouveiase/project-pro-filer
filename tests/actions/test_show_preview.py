from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_without_context(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    output = "Found 0 files and 0 directories\n"
    assert captured.out == output


def test_show_preview(capsys):
    context = {
        'all_files': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6'],
        'all_dirs': ['d1', 'd2', 'd3', 'd4', 'd5', 'd6']
    }

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == '''Found 6 files and 6 directories
First 5 files: ['f1', 'f2', 'f3', 'f4', 'f5']
First 5 directories: ['d1', 'd2', 'd3', 'd4', 'd5']\n'''
