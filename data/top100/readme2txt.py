import os
import argparse
import re


def main(args):
    """retrieve the url links from the readme file and save them in a txt file"""

    os.makedirs(args.output_path, exist_ok=True)
    regax = "https:\/\/github\.com\/[^\s()<>]+"
    urls = []
    with open(args.readme_path, encoding="utf-8") as f:
        for idx, line in enumerate(f):
            line = line.strip()
            urls += re.findall(regax, line)
    print(f"Found {len(urls)} urls")

    with open(
        os.path.join(args.output_path, f"{args.lang}.txt"), "w", encoding="utf-8"
    ) as f:
        for url in urls:
            f.write(f"{url}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--lang",
        type=str,
        required=True,
        help="programming language name. need to match with the language in --readme_path",
        choices=["python", "javascript", "php", "java", "ruby", "go"],
    )
    parser.add_argument(
        "--readme_path",
        type=str,
        required=True,
        help="readme file path downloaded from one of the language readme from https://github.com/kaxap/arl/tree/master",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
        help="output folder path where the txt file consisting of urls will be saved.",
    )
    args = parser.parse_args()
    main(args)
