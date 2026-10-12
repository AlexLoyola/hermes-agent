"""Vendor hardware recognizers derived from host facts.

Recognition uses OS-reported PCI identity without environment-variable input.
"""

from __future__ import annotations


def is_nvidia_n1x_pci_id(pci_id: int) -> bool:
    """Recognize N1X; NVML packs device above the 16-bit vendor ID."""
    return pci_id & 0xFFFF == 0x10DE and 0x2E00 <= pci_id >> 16 <= 0x2E3F
