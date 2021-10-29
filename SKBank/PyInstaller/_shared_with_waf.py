#-----------------------------------------------------------------------------
# Copyright (c) 2005-2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

"""
Code to be shared by PyInstaller and the bootloader/wscript file.

This code must not assume that either PyInstaller or any of its dependencies
installed. i.e. The only imports allowed in here are standard library ones.
Within reason, it is preferable that this file should still run under Python
2.7 as many compiler docker images still have only Python 2 installed.

"""

import platform
import re


def _pyi_machine(machine, system):
    # type: (str, str) -> str
    """Choose an intentionally simplified architecture identifier to be used in
    the bootloader's directory name.

    Args:
        machine:
            The output of ``platform.machine()`` or any known architecture
            alias or shorthand that may be used by a C compiler.
        system:
            The output of ``platform.system()`` on the target machine.
    Returns:
        Either a string tag or, on platforms that don't need an architecture
        tag, ``None``.

    Ideally we'd just use ``platform.machine()`` directly but that makes cross
    compiling the bootloader almost impossible because you need to know at
    compile time exactly what ``platform.machine()`` will be at run time based
    only on the machine name alias or shorthand reported by the C compiler at
    build time. Rather, use a loose differentiation and trust that anyone
    mixing armv6l with armv6h knows what their doing.

    """
    # See the corresponding tests in tests/unit/test_compat.py for examples.

    if platform.machine() == "sw_64":
        # This explicitly inhibits cross compiling the bootloader for or on
        # a SunWay machine.
        return "sw_64"

    if system != "Linux":
        # No architecture specifier for anything par Linux.
        # - Windows only has one 32 and one 64 bit architecture but lots of
        #   aliases for each so it's both pointless and painful to give Windows
        #   an architecture specifier.
        # - macOS is on two 64 bit architectures but they are merged into one
        #   "universal2" bootloader.
        # - BSD supports a wide range of architectures but according to PyPI's
        #   download statistics, every one of our BSD users are on x86_64.
        #   This may change in the distant future.
        return

    if machine.startswith(("arm", "aarch")):
        # ARM has a huge number of similar and aliased subversions.
        # e.g. armv5, armv6l armv8h, aarch64
        return "arm"
    if machine in ("x86_64", "x64", "x86"):
        return "intel"
    if re.fullmatch("i[1-6]86", machine):
        return "intel"
    if machine.startswith(("ppc", "powerpc")):
        # PowerPC comes in 64 vs 32 bit and little vs big endian variants.
        return "ppc"
    # Machines with no known aliases :)
    if machine in ("s390x", "mips"):
        return machine

    # Unknown architectures are allowed by default but will all be placed under
    # one directory. In theory, trying to have multiple unknown architectures
    # in one copy of PyInstaller will not work but that should be sufficiently
    # unlikely to ever happen.
    return "unknown"
