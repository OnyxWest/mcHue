import subprocess


subprocess.Popen(['java', '-Xms1G', '-Xmx1G', '-XX:+UseG1GC', '-jar', 'PySpigot-1.16.4.jar', 'nogui'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, cwd='C:/Users/Cyrus Sweet/Desktop/Programming/mcHue/Main')


