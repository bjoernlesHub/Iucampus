def read_file(filename):
    import io
    try:
        f = io.open(filename, mode="r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        msg = "Sorry, the file "+ filename + " does not exist."
        print(msg) # Sorry, the file John.txt does not exist.

