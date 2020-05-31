from pathlib import Path
import re
import shutil
from zipfile import ZipFile

import fire


def main(f, out_dir):
    f = Path(f)
    out_dir = Path(out_dir)

    unzip_dir = f.parent / f.stem

    with ZipFile(f, "r") as zf:
        zf.extractall(unzip_dir)

    for o in unzip_dir.iterdir():
        if o.is_file():
            html = o
        if o.is_dir():
            shutil.copytree(o, out_dir / "images" / o.stem)
    
    with html.open("r", encoding='utf-8') as hf:
        html_text = hf.read()
    
    title = re.findall("<title>(.+)</title>", html_text)[0]
    # extract title
    html_text = re.sub("<title>.+</title>", "", html_text)

    # remove css
    css_to_replace = re.findall("(html [\w\W]+)\.source", html_text)[0]
    html_text = html_text.replace(css_to_replace, "")

    # remove header
    html_text = re.sub("<header>.+</header>", "", html_text)

    # replace image path
    match_image = re.findall("\w+", title)[0] + "%20"
    html_text = re.sub(match_image, f"/images/{match_image}", html_text)

    # save file
    target_html = out_dir / "_includes/" / str(html.name).replace(" ", "-")

    with target_html.open("w") as th:
        th.write(html_text)
    
    name = "-".join(re.findall("\w+", title)[:2])
    mdfile = out_dir / "_posts" / f"{f.stem}-{name.lower()}.md"

    md_content = f'''---
layout: post
title:  "{title}"
---
{"{%"}\tinclude {target_html.name}\t{"%}"}
'''

    with mdfile.open("w") as mf:
        mf.write(md_content)


if __name__ == "__main__":
    fire.Fire(main)
