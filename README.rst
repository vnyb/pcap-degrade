pcap-degrade
===========

pcap-degrade degrades PCAP captures in order to simulate packet loss and latency
for testing purposes. It works with UDP and TCP and it is particulary useful
to simulate a degraded RTP stream.

Details
-------

Packet loss is performed randomly using a fixed probability (default: 1%)

Delay is performed using a gamma distribution (default: mean delay = 100 ms,
max delay = 500 ms) as described in the plot below.

.. image:: delay-distribution.pcap

Usage
-----

With default settings:

.. code-block:: bash

   pcap-degrade <input_pcap> <output_pcap>


With custom settings:

.. code-block:: bash

   # 5% packet loss, mean delay: 250 ms, max delay: 900 ms
   pcap-degrade --loss 0.05 --delay-mean 250 --delay-max 900 <input_pcap> <output_pcap>
