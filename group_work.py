from textwrap import wrap

def ss(string):
    return [string[i:i+4] for i in range(0, len(string), 4)]

def com(x,y):
    r=''
    for i in range(len(x)):
        if x[i] == y[i]:
            r+=x[i]
        else:
            r+='#'
    return r

def rm_noise(s):
    places=[0,2,5,6,8,9,11,15]
    a=wrap(s,16)
    r=''
    for w in a:
        for p in places:
            r+=w[p]
    return r

def shuffle(s, table):
    a=wrap(s,8)
    r=''
    for w in a:
        for i in table:
            r+=w[i-1]
    return r

def decode(s, table):
    a=wrap(s,2)
    r=''
    for w in a:
        if w in table:
            r+=table[w]
        else:
            r+='?'
    return r

def calc_dict(sample, encoding, table):
    t=rm_noise(encoding)
    tnew=wrap(shuffle(t, table), 2)
    s=wrap(sample,1)
    d={}
    for i in range(len(s)):
        d[tnew[i]]=s[i]
    return d
    

a='AJAOFBKCOCHMLKAOFDGELMDIIHHEJPKKKKICNAFHHMEAFPBHNPABKFMGACHGNKCAHJFHNKCEEHFIBAIMMKEEBEAOJJFOGFFADPDIBKAPIAHILAKKDFEIIMACEABEAKCMKHIKGOACAJGNBFCAKECIBNDOAPBADEBNAMAPINKJFINAOCGHAFJLAIADMABECBHFNCAGKDEPHOHHFHACAOAJBNACIAOAADHOMGCNNOKHPIGOLCEDODIGCHECEJMFLMGIHOFECANMAOIAHDMAFOGCIKCPIHOIBMPKCLKHJFHCAHHMGIMAMMEKHCMPNCMHPBDOKLIMJFDJBPHGIGNEACAGEKMHNEDIOMBOMNCFBIHFGFIEPJMFHOFEDKFFAGEIJCBNACAGCFNCGAFNOBGFNHOKMAHJIFCJAPNKDAHEMFHCAFFMDIPAIFEMMKNDCOGILDGMDKHABNADJACACFBEDDPNAOACBAKNNNEECDHDKKNIDACIPJPDOGIOJANGAADJFHPFOOILLPAFIAHCKHJOMNELAFAFKJAGADHCKCCIBOMMECBIDLKMKCINENKPDIAOMHEDFGAJGADKAHBAGADNNOOFMFAIAJFMPPDNELBIEOHJAFBIIMBACEKPIAODINFAOBBKABAGLMNOJAJEPEDAFBGNGMHAOHKCHFAOMEEEFDOBJICPBGIAAFACOEFOFMABHMBHMNEEIOEEPBONKFBDKDIMODFDCNFPAFBMFAAEPANFJADAOOAAOAILFKMNGEKCEFJFFPNOODKAJIJPAFBAKJKCPADBIPAACLPKEAOIOFAKEAMNIBBMOAIMAMAKPAKCHBHDADAAFOCDCHNILDNMOJNCKMFECGLEGIFMEPJHAHKPACCFGDMADIHPPMHGAHGEHPEAOLIABCMDACFHEJLAMFEBODKPNIPPKCFONEAEIHOBJIFFKJBAANAIJOAGFACIILFHFGMBCHOHNIPFCKFBNNAOFOMEGEMNBOCFFONEMDFNJMFPMIGAAHADPINMHAPEOBBCKDIAKINLJGHEHNLAOBEHPAANIAJAOEBKMACGIHCLEKNFPGDMFDGPLAAJAJCAGGBNKEIIFNFIFMOOCKNHACAPECNPCAAKBBAKFNGCFMCBBKOCEPDEHGFFGAMIACNAALEAMOCBOKNCGANILJIFABANAHMGGEBFFEBFAMJFGCKJICCKPDHOMCCBHMKFOIPEMJNNKPIADDFMAADDJICADEHDLNNCMOCAEFDFAGJHFNEBIBHADAAOHDFGBAKJKIBAJHNCOHILMOOMPIJNJBADOONPNAMNFEAAJDAHFPGKFLOHHIODGFJCDGHPCAMNACHAAFENMEEJGFMJHCEGOAMCOEILNNABEABOHPAMOLIONFNDHABGLHOHBBEMNABFPGPAHCKGACADKENIHAJJDEIDFKGPDMCOEHICOIGMNGOENMEDABBCLMANFJGLLAHBIHFALKAOAEAFLNNPEHFAEOMBECJHCBOHANHGCCNAMMEDJHDFAHDFIKEAEPOGKNAAIJBAKLGOADAFCFACCAFMLPAMNFAKDFNEHACABMLHAKJHBMDOMHGCLHPFAOAFJONNCADIMEOKFMGFAMDEBHACKOEEAFAFDOAAIAJIKOPOHGFAOOLCEDBNJCDMCLHLAFAGIADGOBKONCABBDOBOIHHOFOEFOMCNAMPACEJOODADNDCIACEIHMAINFKKOCDJJDCIHPPGDDOOMIBHAMEACIALFFANKAILDKLAICHBENFAAJMIKDAMHLCKCEFAKAAJONCHAPIEMADMOEPEFOEHIMGOIPCDBPLJNDMAHEAKDKNNNGOHOPAAFMIHHNACOKODMOPJIMEJHPAMNEOCKNFCOLCNBJMMDECKKFLAABIJCFADCHDINNKMOGAKNCFAJJNJNMAIEFAICFONOOHCADIIPMAHDAKACJIGKFFJMFIGANADBDFGANOPADAMIPDAOJBLHCCMKAFIKHFMDCCLADAIPPAINLONIOIJABCANFAIGNNKBIPJOKEDIENPHDDNBOMMACMIHKABMHKOHOMMHNPCABHNPFMKBIIEAOBCOPACCKMMEEEKDFMCGNEIEBMDEPJOHDJBPNFGKFEAIAPANMKHEBAEDPCKJIGGDFPJGHHBOCAKCIAFAIKDHNJDDPLNNABDHOPOOHFEAFNPNCEGNKFIIGAHCGOALJEPAEDABDJEKPNDCDKLAODHOFAHFLCHOHIGHAMAAHHDPGNANABMHKKCINFAAMMFKGCIMHKAFBCFPPNADALDMKPOIHEJADNHFHFGCMDOCKHOIPOKDILNAAEEAFJDIMIKBIDGHHBNFEHLHCOBJNGHOKCJIJIFPEAAAAKAINAGAAEJBDFNHOGFACMIHEJIOEKDMHBOMAPIJJELKFKAPJDOFIEIEJGDPJKKDKBMAFLAAIABIINEPJBNFCEAHPMDJMADAHEPMACIJPEFACKAOJICFIEIEBGKBMKCLHHKAFKIGBAJDPKAPABOFCBAHCMGDANMPEKFDMPECOHILLIKGIGMNKCDINOEGHDFJGGBAAHAJNALHBNKMIKMNMPHENOHJBCKKIEMDFOJGEHDMAAKBIPLAKBDIKJBOBDKOKHMAFMAGNADCPNDPPHKNKANILABFIFNNABFAAAJAPJMKHEHOFOHINOAOPHEIFNCCHLPKFMIGEIKBFKAMAKKFABIAKMMHDOMEEINDOCGOOPIFLFNIOHEKAMIAGCDADONPOBNMNDPAKCIFFDNHAMPOKMAKJNOCBAKAILHCMPJEFHNKAANPAAEFNDJOGGCCJAHEFBEKDAIDBIJICKAFAGFKDHIHCIBMBODDEFBOMDECNODBKMHGFOFFNNAGEGDIINOHEEEAIPAHCAANCAONIICFAFKAKGEJCCCPHEBDHBOHMDNGAONFAOAHAEKALHLANCFNMHPKOCPIBKONFDMKCKCAFNIAHAMPBKNKAHPOFKJMPNFKJAOHNGKANFFANANKCHKHILJAONGNPALAHFDJPLMMAMEJJEJPJMEKBGAOFHAGKIBBHACOKMAMOPJIKENFPAMPECCKNGCOKCHMDMIIEPOKCKAHMIEDHAFNAIONMOFEAAIENHNAOEGOEPIJKNEBPOHCFMNAFMAAAAFMNAOONIHNKEACAAPEENABAMHOKEOINOECFNKPIBFFFDHMOGHMACAIABFCCNFKPKBMMHOONMFKDAIPOILPPOAHANLKKCHIFIEINHOFNDHOCKEHFNCPEMNLAPABOCJILNCHPAAKAAIMHOCFBEHMJMFJANIEAFIAFBEJKOMAECIDOPNNCHDPBBAEACCOMGHEBOHIMCKLIIDDFFJGHHOABAFBMBCAOCHIFJGHHDHAHJOAONINCALMBKNGAHJCOAANPHBFBFDJPLNMADEJEEOJCMEMBFGOOGHINIKKHDNMOICACPIHFANKCKOJOOHHNHCAMHKJBMAMABCEMIOCDJPMIONMAELFKIJIPGMPIADDPKKHAEEJDFLFFMMBECCODBAHDIHIBAMLCCEMADGAMEGEMFFOMANHKJKIGFOPDCNFADBOOKAIINHDBAAMAIGFFCCGNAGKNMKEILBCAABAEHPJKENAAJADOJOILHNBIEENJAPAKEAIJJGFDACFHFNHOAENEHNNEMDCPANMACEJFEFPBMMDEPKOMEACBIJBAAMNEJNFMEHEBGICPHOKICJACHAHAJOJFADJHBBMAEIJEEPMFKNGALKFOHAIBGFMFANMOJJADIIPIAFECKKHCFCOMBECHIALPMHOFGJFANAAMGKJGNMOELNAKFIKAJDJFKKFICPCOONIPKFEHOFDMJBDAMKANHOMACNHAGBFNDHANAGIAHAFJEAMCPMKNCHBPFOENCIAFPEGNAAKPMDIPLCNIBEEBAFPFMODIGMADJAHKALMEACKKANMAHAJCECKFNFDANMOKBHIFIMNPDNKGOCHONAEHFDIBAFDICJMOBANMCINIADEPGAMDAAPFEOBBNMOCCJKAONAFIDDFFDIPAAOAMBACNDDFEKDIIDFKPDIAGEBLDAIAODEFECGIJFANKKMKMNKABMAKICDNFKHKKAKMCECLIFNJMMAEBEHOJCIIHLCCKFENFEFFDACGGGHPAONIDKBAFHACPFKCCNAAGKHMPOEKFBMAEONOFADOFANKHGKPADGHCNKEHOJNIFELONPAAOAFGAAIAKBCAMEEKJOFACNBNCFLMHNGDPAJPGAAAIGMAAIAMGCOLJOHDCKKAHFHOPAKKICDAGKBKOHILCFHDAHCGPGCAKGIGPCFDCGEHPEIMABANLKNBGAAIDLOFAFANMNOEKOGOJPNKMCEBLOACGAANFDGFKNIDHNFAJGMOABHAKMINGCFKPNGHONCDNNAOFAAABANJAAPECIHKBCFOAAICMNBNMDHFHNMPACAAMPCAKEIMPHHPEFJFHHFMMDENJCMHHEAHJIPDAOJDHAMFIEMJNNJKHOFANAMOICPAIKAKFBGGAMAGAJCCHADNHDFPCKMMPEHIAAEDOBIEEAAEEAPJDCIMNEAHBDMJGEHHFCCFOJIPPCDMAPEHNAHNAKJEKFICIEJNNPCKKDCELAMCACCADEGNOMIGOFAJAJCGOOFAHFHKEMMPICKEOCFKMNEPKCMKNCBHFNHOHBFOPFAAEJEGLFBMKEIAAAAAAJAJFEJAABAGFNMFHEOAHPEDFFGPHMAHEACCGDEMFEMBMHKFKIJFCFNCNMAOPOMBAEDNNKPAAMAHGMFPIAEEIKIOMKCOMACNGHJANPCFEOBGOKAFGACIBIHNOENONONBJAKKNNPAKLIMFNOGANOOMFKAEFBPNDHPAHEPFKPAKIIGCCFBIACHEPDOKPICMHMBNCPFJMIOHJFNFFABAAAGEJPNMLECLCKJHIMHDCBDFPGKLAEMAJPJFNHNFIGJCAMCHEIAAKMCKCIILKNIFADKKKOHEMOEHHDPEDMFKJFMAKANFKCHHHNILFFHOGNFKKDKIPFIMFCKOFIIFBMHGEANBBNFFJNGEDKEJIIPHFCAKMIKIDHFAFBDKBHAMEEMNCMFHEBHJBPDOCIAOAAHJAPJAPJEAFAKMHKNOINFBGDNHGHLLCMDOCJHONJOCPKCCNKMACDAHPHACAHHAMFNEADEAPDMNHOEKABPANBAHIKNFDMNCOALEAMNLKPMHHPABHCNEDNGLALGJCAPAJNHAOPACMGAAGAKHDNFJACHOIHAMEEMPDNJCAAHFKGKOIIKFDFMCNDPECOMMKCKIAKHKIOAKLBKAIJCGCMOMEKHCHPFHHHIDAANOJDABHGOFBGJGNAHMAGOIMIFHJFNONCEAHJAFEFNIDEAHOFJJMMIOJLAAMAPDCNEHAHKHCMDOGIAMENIJGBOAANABIPGBADBAPHAONDNEIBMANABAJDAEAKAMICAKNDNEPOAMGPMAEJOKMKGJILEFPCAFFGAPMADNAPCNGCFADAKGODLCPNIOAOMKJKOLNMBIEFAKCEKIEHNGAKDOICAOMGNKBIMCAOEHIMJKOBDMIEABKNOCOICDIDMMAEJAKCKAHBIBNHAFPALGNOMFICAHMHHOLIFMFADEABGAJPMEHBEMCNMNAPHDPBOCBHFBAICAECAGIANAHJHKKHMIFHIPDPKAHJOFAAIAADAHHCNNGADEACIHHCJDMCHHIFIHNMOPEIADLLDOBIMJAAMIADJBNJONOAKDAFPCGCJDJOMHKHHOOFJAGNOAKDNDIPOEMAMNJIEEPFFCAKGJFOKANMMBONAIDEHFMFBCGAEMGJMOOIPGHEJEJDFKLBIADJMHAHJAHHACFJNOGIBPCMFHEHHGHNDEEJHBCFFABMHNFMAILEJOLDKADMDDDCANDAOMHOMHNIFFDMCINEMPMNOCODEPPEMIKEBIKFDAGMIOFEAAHJGNNKAOIGAEFGNKLINDHAJEAHFFEOICHHCBNODHIOAKJLDELJEMOHJAFBIFAPAFKACFFNNFAAMKBCHOCIAJDADAJEPONKAKNICLMCOKKKEBNKKONNEOKDKIHMIADGOMPCMDKFPGNBICFFFMACHGAFFIABACIPKNJADGOOAJIFNMGHAAKAEOENOAAABILAFNEADLHKFCIHHACHMANAHMHNNHAFFNCNDMEEAIFOMHIOGGCKCDPPLENAJNJIAEKMFCAKAHFMDACHMLFLAMBEHGCMFNCBHNGHOHCFBMFADAJPGOJBAAFAJKNMMFEHACFFHFLNLBMHDAHOCGBFACIHIAMKBIIBEOOEOANAJKOKPKICNPDCKHFFNIMCDMKOEECAFOGNEOAIEEECAHAKMFGGHEMOKFIACANNHAEAGJICFAHPEBAANOPILPDNEIGJHDPDOOMEKCAHHMHIACPCFDBPDIKMHJEBIKKLAOHINFAADEAKJMEBMFEGBBIIGIEMHMPAKFNAMBAOKANOANPPNKFCCMNAAIAGAMHHOFFMNKKKEPIOKMPODMNCFJAEBFBDAKBEHNDANDFKMJIJAMNOAMGCFBAMHACNAKOAACEHMMMMJNEPEOEGFALJEPFDAMHEAOAFFANAMKOCAGHBILDBFOGNAIOKFJIOOPMAAFNGIHMDGBHHCGCKENCGIFOBPAMMIOAEAHJFBFACEMKAAACNFOMNKFKDJIHPIPGDKMDCEMAMJIENADPBKOLILJOMFJEINGNKAOKIMKAAOEADJBFCIAAAMFHFDFMMFEGGHOAILABNBNACNPEAOMEEBMFFPPNNGDCADFFMLEAANEAJJLGAINOAAGCKOEIFHPJPIACAMIAMFOCCJPDIOKPIBPDAMNJEPONIBDPPEGOMAACHIHJPNAHAGBFCMIHFNOEGKNLAKLDOAJIJDJHJANIAJHFOECICAHMHPAMADEEKIHIABLFAHHBFMHOFGIADNBEBKEGJLCNFKAGIAMEMANGOKHNNHAOJAMJJANFOBKNOKAOFALHIANAAPKOMLPEDNJHJDONICAAABEAJJKHFMFCGMOIDDIDJHKLPKAMADLKNBHAJIPEMCKLILHINKJADEKLMAKMIHIAACGANABICFFPGBGMAMAJNCJACNOKINLPANIAKCOPBOABJCOMKOAKICBEFNMCEEEBODJICNEIJAEEJIDECOAHPBCFGAMCCPCNKIHIPAJMHHKDIKNDMBNEEPNAFBAIJDEAIMIEGJKHEKHBFEKADHAHLANABAAMJMLKKEDIHIOBHDFMNGIDNFCOBPIMDMDCHEDKDFADBIBEFAACALLNKDLIDGILHJKHKKEIDCAPGENGDNNJAIGMEMJJACAJNAMHCJHAMCICBAEGAKNHAEGFDDFPIGEKIHDLPFDEAMIAMBFMCKKKIKNKMCPEGKKLKDANAKDMJCGALEFNHAAEAGHJDCOHMAPGHNAEAINEABAAEJHFKNCJHBDFAFAJEGDBBNHGHKHMCAIHICLAKKAKJEAFCJMKAGNPCFMOCAAAMMHEKAFHBCMCCLBOHIGFANIGHFKMKFLADFMPKACFOFAEANCKMJJEKIDDCAKDIIFOFCCGCNEKCMFPGNCNKGICBABOOKKDIBNAABGAOJCMGNKIIEOAFEHGBLNNFIDLHCGKADOAIIOAPODFPINOADBAKNBHBEKEILMHHDNFNHMPGOFMAGAKAGAADINKANMHEHHAKCIKMJMFIKKCIDJCOPNIAKBGAOFNMHLDABKACHJEJCNLADPFNGHAPAGGEHKEIAJMAIFADCBAPHMKCHEKKJJIGIHIPAAAJGGHCAMKFFBGIFHPFEMAOPINHAPABOHBFOOKOFANAIGGBAHEFJLKDPIPAIFPFKMMCFAFHPGFLNBIAFEHBEJOOAAIEICCAAHIHGFMDLIPACHCKKFNAKIFHAIFMNKFBKDHPEONMAICIAADAOAEAHEFMGFEONFMFHFKNOOMFBAGBCIONANKAMMCMCJCGHMIJAKOIAEHFEHGAHNNLCNIOOBACOIHOAJPPKOHOANHKMCINHKLNMEFJJBHNOAABFNBPADIHHCCIGEEMHCFMMNFOIEMMCIEACEBBOMACPFAMLHEPADHGCMJCFHOHBGFPNDDKFAJAGCNKBHIBAHBFHHNFJDOFCIAPNHPCKEFJBMNKMACKAJHGAMICCHNOFGINAALFFAHJFMKACIAKCFEEKFNALMOKKOIIODMANKOIEFNMBPEDOOJCDAJJDPIEEABBEOILNBDNAAADHEPNANKBMFLALEMNMJAAEHHFAAGAGHEKANIJBNFCOKOINCCNJDABHGAGDKPILIAMJCEKAHNHKFHNODAANAJDJJEAAFHABJOKIOIFIEIENADALOICAHHNENGCHHJHOMKMPOCBIHNOOAJJLENIFIECOOOMKMOCIHAKPHIDAEMNHKGIGPMAGKJJCOAHKMCCLKKOPGICIPHJFABACOECHHHPJBIMHCDKNAKOEINDIEKPKHCFNLONMOAKIFEGEAHAAHEFCIGFBOEAKJELDCAIIIEKADJLKNLANMKMJPCIKBOGDAFJDBNAOAAAALAJNKCILLOPLAFMNABFADGHDBNNECACAJHLPLJDLHDOHHOHDGEKNNDAFADNMOAPPPAHNAHAFANKMEICGPBDOHHFNGAMNHEEAGIECEIBNNDKFAKFHKFEAMCELOKFCFMJIJHPHAEAGECMCNECKHCFOMCCMFIHIGFHEBEPFIDELIOOEANGINKAAEIBOPDMKACMPHPCANDADDABCKNCJOIHKAEJNFMEPIBMEDEAOFCGDHAAMAJPAPBDNKHICPNKMFIPOINLHAOAOOICAAHOEGKMNOLIIFDAJIACHOPEOKHINJHKCNIEFIKPOAMAILIANIACEANNOKJIIMDJAHPFDJDOCOGIOAKAIHAJCLJEDCNHDIHHOIFOHBNHOMIEAGDNLOACPCFFNNDAKBDFICNFPPELMOAIOFAFLAGPAOEOANEAPACMGJCBHHMJAKIIKHHFFHGHHKFKCNPANJAAABAMJADCEHOFDHNNJIAIAOOCOOMICAPNCBGPCMFDEMBBAPIMABBJMDLBM'
b='NDAHAFNAJOLGCBMAHIFJEKIOIECIKJBK'
c='NGAELFNBJOJGHCAAHFFENKICIECIMFIK'
d='MIBNLCMCBBADNNBMMFBFJMMNBBBBNPHM'

tab=[7,3,2,1,5,8,6,4]

def ex(t):
    d1=calc_dict('танк', b[0:16], t)
    d2=calc_dict('овой', b[16:32], t)
    d3=calc_dict('1___', d[0:16], t)
    d4=calc_dict('____', d[16:32], t)

    dic = d1 | d2 | d3 | d3 | {'AA' : ' ','EB': '«','GB': '»','FP': 'Т','HN': 'Г','EG': '--','AJ': '0','PB': 'М','LJ': 'Ч','KO': 'О','IF': 'ё','AF': 'з','CP': 'ц','IO': 'и','NO': 'д','ED': 'щ', 'FH': 'в', 'EI': 'й', 'IK': 'о', 'HC': 'р', 'OO': 'у', 'GF': 'т', 'EM': 'e', 'HD': 'м', 'BE': 'я', 'PD': 'л', 'JA': 'н', 'ON': 'к', 'AN': 'а', 'JE': ',', 'LA': 'П', 'DD': 'г', 'CM': 'c', 'KC': 'x', 'PJ': 'ю', 'CK': 'ч', 'KJ': 'К', 'HH': 'п', 'MF': 'ы', 'KK': 'б', 'NF': 'ь', 'IC': 'Г', 'CC': 'ф', 'NB': 'ж', 'GN': '.', 'KJ': 'К', 'HF': 'Н', 'EO': 'В', 'OE': 'ш', 'DL': '-', 'FN': 'З', 'LH': 'И', 'HI': 'э', 'MB': 'С', 'FC': 'Ш', 'PG':'А', 'OP': '2', 'GA': '3', 'KB': '4', 'PH': '5', 'BF': '6', 'GH': '7', 'AL': '8', 'FO': '9', 'CF': '(', 'HM': ')'}
    print(f"Dict: {dic}\n\n")
    print(decode(shuffle(rm_noise(a), t), dic))
    

ex(tab)



