"""time"""
def main():
    """sec to sss"""
    sec_time = int(input())
    time_sec = sec_time % 60
    min_time = sec_time // 60
    hour_time = min_time // 60
    min_time = min_time % 60
    day_time = hour_time // 24
    hour_time = hour_time % 24
    print(day_time,hour_time,min_time,time_sec)
main()