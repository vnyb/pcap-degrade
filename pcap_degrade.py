"""
Module for degrading PCAP captures
"""

import argparse
import logging
import random
import sys

# Workaround to suppress annoying IPv6 warning at scapy import
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# pylint: disable=wrong-import-position
from scapy.all import (
    rdpcap,
    wrpcap,
)

DEFAULT_PACKET_LOSS = 0.01

def degrade(in_file, out_file, packet_loss=DEFAULT_PACKET_LOSS):
    """Perform degradation"""

    out_list = []

    for pkt in rdpcap(in_file):
        if random.random() < packet_loss:
            continue # Discard packet

        out_list.append(pkt)

    wrpcap(out_file, out_list)

def restricted_float(x):
    """Restrict argparse float argument to [0.0, 1.0]"""

    x = float(x)
    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % x)
    return x

def main():
    """
    Degrade PCAP captures
    """

    parser = argparse.ArgumentParser(
        description=main.__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'input_file',
        help='input PCAP file',
    )
    parser.add_argument(
        'output_file',
        help='output PCAP file',
    )
    parser.add_argument(
        '-l', '--loss',
        type=restricted_float,
        default=DEFAULT_PACKET_LOSS,
        dest='packet_loss',
        help='packet lot rate',
    )
    args = parser.parse_args()

    try:
        degrade(args.input_file, args.output_file, args.packet_loss)
    except OSError as exn:
        sys.exit(str(exn))

    return 0
