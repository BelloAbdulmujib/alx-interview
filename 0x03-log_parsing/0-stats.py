#!/usr/bin/python3
''' script that reads stdin line by line and computes metrics
'''

import sys
import signal
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0


def print_stats():
    """ Print the computed statistics. """
    print(f"File size: {total_file_size}")
    for status_code in sorted(valid_status_codes):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(sig, frame):
    """ Handle keyboard interruption (CTRL + C). """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip, date, request, status_code, file_size = parts[0], parts[3], \

        parts[5], parts[-2], parts[-1]

        if not status_code.isdigit() or not file_size.isdigit():
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        if status_code not in valid_status_codes:
            continue

        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}")

finally:
    print_stats()
