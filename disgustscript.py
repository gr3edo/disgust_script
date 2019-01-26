import urllib2

CODE_TPL = "8WBR-ATJH-R?CX-TYWZ"


def redeem(code):
    opener = urllib2.build_opener()

    opener.addheaders.append(('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'))
    opener.addheaders.append(('Cookie', 'nx_mpcid=604e03e3-5cb1-4850-bd9c-2d6eef25246d; s_txn=U1Q6ZzQ0bE9MZ3NzNm1ZUDN3UmZJQkw6MzA; utag_main=v_id:0168864f75550019be5636a90b4d02085014107d00bd0$_sn:1$_ss:0$_st:1548445149336$ses_id:1548441580888%3Bexp-session$_pn:3%3Bexp-session'))
    opener.addheaders.append(('Host', 'checkout.ea.com'))
    opener.addheaders.append(('Origin', 'https://checkout.ea.com'))
    opener.addheaders.append(('Referer', 'https://checkout.ea.com/checkout/origin/code?execution=e2077243257s1'))
    opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'))
    opener.addheaders.append(('X-Requested-With', 'XMLHttpRequest'))
    opener.addheaders.append(('X-SESSION-TOKEN', 'VTFRNlp6UTBiRTlNWjNOek5tMVpVRE4zVW1aSlFrdzZNekE'))

    url = 'https://checkout.ea.com/rest/codeType'
    data = "code="+code.replace('-', '')
    print "Exec request to", url, "with data", data
    content = "None content"
    try:
        response = opener.open(url, data)
        content = response.read()
        print "OK" * 1000
    except urllib2.URLError, e:
        content = "Error: " + str(e.code) + "\n" + e.read()
    except Exception as ex:
        content = 'error'
    return content


codes = map(lambda char: CODE_TPL.replace('?', char), list('QWERTYUIOPASDFGHJKLZXCVBNM1234567890'))
for code in codes:
    print "Start redeem code:", code
    res = redeem(code)
    print res
    print "\n\n"
