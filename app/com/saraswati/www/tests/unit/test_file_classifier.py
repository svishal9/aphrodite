"""
file1.txt (size: 100)
file2.txt (size: 200) in collection "collection1"
file3.txt (size: 200) in collection "collection1"
file4.txt (size: 300) in collection "collection2"
file5.txt (size: 10)
"""
from app.com.saraswati.www.src.file_classifier import get_file_size, get_top_classifications


def test_get_file_size():
    input = [
        ["file1.txt", 100, []],
        ["file2.txt", 200, ["collection1"]],
        ["file3.txt", 200, ["collection1"]],
        ["file4.txt", 300, ["collection2"]],
        ["file5.txt", 10, []],
    ]
    expected = 810
    actual = get_file_size(input)
    assert actual == expected


def test_get_top_classifications():
    file_stats = [
        ["file1.txt", 100, []],
        ["file2.txt", 200, ["collection1"]],
        ["file3.txt", 200, ["collection1"]],
        ["file4.txt", 300, ["collection2"]],
        ["file5.txt", 10, []],
    ]
    top_n_classification = 2
    expected = [["collection1", 400], ["collection2", 300]]
    actual = get_top_classifications(file_stats, 3)
    assert actual == expected


def test_get_top_shared_classifications():
    file_stats = [
        ["file1.txt", 100, []],
        ["file2.txt", 200, ["collection1", "collection2", "collection3"]],
        ["file3.txt", 200, ["collection1"]],
        ["file4.txt", 300, ["collection2"]],
        ["file5.txt", 10, []],
    ]
    top_n_classification = 3
    expected = [["collection2", 500], ["collection1", 400], ["collection3", 200]]
    actual = get_top_classifications(file_stats, top_n_classification)
    assert actual == expected
