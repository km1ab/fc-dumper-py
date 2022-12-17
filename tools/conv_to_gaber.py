import os
import sys
import re
import subprocess

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


def convert_geber(args):
    pre_name = ""
    output_name = "simple_version"
    in_dir = "gerber/pre"
    out_dir = "./output"
    if len(args) > 3:
        in_dir = args[1]
        output_name = args[2]
        out_dir = args[3]
    else:
        print("Usage:")
        print(f"  {args[0]} in_dir target_name out_dir")
        return

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

    ret = subprocess.Popen(f"ls {in_dir}", stdout=subprocess.PIPE, shell=True)
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
        subprocess.run(f"mkdir {out_dir}", shell=True)

    # convert filename to gerber format
    for ext, o_name in convert_dict.items():
        in_item = f"{in_dir}/{pre_name}{ext}"
        out_item = f"{out_dir}/{o_name}"
        if not os.path.exists(in_item):
            print(f"err: not exits file {in_item}")
            continue
        print(f"{in_item} ---> {out_item}")
        cmd = f"cp {in_item} {out_item}"
        subprocess.run(cmd, shell=True)

    print("Completed !!")


convert_geber(sys.argv)
