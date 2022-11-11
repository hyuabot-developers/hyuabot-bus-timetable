import csv
import os

def create_timetable(timetable_str: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    with open(f"{dir}/timetable.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for section_index, section in enumerate(timetable_str.split("//")):
            if section_index == 0:
                route_id = section
            else:
                for timetable_index, timetable_item in enumerate(section.split("/")):
                    if timetable_index == 0:
                        start_stop_id = timetable_item
                    else:
                        writer.writerow([route_id, start_stop_id, timetable_item])

# kwbus.co.kr - 공지사항에서 시간표 붙여넣기
# // 으로 각 section 구분 (노선 // 시점ID/시점 시간표 // 종점ID/종점 시간표)
string_3100_week = "216000026//217000283/05:30/06:00/06:30/06:50/07:20/08:00/08:50/09:40/10:20/11:00/11:40/12:20/13:00/13:40/14:20/15:00/15:40/16:20/17:00/17:40/18:20/19:00/19:40/20:20/21:00/21:40/22:10/22:40/23:10"
string_3100_sat = "216000026//217000283/05:30/06:10/06:50/07:30/08:10/08:50/09:30/10:10/10:55/11:45/12:40/13:40/14:35/15:25/16:15/17:05/17:55/18:45/19:35/20:20/21:00/21:40/22:20/23:00"
string_3100_sun = "216000026//217000283/05:30/06:10/06:50/07:30/08:10/08:50/09:30/10:10/10:55/11:45/12:40/13:40/14:35/15:25/16:15/17:05/17:55/18:45/19:35/20:20/21:00/21:40/22:20/23:00"

string_3100N_week = "216000096//217000283/23:50/0:20/0:50"
string_3100N_sat = "216000096//217000283"
string_3100N_sun = "216000096//217000283"

string_3101_week = "216000043//217000283/05:45/06:15/06:40/07:00/07:40/08:20/09:20/10:00/10:40/11:20/12:00/12:40/13:20/14:00/14:40/15:20/16:00/16:40/17:20/18:00/18:40/19:20/20:00/20:40/21:20/21:55/22:25/22:55/23:25"
string_3101_sat = "216000043//217000283/05:50/06:30/07:10/07:50/08:30/09:10/09:50/10:30/11:20/12:10/13:10/14:10/15:00/15:50/16:40/17:30/18:20/19:10/20:00/20:40/21:20/22:00/22:40/23:20"
string_3101_sun = "216000043//217000283/05:50/06:30/07:10/07:50/08:30/09:10/09:50/10:30/11:20/12:10/13:10/14:10/15:00/15:50/16:40/17:30/18:20/19:10/20:00/20:40/21:20/22:00/22:40/23:20"

string_3102_week = "216000061//233003145/05:10/05:30/05:50/06:05/06:20/06:35/06:50/07:10/07:30/07:50/08:20/08:50/09:20/09:50/10:15/10:40/11:00/11:20/11:40/12:00/12:20/12:40/13:10/13:35/14:00/14:20/14:40/15:00/15:20/15:40/16:00/16:20/16:40/17:00/17:20/17:45/18:10/18:35/19:00/19:25/19:50/20:15/20:40/21:05/21:30/22:00/22:30/23:00/23:30"
string_3102_sat = "216000061//233003145/05:30/06:00/06:30/07:00/07:30/08:00/08:30/08:55/09:20/09:45/10:10/10:40/11:10/11:40/12:10/12:50/13:30/14:00/14:30/15:00/15:30/16:00/16:30/17:00/17:30/18:00/18:30/19:00/19:30/20:00/20:30/21:00/21:30/22:10/22:50/23:30"
string_3102_sun = "216000061//233003145/05:30/06:00/06:30/07:00/07:30/08:00/08:30/08:55/09:20/09:45/10:10/10:40/11:10/11:40/12:10/12:50/13:30/14:00/14:30/15:00/15:30/16:00/16:30/17:00/17:30/18:00/18:30/19:00/19:30/20:00/20:30/21:00/21:30/22:10/22:50/23:30"

string_10_1_week = "216000068//216000020/6:30/7:00/7:30/8:00/8:30/9:00/9:30/9:55/10:20/10:45/11:35/12:00/12:50/13:20/13:45/14:10/14:40/15:05/15:35/16:00/16:55/17:25/18:20/18:45/19:15/19:40/20:10/20:35/21:00/21:30/22:30//216000145/6:00/6:30/6:50/7:20/7:50/8:20/8:50/9:20/9:50/10:15/10:40/11:05/11:55/12:20/13:10/13:40/14:05/14:30/15:00/15:25/15:55/16:20/17:15/17:45/18:40/19:05/19:35/20:00/20:30/20:55/21:20/21:50/22:50"
string_10_1_sat = "216000068//216000020/6:30/7:00/7:30/8:00/8:30/9:00/9:30/9:55/10:20/10:45/11:35/12:00/12:50/13:20/13:45/14:10/14:40/15:05/15:35/16:00/16:55/17:25/18:20/18:45/19:15/19:40/20:10/20:35/21:00/21:30/22:30//216000145/6:00/6:30/6:50/7:20/7:50/8:20/8:50/9:20/9:50/10:15/10:40/11:05/11:55/12:20/13:10/13:40/14:05/14:30/15:00/15:25/15:55/16:20/17:15/17:45/18:40/19:05/19:35/20:00/20:30/20:55/21:20/21:50/22:50"
string_10_1_sun = "216000068//216000020/6:30/7:00/7:30/8:00/8:30/9:00/9:30/9:55/10:20/10:45/11:35/12:00/12:50/13:20/13:45/14:10/14:40/15:05/15:35/16:00/16:55/17:25/18:20/18:45/19:15/19:40/20:10/20:35/21:00/21:30/22:30//216000145/6:00/6:30/6:50/7:20/7:50/8:20/8:50/9:20/9:50/10:15/10:40/11:05/11:55/12:20/13:10/13:40/14:05/14:30/15:00/15:25/15:55/16:20/17:15/17:45/18:40/19:05/19:35/20:00/20:30/20:55/21:20/21:50/22:50"

string_110_week = "217000014//217000066/05:30/06:00/06:30/06:50/07:10/07:25/07:45/08:05/08:35/09:05/09:30/09:55/10:20/10:45/11:05/11:35/12:05/12:30/12:55/13:20/13:45/14:10/14:35/15:05/15:30/15:55/16:20/16:45/17:10/17:35/18:05/18:30/18:55/19:20/19:45/20:15/21:05/22:00/22:55//202000208/06:30/07:10/07:40/08:00/08:20/08:40/09:00/09:20/09:50/10:20/10:45/11:10/11:35/12:00/12:20/12:50/13:20/13:45/14:10/14:35/15:00/15:25/15:50/16:20/16:45/17:10/17:35/18:00/18:25/18:50/19:20/19:45/20:10/20:35/21:00/21:30/22:20/23:10/0:00"
string_110_sat = "217000014//217000066/05:30/06:00/06:35/07:10/07:45/08:15/08:55/09:35/10:15/10:55/11:30/12:05/12:40/13:15/13:50/14:30/15:00/15:35/16:10/16:45/17:25/17:55/18:35/19:10/19:45/20:40/21:20/22:05/22:55//202000208/06:30/07:10/07:45/08:25/09:00/09:30/10:10/10:50/11:30/12:10/12:45/13:20/13:55/14:30/15:05/15:45/16:20/16:55/17:30/18:05/18:45/19:15/19:55/20:30/21:05/21:55/22:35/23:05/0:00"
string_110_sun = "217000014//217000066/05:30/06:10/06:50/07:30/08:15/09:00/09:50/10:40/11:30/12:15/13:00/13:45/14:30/15:10/15:55/16:40/17:25/18:05/18:50/19:35/20:20/21:10/22:00/22:55//202000208/06:30/07:15/08:00/08:40/09:30/10:15/11:05/11:55/12:45/13:30/14:15/15:00/15:45/16:30/17:15/18:00/18:45/19:25/20:10/20:55/21:30/22:20/23:05/0:00"

string_707_week = "216000001//217000293/04:30/07:10/10:00/13:20/16:40/19:50//202000208/05:40/08:25/11:15/14:35/17:55/21:10"
string_707_sat = "216000001//217000293/04:30/07:10/10:00/13:20/16:40/19:50//202000208/05:40/08:25/11:15/14:35/17:55/21:10"
string_707_sun = "216000001//217000293/04:30/07:10/10:00/13:20/16:40/19:50//202000208/05:40/08:25/11:15/14:35/17:55/21:10"

string_707_1_week = "216000070//217000283/05:00/07:00/10:20/12:50/15:50/18:40/22:40//202000208/05:50/08:20/11:20/13:50/16:50/19:40/23:40"
string_707_1_sat = "216000070//217000283/05:00/07:00/10:20/12:50/15:50/18:40/22:40//202000208/05:50/08:20/11:20/13:50/16:50/19:40/23:40"
string_707_1_sun = "216000070//217000283/05:00/07:00/10:20/12:50/15:50/18:40/22:40//202000208/05:50/08:20/11:20/13:50/16:50/19:40/23:40"

create_timetable(string_3100_week, "./3100/weekdays")
create_timetable(string_3100_sat, "./3100/saturday")
create_timetable(string_3100_sun, "./3100/sunday")

create_timetable(string_3100N_week, "./3100N/weekdays")
create_timetable(string_3100N_sat, "./3100N/saturday")
create_timetable(string_3100N_sun, "./3100N/sunday")

create_timetable(string_3101_week, "./3101/weekdays")
create_timetable(string_3101_sat, "./3101/saturday")
create_timetable(string_3101_sun, "./3101/sunday")

create_timetable(string_3102_week, "./3102/weekdays")
create_timetable(string_3102_sat, "./3102/saturday")
create_timetable(string_3102_sun, "./3102/sunday")

create_timetable(string_110_week, "./110/weekdays")
create_timetable(string_110_sat, "./110/saturday")
create_timetable(string_110_sun, "./110/sunday")

create_timetable(string_707_week, "./707/weekdays")
create_timetable(string_707_sat, "./707/saturday")
create_timetable(string_707_sun, "./707/sunday")

create_timetable(string_707_1_week, "./707-1/weekdays")
create_timetable(string_707_1_sat, "./707-1/saturday")
create_timetable(string_707_1_sun, "./707-1/sunday")

create_timetable(string_10_1_week, "./10-1/weekdays")
create_timetable(string_10_1_sat, "./10-1/saturday")
create_timetable(string_10_1_sun, "./10-1/sunday")
