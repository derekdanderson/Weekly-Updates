import json, urllib.request

TOKEN = "xoxb-1993819124755-11125079672035-Lt3TBaxkZ7Zhh2ezVNJyLxDn"
CHANNEL = "D0B3TB60R1C"
PDF_URL = "https://www.irondalebands.org/uploads/4/8/3/5/48357505/weekly_update_5-27-2026.pdf"
BANNER_URL = "https://www.irondalebands.org/uploads/4/8/3/5/48357505/ihsmk-header_orig.png"
CALENDAR_URL = "https://docs.google.com/document/d/1B9f32KEW2Y-brFYof47dDMmWk8zuCGnP/edit"
DR_L_EMAIL = "cameron.longabaugh@moundsviewschools.org"

def spacer():
    return {"type": "section", "text": {"type": "mrkdwn", "text": " "}}

def header(text):
    return {"type": "header", "text": {"type": "plain_text", "text": text, "emoji": True}}

def section(text):
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}

def section_with_button(text, btn_label, btn_url):
    return {
        "type": "section",
        "text": {"type": "mrkdwn", "text": text},
        "accessory": {
            "type": "button",
            "text": {"type": "plain_text", "text": btn_label, "emoji": True},
            "url": btn_url
        }
    }

def bold(text):
    return {"type": "text", "text": text, "style": {"bold": True}}

def plain(text):
    return {"type": "text", "text": text}

def link(text, url):
    return {"type": "link", "text": text, "url": url}

blocks = [
    # Banner
    {"type": "image", "image_url": BANNER_URL, "alt_text": "Irondale Marching Knights"},

    # Title
    header(":ihsmk_knight: IRONDALE MARCHING KNIGHTS :ihsmk_knight:"),
    section(f"*<{PDF_URL}|Weekly Update – May 27, 2026>*"),
    {"type": "divider"},

    # Important Dates — rich_text
    {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "text", "text": "Important Dates", "style": {"bold": True}}]
            },
            {
                "type": "rich_text_list",
                "style": "bullet",
                "elements": [
                    {"type": "rich_text_section", "elements": [
                        bold("This Saturday, May 30"), plain(" — Sponsorship Day (arrive at Irondale by 9:00am)")
                    ]},
                    {"type": "rich_text_section", "elements": [
                        bold("Saturday, June 6"), plain(" — All Forms Due + June Camp Day (9:00am–4:00pm) + Last day for uniform measurements")
                    ]},
                    {"type": "rich_text_section", "elements": [
                        bold("By June 15"), plain(" — Financial Aid responses sent")
                    ]},
                    {"type": "rich_text_section", "elements": [
                        bold("Sunday, July 12, 2:00pm"), plain(" — Optional virtual Band Camp info meeting")
                    ]},
                    {"type": "rich_text_section", "elements": [
                        bold("July 19–24"), plain(" — Band Camp at University of Minnesota – Morris")
                    ]},
                    {"type": "rich_text_section", "elements": [
                        link("Rehearsal & Performance Calendar", CALENDAR_URL)
                    ]},
                ]
            }
        ]
    },

    # Parent Volunteers for Sponsorship Day
    spacer(),
    header(":mega: Parent Volunteers for Sponsorship Day"),
    section_with_button(
        "Sponsorship Day is *this Saturday, May 30th*! We are still looking for about 15 more volunteer drivers. "
        "You must be 18 years of age with a valid driver's license. "
        "Students should wear something school-related (Irondale, Mounds View, or similar spirit wear) "
        "and bring money for lunch and their water bottle. "
        "We will begin at Irondale at 9:00am with a brief orientation before heading out to collect donations.",
        "Sign Up to Drive",
        "https://dash.pointapp.org/events/663611"
    ),

    # All Forms Due June 6th
    spacer(),
    header(":clipboard: All Forms Due June 6th"),
    section_with_button(
        "The following forms are due on *Saturday, June 6th*. "
        "Access all forms at irondalebands.org → Parent/Student Info → Forms.",
        "View All Forms",
        "http://www.irondalebands.org/"
    ),
    {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_list",
                "style": "bullet",
                "elements": [
                    {"type": "rich_text_section", "elements": [plain("Registration Form")]},
                    {"type": "rich_text_section", "elements": [plain("Health Form")]},
                    {"type": "rich_text_section", "elements": [plain("Commitment Contract")]},
                    {"type": "rich_text_section", "elements": [plain("Absence Request Form (ARF)")]},
                ]
            }
        ]
    },

    # June Camp Day
    spacer(),
    header(":musical_note: June Camp Day"),
    section(
        "_Our June Camp Day is *Saturday, June 6th* — this is also the final day to get your uniform measurements!_ "
        "Students will have the choice to pack a lunch, have lunch dropped off by a parent, "
        "or go off campus to eat with friends.\n\n"
        "*Tentative Schedule:*\n"
        "• 9:00 AM — Rehearsal at Irondale\n"
        "• 11:45 AM — Lunch\n"
        "• 1:15 PM — Rehearsal at Irondale\n"
        "• 4:00 PM — Dismissal"
    ),

    # Financial Aid
    spacer(),
    header(":money_with_wings: Financial Aid Applications"),
    section_with_button(
        f"_Financial Aid Applications are due on *Saturday, June 6th*._ "
        f"You will receive a response by no later than June 15th. "
        f"Please email *<mailto:{DR_L_EMAIL}|Dr. Longabaugh>* if you have any questions. "
        f"We can grant up to 50% of financial aid in a single season.",
        "Apply for Financial Aid",
        "https://drive.google.com/file/d/1A67_wKsJZoLI-sr0vNF_nsOq5SYC317m/view?usp=sharing"
    ),

    # Mega Raffle
    spacer(),
    header(":ticket: Mega Raffle"),
    section(
        "As a reminder, this year all families are required to sell 20 Mega Raffles as part of our "
        "Fundraising Campaign. Mega Raffles will be available for students to pick up beginning *June 6th*."
    ),

    # Band Camp Parent Volunteers
    spacer(),
    header(":mega: Band Camp Parent Volunteers"),
    section_with_button(
        "Parents! We are looking for volunteers to help out at Band Camp at the "
        "*University of Minnesota – Morris* on *July 19–24*. "
        "There are opportunities to work the full week or part of the week, "
        "as well as the ability to work remotely while at camp. "
        "All parent volunteers can stay in the dorms and eat in the dining hall for free.",
        "Submit Chaperone Form",
        "https://docs.google.com/forms/d/e/1FAIpQLSdzL8PHL2kIE1tYI784rJxAuarN3LNwCof5030tbVexdvECTQ/viewform"
    ),

    # Band Camp Handbook
    spacer(),
    header(":book: 2026 Band Camp Handbook"),
    section_with_button(
        "Every year we provide a Band Camp Handbook so families can begin to plan for their student's "
        "away camp experience. Band Camp is a vital week to bond and learn a significant portion of our competitive show — "
        "it's often an experience students highlight as one of their favorites. "
        "_Please note this document is a work in progress and will be finalized by *July 1st*._\n\n"
        "On *Sunday, July 12th at 2:00pm* we will host an optional virtual meeting walking through Band Camp in detail. "
        "This meeting will also be recorded and shared out afterwards.",
        "View Band Camp Handbook",
        "https://docs.google.com/document/d/1SFS1FaIr80BwOw0T2gogyYt-EYztSrJaLdrMKNuX8h8/edit?usp=sharing"
    ),

    # Footer
    {"type": "divider"},
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": "_Irondale Band Boosters · Weekly Update · May 27, 2026_"}]
    }
]

payload = json.dumps({"channel": CHANNEL, "blocks": blocks}).encode("utf-8")
req = urllib.request.Request(
    "https://slack.com/api/chat.postMessage",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json; charset=utf-8"}
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    if result.get("ok"):
        print(f"Sent! ts={result['ts']}, blocks={len(blocks)}")
    else:
        print(f"Error: {result.get('error')}")
        print(json.dumps(result, indent=2))
