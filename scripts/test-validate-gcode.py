import subprocess

def validate_gcode_file(fileName):
    cli_program = subprocess.Popen(
        ['gvalidate.exe', fileName],
        stdout=subprocess.PIPE,
        encoding='utf-8',
        universal_newlines=True
    )

    output, _ = cli_program.communicate()

    lines = [x for x in output.splitlines() if x != '']
    error = None

    for index, status in enumerate(lines):
        #print("Status of line ", index, " is: ", status, flush=True)
        if status != 'ok':
            error = (index + 1, status)
            break

    cli_program.stdout.close()
    cli_program.wait()
    cli_program.terminate()

    if error:
        print("ERROR: <line: ", error[0], ", code: ", error[1], ">")
    else:
        print("No errors!")

# Example usage
fileName = "HelloWorld.nc"
validate_gcode_file(fileName)
