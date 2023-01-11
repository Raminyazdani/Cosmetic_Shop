def remove_empty_lines(File):
    with open(File, "r") as f:
        lines = f.readlines()
    with open(File, "w") as f:
        for line in lines:
            if line.strip():
                f.write(line)
