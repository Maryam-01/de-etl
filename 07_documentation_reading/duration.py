def format_duration(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"


def test_format_duration():
    assert format_duration(225) == "3:45"
    assert format_duration(60) == "1:00"
    assert format_duration(9) == "0:09"
    assert format_duration(600) == "10:00"


test_format_duration()
print("All tests passed!")