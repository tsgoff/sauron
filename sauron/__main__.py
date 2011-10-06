#! /usr/bin/env python

import argparse				# Options are good
from sauron import Watcher	# Everything

parser = argparse.ArgumentParser(description='Monitoring daemon')
parser.add_argument('--dry-run', dest='dryrun', action='store_true', default=False,
					help='Collect metrics, but do not push them.')
args = parser.parse_args()
w = Watcher(dryrun=args.dryrun)
w.start()