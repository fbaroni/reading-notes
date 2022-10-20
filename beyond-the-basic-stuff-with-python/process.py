import subprocess, locale

process_object = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
print(process_object.stdout.decode(locale.getpreferredencoding()))
