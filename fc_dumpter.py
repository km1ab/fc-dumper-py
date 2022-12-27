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

HEADER_DATA = [
    0x4E,
    0x45,
    0x53,
    0x1A,
    ##########
    # mapper 0
    # 0x01,
    # 0x01,
    # 0x00,
    ##########
    # mapper 3
    0x02,
    0x04,
    0x31,
    ##########
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

SIZE_8K = "8K"
SIZE_16K = "16K"
SIZE_32K = "32K"
# SIZE_64K = "64K"
# SIZE_128K = "128K"
# rom_size: int = 0x4000  # PRG-ROM 16K
# chr_size: int = 0x2000  # CHR-ROM 8K
ROM_SIZE_DICT = {SIZE_8K: 0x2000, SIZE_16K: 0x4000, SIZE_32K: 0x8000}


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


class RomDumper:
    def __init__(self) -> None:
        self.bins = bytearray([])

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

        print(f"address = {hex(addr)}")
        self.set_addr(addr)
        time.sleep(INTV)
        bin = self.read_binary(rom_size)
        self.bins.extend(bin)

        return bin

    def set_addr(self, addr: int):
        set_address(addr)


class RomDumperMapper3(RomDumper):
    # chr_romのバンクの数を入力
    def __init__(self, bank_num: int, hint: str = "default") -> None:
        super().__init__()
        self.bank_num = bank_num
        self.chr_mode = False
        self.hint = hint

    def set_prg_rom_mode(self):
        self.chr_mode = False
        return super().set_prg_rom_mode()

    def set_chr_rom_mode(self):
        self.chr_mode = True
        # romsel と cpu_rwはいじらない
        # unset_cpu_rw()
        # set_romsel()
        unset_m2_o2()
        unset_ppu_w()
        unset_ppu_r()

    def set_chr_rom_bank(self, bank: int):
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

        # Fancon      HC161
        # R//W    --- /LD
        # /ROMSEL --- CK
        unset_cpu_rw()
        unset_romsel()

        if bank == 0:
            # mapper3 bank0 (D0=0 D1=0 D4=1 D5=1 0x30)
            if self.hint == "star":
                self.set_addr(0x812E)  # 0x30
            else:
                self.set_addr(0x82BC)  # 0x30
            set_data(0x30)
            print("bank0")
        elif bank == 1:
            #  mapper3 bank1 (D0=1 D1=0 D4=1 D5=1 0x31)
            if self.hint == "star":
                self.set_addr(0x85A1)
            else:
                self.set_addr(0x859C)  #  0x31
            set_data(0x31)
            print("bank1")
        elif bank == 2:
            #  mapper3 bank2 (D0=0 D1=1 D4=1 D5=1 0x32)
            if self.hint == "star":
                self.set_addr(0x8670)
            else:
                self.set_addr(0x8627)  #  0x32
            set_data(0x32)
            print("bank2")
        else:  # elif bank==3:
            #  mapper3 bank3 (D0=1 D1=1 D4=1 D5=1 0x33)
            if self.hint == "star":
                self.set_addr(0x8679)  #  0x33
            else:
                self.set_addr(0x8698)  #  0x33

            set_data(0x33)
            print("bank3")

        time.sleep(0.03)

        set_romsel()
        set_cpu_rw()
        # データ線を出力→入力に切り替える
        set_data_ctrl_to_intput()

        unset_m2_o2()
        unset_ppu_w()

        time.sleep(0.03)

    def read(self, rom_size: int, addr: int = 0) -> bytearray:
        if self.chr_mode:
            bin = bytearray([])
            for bank in range(self.bank_num):
                self.set_chr_rom_bank(bank)
                self.set_chr_rom_mode()
                bin.extend(super().read(rom_size, addr))
            return bin

        return super().read(rom_size, addr)  # for prg rom mode


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
        choices=[SIZE_16K, SIZE_32K],
        default=SIZE_16K,
        help="program rom size select;",
    )
    argparser.add_argument(
        "-c",
        "--chr_rom_size",
        choices=[SIZE_8K, SIZE_16K, SIZE_32K],
        default=SIZE_8K,
        help="charactor rom size select;",
    )
    argparser.add_argument(
        "-a",
        "--mapper",
        choices=["mapper0", "mapper3"],
        default="mapper0",
        help="mapper select;",
    )
    argparser.add_argument(
        "-t",
        "--hint",
        choices=["default", "star"],
        default="deault",
        help="mapper select;",
    )
    argparser.add_argument(
        "-m", "--mode", choices=["dumper", "led_test"], default="dumper", help="mode"
    )
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


def MainLoop():
    args = sys.argv
    arg_dict = parse_args(args)
    path_w = arg_dict["output_file"]
    mode: str = arg_dict["mode"]
    led_test: bool = False
    mapper: str = arg_dict["mapper"]
    hint: str = arg_dict["hint"]
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
        return

    dump: RomDumper = None
    if mapper == "mapper3":
        dump = RomDumperMapper3(4, hint)
    else:
        dump = RomDumper()

    bin = bytearray([])
    dump.set_prg_rom_mode()
    bin.extend(dump.read(rom_size))
    dump.set_chr_rom_mode()
    bin.extend(dump.read(chr_size))

    with open(path_w, mode="wb") as f:
        header = bytes(HEADER_DATA)
        f.write(header)
        f.write(bin)

    clear_addr()
    term_port()
    print("")
    print("Complete!")


try:
    MainLoop()
except Exception as e:
    print(f"Error: {e}")
    print("Clear Address")
    clear_addr()
    print("Term Port")
    term_port()
