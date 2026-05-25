import calendar
import uuid
from pathlib import Path

import sxtwl


SOLAR_TERMS = [
    "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰",
    "春分", "清明", "谷雨", "立夏", "小满", "芒种",
    "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
    "秋分", "寒露", "霜降", "立冬", "小雪", "大雪",
]


START_YEAR = 2000
END_YEAR = 2100
OUTPUT_FILE = Path("solar_terms_2000_2100.ics")


def ics_escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def generate_events():
    events = []

    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            days_in_month = calendar.monthrange(year, month)[1]

            for day in range(1, days_in_month + 1):
                lunar_day = sxtwl.fromSolar(year, month, day)

                if lunar_day.hasJieQi():
                    term_index = lunar_day.getJieQi()
                    term_name = SOLAR_TERMS[term_index]

                    date_str = f"{year:04d}{month:02d}{day:02d}"
                    uid = f"{year}-{term_name}-{uuid.uuid5(uuid.NAMESPACE_DNS, date_str + term_name)}"

                    events.append(
                        "\r\n".join([
                            "BEGIN:VEVENT",
                            f"UID:{uid}",
                            "DTSTAMP:20260525T000000Z",
                            f"DTSTART;VALUE=DATE:{date_str}",
                            f"SUMMARY:{ics_escape(term_name)}",
                            "TRANSP:TRANSPARENT",
                            "END:VEVENT",
                        ])
                    )

    return events


def main():
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Sunny//24 Solar Terms Calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:二十四节气",
        "X-WR-TIMEZONE:Asia/Shanghai",
        *generate_events(),
        "END:VCALENDAR",
        "",
    ]

    OUTPUT_FILE.write_text("\r\n".join(lines), encoding="utf-8")
    print(f"Generated: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
