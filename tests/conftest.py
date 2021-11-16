def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        help="This is request status code"
    )
