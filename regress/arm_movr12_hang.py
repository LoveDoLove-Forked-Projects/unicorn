#!/usr/bin/python

from unicorn import *
from unicorn.arm_const import *

uc = Uc(UC_ARCH_ARM, UC_MODE_ARM)
uc.mem_map(0x1000, 0x1000)
uc.mem_write(0x1000, '00c000e3'.decode('hex'))
def hook_block(uc, addr, *args):
    print 'enter block 0x%04x' % addr

uc.reg_write(UC_ARM_REG_R12, 0x123)
print 'r12 =', uc.reg_read(UC_ARM_REG_R12)
uc.hook_add(UC_HOOK_BLOCK, hook_block)
print 'block should only run once'
uc.emu_start(0x1000, 0x1004, timeout=250)
print 'r12 =', uc.reg_read(UC_ARM_REG_R12)