import argparse

"""
Module for degrading PCAP captures
"""

def main():
    """
    Degrade PCAP captures
    """

    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        'input_file',
        help='input PCAP file',
    )
    parser.add_argument(
        'output_file',
        help='output PCAP file',
    )

    args = parser.parse_args()

    return 0
