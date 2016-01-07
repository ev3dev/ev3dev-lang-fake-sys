#!/usr/bin/env python

import os
import shutil

# Where to put each device in the arena
class_path = {
        'infrared_sensor' : 'lego-sensor/sensor{0}',
        'touch_sensor'    : 'lego-sensor/sensor{0}',
        'medium_motor'    : 'tacho-motor/motor{0}'
        }

def populate_arena(devices):
    """
    Copies specified devices to arena.
    `devices` is a dictionary mapping device name to a tuple of
    device index/device address.
    """

    for dev,prm in devices.items():
        assert dev in class_path, 'Unregistered device "{0}" requested'.format(dev)

        root = os.path.dirname(os.path.realpath(__file__))
        src = os.path.join(root, 'devices', dev)
        dst = os.path.join(root, 'arena', class_path[dev].format(prm[0]))

        shutil.copytree(src, dst)

        print("\t{0}\t{1}\t{2}".format(prm[0], prm[1], dst))

        if len(prm) > 1:
            with open(os.path.join(dst, 'address'), 'w') as address:
                address.write('{0}\n'.format(prm[1]))

if __name__ == '__main__':
    import sys

    if len(sys.argv[1:]) < 1:
        print('Usage: {0} <device>:<index>@<address> ...'.format(sys.argv[0]))
        sys.exit(1)

    devices = {}
    for arg in sys.argv[1:]:
        dev_idx = arg.split(':')
        assert len(dev_idx) == 2, 'Incorrect command line parameter: {0}'.format(arg)
        devices[dev_idx[0]] = dev_idx[1].split('@')

    populate_arena(devices)
