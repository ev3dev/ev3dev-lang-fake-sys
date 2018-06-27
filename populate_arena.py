#!/usr/bin/env python

import os
import shutil

# Where to put each device in the arena
class_path = {
        'infrared_sensor' : 'lego-sensor/sensor{0}',
        'touch_sensor'    : 'lego-sensor/sensor{0}',
        'medium_motor'    : 'tacho-motor/motor{0}',
        'large_motor'    : 'tacho-motor/motor{0}'
        }

def populate_arena(devices):
    """
    Copies specified devices to arena.
    `devices` is an array of tuples containing device types, indices and
    addresses.
    """

    root = os.path.dirname(os.path.realpath(__file__))
    src = os.path.join(root, 'devices', 'board-info')
    dst = os.path.join(root, 'arena', 'board-info')

    shutil.copytree(src, dst)

    for device in devices:
        (dev_type, index, address) = device
        assert dev_type in class_path, 'Unregistered device "{0}" requested'.format(dev_type)

        src = os.path.join(root, 'devices', dev_type)
        dst = os.path.join(root, 'arena', class_path[dev_type].format(index))

        shutil.copytree(src, dst)

        print("\t{0}\t{1}\t{2}".format(index, address, dst))

        with open(os.path.join(dst, 'address'), 'w') as address_file:
            address_file.write('{0}\n'.format(address))

if __name__ == '__main__':
    import sys

    if len(sys.argv[1:]) < 1:
        print('Usage: {0} <device>:<index>@<address> ...'.format(sys.argv[0]))
        sys.exit(1)

    devices = []
    for arg in sys.argv[1:]:
        dev_idx = arg.split(':', 1)
        assert len(dev_idx) == 2, 'Incorrect command line parameter: {0}'.format(arg)
        location_info = dev_idx[1].split('@')
        devices.append( (dev_idx[0], location_info[0], location_info[1]) )

    populate_arena(devices)
