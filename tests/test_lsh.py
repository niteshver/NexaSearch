import pytest

from src.processing.lsh import find_duplicate_files


def test_find_duplicate_files_reports_duplicates_without_deleting(tmp_path):
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"
    unique = tmp_path / "unique.txt"
    first.write_text("same content", encoding="utf-8")
    second.write_text("same content", encoding="utf-8")
    unique.write_text("different content", encoding="utf-8")

    duplicates = find_duplicate_files(tmp_path)

    assert len(duplicates) == 1
    assert set(next(iter(duplicates.values()))) == {first, second}
    assert first.exists() and second.exists() and unique.exists()


def test_find_duplicate_files_requires_a_directory(tmp_path):
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_duplicate_files(tmp_path / "missing")
