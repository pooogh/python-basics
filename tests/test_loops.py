import pytest

from practice_package.loops import (
    count_vowel_triplets,
    find_fibonacci_index,
    remove_duplicates,
    sum_even_digits,
)


class TestLoopsFunctions:

    @pytest.mark.parametrize("number, expected", [
        (123456, 12),
        (-13579, 0),
        (2468, 20),
        (0, 0),
        (13579, 0),
        (-2468, 20),
        (111122, 4),
    ], ids=["mixed", "all_odd", "all_even", 
            "zero", "all_odd_positive", "all_even_negative", "with_duplicates"])
    def test_sum_even_digits(self, number, expected):
        assert sum_even_digits(number) == expected
    
    @pytest.mark.parametrize("text, expected", [
        ("Beautiful day", 1),
        ("Queueing", 2),
        ("Python", 0),
        ("AeIoU", 1),
        ("", 0),
        ("YyY", 1),
        ("Hello world", 0),
    ], ids=["normal", "double", "no_vowels", 
            "all_vowels", "empty", "only_y", "spaces"])
    def test_count_vowel_triplets(self, text, expected):
        assert count_vowel_triplets(text) == expected
    
    @pytest.mark.parametrize("number, expected", [
        (8, 6),
        (610, 15),
        (4, -1),
        (1, 1),
        (2, 3),
        (144, 12),
        (987, 16),
    ], ids=["small", "medium", "not_fib", 
            "first", "second", "twelfth", "large"])
    def test_find_fibonacci_index(self, number, expected):
        assert find_fibonacci_index(number) == expected
    
    @pytest.mark.parametrize("string, expected", [
        ("aaabbbccca", "abca"),
        ("abcde", "abcde"),
        ("112233311", "1231"),
        ("", ""),
        ("aaaaa", "a"),
        ("ababab", "ababab"),
        ("HHeellloo", "Helo"),
    ], ids=["basic", "no_duplicates", "numbers", 
            "empty", "all_same", "alternating", "mixed_case"])
    def test_remove_duplicates(self, string, expected):
        assert remove_duplicates(string) == expected