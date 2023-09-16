#!/bin/bash

set -m

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
iop --init

fg %1