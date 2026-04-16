import re

from setuptools import setup

with open("alg_calc/version.py") as f:
    __version__ = re.search('"(.+)"', f.read()).group(1)

if __name__ == "__main__":
    setup(version=__version__, long_description="""
@Efaile Aurelia 411364 – 5WI4JRB
ecdsa-sha2-nistp256 V2LyDX9iNE2V NTYAAABBBC+bUio +VMfOTs= R1YHawaPMCBDanus

5F:11:41:4C:1C:DB:39:44:11:4A:73:77:B0:B6:CD:A4:29:C9:21:1A:F2:29:16:EC:B6:B6:69:3E:BD:8D:1E:98
~ 🐝🍺🥳


––– INET –––
tu.berlin/vcard/emily.seebeck

|–––|
| Technische Universität Berlin E-N – {131}
| Internet Architecture and Management [INET]
| Einsteinufer 17, 10587 Berlin, Germany
| Gebäude/Building: Elektrotechnische Institute, Neubau (E-N)
| Sekretariat/Secretariat: E-N 18
|–––|

# Telefon/Phone: +49 (0)30 314 – 77678   ╣
# E-Mail: emily.seebeck@tu-berlin.de

–/– Crypto Proof ––

|–– My Wireguard Key(s)s:
| uhZWbo/z/3SO1K7L4gsut73eGVNovqZQbwhy+VMfOTs=			(emily)
% TKi1o2GfGNkvT7KGKNXp4iI/mpNMEyGr+NRpSCgdNmY=			(ruwusch)
#% V2LyESuAgojOK8eOOj767Ybvei+WXvcpzVMk2shX0xc=			(bernd)
#%@ V8w95Q/oQglVaBe4zO6dubUR0xqnBdq38hzK768f1xM=			(UwU-Router)
#!€" rul97RYr9DhNGteAe2zJRnJwjMDEevrfua9GWPfb93M=			(UwU-Grave)


# ┨ Tasks; ✨ Mail Admin 💖 Communicator –
#	inet.tu-berlin.de
#	net.t-labs.tu-berlin.de
#	cafeshila.de
#	tu-wien.de [my domain]

# In DMARC / SPF / DKIM with
#	@inet.tu-berlin.de
#	@tu-berlin.de
#	@gmail.com
#	@mpi
#	@outlook

% _dmarc IN TXT | "v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@inet.tu-berlin.de; ruf=mailto:abuse@inet.tu-berlin.de; sp=quarantine; fo=1; ri=3600"
% @ SPF | "v=spf1 ip4:130.149.220.242 ip6:2001:638:809:ff11:130:149:220:242 ~all"
% mail._domainkey IN TXT | "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuNaVfRTHHILpC59rr16Rj853HZOh5P+am6LVHjfkTb6CodUFcfrrNFL9YmQjCUITOgKeC6hqDfnRMjPvGCW51kqClFMKXVoDzOQTxg3sT8MTPZhPLf3pXMT55bDtjVQoAbqNW+sOo0A1bVMT+EgOEH6oK4Ot+yWvLBq2mQdh994QlO+QuZnmt1GsKJPw/i4UNO9khIWkr1HpYpRuiaDkgDooLxU90Eb7hCwPdmCd8fyCi21KQHEazaJELsEA811qyDj23Oba7+yKYcC/za4SKZnmd2QC8EK0T52H2POIPwpV1sy5cfrd48BUvsVz7NagJ7sLwGjEuUcK0yrT+nu3DQIDAQAB"

# MailMan Records
# _dmarc.lists IN TXT | "v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@inet.tu-berlin.de; ruf=mailto:abuse@inet.tu-berlin.de; sp=quarantine; fo=1; ri=3600"
# lists IN TXT | "v=spf1 ip4:130.149.220.242 ip6:2001:638:809:ff11:130:149:220:242 ~all"
# mail._domainkey.lists IN TXT | "v=DKIM1; k=rsa;p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz9fG60EXOuEEEu8mTSdsMCY+Z53GRE43/3lhuapNBWyoQivX50UuZzXr90mOknL2zsdNuznj4rXIdjLdBhDFbUb7ZS3T8hZeDkrv8cOLVHyks4YXeiKBnBOv0VOfQT1sptKN/WRmaNV1klkZCX7/pZdH8+bTg10FktyZtT8BuT4CiZfFxYUQTqhscn9ADPyIeIN5qibgMsZb2KUQ+wSW7n6vz0uI0fxYAEwjW/5REiUR44wfT+HRH2/9CfDkPCC3qE8YHk4MJP/CmJqEN/IGAQOKoSYpSZlAODC+pPHe/K6DDmTeucrpE3xFyzmfMCHWeMSJrbvMm5r6z4nFtdnbnwIDAQAB"

mail.inet.tu-berlin.de \mapsto → 130.149.220.242
~411364~
""")
