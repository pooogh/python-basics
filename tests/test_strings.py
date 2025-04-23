import pytest

from practice_package.strings import (
    check_brackets,
    count_vowel_groups,
    encrypt_sentence,
    extract_file_name,
    reverse_domain,
)


class TestStringsFunctions:
    
    @pytest.mark.parametrize("path, expected", [
        ('C:/Users/example.txt', 'example'),
        ('../index.html', 'index'),
        ('/home/user/photo.jpg', 'photo'),
        ('archive.tar.gz', 'archive') 
    ], ids=["windows_path", "relative_path", "unix_path", 
            "double_extension", "no_extension", "hidden_file"])
    def test_extract_file_name(self, path, expected):
        assert extract_file_name(path) == expected
    
    @pytest.mark.parametrize("original, encrypted", [
        ('JavaScript', 'aacitprSvJ'),
        ('Hello, World!', 'el,Wrd!lo olH'),
        ('Hexlet', 'eltexH'),
        ('A', 'A'), 
        ('', ''), 
    ], ids=["normal", "with_punctuation", "even_length", 
            "single_char", "empty_string"])
    def test_encrypt_sentence(self, original, encrypted):
        assert encrypt_sentence(original) == encrypted
    
    @pytest.mark.parametrize("expression, expected", [
        ('(a + b) * (c - d)', 0),
        (')a + b(', 1),
        ('(a + b))', 6),
        ('((a + b)', -1),
        ('no brackets', 0), 
        ('', 0), 
    ], ids=["valid", "invalid_start", "extra_close", 
            "unclosed", "no_brackets", "empty"])
    def test_check_brackets(self, expression, expected):
        assert check_brackets(expression) == expected
    
    @pytest.mark.parametrize("domain, reversed_domain", [
        ('sub.domain.com', 'com.domain.sub'),
        ('hexlet.io', 'io.hexlet'),
        ('localhost', 'localhost'),
        ('a.b.c.d', 'd.c.b.a'), 
        ('single', 'single'), 
    ], ids=["standard", "second_level", "no_dots", 
            "multiple_subdomains", "single_word"])
    def test_reverse_domain(self, domain, reversed_domain):
        assert reverse_domain(domain) == reversed_domain
    
    @pytest.mark.parametrize("word, count", [
        ('JavaScript', 3),
        ('HeLLO', 2),
        ('rhythm', 1),
        ('AeIoU', 1), 
        ('xyz', 0), 
        ('', 0), 
    ], ids=["mixed_case", "all_upper", "only_y", 
            "all_vowels", "no_vowels", "empty"])
    def test_count_vowel_groups(self, word, count):
        assert count_vowel_groups(word) == count
