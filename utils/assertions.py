def assert_status_code(response, expected_status_code: int):
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, "
        f"but received {response.status_code}"
    )


def assert_json_contains(response, expected_keys: list[str]):
    try:
        response_data = response.json()
    except ValueError as exc:
        raise AssertionError("Response is not valid JSON") from exc

    assert isinstance(response_data, dict), (
        f"Expected a JSON object, got {type(response_data).__name__}"
    )

    missing_keys = [
        key for key in expected_keys
        if key not in response_data
    ]

    assert not missing_keys, (
        f"Response is missing expected JSON keys: {missing_keys}"
    )