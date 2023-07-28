import sys
import RPi.GPIO as GPIO
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

INTV = 0.005
# CLK	#RESET
port_tbl_addr_ctrl = [17, 27]

port_tbl_data_ctrl = [20, 21, 22, 23, 4, 5, 6, 7]
# CPU R/W	# /ROMSEL	# M2	# PPU /RD   # PPU /WR  # EXT PIN
port_tbl_port_ctrl = [9, 10, 11, 19, 24, 25]

# PWM0 # PWM1
port_tbl_pwm_ctrl = [12, 13]

HEADER_DATA_COMMON = [0x4E, 0x45, 0x53, 0x1A]

HEADER_DATA_COMMON_FOOTER = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
HEADER_DATA_MAPPER0 = [
    # mapper 0
    0x01,
    0x01,
    0x00,
    0x00,
]

HEADER_DATA_MAPPER3 = [
    # mapper 3
    0x02,
    0x04,
    0x31,
    0x00,
]

HEADER_DATA_MAPPER66 = [
    # mapper 66
    0x08,
    0x04,
    0x21,
    0x40,
]

HEADER_DATA_MAPPER1 = [
    # mapper 1
    0x10,
    0x00,
    0x10,
    0x00,
]

HEADER_DATA_MAPPER23 = [
    # mapper 23
    0x08,
    0x10,
    0x71,
    0x10,
]

SIZE_1K = "1K"
SIZE_8K = "8K"
SIZE_16K = "16K"
SIZE_32K = "32K"
# SIZE_64K = "64K"
# SIZE_128K = "128K"
# rom_size: int = 0x4000  # PRG-ROM 16K
# chr_size: int = 0x2000  # CHR-ROM 8K
ROM_SIZE_DICT = {SIZE_1K: 0x400, SIZE_8K: 0x2000, SIZE_16K: 0x4000, SIZE_32K: 0x8000}

BANK_KEY_LIST = [0x30, 0x31, 0x32, 0x33]  # mapper3
BANK_KEY_MAPPER66_LIST0 = [0x00, 0x11, 0x22, 0x33]  # 4bank
# BANK_KEY_MAPPER66_LIST0 = [0x00, 0x10, 0x20, 0x30]  # 4bank
# BANK_KEY_MAPPER66_LIST1 = [0x30, 0x31, 0x32, 0x33]  # 4bank
# BANK_KEY_MAPPER66_LIST1 = [0x00, 0x01, 0x02, 0x03] # 4bank

BANK_KEY_MAPPER1_CTRL_REG = 0x1F  # chr bank 4KB, bank size 16KB, 4 screen, scroll H
BANK_HOME_MAPPER1 = 0xC000  # 0xC000 - 0xFFFF
BANK_AREA_MAPPER1 = 0x8000  # 0x8000 - 0xBFFF
BANK_PRG_REGISTER = 0xE000  # 0xE000 - 0xFFFF


def init_port(data_in: bool = True):
    GPIO.setmode(GPIO.BCM)
    for d in port_tbl_addr_ctrl:
        GPIO.setup(d, GPIO.OUT)
    if data_in:
        set_data_ctrl_to_intput()
    else:
        set_data_ctrl_to_output()
    for d in port_tbl_port_ctrl:
        GPIO.setup(d, GPIO.OUT)
    for d in port_tbl_pwm_ctrl:
        GPIO.setup(d, GPIO.OUT)
        GPIO.output(d, False)


def term_port():
    GPIO.cleanup()


def set_data_ctrl_to_intput():
    for d in port_tbl_data_ctrl:
        GPIO.setup(d, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def set_data_ctrl_to_output():
    for d in port_tbl_data_ctrl:
        GPIO.setup(d, GPIO.OUT)


def gpio_out(d, f):
    GPIO.output(d, f)


def gpio_in(d):
    return GPIO.input(d)


def gpio_get_data():
    ret = (
        ((gpio_in(port_tbl_data_ctrl[0]) << 0))
        | ((gpio_in(port_tbl_data_ctrl[1]) << 1))
        | ((gpio_in(port_tbl_data_ctrl[2]) << 2))
        | ((gpio_in(port_tbl_data_ctrl[3]) << 3))
        | ((gpio_in(port_tbl_data_ctrl[4]) << 4))
        | ((gpio_in(port_tbl_data_ctrl[5]) << 5))
        | ((gpio_in(port_tbl_data_ctrl[6]) << 6))
        | ((gpio_in(port_tbl_data_ctrl[7]) << 7))
    )
    return ret


# 	print(ret)
# 	return ord(hex(ret))


def gpio_set_data(data: int):
    gpio_out(port_tbl_data_ctrl[0], (data >> 0) & 0x1)
    gpio_out(port_tbl_data_ctrl[1], (data >> 1) & 0x1)
    gpio_out(port_tbl_data_ctrl[2], (data >> 2) & 0x1)
    gpio_out(port_tbl_data_ctrl[3], (data >> 3) & 0x1)
    gpio_out(port_tbl_data_ctrl[4], (data >> 4) & 0x1)
    gpio_out(port_tbl_data_ctrl[5], (data >> 5) & 0x1)
    gpio_out(port_tbl_data_ctrl[6], (data >> 6) & 0x1)
    gpio_out(port_tbl_data_ctrl[7], (data >> 7) & 0x1)


def clear_addr():
    gpio_out(port_tbl_addr_ctrl[1], True)
    gpio_out(port_tbl_addr_ctrl[1], False)


def set_address(addr):
    gpio_out(port_tbl_addr_ctrl[0], True)
    gpio_out(port_tbl_addr_ctrl[1], True)
    time.sleep(INTV)
    gpio_out(port_tbl_addr_ctrl[1], False)
    for i in range(addr):
        gpio_out(port_tbl_addr_ctrl[0], False)
        gpio_out(port_tbl_addr_ctrl[0], True)


def inc_address():
    gpio_out(port_tbl_addr_ctrl[0], False)
    gpio_out(port_tbl_addr_ctrl[0], True)


def set_port_ctrl(i):
    gpio_out(port_tbl_port_ctrl[i], True)


def clear_port_ctrl(i):
    gpio_out(port_tbl_port_ctrl[i], False)


def set_cpu_rw():
    set_port_ctrl(0)


def unset_cpu_rw():
    clear_port_ctrl(0)


def set_romsel():
    set_port_ctrl(1)


def unset_romsel():
    clear_port_ctrl(1)


def set_m2_o2():
    set_port_ctrl(2)


def unset_m2_o2():
    clear_port_ctrl(2)


def set_ppu_w():
    set_port_ctrl(4)


def unset_ppu_w():
    clear_port_ctrl(4)


def set_ppu_r():
    set_port_ctrl(3)


def unset_ppu_r():
    clear_port_ctrl(3)


def set_data(data: int):
    gpio_set_data(data)


def read_rom(addr, chrsize) -> list:
    clear_addr()
    time.sleep(INTV)
    set_address(addr)
    time.sleep(INTV)
    output = []
    for i in range(chrsize):
        # print(chr(gpio_get_data()), end='')
        time.sleep(INTV)
        # gpio_get_data()
        output.append(gpio_get_data())
        inc_address()
    print("")
    return output


class Debug:
    def __init__(self) -> None:
        pass

    def dbg_log(self, log: str):
        print(log)

    def dbg_print(self, log_msg, kaigyo: bool = True):
        if kaigyo:
            print(log_msg)
        else:
            print(log_msg, end="")


class DebugDummy(Debug):
    def __init__(self) -> None:
        pass

    def dbg_log(self, log: str):
        pass


class RomDumper:
    def __init__(self) -> None:
        self.bins = bytearray([])
        self.dbg: Debug = DebugDummy()

    def get_header(self) -> bytes:
        header = HEADER_DATA_COMMON
        header.extend(HEADER_DATA_MAPPER0)
        header.extend(HEADER_DATA_COMMON_FOOTER)
        return bytes(header)

    def set_debug_object(self, obj: Debug):
        self.dbg = obj

    def read_prg_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        self.set_prg_rom_mode()
        return self.read(rom_size, addr)

    def read_chr_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        self.set_chr_rom_mode()
        return self.read(rom_size, addr)

    def read_binary(self, size: int) -> bytearray:
        bin = bytearray([])
        n_mod = 1
        size = size
        if size > 8:
            n_mod = size >> 3
        for i in range(size):
            if i % n_mod == 0:
                sys.stdout.write("#")
                sys.stdout.flush()
                time.sleep(0.001)
            bin.append(gpio_get_data())
            inc_address()

        return bin

    def set_prg_rom_mode(self):
        # PRG-ROM
        # OE  - CpuRw(R//W; Writeが/W)
        # CS  - RomSel(/ROMSEL)
        # WE  - M2(O2; CLKOUT)
        # PPURD - ppu_w(/RD)
        # PPUWR - ppu_r(/WE)

        # OE=1
        #   マッパー0の回路図を見るとCpuRwがない。1でReadにしておく。実質Don't care
        # CS=0
        #   PRG ROMの/OEと/ROMSELが接続。/OEなので0でenable
        # M2=1
        #   マッパー0の回路図を見るとM2(O2)がない。実質Don't care
        # PPUWR=1
        #   マッパー0の回路図を見ると/WEがない。1で無効にしておく。実質Don't care
        # PPURD=1
        #   CHR ROMの/OEと/RDが接続。1で無効にしておく。
        #   また、CHR ROMのPA13と/CSが接続
        set_cpu_rw()
        unset_romsel()

        set_m2_o2()
        set_ppu_w()
        set_ppu_r()

    def set_chr_rom_mode(self):
        # CHR-ROM
        # OE  - CpuRw(R//W; Writeが/W)
        # CS  - RomSel(/ROMSEL)
        # WE  - M2(O2; CLKOUT)
        # PPURD - ppu_w(/RD)
        # PPUWR - ppu_r(/WE)

        # OE=0
        #   マッパー0の回路図を見るとCpuRwがない。0でWriteにしておく。実質Don't care
        # CS=1
        #   PRG ROMの/OEと/ROMSELが接続。/OEなので1でdisable
        # M2=1
        #   マッパー0の回路図を見るとM2(O2)がない。実質Don't care
        # PPUWR=1
        #   マッパー0の回路図を見ると/WEがない。1で無効にしておく。実質Don't care
        # PPURD=1
        #   CHR ROMの/OEと/RDが接続。1で無効にしておく。
        #   また、CHR ROMのPA13と/CSが接続。PA13=0にすることでCHR ROM選択。
        unset_cpu_rw()
        set_romsel()
        unset_m2_o2()
        unset_ppu_w()
        unset_ppu_r()

    def read(self, rom_size: int, addr: int = 0x0000) -> bytearray:
        clear_addr()

        self.dbg.dbg_log(f"read address = {hex(addr)}")
        self.set_addr(addr)
        time.sleep(INTV)
        bin = self.read_binary(rom_size)
        self.bins.extend(bin)

        return bin

    def set_addr(self, addr: int):
        set_address(addr)

    def write_file(self, path: str, data: bytearray):
        with open(path, mode="wb") as f:
            f.write(self.get_header())
            f.write(data)


# 　＄８０００－＄９ＦＦＦ：設定レジスタＲ０　Ｖ－ＲＡＭコントロール
# 　＄Ａ０００－＄ＢＦＦＦ：　　〃　　　Ｒ１　ＣＨＲバンク０
# 　＄Ｃ０００－＄ＤＦＦＦ：　　〃　　　Ｒ２　ＣＨＲバンク１
# 　＄Ｅ０００－＄ＦＦＦＦ：　　〃　　　Ｒ３　ＰＲＧバンク
#
# b15-12 b11-b8 b7-b4  b3-b0
# --------------------------
# 1000   0000   0000   0000   0x8000  b15=1(NC?) b14=0 b13=0 b12=0
# 1010   0000   0000   0000   0xA000  b15=1(NC?) b14=0 b13=1 b12=0
# 1100   0000   0000   0000   0xC000  b15=1(NC?) b14=1 b13=0 b12=0
# 1110   0000   0000   0000   0xE000  b15=1(NC?) b14=1 b13=1 b12=0
class RomDumperMapper1(RomDumper):
    def __init__(self) -> None:
        super().__init__()

    def get_header(self) -> bytes:
        header = HEADER_DATA_COMMON
        header.extend(HEADER_DATA_MAPPER1)
        header.extend(HEADER_DATA_COMMON_FOOTER)
        return bytes(header)

    def reset_bus(self):
        set_cpu_rw()
        set_romsel()
        set_m2_o2()
        set_ppu_r()
        set_ppu_w()

    def clear_sp_register(self, addr: int = 0x0):
        self.reset_bus()

        set_data_ctrl_to_output()
        # clear data
        clear_addr()
        set_address(0x8000 | addr)

        # write data
        unset_m2_o2()
        set_data(0x80)
        unset_cpu_rw()

        unset_romsel()
        time.sleep(INTV)
        set_m2_o2()
        time.sleep(INTV)
        unset_m2_o2()

        self.reset_bus()

    def write_control_register(self, addr: int, value: int, bin_list: list = None):
        self.reset_bus()

        set_data_ctrl_to_output()

        pre = 0
        for i in range(0, 5):
            # set address
            clear_addr()
            set_address(addr)
            unset_m2_o2()
            set_data((value >> i) & 0x1)
            unset_cpu_rw()

            unset_romsel()
            time.sleep(INTV)
            set_m2_o2()
            time.sleep(INTV)
            unset_m2_o2()

            self.reset_bus()

    def select_bank(self, addr: int, bank: int):
        self.dbg.dbg_log(f"select_bank : {bank} addr: {hex(addr)}")
        self.write_control_register(addr, bank)

    def read_prg_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        bins = bytearray([])
        self.set_prg_rom_mode()
        set_data_ctrl_to_intput()
        self.reset_bus()
        self.clear_sp_register()
        self.write_control_register(0x8000, BANK_KEY_MAPPER1_CTRL_REG)

        # PRG bank (1=RAM 0=ROM)
        # 00000 - 01111  0 - 15 bank
        for bank in range(0, 16):
            self.dbg.dbg_log(f"bank: {bank} ")
            self.reset_bus()
            self.select_bank(BANK_PRG_REGISTER, bank)
            self.set_prg_rom_mode()
            set_data_ctrl_to_intput()
            bins.extend(super().read(rom_size, BANK_AREA_MAPPER1))
            self.clear_sp_register()

        return bins

    def read_chr_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        return bytearray([])


class RomDumperMapper3(RomDumper):
    # chr_romのバンクの数を入力
    def __init__(self) -> None:
        super().__init__()
        # self.bank_num = bank_num
        # self.hint = hint

    def get_header(self) -> bytes:
        header = HEADER_DATA_COMMON
        header.extend(HEADER_DATA_MAPPER3)
        header.extend(HEADER_DATA_COMMON_FOOTER)
        return bytes(header)

    # def set_chr_rom_mode(self):
    #     # romsel と cpu_rwはいじらない
    #     # unset_cpu_rw()
    #     # set_romsel()
    #     unset_m2_o2()
    #     unset_ppu_w()
    #     unset_ppu_r()

    def find_mapper_selecting_key(self, key) -> int:
        addr: int = 0
        # print(f"type: {type(key)}")
        for value in self.bins:
            if value == key and addr != 0x0000:
                return addr
            addr = addr + 1

        return 0x0000

    def change_chr_rom_bank(self, key: int, addr: int):
        # データ線を入力→出力に切り替える
        set_data_ctrl_to_output()
        set_m2_o2()
        set_ppu_w()
        set_ppu_r()

        clear_addr()

        # clear_bank_bits() # これはD0,D1を両方共ゼロにする
        set_data(0x00)
        # unset_ppu_r() # おそらくいらない。CHR ROMが出力されてしまう

        # mapper3 のCHR ROMの/OEと/RDが接続されている
        # mapper3 のCHR ROMの/CEと/PA13が接続されている.
        # 参考にした資料はPA13となっているが、これは/PA13のことと思われる。
        # これにより最上位ビット(bit0 - bit15のbit15)が1のときに/CEの入力が1でchip enable がdisableになる

        self.dbg.dbg_log("")
        addr = 0x8000 + addr
        self.set_addr(addr)

        # Fancon      HC161
        # R//W    --- /LD
        # /ROMSEL --- CK
        unset_cpu_rw()
        unset_romsel()

        set_data(key)
        self.dbg.dbg_log(f"key: {hex(key)} addr:{hex(addr)}")

        time.sleep(0.03)

        set_romsel()
        set_cpu_rw()
        # データ線を出力→入力に切り替える
        set_data_ctrl_to_intput()

        unset_m2_o2()
        unset_ppu_w()

        time.sleep(0.03)

    # def set_chr_rom_bank(self, bank: int):
    #     # データ線を入力→出力に切り替える
    #     set_data_ctrl_to_output()
    #     set_m2_o2()
    #     set_ppu_w()
    #     set_ppu_r()

    #     clear_addr()

    #     # clear_bank_bits() # これはD0,D1を両方共ゼロにする
    #     set_data(0x00)
    #     # unset_ppu_r() # おそらくいらない。CHR ROMが出力されてしまう

    #     # mapper3 のCHR ROMの/OEと/RDが接続されている
    #     # mapper3 のCHR ROMの/CEと/PA13が接続されている.
    #     # 参考にした資料はPA13となっているが、これは/PA13のことと思われる。
    #     # これにより最上位ビット(bit0 - bit15のbit15)が1のときに/CEの入力が1でchip enable がdisableになる

    #     # Fancon      HC161
    #     # R//W    --- /LD
    #     # /ROMSEL --- CK
    #     unset_cpu_rw()
    #     unset_romsel()

    #     print("")
    #     if bank == 0:
    #         # mapper3 bank0 (D0=0 D1=0 D4=1 D5=1 0x30)
    #         if self.hint == "star":
    #             self.set_addr(0x812E)  # 0x30
    #         else:
    #             self.set_addr(0x82BC)  # 0x30
    #         set_data(0x30)
    #         print("bank0")
    #     elif bank == 1:
    #         #  mapper3 bank1 (D0=1 D1=0 D4=1 D5=1 0x31)
    #         if self.hint == "star":
    #             self.set_addr(0x85A1)
    #         else:
    #             self.set_addr(0x859C)  #  0x31
    #         set_data(0x31)
    #         print("bank1")
    #     elif bank == 2:
    #         #  mapper3 bank2 (D0=0 D1=1 D4=1 D5=1 0x32)
    #         if self.hint == "star":
    #             self.set_addr(0x8670)
    #         else:
    #             self.set_addr(0x8627)  #  0x32
    #         set_data(0x32)
    #         print("bank2")
    #     else:  # elif bank==3:
    #         #  mapper3 bank3 (D0=1 D1=1 D4=1 D5=1 0x33)
    #         if self.hint == "star":
    #             self.set_addr(0x8679)  #  0x33
    #         else:
    #             self.set_addr(0x8698)  #  0x33

    #         set_data(0x33)
    #         print("bank3")

    #     time.sleep(0.03)

    #     set_romsel()
    #     set_cpu_rw()
    #     # データ線を出力→入力に切り替える
    #     set_data_ctrl_to_intput()

    #     unset_m2_o2()
    #     unset_ppu_w()

    #     time.sleep(0.03)

    def get_bank_key_list(self) -> list:
        return BANK_KEY_LIST

    def read_chr_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        bin = bytearray([])
        for bin_key in self.get_bank_key_list():
            # bank key を探してその値をそれぞれ書き込んでバンクを切り替える
            bnk_addr = self.find_mapper_selecting_key(bin_key)
            self.dbg.dbg_log(f"key: {hex(bin_key)} addr={hex(bnk_addr)}")
            self.change_chr_rom_bank(bin_key, bnk_addr)
            self.set_chr_rom_mode()
            bin.extend(super().read(rom_size, addr))
        return bin


class RomDumperMapper66(RomDumperMapper3):
    def __init__(self) -> None:
        super().__init__()
        # self.prg_rom:bytearray = bytearray([])
        self.chr_rom: bytearray = bytearray([])

    def get_bank_key_list(self) -> list:
        return BANK_KEY_MAPPER66_LIST0

    def get_header(self) -> bytes:
        header = HEADER_DATA_COMMON
        header.extend(HEADER_DATA_MAPPER66)
        header.extend(HEADER_DATA_COMMON_FOOTER)
        return bytes(header)

    def read_prg_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        bin = bytearray([])
        self.set_prg_rom_mode()
        super().read(rom_size, 0x8000)
        for bin_key in self.get_bank_key_list():
            # bank key を探してその値をそれぞれ書き込んでバンクを切り替える
            bnk_addr = self.find_mapper_selecting_key(bin_key)
            self.bins.clear()
            self.dbg.dbg_log(f"key: {hex(bin_key)} addr={hex(bnk_addr)}")
            self.change_chr_rom_bank(bin_key, bnk_addr)
            self.set_prg_rom_mode()
            bin.extend(super().read(rom_size, 0x8000))

            bnk_addr = self.find_mapper_selecting_key(bin_key)
            set_address(0)
            unset_romsel()
            unset_cpu_rw()
            set_data_ctrl_to_output()
            set_address(bnk_addr)
            set_data(bin_key)
            set_cpu_rw()
            set_romsel()
            set_data_ctrl_to_intput()
            unset_ppu_r()
            # self.set_chr_rom_mode()
            self.chr_rom.extend(super().read(0x2000, 0x0000))

        return bin

    def read_chr_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        return self.chr_rom


# VRC2
# Nickname	PCB	A0	A1	Registers	iNES mapper	submapper
# VRC2a	351618	A1	A0	$x000, $x002, $x001, $x003	22	0
# VRC2b	many†	A0	A1	$x000, $x001, $x002, $x003	23	3 ***
# VRC2c	351948	A1	A0	$x000, $x002, $x001, $x003	25	3
# --------------------------------------------------------------------
# Wai Wai World	VRC2b	23
# --------------------------------------------------------------------
# Reference
# https://www.nesdev.org/wiki/VRC2_and_VRC4
# https://github.com/ahefner/tenes/blob/master/tech/everynes.txt#L2775C1-L2775C1
# https://www.famicomworld.com/forum/index.php?topic=4438.0


class RomDumperMapper23(RomDumperMapper66):
    def __init__(self) -> None:
        super().__init__()

    def get_header(self) -> bytes:
        header = HEADER_DATA_COMMON
        header.extend(HEADER_DATA_MAPPER23)
        header.extend(HEADER_DATA_COMMON_FOOTER)
        return bytes(header)

    def get_bank_key_list(self) -> list:
        return [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
        ]

    def read_prg_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        bin = bytearray([])
        self.set_prg_rom_mode()
        super().read(rom_size, 0x8000)
        for bin_key in self.get_bank_key_list():
            bnk_addr = 0x8000
            self.bins.clear()
            self.dbg.dbg_log(f"key: {hex(bin_key)} addr={hex(bnk_addr)}")
            self.change_chr_rom_bank(bin_key, bnk_addr)
            self.set_prg_rom_mode()
            bin.extend(super().read(rom_size, 0x8000))

        return bin

    def read_chr_rom(self, rom_size: int, addr: int = 0) -> bytearray:
        bin = bytearray([])
        start = 0x0000
        addr = 0
        bnk_addr_low_list = [0xB000]
        # , 0xB002, 0xC000, 0xC002, 0xD000, 0xD002, 0xE000, 0xE002
        # i = 0
        # print(f"size={rom_size}")
        for bin_key in range(128):  # 128KB only (1 KiB switchable CHR bank)
            for bnk_addr in bnk_addr_low_list:
                self.change_chr_rom_bank(bin_key & 0x0F, bnk_addr)
                self.change_chr_rom_bank((bin_key >> 4) & 0x0F, bnk_addr + 1)
                self.set_chr_rom_mode()
                bin.extend(super().read(rom_size, start + addr))
                # print_binary_view(
                #     self.dbg, i * 16, bin, True if i == 0 else False, False
                # )
                # print(f" bin_key={bin_key}", end="")
                # print(f" bin_key={bin_key}")
                # i = i + 1
        return bin


def led_testing(arg_dict: dict):
    led_freq: list[float] = arg_dict["led_freq"]
    led_duty: list[float] = arg_dict["led_duty"]
    led_time: int = arg_dict["led_time"]
    led_number: list[int] = arg_dict["led_number"]
    print("LED test")
    pwm = []
    led_freq.reverse()
    led_duty.reverse()
    for no in led_number:
        pwm.append(GPIO.PWM(port_tbl_pwm_ctrl[no], led_freq.pop()))
    # p.ChangeFrequency(20)
    for p in pwm:
        p.start(led_duty.pop())
    time.sleep(led_time)
    for p in pwm:
        p.stop()
    term_port()


def parse_args(args: list) -> dict:
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    argparser.add_argument(
        "-o", "--output_file", default="output.nes", help="output file name;"
    )
    argparser.add_argument(
        "-p",
        "--prg_rom_size",
        choices=[SIZE_8K, SIZE_16K, SIZE_32K],
        default=SIZE_16K,
        help="program rom size select;",
    )
    argparser.add_argument(
        "-c",
        "--chr_rom_size",
        choices=[SIZE_1K, SIZE_8K, SIZE_16K, SIZE_32K],
        default=SIZE_8K,
        help="charactor rom size select;",
    )
    argparser.add_argument(
        "-a",
        "--mapper",
        choices=["mapper0", "mapper1", "mapper3", "mapper66", "mapper23"],
        default="mapper0",
        help="mapper select;",
    )
    # argparser.add_argument(
    #     "-t",
    #     "--hint",
    #     choices=["default", "star"],
    #     default="deault",
    #     help="mapper select;",
    # )
    argparser.add_argument(
        "-m", "--mode", choices=["dumper", "led_test"], default="dumper", help="mode"
    )
    argparser.add_argument(
        "-d", "--debug", nargs="?", const=True, default=False, help="debug log"
    )
    argparser.add_argument(
        "-i", "--info", nargs="?", const=True, default=False, help="game infomation"
    )
    argparser.add_argument("-s", "--size", type=int, default=256, help="read size")
    argparser.add_argument(
        "-D", "--led_duty", nargs="*", type=float, default=[1], help="LED testing only"
    )
    argparser.add_argument(
        "-F", "--led_freq", nargs="*", type=float, default=[20], help="LED testing only"
    )
    argparser.add_argument(
        "-N", "--led_number", nargs="*", type=int, default=[0], help="LED testing only"
    )
    argparser.add_argument("-T", "--led_time", default=5, help="LED testing only")
    # argparser.add_argument("-d", "--output_dir", type=str, default=OUTPUT_DIR)
    user_args = args.copy()
    user_args.pop(0)  # pop first param(conv_to_geber.py path)
    parse_args = argparser.parse_args(user_args)
    return vars(parse_args)


def print_binary_view(
    dbg: Debug,
    startaddr: int,
    data: dict,
    first_line: bool = True,
    last_line: bool = True,
):
    if first_line:
        dbg.dbg_print("======================================================")
    addr = startaddr
    if first_line:
        dbg.dbg_print("     |", False)
        for value in range(16):
            formated = format(value, "02x").upper()
            dbg.dbg_print(f" {formated}", False)
        dbg.dbg_print("\n------------------------------------------------------", False)
    idx = 0
    for value in data:
        if idx % 16 == 0:
            dbg.dbg_print("")
            formated = format(addr + idx, "04x").upper()
            dbg.dbg_print(f"{formated} |", False)
        formated = format(value, "02x").upper()
        dbg.dbg_print(f" {formated}", False)
        idx = idx + 1
    if last_line:
        dbg.dbg_print("")
        dbg.dbg_print("======================================================")


def print_game_info(dump: RomDumper, size: int):
    data = dump.read_prg_rom(size)
    # print(len(data))
    print("")
    data_l = []
    for i in range(len(data)):
        data_l.append(data[i])
        # print(f'{format(data[i],"02X")} ', end="")
    print_binary_view(Debug(), 0, data_l)
    print("")


def Term():
    clear_addr()
    print("Term Port")
    term_port()


def MainLoop():
    args = sys.argv
    arg_dict = parse_args(args)
    path_w = arg_dict["output_file"]
    mode: str = arg_dict["mode"]
    led_test: bool = False
    mapper: str = arg_dict["mapper"]
    # hint: str = arg_dict["hint"]
    debug: bool = arg_dict["debug"]
    info: bool = arg_dict["info"]
    size: int = arg_dict["size"]
    if mode == "led_test":
        led_test = True

    rom_size: int = ROM_SIZE_DICT[arg_dict["prg_rom_size"]]  # 0x4000  # PRG-ROM 16K
    chr_size: int = ROM_SIZE_DICT[arg_dict["chr_rom_size"]]  # 0x2000  # CHR-ROM 8K
    # start_address: int = 0x0000

    init_port()

    # print(f"{type(led_freq)}")
    # print(f"{type(led_duty)}")
    # print(f"{type(led_time)}")
    if led_test:
        led_testing(arg_dict)
        Term()
        return

    dump: RomDumper = None
    if mapper == "mapper3":
        dump = RomDumperMapper3()
    elif mapper == "mapper66":
        dump = RomDumperMapper66()
    elif mapper == "mapper1":
        dump = RomDumperMapper1()
    elif mapper == "mapper23":
        dump = RomDumperMapper23()
    else:
        dump = RomDumper()

    if debug:
        dump.set_debug_object(Debug())

    if info:
        print_game_info(dump, size)
        Term()
        return

    bin = bytearray([])
    bin.extend(dump.read_prg_rom(rom_size))
    bin.extend(dump.read_chr_rom(chr_size))

    dump.write_file(path_w, bin)
    # with open(path_w, mode="wb") as f:
    #     header = bytes(HEADER_DATA)
    #     f.write(header)
    #     f.write(bin)

    clear_addr()
    term_port()
    print("")
    print("Complete!")


try:
    MainLoop()
except Exception as e:
    print(f"Error: {e}")
    print("Clear Address")
    Term()
