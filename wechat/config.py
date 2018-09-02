WEIXIN_TOKEN = 'hu1234'
WEIXIN_APPID = 'wxa02ecc82e50aff15'
WEIXIN_APPSECRET = '701325a877263198fafbb3cedd8e338f'

HOME_URL = 'http://www.hfwb.xyz/home/'
REDIR_URL = 'http://www.hfwb.xyz/userinfo/'
CREATE_MENU_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=' + REDIR_URL + '&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect'

WEIXIN_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + WEIXIN_APPID + '&secret=' + WEIXIN_APPSECRET
WEIXIN_ACCESS_TOKEN = ''
WEIXIN_ACCESS_TOKEN_LASTTIME = 0
WEIXIN_ACCESS_TOKEN_EXPIRES_IN = 0


WEIXIN_LASTTIME =0
WEIXIN_EXPIRES_IN = 0


WEIXIN_JSAPI_TICKET = ''
