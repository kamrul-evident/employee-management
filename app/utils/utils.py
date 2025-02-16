from datetime import UTC, datetime


def utc_now():
    return datetime.now(tz=UTC)
