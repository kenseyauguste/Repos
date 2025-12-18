events = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "ERROR"]

count_of_error = events.count("ERROR")
count_of_info = events.count("INFO")
count_of_warning = events.count("WARNING")

print(f' Error: {count_of_error}\n Info: {count_of_info}\n Warning: {count_of_warning}')
