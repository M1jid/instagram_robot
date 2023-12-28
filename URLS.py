class Url:
    '''
    This class for make and use site url .
    
    Input: SiteName  .
     
    Output: Site Url .
    
    '''
    #for instagram url
    def instagram():
        return 'https://www.instagram.com/'
    
    #next version
    def site_url(site_name):
        import requests
        requests.get(f'https://www.google.com/search?q={site_name}&sca_esv=574459239&source=hp&ei=LusvZdaxFLqKxc8PpfOogAY&iflsig=AO6bgOgAAAAAZS_5PiYotxCFxaLRBd_YBipIUjhDr4aA&ved=0ahUKEwjWgM_y5v-BAxU6RfEDHaU5CmAQ4dUDCAk&uact=5&oq=facebook&gs_lp=Egdnd3Mtd2l6IghmYWNlYm9vazINEC4YigUYxwEY0QMYQzIHEAAYigUYQzIHEAAYigUYQzIHEAAYigUYQzIHEAAYigUYQzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESJZ7ULAPWPN4cAZ4AJABAJgB6AOgAfUdqgEIMi0xMC4xLjK4AQPIAQD4AQGoAgDCAgsQLhiABBjHARjRA8ICCBAuGIAEGNQCwgIFEC4YgATCAggQABiKBRiRAsICBxAAGIAEGArCAg0QLhiABBjHARjRAxgKwgIHEC4YgAQYCg&sclient=gws-wiz')
        