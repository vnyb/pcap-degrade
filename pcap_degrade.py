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
DEFAULT_DELAY_MEAN_MS = 100
DEFAULT_DELAY_MAX_MS = 500

def variate(mean_ms, delay_max_ms):
    """
    Generate delay following a gamma distribution.
    """
    while True:
        x = mean_ms * random.gammavariate(2.0, 0.5)
        if x <= delay_max_ms:
            return x

def degrade(in_file, out_file,
            packet_loss=DEFAULT_PACKET_LOSS,
            delay_mean_ms=DEFAULT_DELAY_MEAN_MS,
            delay_max_ms=DEFAULT_DELAY_MAX_MS):
    """Perform degradation"""

    out_list = []
    previous_time = 0.0

    for pkt in rdpcap(in_file):
        # Packet loss
        if random.random() < packet_loss:
            continue # Discard packet

        # Delay
        pkt.time += variate(delay_mean_ms, delay_max_ms) / 1000
        if pkt.time < previous_time:
            # Avoid overlap
            pkt.time = previous_time

        out_list.append(pkt)
        previous_time = pkt.time

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
    parser.add_argument(
        '-m', '--delay-mean',
        type=float,
        default=DEFAULT_DELAY_MEAN_MS,
        dest='delay_mean_ms',
        help='mean delay (milliseconds)',
    )
    parser.add_argument(
        '-M', '--delay-max',
        type=float,
        default=DEFAULT_DELAY_MAX_MS,
        dest='delay_max_ms',
        help='mean delay (milliseconds)',
    )
    args = parser.parse_args()

    try:
        degrade(
            args.input_file, args.output_file,
            args.packet_loss,
            args.delay_mean_ms, args.delay_max_ms,
        )
    except OSError as exn:
        sys.exit(str(exn))

    return 0
