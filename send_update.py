import json, os, urllib.request

if "SLACK_BOT_TOKEN" not in os.environ:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#") and "=" in line:
                    key, _, value = line.strip().partition("=")
                    os.environ.setdefault(key, value)

TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL = "D0B3TB60R1C"
PDF_URL = "https://www.irondalebands.org/uploads/4/8/3/5/48357505/weekly_update_7-8-2026.pdf"
CALENDAR_URL = "https://www.irondalebands.org/calendar.html"
SCHEDULE_URL = "https://docs.google.com/spreadsheets/d/1h7C1evg16yoKaVHpn5dAecfs2VfCmlfZYdy9w9-uxGM/edit?usp=sharing"
HANDBOOK_URL = "https://docs.google.com/document/d/1SFS1FaIr80BwOw0T2gogyYt-EYztSrJaLdrMKNuX8h8/edit?usp=sharing"

text = f"""\
:ihsmk_knight: *IRONDALE MARCHING KNIGHTS* :ihsmk_knight:
*<{PDF_URL}|Weekly Update – July 8, 2026>*

*<{CALENDAR_URL}|Important Dates>:*
• *Saturday, July 11* — July Camp Day (9:00am–5:00pm)
• *Sunday, July 12, 2:00pm* — Optional Virtual Band Camp Meeting
• *July 19–24* — Band Camp (University of Minnesota – Morris)
• *Saturday, August 8* — Stockyard Days Parade (first Instep posted)

:iphone: *UDB APP:*
All hornline, batterie, and color guard students should have *UDB Powered by Arc* downloaded on their smart device. Front Ensemble does NOT need to download UDB. If your student does not have a smartphone, we will have a smartphone available for drill learning only (it does not house any other apps).

:sunny: *JULY CAMP DAY:*
_Our July Camp Day is *Saturday, July 11th from 9:00am–5:00pm*._ Lunch is NOT provided to students on this day — students can bring a lunch or go out for lunch, and parents are also welcome to drop off a lunch for their student at Irondale.

*Schedule:*
• 9:00 AM — Rehearsal at Irondale
• 12:30 PM — Lunch
• 2:00 PM — Rehearsal at Irondale
• 5:00 PM — Dismissal

:bus: *BAND CAMP DETAILS:*
In addition to the details in the Band Camp Handbook, Dr. L has ironed out some additional details with the University of Minnesota – Morris:
• Report time to Irondale on *Sunday, July 19th* is *1:30pm*; buses are planned to depart by *3:00pm*.
• Students should pack only what they need for band camp — _there are no elevators in the dorms_, so anything they bring must be hauled up and down the stairs at check-in and check-out. More information will be shared at the virtual meeting.
• Free time at the indoor UMN recreation pool is tentatively scheduled for *12:30–2:00pm on Wednesday*. Students who want to take advantage of this during their Wednesday free time are welcome to pack a swimsuit.

*<{SCHEDULE_URL}|View the full Band Camp schedule>* — more details will be shared this coming Sunday!

:books: *BAND CAMP HANDBOOK & VIRTUAL MEETING:*
Dr. L has started working on the *<{HANDBOOK_URL}|2026 IHSMK Band Camp Handbook>*. _Please note this is a live document, and information may change between now and July 1st._ We will have an optional Band Camp Virtual Meeting on *Sunday, July 12th at 2:00pm* — the Google Meet link is posted on the *<{CALENDAR_URL}|Google Calendar>* event.

:footprints: *INSTEPS:*
Insteps are the itineraries for our performances throughout the season. Every instep for the season will be posted on our website — select "Parent / Student Info" then "Insteps." Dr. L has posted the first instep of the season for the *Stockyard Days Parade on Saturday, August 8th*. _Please note that the report time in this instep will likely change once the parade route and street closures are finalized._

_Irondale Band Boosters · Weekly Update · July 8, 2026_"""

payload = json.dumps({"channel": CHANNEL, "text": text}).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json; charset=utf-8"}
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    if result.get("ok"):
        print(f"Sent! ts={result['ts']}")
    else:
        print(f"Error: {result.get('error')}")
        print(json.dumps(result, indent=2))
