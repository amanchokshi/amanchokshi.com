import glob
import re


def get_partial(placeholder, whitespace):
    partialfile = f"./src/snippets/{placeholder}.html"
    with open(partialfile, "r") as pfile:
        sub = ""
        for line in pfile:
            sub = f"{sub}{whitespace}{line}"
    return sub


def check_placeholders(line):
    # pattern to find @@include(partial)
    def get_whitespace(string):
        whitespace = re.sub(r"[a-z]+", "", string)
        whitespace = whitespace.replace("\n", "")
        whitespace = whitespace.replace("@@()", "")
        return whitespace

    pattern = r"@@include\([a-z]*\)"
    if re.search(pattern, line):
        line2 = re.sub(r"(@@include)\(", "", line)
        line2 = re.sub("\)", "", line2)
        # partial name with no spaces, eg. header / footer etc.
        partial_name = line2.strip()
        whitespace = get_whitespace(line)
        return partial_name, whitespace
    else:
        return None, None


def fill_placeholders(line):
    placeholder, whitespace = check_placeholders(line)
    if placeholder:
        return get_partial(placeholder, whitespace)
    else:
        return line


def iterate_source_html_files():
    for file in glob.glob("./src/*.html"):
        file_name = re.sub("./src", "", file)
        file_name = re.sub(".html", "", file_name)
        file_name = file_name.replace("\\", "")
        file_name = file_name.replace("/", "")
        with open(file, "r") as readfile:
            with open(f"./build/{file_name}.html", "w+") as writefile:
                for line in readfile:
                    new_line = fill_placeholders(line)
                    writefile.write(new_line)


if __name__ == "__main__":
    iterate_source_html_files()
