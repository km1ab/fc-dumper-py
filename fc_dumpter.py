import sys
import RPi.GPIO as GPIO
import time

INTV = 0.005
# CLK	#RESET
port_tbl_addr_ctrl = [17, 27]

port_tbl_data_ctrl = [20, 21, 22, 23, 4, 5, 6, 7]
# CPU R/W	# /ROMSEL	# M2	# PPU /RD   # PPU /WR  # EXT PIN
port_tbl_port_ctrl = [9, 10, 11, 19, 24, 25]

HEADER_DATA = [
    0x4E,
    0x45,
    0x53,
    0x1A,
    0x01,
    0x01,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
]

args = sys.argv


def InitPort():
    GPIO.setmode(GPIO.BCM)
    for d in port_tbl_addr_ctrl:
        GPIO.setup(d, GPIO.OUT)
    for d in port_tbl_data_ctrl:
        GPIO.setup(d, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for d in port_tbl_port_ctrl:
        GPIO.setup(d, GPIO.OUT)


def TermPort():
    GPIO.cleanup()


def GpioOut(d, f):
    GPIO.output(d, f)


def GpioIn(d):
    return GPIO.input(d)


def GpioGetData():
    ret = (
        ((GpioIn(port_tbl_data_ctrl[0]) << 0))
        | ((GpioIn(port_tbl_data_ctrl[1]) << 1))
        | ((GpioIn(port_tbl_data_ctrl[2]) << 2))
        | ((GpioIn(port_tbl_data_ctrl[3]) << 3))
        | ((GpioIn(port_tbl_data_ctrl[4]) << 4))
        | ((GpioIn(port_tbl_data_ctrl[5]) << 5))
        | ((GpioIn(port_tbl_data_ctrl[6]) << 6))
        | ((GpioIn(port_tbl_data_ctrl[7]) << 7))
    )
    return ret


# 	print(ret)
# 	return ord(hex(ret))


def ClearAddr():
    GpioOut(port_tbl_addr_ctrl[1], True)
    GpioOut(port_tbl_addr_ctrl[1], False)


def SetAddress(addr):
    GpioOut(port_tbl_addr_ctrl[0], True)
    GpioOut(port_tbl_addr_ctrl[1], True)
    time.sleep(INTV)
    GpioOut(port_tbl_addr_ctrl[1], False)
    for i in range(addr):
        GpioOut(port_tbl_addr_ctrl[0], False)
        GpioOut(port_tbl_addr_ctrl[0], True)


def IncAddress():
    GpioOut(port_tbl_addr_ctrl[0], False)
    GpioOut(port_tbl_addr_ctrl[0], True)


def SetPortCtrl(i):
    GpioOut(port_tbl_port_ctrl[i], True)


def ClearPortCtrl(i):
    GpioOut(port_tbl_port_ctrl[i], False)


def EnableCpuRw():
    SetPortCtrl(0)


def DisableCpuRw():
    ClearPortCtrl(0)


def EnableRomSel():
    SetPortCtrl(1)


def DisableRomSel():
    ClearPortCtrl(1)


def EnableM2():
    SetPortCtrl(2)


def DisableM2():
    ClearPortCtrl(2)


def EnablePpuWr():
    SetPortCtrl(4)


def DisablePpuWr():
    ClearPortCtrl(4)


def EnablePpuRd():
    SetPortCtrl(3)


def DisablePpuRd():
    ClearPortCtrl(3)


def ReadRom(addr, chrsize) -> list:
    ClearAddr()
    time.sleep(INTV)
    SetAddress(addr)
    time.sleep(INTV)
    output = []
    for i in range(chrsize):
        # print(chr(GpioGetData()), end='')
        time.sleep(INTV)
        # GpioGetData()
        output.append(GpioGetData())
        IncAddress()
    print("")
    return output


# def ReadLoRom(addr,chrsize)
# 	ClearAddr()
# 	gpio_sleep(50)
# 	SetAddress(addr)
# 	upper = 0
# 	for i=1,chrsize*2 do
# 	    if (i-1)>upper * 2 * 0x8000 then
# 		    if 0==((i-1) % 0x8000) then
# 				upper = upper + 1
# 		    end
# 	    end
# 		address = upper * 2 * 0x8000 + ((i-1) % 0x8000) + 0x8000
# 	    if (i-1)+0x8000==address then
# 			val = gpio_get_value(port_tbl_data_ctrl[1], 0, 0xff)
# 			dumper_write(val)
# 		end
# 		IncAddress()
# 		i=i+1
# 	end
# end
# def conver_address(in_addr: int) -> int:
#     address = in_addr
#     upper = int(address / 0x8000)
#     lower = address % 0x8000
#     address = upper * 2 * 0x8000 + lower + 0x8000
#     if (address % 0x8000) == 0:
#         # clear addr
#         ClearAddr()
#         # set addr
#         SetAddress(address)

#     return address


ROM_INFO_SIZE = 25
# OE  - CpuRw
# CS  - RomSel
# WE  - M2_PpuWr
# RST - PpuRd
def MainLoop():
    if len(args) < 2:
        print("error")
        return

    path_w = args[1]

    InitPort()

    rom_size: int = 0x4000  # PRG-ROM 16K
    chrsize: int = 0x2000  # CHR-ROM 8K

    # PRG-ROM
    # OE + CS + !WE + !RST
    EnableCpuRw()
    DisableRomSel()
    EnableM2()
    EnablePpuWr()
    EnablePpuRd()

    ClearAddr()

    start_address: int = 0x0000

    print(f"start_address = {hex(start_address)}")
    SetAddress(start_address)
    time.sleep(INTV)
    bin = bytearray([])
    n_mod = 1
    size = rom_size
    if size > 8:
        n_mod = size >> 3
    for i in range(size):
        if i % n_mod == 0:
            sys.stdout.write("#")
            sys.stdout.flush()
            time.sleep(0.001)
        bin.append(GpioGetData())
        IncAddress()

    # CHR-ROM
    # OE + CS + !WE + !RST
    DisableCpuRw()
    EnableRomSel()
    DisableM2()
    DisablePpuWr()
    DisablePpuRd()

    ClearAddr()

    n_mod = 1
    size = chrsize
    if size > 8:
        n_mod = size >> 3
    for i in range(size):
        if i % n_mod == 0:
            sys.stdout.write("#")
            sys.stdout.flush()
            time.sleep(0.001)
        bin.append(GpioGetData())
        IncAddress()

    with open(path_w, mode="wb") as f:
        header = bytes(HEADER_DATA)
        f.write(header)
        f.write(bin)

    ClearAddr()
    TermPort()
    print("")
    print("Complete!")


try:
    MainLoop()
except Exception as e:
    print(f"Error: {e}")
    print("Clear Address")
    ClearAddr()
    print("Term Port")
    TermPort()
