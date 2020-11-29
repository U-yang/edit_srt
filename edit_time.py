import os
import datetime
import re

fname = "path_to_file"
assert os.path.exists(fname)


def set_time(line):
    duration = line.split(" --> ")
    start = duration[0].split(":")
    end = duration[1].split(":")
    td_start = datetime.timedelta(hours=int(start[0]), minutes=int(start[1]), seconds=int(start[-1].split(",")[0]), milliseconds=int(start[-1].split(",")[-1]))
    td_end = datetime.timedelta(hours=int(end[0]), minutes=int(end[1]), seconds=int(end[-1].split(",")[0]), milliseconds=int(end[-1].split(",")[-1]))
    return td_start, td_end


def decrease_time(start, end, seconds=0, milliseconds=0, minutes=0, hours=0):
    diff = datetime.timedelta(seconds=seconds, milliseconds=milliseconds, minutes=minutes, hours=hours)
    res_start = start - diff
    res_end = end - diff
    return res_start, res_end


def increase_time(start, end, seconds=0, milliseconds=0, minutes=0, hours=0):
    diff = datetime.timedelta(seconds=seconds, milliseconds=milliseconds, minutes=minutes, hours=hours)
    res_start = start + diff
    res_end = end + diff
    return res_start, res_end


def change_format(start, end):
    srt_start = [i.zfill(2) if num < 3 else i[:3] for num, i in enumerate(re.split("[:.]", str(start)))]
    srt_end = [i.zfill(2) if num < 3 else i[:3] for num, i in enumerate(re.split("[:.]", str(end)))]
    combined = f"{srt_start[0]}:{srt_start[1]}:{srt_start[2]},{srt_start[-1]} --> {srt_end[0]}:{srt_end[1]}:{srt_end[2]},{srt_end[-1]}\n"
    return combined


with open(fname, encoding="utf-8", mode="r") as f:
    with open("jpn.srt.v2.srt", encoding="utf-8", mode="w") as fw:
        for num, i in enumerate(f.readlines()):
            if "-->" in i:
                start, end = set_time(i)
                new_start, new_end = increase_time(start, end, seconds=1)
                str_format = change_format(new_start, new_end)
                fw.writelines(str_format)
            else:
                fw.writelines(i)
