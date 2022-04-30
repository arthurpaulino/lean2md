import os
import sys

__version__ = "0.0.2"

def build_blocks(lines):
    reading_lean_code = True
    blocks = []
    content = ""
    for i, line_n in enumerate(lines):
        line = line_n.split("\n")[0]
        if line.startswith("/-"):
            if not reading_lean_code:
                raise RuntimeError(
                    "Nested lean commentary sections not allowed in:\n" +
                    "  line {}: {}".format(str(i + 1), line)
                )
            blocks.append({"content" : content.strip(), "is_code" : True})
            reading_lean_code = False
            content = line.split("/-!" if line.startswith("/-!") else "/-")[-1]
            content += "\n"
            if line.endswith("-/"):
                reading_lean_code = True
                content = content.split("-/")[0]
                blocks.append({"content" : content.strip(), "is_code" : False})
                content = ""
        elif line.endswith("-/"):
            content += line.split("-/")[0]
            reading_lean_code = True
            blocks.append({"content" : content.strip(), "is_code" : False})
            content = ""
        else:
            content += line + "\n"
    if content != "":
        blocks.append({"content" : content.strip(), "is_code" : True})
    return blocks

def merge_blocks(blocks):
    res = ""
    for block in blocks:
        if block["content"] == "":
            continue
        if block["is_code"]:
            res += "```lean\n" + block["content"] + "\n```\n\n"
        else:
            res += block["content"] + "\n\n"
    return res.strip() + "\n"


def lean_file_2_md(filename):
    lines = open(filename, "r").readlines()
    blocks = build_blocks(lines)
    return merge_blocks(blocks)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m lean2md <lean_src_dir> <md_tgt_dir>")
        exit()
    src = sys.argv[1]
    if not src.endswith("/"):
        src += "/"
    tgt = sys.argv[2]
    if not tgt.endswith("/"):
        tgt += "/"
    os.makedirs(tgt, exist_ok=True)
    for filename in os.listdir(src):
        if not filename.endswith(".lean"):
            continue
        tgt_filename = tgt + filename.split("/")[-1].split(".lean")[0] + ".md"
        f = open(tgt_filename, "w")
        f.write(lean_file_2_md(src + filename))
        f.close()
