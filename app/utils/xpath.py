class Players:
    class Injuries:
        RESULTS = "//div[@id='yw1']//tbody//tr"
        SEASONS = ".//td[1]//text()"
        INJURY = ".//td[2]//text()"
        FROM = ".//td[3]//text()"
        UNTIL = ".//td[4]//text()"
        DAYS = ".//td[5]//text()"
        GAMES_MISSED = ".//td[6]//span//text()"
        GAMES_MISSED_CLUBS_URLS = ".//td[6]//a//@href"

    class JerseyNumbers:
        HEADERS = "//table[@class='items']//thead//tr//@title"
        SEASONS = "//table[@class='items']//td[@class='zentriert']//text()"
        CLUBS_URLS = "//table[@class='items']//td[@class='hauptlink no-border-links']//a//@href"
        DATA = "//table[@class='items']//td[@class='zentriert hauptlink']//text()"

    class Profile:
        ID = "//tm-subnavigation[@controller='spieler']//@id"
        URL = "//link[@rel='canonical']//@href"
        NAME = "//h1[@class='data-header__headline-wrapper']/descendant-or-self::*[not(self::span)]/text()"
        DESCRIPTION = "//meta[@name='description']//@content"
        IMAGE_URL = "//div[@id='fotoauswahlOeffnen']//img//@src"
        SHIRT_NUMBER = "//span[@class='data-header__shirt-number']//text()"
        CURRENT_CLUB_NAME = "//span[@class='data-header__club']//text()"
        CURRENT_CLUB_URL = "//span[@class='data-header__club']//a//@href"
        CURRENT_CLUB_JOINED = "//span[contains(text(),'Joined')]//following::span[1]//text()"
        LAST_CLUB_NAME = "//span[contains(text(),'Last club:')]//span//a//@title"
        LAST_CLUB_URL = "//span[contains(text(),'Last club:')]//span//a//@href"
        MOST_GAMES_FOR_CLUB_NAME = "//span[contains(text(),'Most games for:')]//span//a//text()"
        RETIRED_SINCE_DATE = "//span[contains(text(),'Retired since:')]//span//text()"
        CURRENT_CLUB_CONTRACT_EXPIRES = "//span[contains(text(),'Contract expires')]//following::span[1]//text()"
        CURRENT_CLUB_CONTRACT_OPTION = "//span[contains(text(),'Contract option:')]//following::span[1]//text()"
        NAME_IN_HOME_COUNTRY = "//span[text()='Name in home country:']//following::span[1]//text()"
        FULL_NAME = "//span[text()='Full name:']//following::span[1]//text()"
        DATE_OF_BIRTH_AGE = "//span[@itemprop='birthDate']//text()"
        PLACE_OF_BIRTH_CITY = "//span[contains(text(),'Place of birth')]//following::span[1]//text()"
        PLACE_OF_BIRTH_COUNTRY = "//span[contains(text(),'Place of birth')]//following::span[1]//img//@title"
        HEIGHT = "//span[text()='Height:']//following::span[1]//text()"
        CITIZENSHIP = "//span[text()='Citizenship:']//following::span[1]//text()"
        POSITION = "//span[text()='Position:']//following::span[1]//text()"
        POSITION_MAIN = "//dt[contains(text(),'Main position:')]//following::dd[1]//text()"
        POSITION_OTHER = "//dt[contains(text(),'Other position:')]//following::dd//text()"
        FOOT = "//span[text()='Foot:']//following::span[1]//text()"
        MARKET_VALUE = "//a[@class='data-header__market-value-wrapper']//text()"
        AGENT_NAME = "//span[text()='Player agent:']//following::span[1]//text()"
        AGENT_URL = "//span[text()='Player agent:']//following::span[1]//a//@href"
        OUTFITTER = "//span[contains(text(),'Outfitter:')]//following::span[1]//text()"
        SOCIAL_MEDIA = "//div[@class='social-media-toolbar__icons']//@href"
        TRAINER_PROFILE_URL = "//a[@class='data-header__box--link']//@href"
        TRAINER_PROFILE_POSITION = "//div[@class='dataProfileDaten']//span[1]//text()"
        RELATIVES = (
            "//div[@class='box tm-player-additional-data']"
            "//a[contains(@href, 'profil/spieler') or contains(@href, 'profil/trainer')]"
        )
        RELATIVE_URL = ".//@href"
        RELATIVE_NAME = ".//text()"

    class Search:
        FOUND = "//text()"
        BASE = "//div[@class='box'][h2[contains(text(), 'players')]]"
        RESULTS = BASE + "//tbody//tr[@class='odd' or @class='even']"
        ID = ".//td[@class='hauptlink']//a/@href"
        NAME = ".//td[@class='hauptlink']//a//@title"
        POSITION = ".//td[@class='zentriert'][1]//text()"
        CLUB_NAME = ".//img[@class='tiny_wappen']//@title"
        CLUB_IMAGE = ".//img[@class='tiny_wappen']//@src"
        AGE = ".//td[@class='zentriert'][3]//text()"
        NATIONALITIES = ".//img[@class='flaggenrahmen']/@title"
        MARKET_VALUE = ".//td[@class='rechts hauptlink']//text()"

    class MarketValue:
        URL = "//a[@class='data-header__market-value-wrapper']//@href"
        CURRENT = (
            "//a[@class='data-header__market-value-wrapper']//text()[not(parent::p/@class='data-header__last-update')]"
        )
        HIGHCHARTS = "//script[@type='text/javascript'][text()[contains(.,'Highcharts.Chart')]]//text()"
        RANKINGS_NAMES = "//h3[@class='quick-fact__headline']//text()"
        RANKINGS_POSITIONS = "//span[contains(@class, 'quick-fact__content--large')]//text()"

    class Transfers:
        YOUTH_CLUBS = (
            "//div[@class='box tm-player-additional-data'][descendant::*[contains(text(), 'Youth')]]"
            "//div[@class='content']//text()"
        )

    class Stats:
        ROWS = "//table[@class='items']//tbody//tr"
        HEADERS = "//table[@class='items']//thead//tr//@title"
        COMPETITIONS_URLS = "//table[@class='items']//td[@class='hauptlink no-border-links']//a//@href"
        CLUBS_URLS = "//table[@class='items']//td[@class='hauptlink no-border-rechts zentriert']//a//@href"
        DATA = ".//text()"

    class Achievements:
        ACHIEVEMENTS = "//div[@class='box'][descendant::table[@class='auflistung']]"
        TITLE = ".//h2//text()"
        DETAILS = ".//table[@class='auflistung']//tr"
        SEASON = ".//td[contains(@class, 'erfolg_table_saison')]//text()"
        CLUB_NAME = ".//a[contains(@href, '/verein/')][not(img)]/@title"
        CLUB_URL = ".//a[contains(@href, '/verein/')][not(img)]/@href"
        COMPETITION_NAME = ".//a[contains(@href, '/wettbewerb/') or contains(@href, '/pokalwettbewerb/')]/text()"
        COMPETITION_URL = ".//a[contains(@href, '/wettbewerb/') or contains(@href, '/pokalwettbewerb/')]/@href"


class Clubs:
    class Profile:
        URL = "//div[@class='datenfakten-wappen']//@href"
        NAME = "//header//h1//text()"
        NAME_OFFICIAL = "//th[text()='Official club name:']//following::td[1]//text()"
        IMAGE = "//div[@class='datenfakten-wappen']//@src"
        LEGAL_FORM = "//th[text()='Legal form:']//following::td[1]//text()"
        ADDRESS_LINE_1 = "//th[text()='Address:']//following::td[1]//text()"
        ADDRESS_LINE_2 = "//th[text()='Address:']//following::td[2]//text()"
        ADDRESS_LINE_3 = "//th[text()='Address:']//following::td[3]//text()"
        TEL = "//th[text()='Tel:']//following::td[1]//text()"
        FAX = "//th[text()='Fax:']//following::td[1]//text()"
        WEBSITE = "//th[text()='Website:']//following::td[1]//text()"
        FOUNDED_ON = "//th[text()='Founded:']//following::td[1]//text()"
        MEMBERS = "//th[text()='Members:']//following::td[1]//text()"
        MEMBERS_DATE = "//th[text()='Members:']//following::td[1]//span//text()"
        OTHER_SPORTS = "//th[text()='Other sports:']//following::td[1]//text()"
        COLORS = "//p[@class='vereinsfarbe']//@style"
        STADIUM_NAME = "//li[contains(text(), 'Stadium:')]//span//a//text()"
        STADIUM_SEATS = "//li[contains(text(), 'Stadium:')]//span//span//text()"


        TRANSFER_RECORD = "//li[contains(text(), 'Current transfer record:')]//a//text()"
        MARKET_VALUE = "//a[@class='data-header__market-value-wrapper']//text()"
        CONFEDERATION = "//li[contains(text(), 'Confederation:')]//span//text()"
        RANKING = "//li[contains(text(), 'FIFA World Ranking:')]//span//a//text()"
        SQUAD_SIZE = "//li[contains(text(), 'Squad size:')]//span//text()"
        SQUAD_AVG_AGE = "//li[contains(text(), 'Average age:')]//span//text()"
        SQUAD_FOREIGNERS = "//li[contains(text(), 'Foreigners:')]//span[1]//a//text()"
        SQUAD_NATIONAL_PLAYERS = "//li[contains(text(), 'National team players:')]//span//a//text()"
        LEAGUE_ID = "//span[@itemprop='affiliation']//a//@href"
        LEAGUE_NAME = "//span[@itemprop='affiliation']//a//text()"
        LEAGUE_COUNTRY_ID = "//div[@class='data-header__club-info']//img[contains(@class, 'flaggenrahmen')]//@data-src"
        LEAGUE_COUNTRY_NAME = "//div[@class='data-header__club-info']//img[contains(@class, 'flaggenrahmen')]//@title"
        LEAGUE_TIER = "//div[@class='data-header__club-info']//strong//text()//following::span[1]/a/text()[2]"
        CRESTS_HISTORICAL = "//div[@class='wappen-datenfakten-wappen']//@src"

    class Search:
        BASE = "//div[@class='box'][h2[contains(text(), 'Clubs')]]"
        NAMES = BASE + "//td[@class='hauptlink']//a//@title"
        URLS = BASE + "//td[@class='hauptlink']//a//@href"
        COUNTRIES = BASE + "//td[@class='zentriert']//img[@class='flaggenrahmen']//@title"
        MARKET_VALUES = BASE + "//td[@class='rechts']//text()"
        SQUADS = BASE + "//td[@class='zentriert']//text()"

    class NationalPlayers:
        # Basic team info
        TEAM_NAME = "//h1[@class='data-header__headline-wrapper data-header__headline-wrapper--oswald']//text()"
        TEAM_URL = "//li[@id='overview']//@href"

        # Player rows
        PLAYER_ROWS = "//table[@class='items']//tbody//tr"

        # Player basic info - name, URL and position are correctly structured
        NAMES = "//table[@class='inline-table']//td[@class='hauptlink']//a//text()"
        URLS = "//table[@class='inline-table']//td[@class='hauptlink']//a//@href"
        POSITIONS = "//table[@class='inline-table']//tr[2]//td//text()"

        # Player details - column indexing with proper parent context
        DOB_AGE = "//table[@class='items']//tbody//tr//td[3]//text()"  # Format: "Nov 6, 2001 (23)"

        # Club information - needs to target the title attribute in the anchor
        CURRENT_CLUBS = "//table[@class='items']//tbody//tr//td[4]//a/@title"
        CURRENT_CLUB_URLS = "//table[@class='items']//tbody//tr//td[4]//a/@href"

        # Physical attributes
        HEIGHTS = "//table[@class='items']//tbody//tr//td[5]//text()"
        FOOTS = "//table[@class='items']//tbody//tr//td[6]//text()"

        # National team specifics
        INTERNATIONAL_MATCHES = "//table[@class='items']//tbody//tr//td[7]//text()"
        GOALS = "//table[@class='items']//tbody//tr//td[8]//text()"
        JOINED_ON = ".//td[9]/text()"

        # Market values
        MARKET_VALUES = "//table[@class='items']//tbody//tr//td[10]//a//text()"

        # Status indicators (injuries, captain)
        STATUSES = "//table[@class='inline-table']//td[@class='hauptlink']//a//span[contains(@class, 'verletzt-table') or contains(@class, 'kapitaenicon-table')]/@title"

        # Nationality flags - may appear elsewhere in the page
        NATIONALITY = ".//img[@class='flaggenrahmen']/@title"

        # Jersey numbers
        JERSEY_NUMBERS = "//td[contains(@class, 'rueckennummer')]/div[@class='rn_nummer']/text()"

        # Position categories
        POSITION_CATEGORIES = "//td[contains(@class, 'rueckennummer')]/@title"

        # For relative XPath within each player row context
        class WithinRow:
            NAME = ".//table[@class='inline-table']//td[@class='hauptlink']//a//text()"
            POSITION = ".//table[@class='inline-table']//tr[2]//td//text()"
            DOB_AGE = ".//td[3]//text()"
            CLUB = ".//td[4]//a/@title"
            HEIGHT = ".//td[5]//text()"
            FOOT = ".//td[6]//text()"
            MATCHES = ".//td[7]//text()"
            GOALS = ".//td[8]//text()"
            DEBUT = ".//td[9]/text()"
            MARKET_VALUE = ".//td[10]//a//text()"
            STATUS = ".//span[contains(@class, 'verletzt-table') or contains(@class, 'kapitaenicon-table')]/@title"
            JERSEY_NUMBER = ".//td[1]/div[@class='rn_nummer']/text()"
            POSITION_CATEGORY = ".//td[1]/@title"

    class Players:
        PAST_FLAG = "//div[@id='yw1']//thead//text()"
        CLUB_NAME = "//header//h1//text()"
        CLUB_URL = "//li[@id='overview']//@href"
        PAGE_NATIONALITIES = "//td[img[@class='flaggenrahmen']]"
        PAGE_INFOS = "//td[@class='posrela']"
        NAMES = "//td[@class='posrela']//a//text()"
        URLS = "//td[@class='hauptlink']//@href"
        POSITIONS = "//td[@class='posrela']//tr[2]//text()"
        DOB_AGE = "//div[@id='yw1']//td[3]//text()"
        NATIONALITIES = ".//img//@title"
        JOINED = ".//span/node()/@title"
        SIGNED_FROM = ".//a//img//@title"
        MARKET_VALUES = "//td[@class='rechts hauptlink']//text()"
        STATUSES = ".//td[@class='hauptlink']//span//@title"
        JOINED_ON = ".//text()"

        class Present:
            PAGE_SIGNED_FROM = "//div[@id='yw1']//td[8]"
            PAGE_JOINED_ON = "//div[@id='yw1']//td[7]"
            HEIGHTS = "//div[@id='yw1']//td[5]//text()"
            FOOTS = "//div[@id='yw1']//td[6]//text()"
            CONTRACTS = "//div[@id='yw1']//td[9]//text()"

        class Past:
            PAGE_SIGNED_FROM = "//div[@id='yw1']//td[9]"
            PAGE_JOINED_ON = "//div[@id='yw1']//td[8]"
            CURRENT_CLUB = "//div[@id='yw1']//td[5]//img//@title"
            HEIGHTS = "//div[@id='yw1']//td[6]/text()"
            FOOTS = "//div[@id='yw1']//td[7]//text()"

    class Managers:
        # Main table selector
        TABLE = '//table[@class="items"]'

        # For individual managers
        ROWS = '//table[@class="items"]/tbody/tr'

        ID = r"/[\w-]+/profil/trainer/(?P<id>\d+)"

        # Specific data columns within each row
        NAME = './/td[@class="hauptlink"]/a/text()'
        PROFILE_URL = './/td[@class="hauptlink"]/a/@href'
        DATE_OF_BIRTH = './/table[@class="inline-table"]/tbody/tr[2]/td/text()'
        IMAGE_URL = './/table[@class="inline-table"]//img/@src'

        # Nationality data (might return multiple flags)
        NATIONALITY = './/td[@class="zentriert"][1]/img/@title'

        # Date information
        APPOINTED = './/td[@class="zentriert"][2]/text()'
        END_DATE = './/td[@class="zentriert"][3]/text()'
        TIME_IN_POST = './/td[@class="rechts"]/text()'

        # Performance data
        MATCHES = './/td[@class="zentriert"][4]/a/text()'
        MATCHES_URL = './/td[@class="zentriert"][4]/a/@href'
        PPG = './/td[@class="zentriert"][5]/text()'


class Competitions:
    class Profile:
        URL = "//a[@class='tm-tab']//@href"
        NAME = "//div[@class='data-header__headline-container']//h1//text()"
        KNOCKOUT_NAME = "//div[contains(@class, 'data-header__headline-wrapper')]//text()[normalize-space()]"

    class Search:
        BASE = "//div[@class='box'][h2[contains(text(), 'competitions')]]"
        URLS = BASE + "//td//a//@href"
        NAMES = BASE + "//td//a//@title"
        COUNTRIES = BASE + "//td[@class='zentriert'][1]//@title"
        CLUBS = BASE + "//td[@class='zentriert'][2]//text()"
        PLAYERS = BASE + "//td[@class='rechts']//text()"
        TOTAL_MARKET_VALUES = BASE + "//td[@class='zentriert'][3]//text()"
        MEAN_MARKET_VALUES = BASE + "//td[@class='zentriert'][4]//text()"
        CONTINENTS = BASE + "//td[@class='zentriert'][5]//text()"

    class Clubs:
        URLS = "//td[@class='hauptlink no-border-links']//a[1]//@href"
        NAMES = "//td[@class='hauptlink no-border-links']//a//text()"
        KNOCKOUT_URLS = "//table[@class='items']//tbody//tr//td[contains(@class, 'hauptlink')]//a/@href"
        KNOCKOUT_NAMES = "//table[@class='items']//tbody//tr//td[contains(@class, 'hauptlink')]//a/text()"


class Pagination:
    PAGE_NUMBER_LAST = "//li[contains(@class, 'list-item--icon-last-page')]//@href"
    PAGE_NUMBER_ACTIVE = "//li[contains(@class, 'list-item--active')]//@href"

class Managers:
    class ManagerProfile:
        """XPath expressions for manager profile data."""

        PROFILE_URL = "//meta[@property='og:url']/@content"

        # Basic manager information
        NAME_FIRST = "//h1[@class='data-header__headline-wrapper']/text()[1]"
        NAME_LAST = "//h1[@class='data-header__headline-wrapper']/strong/text()"
        FULL_NAME = "//h1[@class='data-header__headline-wrapper']"  # Will need text processing

        # Manager image URL
        IMAGE_URL = "//div[@class='modal-trigger']//img[@class='data-header__profile-image']/@src"


        # Basic information
        DOB_AND_AGE = "//li[@class='data-header__label'][contains(text(), 'Date of birth')]/span[@class='data-header__content']/text()"

        # Place of birth (need to extract city and country separately)
        PLACE_OF_BIRTH_CITY = "//li[@class='data-header__label'][contains(text(), 'Place of birth')]/span[@class='data-header__content']/text()"
        PLACE_OF_BIRTH_COUNTRY = "//li[contains(.,'Place of birth')]/img[@class='flaggenrahmen']/@alt"

        # Citizenship (can be multiple)
        CITIZENSHIP = "//li[@class='data-header__label'][contains(text(), 'Citizenship')]/span[@class='data-header__content']"

        # Coaching information (not in schema but useful)
        COACHING_LICENCE = "//li[@class='data-header__label'][contains(text(), 'Coaching Licence')]/span[@class='data-header__content']/text()"
        AVG_TERM_AS_COACH = "//li[@class='data-header__label'][contains(text(), 'Avg. term as coach')]/span[@class='data-header__content']/text()"
        PREFERRED_FORMATION = "//li[@class='data-header__label'][contains(text(), 'Preferred formation')]/span[@class='data-header__content']/text()"

        # Current club information
        CLUB_NAME = "//div[@class='data-header__club-info']/span[@class='data-header__club']/a/text()"
        CLUB_ID = "//div[@class='data-header__box--big']/a[img]/@href"  # Need regex to extract ID
        CLUB_ROLE = "//div[@class='data-header__club-info']/span[@class='data-header__label']/b/text()"

        # Contract dates
        CLUB_START_DATE = "//span[@class='data-header__label'][contains(text(), 'Appointed')]/span[@class='data-header__content']/text()"
        CLUB_END_DATE = "//span[@class='data-header__label'][contains(text(), 'Contract until')]/span[@class='data-header__content']/text()[normalize-space()]"

        # Player profile (for former players)
        IS_FORMER_PLAYER = "boolean(//a[contains(@class, 'data-header__box--link')])"
        PLAYER_ID = "//a[contains(@class, 'data-header__box--link')]/@href"  # Need regex to extract ID
        PLAYER_URL = "//a[contains(@class, 'data-header__box--link')]/@href"  # Complete URL
        LAST_CLUB_AS_PLAYER = "//span[@class='data-header__label'][contains(text(), 'Last club')]/span[@class='data-header__content']/text()"
        RETIRED_ON = "//span[@class='data-header__label'][contains(text(), 'Retired')]/span[@class='data-header__content']/text()[normalize-space()]"

    class Contracts:

        PROFILE_URL = "//meta[@property='og:url']/@content"

        # Table containing all manager contracts
        TABLE = ".//table[contains(@class, 'items')]"

        # Rows of the table (excluding extra rows with Assistant Manager info)
        ROWS = ".//tbody/tr[not(contains(@class, 'extrarow'))]"

        # Club link, which contains the club ID
        CLUB_LINK = ".//td[contains(@class, 'hauptlink')]/a/@href"

        # Club name
        CLUB_NAME = ".//td[contains(@class, 'hauptlink')]/a/text()"

        # Manager role (appears in second line after club name)
        ROLE = ".//td[contains(@class, 'hauptlink')]/br/following-sibling::text()"

        # Start date information
        START_DATE = ".//td[position()=3]/text()"

        # End date information
        END_DATE = ".//td[4]/text() | .//td[4]/i/text()"



