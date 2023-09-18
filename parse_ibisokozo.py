import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ibisokozo_api.settings")

import django
django.setup()

from api.models import *

data = [
{
"igisokozo":'Icutabonye', 
"inyishu":'Ubugeni bwaso na nyoko',
"insiguro":'Ibi babivuga kubera bidakunda kubona ubugeni bwabavyeyi'
},
{
"igisokozo":'Abatama bakera baca imanza bunamye', 
"inyishu":'Imigondoro yibiharage',
"insiguro":"Ibi babivuga kubera imigondoro y'ibiharage umengo irunamye"
},
{
"igisokozo":'Ndakibona nsigifata', 
"inyishu":'Igitutu',
"insiguro":"Ibi babivuga kubera igitutu uguma ukibona ariko utari bugifate"
},
{
"igisokozo":'Karayengera', 
"inyishu":'Akotsi k abungere',
"insiguro":"Ibi babivuga kubera abungere baragiye bacana igicaniro bigatuma ubona urikure akotsi kariko karayengera"
},
{
"igisokozo":'Umwana wanje yokunesha ari muto', 
"inyishu":'Uruyuki',
"insiguro":"Ibi babivuga kubera uruyuki rushobora kukurya ukanakoma induru bititaye uko ungana kwose"
},
{
"igisokozo":'Ane meza', 
"inyishu":'Amabere y Inka',
"insiguro":"Ibi babivuga kubera amabere y Inka akamwa amata kndi amata nikirumara mubuzima bw Abarundi",
},
{
 "igisokozo":'Icutabonye', 
 "inyishu":'Ubugeni bwaso na nyoko',
 "insiguro":'Ibi babivuga kubera bidakunda kubona ubugeni bwabavyeyi'
},
{
 "igisokozo":'Abatama bakera baca imanza bunamye', 
 "inyishu":'Imigondoro yibiharage',
 "insiguro":"Ibi babivuga kubera imigondoro y'ibiharage umengo irunamye"
},
{
 "igisokozo":'Ndakibona nsigifata', 
 "inyishu":'Igitutu',
 "insiguro":"Ibi babivuga kubera igitutu uguma ukibona ariko utari bugifate"
},
{
 "igisokozo":'Karayengera', 
 "inyishu":'Akotsi k abungere',
 "insiguro":"Ibi babivuga kubera abungere baragiye bacana igicaniro bigatuma ubona urikure akotsi kariko karayengera"
},
{
 "igisokozo":'Umwana wanje yokunesha ari muto', 
 "inyishu":'Uruyuki',
 "insiguro":"Ibi babivuga kubera uruyuki rushobora kukurya ukanakoma induru bititaye uko ungana kwose"
},
{
 "igisokozo":'Abana banje bakubita ibiganza hirya no hino', 
 "inyishu":'Imitwe y Inzuzi',
 "insiguro":"Ibi babivuga kubera inzuzi zirandaranda impande zose"
},
{
"igisokozo":'Kira se katamobwa', 
"inyishu":'Agahanga kimbwa',
"insiguro":"Ibi babivuga kubera imbwa itigera imobwa"
},
{
"igisokozo":'Uhhhmmm', 
"inyishu":'Igikamiwe make',
"insiguro":"...."
},
{
"igisokozo":'Aha twese turaririye umwe', 
"inyishu":'Inkono kuziko',
"insiguro":"Ibi babivuga kubera ahohambere iyo batetse wasanga abo mumuryango bose bicaye barindiriye ko bisha"
},
{
"igisokozo":'Kararungera', 
"inyishu":'Akotsi kabungere',
"insiguro":"Ibi babivuga kubera ahohambere iyo angungere baragiye baracana rero akotsi kagaca kaduga hejuru gose kubera bari bari kumusozi"
},
{
"igisokozo":'Aho hepfo haciye ingoma itavuga.', 
"inyishu":'Umugore afise inda',
"insiguro":"Ibi babivuga kubera umugore yibungenze abafise inda nini ingana ningoma, rero baca babigereranya ningoma ariko idashobora kuvuga nkizindi"
},
{
"igisokozo":'Wigera mu Barembe wari Umurembe!', 
"inyishu":'Impene muntama',
"insiguro":"Ibi babivuga bashatse kuvuga umuntu canke ikintu kiri mubundi bitandukanye, cisa arikimwe"
},
{
"igisokozo":'Abo kwa Ruringaniza bambariye imiringa mu kuzimu.', 
"inyishu":'Ibijumbu',
"insiguro":"Ibi babivuga kubera ibijumbu vyamira munsi yivu"
},
{
"igisokozo":'Akavumu kanje mpungurura bunyoni.', 
"inyishu":'Inkono yumurango niryumwe',
"insiguro":"Ibi babivuga kubera aho hambere iyo bahishije abantu bose bomumuryango baca bakorana kugira bafungure, rero bavuga ko ari mpungurura kubera bose baca bahagarika ivyo bariko barakora hama bakaza gufungura"
},
{
"igisokozo":'Karahinda iduri.', 
"inyishu":'Akato mumpange',
"insiguro":"..."
},
{
"igisokozo":'Urabona ngo bitugu vya sogokuru ansimbira urugo!', 
"inyishu":'Ikivumvuri',
"insiguro":"Ibi babivuga kubera ikivumvuri gifise ibitugu bisumba izosi"
},
{
"igisokozo":"Abagore ba kera baheka abana neza nayo ab'ubu ntumbarire.", 
"inyishu":'Ibigori bisimbije',
"insiguro":"..."
},
{
"igisokozo":"Abakobwa bansanze ku mugina nti enda bakobwa nkirigita.", 
"inyishu":'Inkumi yinkezi',
"insiguro":"..."
},
{
"igisokozo":"Abakuru baraho baca imanza bunamwe.", 
"inyishu":"Impfizi z'intama zirwana.",
"insiguro":"..."
},
{
"igisokozo":"Abambara ba Ruhinda bambariye impeko mu kuzimu.", 
"inyishu":"Ibiyoba",
"insiguro":"..."
},
{
"igisokozo":"Abanyabuhura ntibubaka barahonjagira.", 
"inyishu":"Umuyirwe w'ibigori.",
"insiguro":"..."
},
{
"igisokozo":"Abanyakigwa ntibubaka barahonjagira.", 
"inyishu":"amarenga.",
"insiguro":"..."
},
{
"igisokozo":"Abanyakirirmiro ntibubaka barahonjagira.", 
"inyishu":"Amajigo.",
"insiguro":"..."
},
{
"igisokozo":"Abazungu ba bujumbura bambaye ibirato bose.", 
"inyishu":"Amavunja.",
"insiguro":"..."
},
{
"igisokozo":"Agacumu kanje runyura bisaka.", 
"inyishu":"Umuravyo.",
"insiguro":"Ibi babivuga kubera umuravyo ari ikintu kinyaruka gose"
},
{
"igisokozo":"Tora akato ntore akandi tuje kurondera ico tutari bubone.", 
"inyishu":"Amaganga y'inkoko.",
"insiguro":"Ibi babivuga kubera inkoko atamaganga igira, rero baba bashatse kuvuga ikintu kidakunda"
},
{
"igisokozo":"Aho Jabwe na Soro barwaniye nubu ni inkumbagare.", 
"inyishu":"Ubuhanza",
"insiguro":"Ibi babivuga kubera umuntu afise ubuhanza umushatsi usanga waravungutse"
},
{
"igisokozo":"Nkubise inyuma y’urugo nza ndatwenga.", 
"inyishu":"Ikigori mu minwe",
"insiguro":"Ibi babivuga kubera baba bashatse kuvuga kwiyo umuntu aje azanye ikigori aza aryohewe"
},
{
"igisokozo":"Ubugabo buva hasi nokuriza ndi muto.", 
"inyishu":"Isusa",
"insiguro":"Ibi babivuga kubera agasusa gashobora kukubaba kakakubabaza cane kandi ubona ari gato"
},
{
"igisokozo":"Urusenge rwanje rwuzuye inzahabu naho woraramwo ntiwoziharura.", 
"inyishu":"Inyenyeri kwijuru",
"insiguro":"Ibi babivuga kubera kugicu hari inyenyeri nyishi kuburyo utoshobora no kuziharura.",
},
{
"igisokozo":'Abana banje bazi gucuraranga bose', 
"inyishu":'Imirya y’inanga',
"insiguro":''
},
{
"igisokozo":'Abagabo barara bahagaze bakirirwa bahagaze', 
"inyishu":'Inkingi z’inzu',
"insiguro":''
},
{
"igisokozo":'Tubana tutava aho turi ariko ntitwigera turamukanya', 
"inyishu":'Amabere y’umugore / umukobwa;Inkombe z’uruzi',
"insiguro":''
},
{
"igisokozo":'Ubugabo buva hasi nokuriza ndi muto', 
"inyishu":'Isusa/Ikiboroza/Igisuru',
"insiguro":''
},
{
"igisokozo":'Tubana dutinyana', 
"inyishu":'Umuriro n’amazi/Umwijima n’umuriro/Umwijima n’umuco',
"insiguro":''
},
{
"igisokozo":'Ico utazi utabonye', 
"inyishu":'Ubukumi bwa nyoko/Ubusore bwa so/Ubugeni bwa so na nyoko',
"insiguro":''
},
{
"igisokozo":'Bwenge bw’aha bwogutana', 
"inyishu":'Wotambika urucaca kuruzi ukajabuka',
"insiguro":''
},
{
"igisokozo":'Agafyiri gakamwa ayera', 
"inyishu":'Inzoka igenda itagira amaguru/Inkoko icutsa itonkeje',
"insiguro":''
},
{
"igisokozo":'Abagabo barara bahagaze bwaca bakaryama', 
"inyishu":'Imyugariro',
"insiguro":''
},
{
"igisokozo":'Ivyiza biva kuzimu vyambaye inyerere bigacambirwa n’Abamikazi', 
"inyishu":'Amateke',
"insiguro":''
},
{
"igisokozo":'Aho turi ku mbuga tungana twese', 
"inyishu":'Ifundi',
"insiguro":''
},
{
"igisokozo":'Aho Jabwe na Soro barwaniye nubu ni inkumbagare', 
"inyishu":'Ubuhanza',
"insiguro":''
},
{
"igisokozo":'Ndi mugiraneza muvyara w’urupfu', 
"inyishu":'Itiro',
"insiguro":''
},
{
"igisokozo":'Karahara mu ruganda ntibacura', 
"inyishu":'Inyundo',
"insiguro":''
},
{
"igisokozo":'Urusenge rwanje rwuzuye inzahabu naho woraramwo ntiwoziharura', 
"inyishu":'Ijuru n’inyenyeri',
"insiguro":''
},
{
"igisokozo":'Kajuju ka Ntimba kiyereka aho katatumiwe', 
"inyishu":'Akanyugunyugu',
"insiguro":''
},
{
"igisokozo":'Dukumburanye tubana', 
"inyishu":'Amabere',
"insiguro":''
},
{
"igisokozo":'Ndatambatamba ntazi iyo nja nkavuna inzara', 
"inyishu":'Uruyuzi',
"insiguro":''
},
{
"igisokozo":'Dusa tudasa', 
"inyishu":'Intore n’intobotobo',
"insiguro":''
},
{
"igisokozo":'Ntugire ubwoba ndasamye ariko sindyana', 
"inyishu":'Umuryango w’inzu itugaye',
"insiguro":''
},
{
"igisokozo":'Fata isuka mfate iyindi tuje kwimba ico tutabona', 
"inyishu":'Umuzi w’ibuye',
"insiguro":''
},
{
"igisokozo":'Nasezeye umusezero kera kuri Cambarantama nubu nturasezuruka', 
"inyishu":'Ubwoya bw’inka',
"insiguro":''
},
{
"igisokozo":'Aha ngo fye, hirya no hino ngo fye fye. Ngo twa', 
"inyishu":'Imiravyo n’umuturagaro',
"insiguro":''
},
{
"igisokozo":'Iyi nzira njanye, idashitse abanje barahera', 
"inyishu":'Inzira ija mu kigega',
"insiguro":''
},
{
"igisokozo":'Akana kanje kokuriza ari gato', 
"inyishu":'Akanyarirajisho',
"insiguro":''
},
{
"igisokozo":'Abeza bahetse n’ubusage ku mutwe', 
"inyishu":'Umurima w’ibigori uhetse',
"insiguro":''
},
{
"igisokozo":'Ntaco umfyurira amaso sindaguha', 
"inyishu":'Imyenge y’inzu',
"insiguro":''
},
{
"igisokozo":'Mvuye kwikura Bushoro aca anyoma amaguru inyuma', 
"inyishu":'Umunyota',
"insiguro":''
},
{
"igisokozo":'Nsha umugongo simpunge', 
"inyishu":'Urusenge',
"insiguro":''
},
{
"igisokozo":'Iyo tuva turyoha duhambwe', 
"inyishu":'Imihwi',
"insiguro":''
},
{
"igisokozo":'Aha turi havuyemwo umwe mwese muraburara', 
"inyishu":'Amashiga',
"insiguro":''
},
{
"igisokozo":'Umurwa ukuka amazi niwawumenya nguhere', 
"inyishu":'Umukenke',
"insiguro":''
},
{
"igisokozo":'Umugozi utekera amazi niwawumenya nguhere.', 
"inyishu":'Ifu',
"insiguro":''
},
{
"igisokozo":'Ehe urya musozi wishika ibikanu.', 
"inyishu":'Abahizi.',
"insiguro":''
},
{
"igisokozo":'Narajishe inkoko none sindayirirako.', 
"inyishu":'Agasongero.',
"insiguro":''
},
{
"igisokozo":'Hano dufise impindu twese.', 
"inyishu":'Imirizo y’imbeba.',
"insiguro":''
},
{
"igisokozo":'Nyoko yambara ibiheko vyinshi nkeka aroga.', 
"inyishu":'Umutobotobo.',
"insiguro":''
},
{
"igisokozo":'Ndarwaje.', 
"inyishu":'Inzara mu bana.',
"insiguro":''
},
{
"igisokozo":'Ngo tuje kugarura Rugamba irambutse.', 
"inyishu":'Ikinyugunyugu.',
"insiguro":''
},
{
"igisokozo":'Narungitse umwana kurahura none n’ubu ntaraza.', 
"inyishu":'Umwotsi.',
"insiguro":''
},
{
"igisokozo":'Kubita binati ntiyota arasara.', 
"inyishu":'Urubumbiro.',
"insiguro":''
},
{
"igisokozo":'Nyegera nyegera bana banje turashize', 
"inyishu":'Uburo mu ngasiro.',
"insiguro":''
},
{
"igisokozo":'Bugingo bwa none bwogutana.', 
"inyishu":'Wotekera amazi mu rukangaga?',
"insiguro":''
},
{
"igisokozo":'Karahinda iduri.', 
"inyishu":'Akato mu mpange.',
"insiguro":''
},
{
"igisokozo":'Tora akato ntore akandi tuje kuvoma ico tutari bubone.', 
"inyishu":'Amaganga y’inkoko.',
"insiguro":''
},
{
"igisokozo":'Ndi mugufi nkaba mu rwanje.', 
"inyishu":'Igicaniro',
"insiguro":''
},
{
"igisokozo":'Wigera mu Barembe wari umurembe?', 
"inyishu":'Impene mu ntama',
"insiguro":''
},
{
"igisokozo":'Abo kwa Ruringaniza bambariye imiringa mu kuzimu.', 
"inyishu":'Ibijumbu.',
"insiguro":''
},
{
"igisokozo":'Abana banje bakubita ibiganza hirya no hino', 
"inyishu":'Imitwe y’inzuzi.',
"insiguro":''
},
{
"igisokozo":'Mbe nyoku ko useye bwinshi urarirwa na bande?', 
"inyishu":'Itimbi ry’ifuku.',
"insiguro":''
},
{
"igisokozo":'Gira so katamobwa.', 
"inyishu":'Agahanga k’imbwa.',
"insiguro":''
},
{
"igisokozo":'Urabona ngo bitugu vya sogokuru ngo ansimbira urugo?', 
"inyishu":'Ikivumvuri.',
"insiguro":''
},
{
"igisokozo":'Aha twese turariye umwe.', 
"inyishu":'Inkono ku ziko.',
"insiguro":''
},
{
"igisokozo":'Ikiri kure kirya abari n’amaguru.', 
"inyishu":'Ikigazi',
"insiguro":''
},
{
"igisokozo":'Umunani mabi', 
"inyishu":'Amabere y’imbwa',
"insiguro":''
},
{
"igisokozo":'Ane meza', 
"inyishu":'Amabere y’inka',
"insiguro":''
},
{
"igisokozo":'Batatu badatana mu ndagano', 
"inyishu":'Amashiga',
"insiguro":''
},
{
"igisokozo":'Ndahamanuka sindahaduga', 
"inyishu":'Amazi',
"insiguro":''
},
{
"igisokozo":'Ndara ndagenda, nkirirwa ndagenda', 
"inyishu":'Uruzi',
"insiguro":''
},
{
"igisokozo":'Mvuye guta nyokuru agaruka ankurikira', 
"inyishu":'Umwavu',
"insiguro":''
},
{
"igisokozo":'Karadundega', 
"inyishu":'Akana kaja iwabo',
"insiguro":''
},
{
"igisokozo":'Mpa utwo mbona', 
"inyishu":'Utuboga ku menyo',
"insiguro":''
},
{
"igisokozo":'Ndavye hejuru ndanungwanungwa', 
"inyishu":'Umuhwi',
"insiguro":''
},
{
"igisokozo":'Ngenda mfoye ariko sindekura', 
"inyishu":'Amabere y’inkumi ataragwa',
"insiguro":''
},
{
"igisokozo":'Umututsi muremure yavuye imagamba', 
"inyishu":'Imvura',
"insiguro":'...'
},
{
"igisokozo":'Ahohepfo haciye ivyiza bisa', 
"inyishu":'Umuzungo kwipikipiki',
"insiguro":'...'
},
{
"igisokozo":'Ahohiyo ngo to to to', 
"inyishu":'Imvura kumabati',
"insiguro":'Ibi babivuga kubera imvura iriko iragwa kumabati iguma ivuga ngo to to to'
},
{
"igisokozo":'Fata inkoni mfate iyindi tuje kugarura umugamba iramburutse', 
"inyishu":'Ikinyugunyugu',
"insiguro":'...'
},
{
"igisokozo":'Akayobera kayobeye umwami nabagabo', 
"inyishu":"Inka y'umufyiri ikamwa ayera",
"insiguro":'...'
},
{
"igisokozo":'Nkurira rudagaza kwirembo', 
"inyishu":"Igikona",
"insiguro":'...'
},
{
"igisokozo":'Karanutaraye binati', 
"inyishu":"Igikona kwibuye",
"insiguro":'...'
},
{
"igisokozo":'Nkurira fyiroko mwitongo', 
"inyishu":"Impene muntama",
"insiguro":'...'
},
{
"igisokozo":'Gima gima muka barihuta', 
"inyishu":"Inuma kukivumu",
"insiguro":'...'
},
{
"igisokozo":'komera amashi bizungagi', 
"inyishu":"Igitsembetsembe c'intama",
"insiguro":'...'
},
{
"igisokozo":'inaga ya buruhukiro ntivuga irimonogoza', 
"inyishu":"Inkona kwijuru",
"insiguro":'...'
},
{
"igisokozo":'Karabigendura katabirimye', 
"inyishu":"Igikere",
"insiguro":'...'
},
{
"igisokozo":'Demwa Demwa mushiki wa rubano', 
"inyishu":"Ikinyobwa",
"insiguro":'...'
}
]


for el in data:
    igisokozo = Igisokozo(
        igisokozo=el['igisokozo'],
        )
    igisokozo.save()
    inyishuIg = InyishuIgisokozo(
        igisokozo=igisokozo,
        inyishu=el['inyishu'],
        insiguro=el['insiguro']
        )
    inyishuIg.save()
