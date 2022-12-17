import os
import sys
import re
import subprocess
import platform
from argparse import ArgumentParser

####################
# gerber info
# TOP LAYER(F.Cu):ファイル名.GTL
# BOTTOM LAYER(B.Cu):ファイル名.GBL
# SOLDER STOP MASK TOP(F.Mask):ファイル名.GTS
# SOLDER STOP MASK BOTTOM(B.Mask):ファイル名.GBS
# SILK TOP:ファイル名.GTO
# SILK BOTTOM(B.SilkS):ファイル名.GBO
# NC DRILL:ファイル名.TXT
# MECHANICAL LAYER(Edge.Cuts):ファイル名.GML

TOP_LAYER = "F_Cu.gtl"  # ファイル名.GTL
BOTTOM_LAYER = "B_Cu.gbl"  # ファイル名.GBL
SOLDER_STOP_MASK_TOP = "F_Mask.gts"  # ファイル名.GTS
SOLDER_STOP_MASK_BOTTOM = "B_Mask.gbs"  # ファイル名.GBS
SILK_TOP = "F_Silkscreen.gto"  # ファイル名.GTO  [kicad 6.0]
SILK_BOTTOM = "B_Silkscreen.gbo"  # ファイル名.GBO  [kicad 6.0]
NC_DRILL_1 = "NPTH.drl"  # ファイル名.TXT
NC_DRILL_2 = "PTH.drl"  # ファイル名.TXT
MECHANICAL_LAYER = "Edge_Cuts.gm1"  # ファイル名.GML

####################
# const info
OUTPUT_NAME = "gerber_output"
OUTPUT_DIR = "./output"

WINDOWS_PLATFM = "Windows"


def parse_args(args: list) -> dict:
    argparser = ArgumentParser()
    argparser.add_argument("in_dir")
    argparser.add_argument("-o", "--output_name", type=str, default=OUTPUT_NAME)
    argparser.add_argument("-d", "--output_dir", type=str, default=OUTPUT_DIR)
    user_args = args.copy()
    user_args.pop(0)  # pop first param(conv_to_geber.py path)
    parse_args = argparser.parse_args(user_args)
    # print(parse_args)
    # print(vars(parse_args))
    return vars(parse_args)


def convert_gerber(args: list):
    arg_dict = parse_args(args)
    in_dir: str = arg_dict["in_dir"]
    output_name: str = arg_dict["output_name"]
    out_dir: str = arg_dict["output_dir"]
    # print(f"in_dir={in_dir}")
    # print(f"output_name={output_name}")
    # print(f"output_dir={out_dir}")

    pre_name = ""
    convert_dict = {
        TOP_LAYER: f"{output_name}.GTL",
        BOTTOM_LAYER: f"{output_name}.GBL",
        SOLDER_STOP_MASK_TOP: f"{output_name}.GTS",
        SOLDER_STOP_MASK_BOTTOM: f"{output_name}.GBS",
        SILK_TOP: f"{output_name}.GTO",
        SILK_BOTTOM: f"{output_name}.GBO",
        NC_DRILL_1: f"{output_name}-NPTH.TXT",
        NC_DRILL_2: f"{output_name}-PTH.TXT",
        MECHANICAL_LAYER: f"{output_name}.GML",
    }

    # check file input_dir
    if not os.path.exists(in_dir):
        print(f"err: not exits directory {in_dir}")
        return

    cmd = "ls"
    pf = platform.system()
    # print(pf)
    if pf == WINDOWS_PLATFM:
        cmd = "dir /B "
    ret = subprocess.Popen(f"{cmd} {in_dir}", stdout=subprocess.PIPE, shell=True)

    input_file_list = []
    for line in ret.stdout:
        dec = line.decode("utf-8").strip()
        # print(dec)
        input_file_list.append(dec)

    # check pattern
    check_pattern = ""
    pre_pattern = ""

    input: str = ""
    for input in input_file_list:
        print(f"check: {input}")
        for ext, o_name in convert_dict.items():
            result = re.search(ext, input)
            if result:
                # print(result.group())
                ret = input.replace(result.group(), "")
                # print(ret )
                check_pattern = ret
                if pre_pattern == "":
                    pre_pattern = check_pattern
                else:
                    if check_pattern != pre_pattern:
                        # NG
                        print("err: pattern invalid")
                        return
                    pre_pattern = check_pattern
                break

    print(f"check_pattern: '{check_pattern}'")

    pre_name = check_pattern
    # check output directory
    if not os.path.exists(out_dir):
        print(f"warning: not exits directory {out_dir}")
        print(f"create directory {out_dir}")
        cmd = "mkdir"
        pf = platform.system()
        if pf == WINDOWS_PLATFM:
            cmd = "md"
            out_dir = out_dir.replace("/", "\\")
            # print(out_dir)
        subprocess.run(f"{cmd} {out_dir}", shell=True)

    # convert filename to gerber format
    for ext, o_name in convert_dict.items():
        in_item = f"{in_dir}/{pre_name}{ext}"
        out_item = f"{out_dir}/{o_name}"
        if not os.path.exists(in_item):
            print(f"err: not exits file {in_item}")
            continue
        cmd = "cp"
        pf = platform.system()
        if pf == WINDOWS_PLATFM:
            cmd = "copy"
            in_item = in_item.replace("/", "\\", -1)
            out_item = out_item.replace("/", "\\", -1)
        print(f"{in_item} ---> {out_item}")
        cmd = f"{cmd} {in_item} {out_item}"
        subprocess.run(cmd, shell=True)

    print("Completed !!")


convert_gerber(sys.argv)
