#!/bin/bash

# Immeditely exit if any command returns an error status.
set -e

DEBUG=TRUE
IS_DRY_RUN=FALSE

# Makes sure to stop any child
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

# Starts a bunch of simulationed recievers with different characteristics.
python dummy_reciever.py \
  --reciever_name='meshtastic_node' \
  --recieve_interval=20 \
  --decode_chance=1.0 \
  --debug="$DEBUG" \
  --dry_run="$IS_DRY_RUN" &

python dummy_reciever.py \
  --reciever_name='RS41' \
  --recieve_interval=5 \
  --decode_chance=0.9 \
  --debug="$DEBUG" \
  --dry_run="$IS_DRY_RUN" &

python dummy_reciever.py \
  --reciever_name='baofeng_homebrewed_protocol' \
  --recieve_interval=10 \
  --decode_chance=0.5 \
  --debug="$DEBUG" \
  --dry_run="$IS_DRY_RUN" &

# Wait for all background processes to complete (which won't happen so you will have to stop this with Ctrl+C)
wait