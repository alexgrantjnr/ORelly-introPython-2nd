minute = 60
hour = 60
day = 24

ans = input("Calculate seconds per day or hour enter day/hour")

sec_per_hur = minute * hour
sec_per_day = day * sec_per_hur

if ans == "day":
    print(sec_per_hur)
else:
    print(sec_per_day)
    print(sec_per_day / sec_per_hur)
    print(sec_per_day // sec_per_hur)
