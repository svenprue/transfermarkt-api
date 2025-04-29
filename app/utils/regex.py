REGEX_DOB: str = r"^(?P<dob>.*)\s\((?P<age>\d*)\)"
REGEX_MEMBERS_DATE: str = r"\(Score: (?P<date>.+)\)"
REGEX_BG_COLOR: str = r"background-color:(?P<color>.+);"
REGEX_CHART_CLUB_ID: str = r"(?P<club_id>\d+)"
REGEX_COUNTRY_ID: str = r"(?P<id>\d)"
REGEX_DOB_AGE: str = r"^(?P<dob>\w{3} \d{1,2}, \d{4}) \((?P<age>\d{2})\)"

REGEX_CLUB_ID: str = r"/verein/(?P<club_id>\d+)"

# For extracting player IDs from URLs like "https://www.transfermarkt.com/player-name/profil/spieler/28003"
REGEX_PLAYER_ID: str = r"/spieler/(?P<player_id>\d+)"

# For extracting manager IDs from URLs like "https://www.transfermarkt.com/manager-name/profil/trainer/5672"
REGEX_MANAGER_ID: str = r"/trainer/(?P<manager_id>\d+)"

# For parsing dates that might appear in different formats on manager profiles
REGEX_DATE_FORMAT: str = r"(?P<date>\w{3} \d{1,2}, \d{4}|\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})"