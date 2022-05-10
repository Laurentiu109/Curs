# Log Levels : DEBUG, INFO, WARNING, ERROR, CRITICAL

from logging import warning


def log(msg, level):
    print("[", level, "]" , msg)

# debug("Mesaj") -> [DEBUG] Mesaj
# info("Mesaj") -> [INFO] Mesaj
# warning("Mesaj") -> [WARNING] Mesaj
# error("Mesaj") -> [ERROR] Mesaj
# critical("Mesaj") -> [CRITICAL] Mesaj

def debug(msg):
    log(msg, "DEBUG" )

def info(msg):
    log(msg, "INFO")

def warning(msg):
    log(msg, "WARNING")

def error(msg):
    log(msg, "ERROR")

def critical(msg):
    log(msg, "CRITICAL")

info("Start script!")