import pathlib
from pathlib import Path
from datetime import datetime
import lavalink
import json
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
cwd = Path(__file__).parents[0]
print(cwd)
def read_json(filename):
    """Read a json file in /bot_config/"""
    jsonFile = open(str(cwd)+'/' +filename+'.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()
    return data

def write_json(data, filename):
    """Write to a json file in the /bot_config/ directory"""
    jsonFile = open(str(cwd)+'/' +filename+'.json', 'w+')
    jsonFile.write(json.dumps(data))
    jsonFile.close()
alts = "lilmustaf_1996@hotmail.com:mustaf123 cbclark007@gmail.com:cbc88898 jimmyspelarwow@hotmail.com:Cortcgp40 dfayn35@gmail.com:blackhawk01 adrien@delouye.com:nes35blarch justin.gossage@gmail.com:pokemon12 murashell@gmail.com:3lm3rsglu3 vaskinmyglory@gmail.com:lovebug270 tigers.321@hotmail.com:gotigers24 roversword@gmail.com:Toomai01 morganbedford68@me.com:Np165luu marj.armstrong@sky.com:joejoe0311 bo3abed2000@hotmail.com:eyad5332 el_samael1@livedoor.com:tabata01 peteng24@gmail.com:Cctv1234 ps@atexweb.pl:piotrek1 therealgeorgebuck@hotmail.com:100795buck mirosiil2@gmail.com:12wqasxz Kat@castlestone.org:m00nbeam shima_to_ra@yahoo.co.jp:shima3254 andrew.8433@gmail.com:falcons2016 richardfilby25@gmail.com:2cslorhe paalajohansen@gmail.com:U66d2n6a kunzmarcel99@gmail.com:asdfqq99 tim.tallis@hotmail.com:Tallis920827 kaijade143@gmail.com:rskj4life scottforeman@sky.com:alfie2009 matt@optimiseu.com:mm290478 lagri71@hotmail.com:Hermanflink08 johnathanmanuel@gmail.com:johnboy1 4ron.stanley@gmail.com:august27 Erik071995@gmx.de:Lebenslang1 jkaplanhall@gmail.com:harrypotter55 Eidsgaard92@hotmail.com:Flaggstang201 donnahibbert8@gmail.com:Hibbert79 jord_jmf@hotmail.com:Fieldhouse5 Abeck0486@gmail.com:Trancey1 bokaj02@gmail.com:matilda10 markjet7@gmail.com:Jetseven7 supermatt512@gmail.com:dinodog1 Matze1711@t-online.de:david229 stanmond@gmail.com:dandan123 karoline@poulsgaard.dk:Ravperlen123 daleboy93@hotmail.com:Laika1993 mandistahl1@gmail.com:freesoul1 93asd500@naver.com:cofls664 edhens16@gmail.com:rasengan1 petercroston306@hotmail.com:elvispre1 deniswillian27@hotmail.com:67351810h cathy.urinyi@gmail.com:Bubbles2002 hbmayhem204@aol.com:robert204 noel.mcdonnell07@btinternet.com:Oranoran01 Tibbi64@gmail.com:Turtle84 spygordon@gmail.com:tiger1512 kleintiroler84@web.de:Nicole1984 tom.roach1234@gmail.com:reach4321 Johnmosterhout@yahoo.com:Helaina1 wyvern_84@hotmail.com:Turnip84 rye_md@yahoo.com:0d0gaigf sawtellhayden@ymail.com:hs100005hs5 seth762@gmail.com:Shturmovik762! amandacoble77@gmail.com:paxton08 archie.keylock@yahoo.co.uk:Rabbid122 andarelli.jdo@gmail.com:ajaccio20 dancelikebubs@sbcglobal.net:tigger4 davidjmellor@ntlworld.com:riverside38 gatschnegg@hotmail.com:kn3tmaus severin.hintermann@gmail.com:VanSchnitzel2402 sturla.hallas@gmail.com:Sturla69 christian.sladky@web.de:Komisch132 robertgudauskas@gmail.com:c2r8ppkr nickdan@xtra.co.nz:connor01 carres@sky.com:cadenza1 tonywilliams101@gmail.com:!Oliver101 jackp2309@gmail.com:awesome99 pickle_headz@hotmail.com:Rebecca89 mig.tijero@gmail.com:sk84ever wparkiris@gmail.com:woorim10 mrjhooper@gmail.com:Hooper32 janzim@ewe.net:Fifastreet2 hazzas@live.co.uk:Kiara123 badger1@btinternet.com:Tornado01 jeackid@hotmail.com:fu8fxcs8 jannik1603@gmx.de:jannikjesko03 glayn98@gmail.com:Sabreman1 dackeskogen@hotmail.com:De221200 patrickbond83@yahoo.com:Spellmas006 prosebsterhd@gmail.com:szwedzik20 Philipp.grummer@gmx.at:fliger1996 moescheid@gmail.com:team47!! cyril.lauret@gmail.com:cla280173 horvath.k@mac.com:BaBa13526 spedersen90@gmail.com:liverpool123 ruediger-gonzales@gmx.de:f0708amw travsfox@gmail.com:jason1579 kierkjr@hotmail.com:Sephiroth1 monkeysnitch796@gmail.com:navekiller10 Bluebert86@hotmail.com:Apelsin86 kestrel731@gmail.com:jake55 danielmowle101@hotmail.com:Liverpool8 larsson2899@hotmail.com:lars2899 hiroya.soccer030664@gmail.com:hiroya0306 teddytribert@gmail.com:Nkqdpars79 dominic@hmi.uk.com:Dominic74 kkamauf@gmail.com:Arabic77 Haraldseth.mike@gmail.com:Karowold91 mattiabierer@gmail.com:25wa0xSS tk408@online.de:tionar31rch lopez152@hotmail.com:bulldog411 pjonster@gmail.com:chargers123 tcunningham0220@yahoo.com:cunn0220 sigridrokne@gmail.com:Godis200 jb16rabbit@gmail.com:scionescio geovanyludizaca523@gmail.com:geovany1234 lukewcarter@hotmail.com:boxerdoggy1 christophesalido@hotmail.fr:poimlk987 dylanminyard97@gmail.com:Troylm123 richandmaggie.york@virgin.net:smidge99 PigGirlGamer@hotmail.com:nilmar21 markusreister@hotmail.de:markus23 fer_cnp_87@hotmail.com:7318701fer tomihuj@gmail.com:nexus666 Chris-bryson1295@hotmail.com:Freedom1295 jyoung66@hotmail.co.uk:161292wsc ratreene@hotmail.ca:Horse2001 jonny92101@gmail.com:jonny921 Frt.section3@web.de:starter123 wentworthj13@gmail.com:kyuubi100 stoz22@hotmail.com:Rankin14 zboyd82@gmail.com:Bigboy123 hitmefuger@hotmail.com:Imcool123 e.cooper@talktalk.net:everton9 crazydude784@gmail.com:pay108tent743 hollykrog@gmail.com:krogs1664 hello.lm.bs@gmail.com:777family xxpyromancerxx@gmail.com:Mcgregor!4 ryfle0969@yahoo.co.uk:Aeris1987 ross410@btinternet.com:25174432li5 rmhess99@gmail.com:ronnie99 matheo.holgersson@hotmail.com:matheo01 sepharoth666@live.com:122519aA s_bendis@yahoo.com:tyler111 carlos-carchi12@hotmail.com:Marchiso12345 penegor@yahoo.com:stephen22 Swagminer99@gmail.com:harlie123 lets135@gmail.com:samir310 naurius88@gmail.com:diskas123 Nojsen10@gmail.com:erq23vmf yohan424@naver.com:Sbe07063 joshdavis91@gmail.com:scorpia1991"
print(len("lilmustaf_1996@hotmail.com:mustaf123"))
altChar = []
seperatedAlts = []
for char in alts:
    altChar.append(char)
len = len(altChar)
x = 0
y = 36
for i in range(int(len)):
    if altChar[i] == ' ':
        x = y
        y = i
        text = "".join(altChar[x+1:y])
        seperatedAlts.append(text)
#print(seperatedAlts)
itemCount = 0
for item in seperatedAlts:
    itemCount += 1
data = read_json('altSorter')
for i in range(itemCount):
        data[i] = {}
        data[i]['alt'] = seperatedAlts[i]
        data[i]['used'] = False

write_json(data, 'altSorter')
print("Done")
