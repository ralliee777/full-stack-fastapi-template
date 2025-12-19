"""Example file with deprecated datetime usage for E2E test."""

from datetime import datetime, timezone


def get_current_utc_time():
    """Get current UTC time using the updated method."""
    return datetime.now(timezone.utc)


def get_timestamp():
    """Get timestamp using the updated method."""
    return datetime.now(timezone.utc).timestamp()
