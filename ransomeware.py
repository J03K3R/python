#!/usr/bin/env python

import signal
from time import sleep
import string
from tqdm import tqdm

def ctrlc_handler(signum, frm) :
    print "--- Ah ah ah, You didn't say the magic word ---"

print"--- RANSOMEWARE ENCRYPTING DRIVE ---"
signal.signal(signal.SIGINT, ctrlc_handler)
for i in tqdm(range(100)):
    sleep(0.1)

print "--- DRIVE ENCRYPTED ---"
print "--- SEND 100 BITCOIN TO 3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX ---"

while True:
    pass
