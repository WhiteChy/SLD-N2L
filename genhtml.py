#!/usr/bin/env python3

from jinja2 import FileSystemLoader, Environment

import os
from glob import glob

def gen_rows(gtype):
    ret = []

    SLD_N2L = 'data/SLD_N2L'
    CycleGAN = 'data/CycleGAN'
    StarGAN = 'data/StarGAN'
    Freevc = 'data/Freevc'
    DDDMVC = 'data/DDDMVC'
    lombard = 'data/default'
    normal = 'data/normal'

    wavs = sorted(glob(f'data/normal/{gtype}/*.wav'))

    for wav in wavs:
        basename = os.path.basename(wav).split('.')[0]
        src_basename = basename
        tgt_basename = basename
        if gtype == '-8.5SSN':
            tmp = '-8.5SSN'
        elif gtype =='-8.5Babble':
            tmp = '-8.5Babble'
        else:
            tmp = 'clean'

        src = os.path.join("data", 'normal',tmp, f"{src_basename}.wav")
        tgt = os.path.join("data", "default", tmp,f"{tgt_basename}.wav")
        row = (
                src_basename,
                tgt_basename.replace('SSN40','SSN80'),
                src, 
                tgt,
                os.path.join(CycleGAN, gtype, f'{src_basename}.wav'),
                os.path.join(StarGAN, gtype, f'{src_basename}.wav'),
                os.path.join(Freevc, gtype, f'{src_basename}.wav'),
                os.path.join(DDDMVC, gtype, f'{src_basename}.wav'),
                os.path.join(SLD_N2L, gtype, f'{src_basename}.wav'),
        )
        ret.append(row)
        print(row)
    return ret


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("base.html.jinja2")

    s2s_rows = gen_rows("clean")
    u2s_rows = gen_rows("-8.5SSN")
    u2u_rows = gen_rows("-8.5Babble")

    html = template.render(
        s2s_rows=s2s_rows,
        u2s_rows=u2s_rows,
        u2u_rows=u2u_rows
    )
    print(html)
    with open("index.html", "w+", encoding="utf-8") as file:
        file.write(html)

    print("HTML content has been written to index.html")
if __name__ == "__main__":
    main()
