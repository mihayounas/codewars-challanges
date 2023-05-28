def strip_comments(string, markers):
    lines = string.split("\n")  # Split the string into lines
    for i in range(len(lines)):
        for marker in markers:
            index = lines[i].find(marker)  # Find the marker in the line
            if index != -1:
                lines[i] = lines[i][:index].rstrip()  # Remove text after the marker
                break  # Stop searching for markers in this line

    return "\n".join(lines)  # Join the lines back into a string



few tests failing needs fixing