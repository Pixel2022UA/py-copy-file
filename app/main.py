import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        file_1 = parts[1]
        file_2 = parts[2]
        if os.path.exists(file_1):
            if file_1 != file_2:
                with (open(file_1, "r") as file_in,
                      open(file_2, "w") as file_out):
                    file_out.write(file_in.read())
