class Xpath:
    '''
    NAME
        Xpath
    ==========================
    this class for make xpath .
    use xpath to find elements to target site .
    ==========================
    input: this version no input .
    ==========================
    output: return the site elements to xpath .
    ==========================
    '''
    #cookies
    def cooki(cooki = '//button[@class="_a9-- _a9_0"]'):
        return cooki
    #username input xpath
    def username( username_xpath = '//input[@name="username"]'):
        return username_xpath
    
    #password input xpath
    def password( password_xpath = '//input[@name="password"]'):
        return password_xpath
    
    #login bottun xpath
    def login_button( login_button = '//button[@type="submit"]'):
        return login_button
    
    #SaveInfo
    def saveinfo_button( info_button = '//button[@type="button"]'):
        return info_button
    
    #notifications
    def notif( notif_xpath = '//button[@class="_a9-- _a9_1"]'):
        return notif_xpath
    
    #like posts
    def posts( post_xpath = "//*[local-name()='svg' and @aria-label='Like']"):
        return post_xpath
    
    #Home button
    def home( home_xpath = "//*[local-name()='svg' and @aria-label='Home']"):
        return home_xpath
    
    #chek page-notif 
    def notif_page( notif_page_xpath = "//*[local-name()='svg' and @aria-label='Notifications']"):
        return notif_page_xpath
    
    #Reels
    def reels( reels_xpath = "//*[local-name()='svg' and @aria-label='Reels']"):
        return reels_xpath
    
    #add comments
    def comments( comment_xpath = "//*[local-name()='textarea' and @aria-label='Add a comment…']"):
        return comment_xpath
    
    #send comments
    def send_comment(send_xpath = '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37"]'):
        return send_xpath
    
    # Emoji
    def emoji(emoji_xpath = "//*[local-name()='svg' and @aria-label='Emoji']"):
        return emoji_xpath
    
    