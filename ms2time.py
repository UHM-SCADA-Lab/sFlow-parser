#Function that converts ms to days, hours, minutes, and seconds
def ms2time(ms):
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    hrs, m = divmod(m, 60)
    days, hrs = divmod(hrs, 24)
    s = s + ms/1000
    return days, hrs, m, s
