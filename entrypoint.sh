#!/bin/bash

set -m

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
iop --init

# start production
iop --start &

fg %1