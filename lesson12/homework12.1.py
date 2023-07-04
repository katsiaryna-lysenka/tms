import re

phone_number_regex = re.compile(r"\+\d{1,3}-\d{2}-\d{2}-\d{5,7}")
if phone_number_regex.fullmatch("+375-29-7776655"):
    print("Номер телефона соответствует шаблону")
else:
    print("Номер телефона не соответствует шаблону")


def test_valid_phone_numbers(regex_compiled):
    valid = (
        "+375-29-7776655",
        "+37-29-7776655",
        "+3-29-7776655",
        "+375-44-777665",
        "+375-44-77766",
    )
    for n in valid:
        res = regex_compiled.fullmatch(n)
        assert res.group() == n


def test_invalid_phone_numbers(regex_compiled):
    invalid = (
        "",
        "test12345test"
        "375-29-7776655",
        "+-29-7776655",
        "+3a5-29-7776655",
        "+3756-29-7776655",
        "+375--7776655",
        "+375-4-7776655",
        "+375-444-7776655",
        "+375-c4-7776655",
        "+375-33-",
        "+375-33-7",
        "+375-33-7776",
        "+375-33-77766554",
        "+375-29-7776e55",
    )

    for n2 in invalid:
        assert regex_compiled.fullmatch(n2) is None