
def write_file(logfile):
  count = 0
  with open(logfile, 'a') as f:
      for line in f:
         if "ERROR" in line:
            f.write("\nWrite it up one more time")




       