Last login: Wed Jul 10 18:06:39 on ttys000
Joys-MacBook-Pro:~ JoyCowper$ python
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import webbrowser
>>> import requests
>>> Req = requests.get('https://artprice.com')
Re>>> Req
<Response [200]>
>>> Req.history
[<Response [301]>]
>>> Req = requests.get('https://www.artprice.com')
Re>>> Req
<Response [200]>
>>> Req.history
[]
>>> if Req.history == 0:
...     print('Yes')
...
>>>
>>>
>>> end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'end' is not defined
>>>
>>> if Req.history == 0:
...     print('Yes')
... else:
...     print('No')
...
No
>>> type(Req.history)
<class 'list'>
>>> len(Req.history)
0
>>> if len(Req.history) == 0:
...     print('Empty')
... else:
...     print('history exists')
...
Empty
>>> exit()
Joys-MacBook-Pro:~ JoyCowper$ ls
-bash			AndroidStudioProjects	Documents		Library			Pictures		Untitled.ipynb		rhino
=			Applications		Downloads		Movies			Public			VirtualBox VMs
Adlm			Desktop			Google Drive		Music			Samsung			anaconda3
Joys-MacBook-Pro:~ JoyCowper$ cd Desktop
Joys-MacBook-Pro:Desktop JoyCowper$ ls
AWI					Deadline Distribution.xlsx		MarketMogul.pdf				Screenshot 2019-07-01 at 16.39.41.png	Year 3
ArtScrape.py				Dissertation				PGT Conditional Offer Letter.pdf	Screenshot 2019-07-04 at 00.55.06.png	hindi_cons.gif
ArtSearch.py				End of Year Evaluation 2017:18.pdf	Redirect Test in Python			Screenshot 2019-07-07 at 19.11.20.png	hindi_num.gif
ArtTrans.json				Growth					SDirection II-ii.pdf			SoQ-Form - Joy Cowper.pdf		hindi_vwl.gif
ArtURLs.xlsx				IBM IPAT.pdf				Screenshot 2019-06-09 at 19.53.33.png	Terminal Output				hiragana_chart.jpg
Artprice Blocks of 500.xlsx		KimiUso.jpg				Screenshot 2019-06-16 at 20.06.29.png	Test.csv				~$Artprice Blocks of 500.xlsx
Artprice.html				LinkTester.py				Screenshot 2019-07-01 at 16.13.19.png	Test.py
Databook 2016.pdf			Links 141-642.csv			Screenshot 2019-07-01 at 16.33.47.png	Year 2
Joys-MacBook-Pro:Desktop JoyCowper$ python3 LinkTester.py
['Link'
 'https://www.artprice.com/marketplace/1885025/georges-bastia/drawing-watercolor/luis-mariano-rossignol'
 'https://www.artprice.com/marketplace/1885022/georges-bastia/drawing-watercolor/jean-marais-cerf'
 'https://www.artprice.com/marketplace/1885019/georges-bastia/drawing-watercolor/odette-laure-ecureuil'
 'https://www.artprice.com/marketplace/1885013/georges-bastia/drawing-watercolor/robert-lamoureux'
 'https://www.artprice.com/marketplace/1883134/hrasarkos/drawing-watercolor/pastel-22-nu-22'
 'https://www.artprice.com/marketplace/1882609/tony-agostini/drawing-watercolor/dessin-a-l-27aquarelle-signe-handsigned-watercolor-drawing'
 'https://www.artprice.com/marketplace/1882492/henri-jean-pontoy/drawing-watercolor/paysage-orientaliste'
 'https://www.artprice.com/marketplace/1427823/louis-pons/drawing-watercolor/aix'
 'https://www.artprice.com/marketplace/967131/louis-pons/drawing-watercolor/aix'
 'https://www.artprice.com/marketplace/1882004/emil-orlik/drawing-watercolor/pot-with-a-flower'
 'https://www.artprice.com/marketplace/1500126/alois-erbach/drawing-watercolor/der-anspruchsvolle-gast'
 'https://www.artprice.com/marketplace/1877305/clement-serveau/drawing-watercolor/dessin-a-l-27encre-1952-signe-handsigned-ink-drawing'
 'https://www.artprice.com/marketplace/1877287/pierre-emile-gabriel-lelong/drawing-watercolor/dessin-a-la-gouache-1954-signe-handsigned-gouache-drawing'
 'https://www.artprice.com/marketplace/1877284/philippe-henri-noyer/drawing-watercolor/dessin-a-la-gouache-1952-signe-handsigned-gouache-drawing'
 'https://www.artprice.com/marketplace/1876985/eugene-deveria/drawing-watercolor/sophie'
 'https://www.artprice.com/marketplace/1876979/edouard-elle/drawing-watercolor/moulin-a-eau'
 'https://www.artprice.com/marketplace/1876970/antoine-auguste-thivet/drawing-watercolor/orientale-au-tambourin'
 'https://www.artprice.com/marketplace/1876967/antoine-auguste-thivet/drawing-watercolor/marchande-d-27oranges'
 'https://www.artprice.com/marketplace/398573/didier-angels/drawing-watercolor/une-autre-vie-apres-l-27apocalypse-serie-a24'
 'https://www.artprice.com/marketplace/1876672/claude-bleynie/drawing-watercolor/papillon-de-jour'
 'https://www.artprice.com/marketplace/1876210/georges-ripart/drawing-watercolor/delassements-champetre'
 'https://www.artprice.com/marketplace/1876204/francois-heaulme/drawing-watercolor/portrait-d-27homme'
 'https://www.artprice.com/marketplace/1876048/henry-waroquier-de/drawing-watercolor/dessin-crayon-signe-1961-handsigned-pencil-drawing-portrait'
 'https://www.artprice.com/marketplace/1876045/andre-albert-marie-dunoyer-de-segonzac/drawing-watercolor/dessin-a-l-27encre-et-lavis-signe-handsigned-ink-drawing'
 'https://www.artprice.com/marketplace/1876042/andre-albert-marie-dunoyer-de-segonzac/drawing-watercolor/dessin-encre-et-lavis-signe-ads-handsigned-ink-drawing'
 'https://www.artprice.com/marketplace/1874818/biagio-pancino/drawing-watercolor/sans-titre'
 'https://www.artprice.com/marketplace/1874812/biagio-pancino/drawing-watercolor/vitam-e-mortem-n-c2-b01'
 'https://www.artprice.com/marketplace/1874809/biagio-pancino/drawing-watercolor/vitam-e-mortem-n-c2-b06'
 'https://www.artprice.com/marketplace/1874785/wladyslaw-granzow/drawing-watercolor/2-portraits'
 'https://www.artprice.com/marketplace/1874486/edouard-pignon/drawing-watercolor/dessin-au-fusain-1944-signe-handsigned-charcoal-drawing'
 'https://www.artprice.com/marketplace/1874380/patrick-loiseau/drawing-watercolor/mireille-matthieu'
 'https://www.artprice.com/marketplace/1874290/auguste-sebastien-benard/drawing-watercolor/cavaliers-baschkirs'
 'https://www.artprice.com/marketplace/1874287/auguste-sebastien-benard/drawing-watercolor/cavaliers-tartares'
 'https://www.artprice.com/marketplace/1345266/placid/drawing-watercolor/sans-titre'
 'https://www.artprice.com/marketplace/1863182/desire-donny/drawing-watercolor/sturmische-see-mit-booten'
 'https://www.artprice.com/marketplace/1863176/carsten-nicolai/drawing-watercolor/kopf-an-korper'
 'https://www.artprice.com/marketplace/1863164/paul-kuhfuss/drawing-watercolor/markischer-see'
 'https://www.artprice.com/marketplace/1863010/gustav-adolf-hahn/drawing-watercolor/klosterkirche-maulbronn'
 'https://www.artprice.com/marketplace/1863001/max-oppenheimer/drawing-watercolor/pekinesen'
 'https://www.artprice.com/marketplace/1862995/leopold-bode/drawing-watercolor/petrus'
 'https://www.artprice.com/marketplace/1862992/inge-karsch/drawing-watercolor/tiefer-neuschnee'
 'https://www.artprice.com/marketplace/1862986/kaspar-kaltenmoser/drawing-watercolor/hausliche-komposition-mit-liebespaar'
 'https://www.artprice.com/marketplace/1862983/alexandre-leblanc/drawing-watercolor/convent-pres-de-frascati'
 'https://www.artprice.com/marketplace/1862977/werner-tubke/drawing-watercolor/ravensburg'
 'https://www.artprice.com/marketplace/1862968/ludwig-franz-karl-bohnstedt/drawing-watercolor/gelageszene-am-golf-von-sorrent-villa-pollio-felice'
 'https://www.artprice.com/marketplace/1862953/erich-buchholz/drawing-watercolor/o-t-28abstrakte-komposition-29'
 'https://www.artprice.com/marketplace/1862947/johann-heinrich-lips/drawing-watercolor/portrats-von-g-coustou-und-joseph'
 'https://www.artprice.com/marketplace/1862941/aleksey-alexandrov-pisemsky/drawing-watercolor/dorfansicht'
 'https://www.artprice.com/marketplace/1862582/curt-querner/drawing-watercolor/sommerabend-28sitzender-weiblicher-akt-29'
 'https://www.artprice.com/marketplace/1862261/maurice-esteve/drawing-watercolor/48-c'
 'https://www.artprice.com/marketplace/1856087/otto-robert-nowak/drawing-watercolor/wald-bei-ober-st-veit'
 'https://www.artprice.com/marketplace/1287393/arno-breker/drawing-watercolor/akt'
 'https://www.artprice.com/marketplace/660540/edouard-detaille/drawing-watercolor/lieutenant-d-27infanterie-second-empire'
 'https://www.artprice.com/marketplace/1855649/erich-heckel/drawing-watercolor/lake-between-mountains-2c-karnte'
 'https://www.artprice.com/marketplace/1855585/roger-paul-froidevaux/drawing-watercolor/paysage-en-ete'
 'https://www.artprice.com/marketplace/1849702/r-renneson/drawing-watercolor/croix-de-village-et-chalets-en-montagne'
 'https://www.artprice.com/marketplace/1855469/mario-schifano/drawing-watercolor/the-futurists-7c-i-futuristi'
 'https://www.artprice.com/marketplace/1520628/francisco-bores/drawing-watercolor/personnage'
 'https://www.artprice.com/marketplace/1855051/david-schneuer/drawing-watercolor/figures-in-paris'
 "https://www.artprice.com/marketplace/1193692/haywen-t'ang/drawing-watercolor/sans-titre-2c-vers-1975"
 'https://www.artprice.com/marketplace/1854838/ernst-graner/drawing-watercolor/landschaft-mit-pinie'
 'https://www.artprice.com/marketplace/1840387/egisto-massoni/drawing-watercolor/puerta-del-palacio-del-dogo-venecia'
 'https://www.artprice.com/marketplace/1840117/ben/drawing-watercolor/tout-est-ecrit'
 'https://www.artprice.com/marketplace/1828477/jean-claude-latil/drawing-watercolor/untitled'
 'https://www.artprice.com/marketplace/1840133/mane-katz/drawing-watercolor/hands-and-heads-of-jewish-portraits'
 'https://www.artprice.com/marketplace/743087/amos-yaskil/drawing-watercolor/maria-27s-well-in-nazareth'
 'https://www.artprice.com/marketplace/743086/amos-yaskil/drawing-watercolor/mount-tabor'
 'https://www.artprice.com/marketplace/1839938/hermann-corrodi/drawing-watercolor/27-landscape-with-characters-27'
 'https://www.artprice.com/marketplace/1822549/domenico-gargiulo/drawing-watercolor/the-martyrdom-of-st-andrew'
 'https://www.artprice.com/marketplace/1822537/mose-di-giosue-bianchi/drawing-watercolor/la-pusterla-dei-fabbri-2c-milano'
 'https://www.artprice.com/marketplace/1822525/gerolamo-induno/drawing-watercolor/fame-e-freddo'
 'https://www.artprice.com/marketplace/1822519/telemaco-signorini/drawing-watercolor/a-view-of-northumberland-place-2c-bath-2c-1881'
 'https://www.artprice.com/marketplace/1822507/alberto-pasini/drawing-watercolor/view-of-the-sunset-in-bauchir'
 'https://www.artprice.com/marketplace/1820134/henry-moret/drawing-watercolor/22cote-bretonne-22-22personnages-sur-la-plage-22'
 'https://www.artprice.com/marketplace/1211779/alberto-pasini/drawing-watercolor/transito-di-una-carovana-tra-la-persia-e-il-khorasan'
 'https://www.artprice.com/marketplace/1821982/jeremie-iordanoff/drawing-watercolor/n-c2-b0623-22au-travers-du-rideau-22'
 'https://www.artprice.com/marketplace/1821979/jeremie-iordanoff/drawing-watercolor/n-c2-b0667-22les-barriques-22'
 'https://www.artprice.com/marketplace/1821976/jeremie-iordanoff/drawing-watercolor/n-c2-b0666-22avec-du-rouge-22'
 'https://www.artprice.com/marketplace/1821964/jeremie-iordanoff/drawing-watercolor/n-c2-b0663-22cerneaux-de-noix-22'
 'https://www.artprice.com/marketplace/1821967/jeremie-iordanoff/drawing-watercolor/n-c2-b0664-22echographie-22'
 'https://www.artprice.com/marketplace/1821961/jeremie-iordanoff/drawing-watercolor/n-c2-b0662-22stegosaurus-22'
 'https://www.artprice.com/marketplace/1821829/henri-fehr/drawing-watercolor/femme-denudee'
 'https://www.artprice.com/marketplace/1821775/roger-ferrero/drawing-watercolor/clown-blanc'
 'https://www.artprice.com/marketplace/1810465/edward-ardizzone/drawing-watercolor/complete-poems-for-children'
 'https://www.artprice.com/marketplace/1810462/mary-robinson-blair/drawing-watercolor/cinderella'
 'https://www.artprice.com/marketplace/1810459/pamela-ruby-bianco/drawing-watercolor/little-mice-at-play'
 'https://www.artprice.com/marketplace/1810453/richard-dadd/drawing-watercolor/the-rabbit-hutch'
 'https://www.artprice.com/marketplace/1810456/eleanore-vere-boyle/drawing-watercolor/long-did-his-thoughts-waiver'
 'https://www.artprice.com/marketplace/1810450/felix-octavius-carr-darley/drawing-watercolor/oliver-twist-3a-first-meeting-with-the-artful-dodger'
 'https://www.artprice.com/marketplace/1698612/jean-leppien/drawing-watercolor/sans-titre'
 'https://www.artprice.com/marketplace/1698609/walter-kohlhoff/drawing-watercolor/hauser-am-schlesischen-tor-berlin'
 'https://www.artprice.com/marketplace/1698600/walter-kohlhoff/drawing-watercolor/kanal-oder-fluss-in-berlin'
 'https://www.artprice.com/marketplace/1698529/walter-kohlhoff/drawing-watercolor/bethanien-am-mariannenplatz-2c-berlin'
 'https://www.artprice.com/marketplace/1698526/walter-kohlhoff/drawing-watercolor/industrieareal-verso-tuschzeichnung'
 'https://www.artprice.com/marketplace/1698523/walter-kohlhoff/drawing-watercolor/st-thomas-kirche-am-mariannenplatz'
 'https://www.artprice.com/marketplace/1698511/walter-kohlhoff/drawing-watercolor/berliner-kudamm-mit-gedachtniskirche'
 'https://www.artprice.com/marketplace/1698487/walter-kohlhoff/drawing-watercolor/stilleben-mit-blumenstrauss'
 'https://www.artprice.com/marketplace/1698484/walter-kohlhoff/drawing-watercolor/burg-in-den-alpen-28-hohenwerfen-3f-29'
 'https://www.artprice.com/marketplace/1698108/piotr-potworowski/drawing-watercolor/szkice-kostiumu'
 'https://www.artprice.com/marketplace/1683922/aristide-maillol/drawing-watercolor/standing-nude-7c-nude-with-raised-arms'
 'https://www.artprice.com/marketplace/1683496/bela-kadar/drawing-watercolor/constructivist-cityscape-with-green-horse'
 'https://www.artprice.com/marketplace/1681689/david-lan-bar/drawing-watercolor/abstract-composition'
 'https://www.artprice.com/marketplace/1681564/xanda-mccagg/drawing-watercolor/adjacent-7'
 'https://www.artprice.com/marketplace/1671927/zaida-rio-del/drawing-watercolor/series-alto-de-la-mina-iii'
 'https://www.artprice.com/marketplace/1676964/tom-hops/drawing-watercolor/sylter-kuste'
 'https://www.artprice.com/marketplace/1676955/august-lange-brock/drawing-watercolor/hafen-von-hvar-mit-fischerbooten'
 'https://www.artprice.com/marketplace/1676883/evgeniy-andreevich-agafonov/drawing-watercolor/nude'
 'https://www.artprice.com/marketplace/1676521/friedrich-wilhelm-schwinge/drawing-watercolor/aussenalster-hamburg'
 'https://www.artprice.com/marketplace/1675929/friedrich-ahlers-hestermann/drawing-watercolor/blumen-stilleben-in-glasvase-auf-tisch'
 'https://www.artprice.com/marketplace/1043963/andre-charles-voillemot/drawing-watercolor/l-27ivresse-des-putti'
 'https://www.artprice.com/marketplace/1010926/lucien-coutaud/drawing-watercolor/la-plage-de-trouville-2c1974'
 'https://www.artprice.com/marketplace/1674609/richard-caldicott/drawing-watercolor/untitled-2c-2014-28381-29'
 'https://www.artprice.com/marketplace/1674849/walter-kohlhoff/drawing-watercolor/mauer-mit-zaun-an-strasse'
 'https://www.artprice.com/marketplace/1674846/walter-kohlhoff/drawing-watercolor/berliner-dacher-2c-giebel-und-hochhaus'
 'https://www.artprice.com/marketplace/1510971/didier-angels/drawing-watercolor/arpege-2'
 'https://www.artprice.com/marketplace/1673544/tilman/drawing-watercolor/untitled-25711'
 'https://www.artprice.com/marketplace/1672680/walter-kohlhoff/drawing-watercolor/findlinge-und-wurzeln-im-wald'
 'https://www.artprice.com/marketplace/1672677/walter-kohlhoff/drawing-watercolor/umgegend-von-berlin-hauser-im-wald'
 'https://www.artprice.com/marketplace/1663470/walter-kohlhoff/drawing-watercolor/see-mit-baumbestandenem-ufer'
 'https://www.artprice.com/marketplace/1663465/francis-de-lassus-saint-genies/drawing-watercolor/dessin-erotique-crayon-pastel-signe-handsigned-erotic-drawin'
 'https://www.artprice.com/marketplace/1662702/nedzad-nedzo-durakovic/drawing-watercolor/girl-with-green-glasses'
 'https://www.artprice.com/marketplace/1662693/nedzad-nedzo-durakovic/drawing-watercolor/volcano'
 'https://www.artprice.com/marketplace/1662142/ladislav-iosifovich-trakal/drawing-watercolor/lot-of-7-decorative-compositions'
 'https://www.artprice.com/marketplace/1662139/ladislav-iosifovich-trakal/drawing-watercolor/lot-of-two-paintings-poem-of-life-26-poem-of-death'
 'https://www.artprice.com/marketplace/1662136/jules-crosnier/drawing-watercolor/fleurs'
 'https://www.artprice.com/marketplace/1662105/walter-kohlhoff/drawing-watercolor/st-clara-kirche-in-berlin-neukolln'
 'https://www.artprice.com/marketplace/1662099/walter-kohlhoff/drawing-watercolor/blick-in-den-osten-berlins'
 'https://www.artprice.com/marketplace/1662090/walter-kohlhoff/drawing-watercolor/eisenbahnstrecke-berlin'
 'https://www.artprice.com/marketplace/1661734/walter-kohlhoff/drawing-watercolor/haus-und-schuppen-im-schnee'
 'https://www.artprice.com/marketplace/1661731/walter-kohlhoff/drawing-watercolor/admiralbrucke-in-berlin-kreuzberg'
 'https://www.artprice.com/marketplace/1661728/walter-kohlhoff/drawing-watercolor/schrebergarten-mit-hausern'
 'https://www.artprice.com/marketplace/1661725/walter-kohlhoff/drawing-watercolor/hauser-mit-litfasssaule'
 'https://www.artprice.com/marketplace/1661722/walter-kohlhoff/drawing-watercolor/landschaft-mit-hausern'
 'https://www.artprice.com/marketplace/1661719/walter-kohlhoff/drawing-watercolor/strassenzug-wohl-in-252fum-berlin'
 'https://www.artprice.com/marketplace/1661716/walter-kohlhoff/drawing-watercolor/strassengasse-im-suden'
 'https://www.artprice.com/marketplace/1604004/josep-coll-bardolet/drawing-watercolor/paisaje-region-de-wengen'
 'https://www.artprice.com/marketplace/1603792/august-geiger-thuring/drawing-watercolor/lac-alpin'
 'https://www.artprice.com/marketplace/1485141/ludwig-meidner/drawing-watercolor/portrait'
 'https://www.artprice.com/marketplace/1597675/marguerite-anne-blonay-de/drawing-watercolor/5-dessins-aquarelle-signes-5-handsigned-watercolor-drawings'
 'https://www.artprice.com/marketplace/1597243/fabien-fabiano/drawing-watercolor/etudes-de-nu-feminin'
 'https://www.artprice.com/marketplace/1597240/francoise-adnet/drawing-watercolor/dessin-original-au-crayon-signe-handsigned-drawing'
 'https://www.artprice.com/marketplace/1596798/raymond-moretti/drawing-watercolor/dessin-original-au-feutre-signe-handsigned-felt-drawing'
 'https://www.artprice.com/marketplace/1595608/bernard-quentin/drawing-watercolor/arbre-nuage-oiseau'
 'https://www.artprice.com/marketplace/1595605/bernard-quentin/drawing-watercolor/arbre-fleur-oiseau'
 'https://www.artprice.com/marketplace/1595602/bernard-quentin/drawing-watercolor/nuage-blanc'
 'https://www.artprice.com/marketplace/1595599/bernard-quentin/drawing-watercolor/evanescente'
 'https://www.artprice.com/marketplace/1595593/bernard-quentin/drawing-watercolor/dans-cette-vaste-etendue'
 'https://www.artprice.com/marketplace/676884/louis-gonyn/drawing-watercolor/le-ramassage-du-varech-au-crepuscule'
 'https://www.artprice.com/marketplace/1425384/matt-bult/drawing-watercolor/cloud-study-ii'
 'https://www.artprice.com/marketplace/1440906/pal-fried/drawing-watercolor/seated-ballerina'
 'https://www.artprice.com/marketplace/1594623/wilhelm-grimm/drawing-watercolor/portrat-einer-frau'
 'https://www.artprice.com/marketplace/1594620/kurt-prignitz/drawing-watercolor/selbstportrat'
 'https://www.artprice.com/marketplace/1547871/hans-arp/drawing-watercolor/french-form-7c-forme-francaise'
 'https://www.artprice.com/marketplace/1546951/angelo-maisto/drawing-watercolor/nocino'
 'https://www.artprice.com/marketplace/1546948/angelo-maisto/drawing-watercolor/spinetta'
 'https://www.artprice.com/marketplace/1546936/angelo-maisto/drawing-watercolor/fringuello-zafferano'
 'https://www.artprice.com/marketplace/902175/lucien-hector-jonas/drawing-watercolor/le-caporal-prevost'
 'https://www.artprice.com/marketplace/333679/michael-argov/drawing-watercolor/abstract-composition'
 'https://www.artprice.com/marketplace/1545819/fieroza-doorsen/drawing-watercolor/untitled-28id-353-29'
 'https://www.artprice.com/marketplace/1544352/max-liebermann/drawing-watercolor/figure-study-of-paul-with-the-serpent-before-the-maltese'
 'https://www.artprice.com/marketplace/1544385/lesser-ury/drawing-watercolor/landscape-in-walcheren-with-big-trees-and-grazing-cows-7c-lan'
 'https://www.artprice.com/marketplace/1544370/freddy-defossez/drawing-watercolor/cheval-et-jockey-avant-la-course'
 'https://www.artprice.com/marketplace/1544367/freddy-defossez/drawing-watercolor/course-de-chevaux'
 'https://www.artprice.com/marketplace/1544364/freddy-defossez/drawing-watercolor/cheval-avant-la-course'
 'https://www.artprice.com/marketplace/1544346/otto-dix/drawing-watercolor/forest-clearing-7c-waldlichtung'
 'https://www.artprice.com/marketplace/1544337/andre-derain/drawing-watercolor/ballerina'
 'https://www.artprice.com/marketplace/1543539/didier-angels/drawing-watercolor/tourbillon-de-la-vie-b'
 'https://www.artprice.com/marketplace/1525866/georges-kars/drawing-watercolor/seated-young-woman'
 'https://www.artprice.com/marketplace/1481301/ludwig-hoffmann/drawing-watercolor/landscape-by-the-lake'
 'https://www.artprice.com/marketplace/1524534/pierre-comba/drawing-watercolor/chasseurs-alpins'
 'https://www.artprice.com/marketplace/1498212/istvan-szonyi/drawing-watercolor/harvest'
 'https://www.artprice.com/marketplace/1066201/philipp-franck/drawing-watercolor/herbstlandschaft-mit-bach'
 'https://www.artprice.com/marketplace/1248304/henry-waroquier-de/drawing-watercolor/tete-cubiste'
 'https://www.artprice.com/marketplace/762370/georges-guido-filiberti/drawing-watercolor/decor-de-theatre-pour-une-piece-de-macbeth'
 'https://www.artprice.com/marketplace/762367/georges-guido-filiberti/drawing-watercolor/la-ronde-des-trois-graces'
 'https://www.artprice.com/marketplace/762366/georges-guido-filiberti/drawing-watercolor/l-60enfer-du-jeu'
 'https://www.artprice.com/marketplace/762358/georges-guido-filiberti/drawing-watercolor/au-cafe-de-l-60arrive-et-du-depart'
 'https://www.artprice.com/marketplace/762336/andre-fau/drawing-watercolor/la-crique'
 'https://www.artprice.com/marketplace/762324/jean-villeri/drawing-watercolor/ouverture-sur-le-balcon-et-le-jardin'
 'https://www.artprice.com/marketplace/18066/leopold-survage/drawing-watercolor/allegories-a-la-danse'
 'https://www.artprice.com/marketplace/637644/henry-moret/drawing-watercolor/cotes-rocheuse-en-bretagne'
 'https://www.artprice.com/marketplace/1486599/andre-marchand/drawing-watercolor/portrait-de-jean-giono'
 'https://www.artprice.com/marketplace/1486551/marcel-prunier/drawing-watercolor/danseuse-a-l-27accordeon'
 'https://www.artprice.com/marketplace/1486518/andre-deslignieres/drawing-watercolor/roses'
 'https://www.artprice.com/marketplace/1486452/yves-brayer/drawing-watercolor/portrait-de-jean-giono'
 'https://www.artprice.com/marketplace/1485549/mariette-lydis/drawing-watercolor/dessin-erotique-crayon-gouache-signe-handsigned-drawing'
 'https://www.artprice.com/marketplace/1485546/mariette-lydis/drawing-watercolor/dessin-erotique-au-crayon-signe-handsigned-pencil-drawing'
 'https://www.artprice.com/marketplace/1485543/mariette-lydis/drawing-watercolor/dessin-au-crayon-signe-handsigned-pencil-drawing'
 'https://www.artprice.com/marketplace/1485630/bernard-taurelle/drawing-watercolor/portrait-imaginaire-dream-face'
 'https://www.artprice.com/marketplace/1485612/bernard-taurelle/drawing-watercolor/nu-allonge'
 'https://www.artprice.com/marketplace/1485240/ilya-kabakov/drawing-watercolor/22abc-22-sketch-illustration-of-the-book-22abc-22'
 'https://www.artprice.com/marketplace/1485237/ilya-kabakov/drawing-watercolor/22abc-22-sketch-illustration-of-the-book-22abc-22'
 'https://www.artprice.com/marketplace/1485225/ilya-kabakov/drawing-watercolor/masters-made-sketch-illustration-magazine-22murzilka-27'
 'https://www.artprice.com/marketplace/1485216/ilya-kabakov/drawing-watercolor/27masters-made-sketch-illustration-2c-magazine-22murzilka-27-2c-e2-84-963'
 'https://www.artprice.com/marketplace/1422555/manoel-kantor/drawing-watercolor/fishermen'
 'https://www.artprice.com/marketplace/1381467/anna-ticho/drawing-watercolor/landscape-around-jerusalem'
 'https://www.artprice.com/marketplace/685174/henrihs-vorkals/drawing-watercolor/reading-makes-a-country-great'
 'https://www.artprice.com/marketplace/1318368/frantisek-kupka/drawing-watercolor/femme-nue'
 'https://www.artprice.com/marketplace/1013371/frantisek-kupka/drawing-watercolor/etude-de-femme'
 'https://www.artprice.com/marketplace/590583/hans-reichel/drawing-watercolor/compo-1935'
 'https://www.artprice.com/marketplace/70593/tony-gonnet/drawing-watercolor/profil'
 'https://www.artprice.com/marketplace/1340820/leon-augustin-lhermitte/drawing-watercolor/farmer'
 'https://www.artprice.com/marketplace/583356/alfred-east/drawing-watercolor/rural-landscape'
 'https://www.artprice.com/marketplace/1339773/max-poosch-von/drawing-watercolor/illustration-for-22travel-and-adventure-in-many-lands-22'
 'https://www.artprice.com/marketplace/1339416/tony-soulie/drawing-watercolor/technique-mixte-papier-1987-signe-handsigned-mixed-technic'
 'https://www.artprice.com/marketplace/1339107/john-patrick-downie/drawing-watercolor/the-morning-breeze-22-firth-of-clyde'
 'https://www.artprice.com/marketplace/737939/gerard-passet/drawing-watercolor/la-village'
 'https://www.artprice.com/marketplace/737940/gerard-passet/drawing-watercolor/compagne'
 'https://www.artprice.com/marketplace/737604/chaim-gross/drawing-watercolor/2amodels-pencil-and-watercolor'
 'https://www.artprice.com/marketplace/737147/erte/drawing-watercolor/2athe-last-scene-2c-22song-22-and-the-last-scene-22song-22-2c-blue-lady'
 'https://www.artprice.com/marketplace/737152/tully-filmus/drawing-watercolor/2astudying'
 'https://www.artprice.com/marketplace/1295223/cesar-legaspi/drawing-watercolor/nu'
 'https://www.artprice.com/marketplace/1237894/nikolai-semenovich-samokish/drawing-watercolor/the-carriage'
 'https://www.artprice.com/marketplace/1237847/diego-rivera/drawing-watercolor/dibujo-2314'
 'https://www.artprice.com/marketplace/1237839/robert-rafaelovich-falk/drawing-watercolor/double-sided-study-of-a-seated-nude'
 'https://www.artprice.com/marketplace/1108596/leon-bakst/drawing-watercolor/costume-design-of-a-young-beothian-in-27narcisse-27'
 'https://www.artprice.com/marketplace/1237663/george-fikry-ibrahim/drawing-watercolor/untitled'
 'https://www.artprice.com/marketplace/1237413/jean-pierre-alaux/drawing-watercolor/dessin-crayon-aquarelle-encre-signe-handsigned-drawing'
 'https://www.artprice.com/marketplace/1237410/catherine-keun/drawing-watercolor/dessin-crayon-fusain-pastel-signe-crayon-handsigned-drawing'
 'https://www.artprice.com/marketplace/591412/charles-emile-jacque/drawing-watercolor/la-bergere'
 'https://www.artprice.com/marketplace/1013345/frantisek-kupka/drawing-watercolor/etudes-1916-1918'
 'https://www.artprice.com/marketplace/1235965/jacob-gildor/drawing-watercolor/faces'
 'https://www.artprice.com/marketplace/1235813/jean-carzou/drawing-watercolor/dessin-au-crayon-1979-signe-main-handsigned-pencil-drawing'
 'https://www.artprice.com/marketplace/1220807/frantisek-kupka/drawing-watercolor/fete-champetre-au-parc-de-st-cloud'
 'https://www.artprice.com/marketplace/1235482/henri-grenier/drawing-watercolor/paris-2c-animee-scene'
 'https://www.artprice.com/marketplace/1234936/jules-joseph-meynier/drawing-watercolor/etude-de-buste-de-femme-drapee-a-l-27antique'
 'https://www.artprice.com/marketplace/1234935/jules-joseph-meynier/drawing-watercolor/etude-de-femme-drapee-a-l-27antique-portant-un-plat'
 'https://www.artprice.com/marketplace/1212594/marcel-janco/drawing-watercolor/figures-on-the-beach'
 'https://www.artprice.com/marketplace/1212515/jacob-gildor/drawing-watercolor/couple-homage-to-tremois'
 'https://www.artprice.com/marketplace/1212512/jacob-gildor/drawing-watercolor/boy-with-panther'
 'https://www.artprice.com/marketplace/1094872/georges-braque/drawing-watercolor/mythological-figure'
 'https://www.artprice.com/marketplace/1211381/ben-silbert/drawing-watercolor/paysage-marin-avec-un-voilier-longeant-la-cote'
 'https://www.artprice.com/marketplace/1211087/henry-bing/drawing-watercolor/aquarelle-signee-handsigned-watercolor-drawing'
 'https://www.artprice.com/marketplace/1210935/heinrich-leitner/drawing-watercolor/schiffe-im-winterlichen-hafen'
 'https://www.artprice.com/marketplace/1210076/marcel-janco/drawing-watercolor/two-women'
 'https://www.artprice.com/marketplace/1210036/chana-orloff/drawing-watercolor/mother-holding-her-child'
 'https://www.artprice.com/marketplace/591237/marcelle-delphine-cahn/drawing-watercolor/composition'
 'https://www.artprice.com/marketplace/1209657/edgar-stoebel/drawing-watercolor/dessin-au-pastel-feutre-signe-signed-pastel-drawing'
 'https://www.artprice.com/marketplace/1209656/edgar-stoebel/drawing-watercolor/encre-gouache-aquarelle-signe-ink-watercolor-drawing'
 'https://www.artprice.com/marketplace/1173039/edouard-jacquenoud/drawing-watercolor/composition-abstraite'
 'https://www.artprice.com/marketplace/1173030/gerard-lauzier/drawing-watercolor/soldats-2c-souvenez-vous-que-du-haut-de-ces-pyramides'
 'https://www.artprice.com/marketplace/1173029/jean-baptiste-pichot/drawing-watercolor/paysage-anime-au-moulin'
 'https://www.artprice.com/marketplace/1173027/hubert-clerget/drawing-watercolor/vue-de-boulogne-sur-mer'
 'https://www.artprice.com/marketplace/1173024/jean-mayodon/drawing-watercolor/vue-du-chateau-d-27hellenvilliers-dans-l-27eure-28normandie-29'
 'https://www.artprice.com/marketplace/1173023/lucien-boulier/drawing-watercolor/portrait-de-petite-fille-28nina-29'
 'https://www.artprice.com/marketplace/1173020/jean-humbert/drawing-watercolor/champs-a-reze'
 'https://www.artprice.com/marketplace/1173007/georges-francois/drawing-watercolor/femmes-africaines'
 'https://www.artprice.com/marketplace/1173006/lucien-madrassi/drawing-watercolor/portrait-d-27enfant-du-ghetto'
 'https://www.artprice.com/marketplace/1173004/odon-tull/drawing-watercolor/avocette-elegante-28recurvirostra-avosetta-29'
 'https://www.artprice.com/marketplace/1173001/jean-nicol/drawing-watercolor/vue-animee-de-la-plage-a-tregastel'
 'https://www.artprice.com/marketplace/1172997/abel-bertram/drawing-watercolor/nu-de-dos'
 'https://www.artprice.com/marketplace/1172996/theophile-alexandre-steinlen/drawing-watercolor/portrait-de-femme-de-profil'
 'https://www.artprice.com/marketplace/1172995/theophile-alexandre-steinlen/drawing-watercolor/nus-allonges'
 'https://www.artprice.com/marketplace/1172994/theophile-alexandre-steinlen/drawing-watercolor/portrait-presume-d-27oscar-wilde'
 'https://www.artprice.com/marketplace/1172983/gaston-louis-marchal/drawing-watercolor/monstre'
 'https://www.artprice.com/marketplace/1172643/theophile-narcisse-chauvel/drawing-watercolor/hameau'
 'https://www.artprice.com/marketplace/1172737/lucien-madrassi/drawing-watercolor/portrait-de-jeune-fille'
 'https://www.artprice.com/marketplace/1170354/gerard-morot-sir/drawing-watercolor/untitled'
 'https://www.artprice.com/marketplace/1170353/joel-blanc/drawing-watercolor/longchamp'
 'https://www.artprice.com/marketplace/1169965/charles-constantine-hoffbauer/drawing-watercolor/alpine-scene'
 'https://www.artprice.com/marketplace/1169133/joseph-zaritsky/drawing-watercolor/flowers-on-the-window-sill'
 'https://www.artprice.com/marketplace/655528/maurice-henry/drawing-watercolor/emmures-vivants-2c-1960'
 'https://www.artprice.com/marketplace/1164823/jean-baptiste-valadie/drawing-watercolor/clementine'
 'https://www.artprice.com/marketplace/1018309/andre-derain/drawing-watercolor/sitting-nude'
 'https://www.artprice.com/marketplace/1160455/gerhard-buhler/drawing-watercolor/kilchli-vo-walkringen-kanton-bern'
 'https://www.artprice.com/marketplace/1156914/francois-louis-fritz-niederhausern-de/drawing-watercolor/eiger-monch-et-jungfrau'
 'https://www.artprice.com/marketplace/1156913/eric-menetrier/drawing-watercolor/sur-les-quais-a-paris'
 "https://www.artprice.com/marketplace/78838/louis-caillaud-d'angers/drawing-watercolor/aldeas-bleus-et-roses"
 'https://www.artprice.com/marketplace/1106583/nathalie-gontcharova/drawing-watercolor/water-lilies'
 'https://www.artprice.com/marketplace/1126160/arthur-vladimirovich-fonvisin/drawing-watercolor/portrait-of-ballerina-maja-plisetskaia'
 'https://www.artprice.com/marketplace/1126115/alexandre-fasini/drawing-watercolor/cubistic-still-life'
 'https://www.artprice.com/marketplace/1125910/erte/drawing-watercolor/costume-for-22athena-22'
 'https://www.artprice.com/marketplace/1017981/lucien-coutaud/drawing-watercolor/fin-d-27apres-midi-2c1975'
 'https://www.artprice.com/marketplace/1124378/alexandre-boregianoff/drawing-watercolor/autumn-landscape'
 'https://www.artprice.com/marketplace/1123790/jean-rene-bazaine/drawing-watercolor/sans-titre-1963'
 'https://www.artprice.com/marketplace/1123079/olga-della-vos-kardovskaya/drawing-watercolor/lady-in-the-park'
 'https://www.artprice.com/marketplace/1077467/fernand-leduc/drawing-watercolor/graphique-g7'
 'https://www.artprice.com/marketplace/1077396/michel-adlen/drawing-watercolor/portrait-of-a-woman'
 'https://www.artprice.com/marketplace/1073094/renee-lubarow/drawing-watercolor/soleil-du-matin'
 'https://www.artprice.com/marketplace/1072381/efraim-modzelevich/drawing-watercolor/gray-city'
 'https://www.artprice.com/marketplace/614810/tony-soulie/drawing-watercolor/22amazonie-22'
 'https://www.artprice.com/marketplace/115169/manuel-montero/drawing-watercolor/dark-simonetta'
 'https://www.artprice.com/marketplace/103349/manuel-montero/drawing-watercolor/portrait-de-la-mere-de-saint-augustin'
 'https://www.artprice.com/marketplace/108728/manuel-montero/drawing-watercolor/papesse-ii'
 'https://www.artprice.com/marketplace/105982/manuel-montero/drawing-watercolor/empedocle'
 'https://www.artprice.com/marketplace/1070014/abraham-weinbaum/drawing-watercolor/figuers-in-the-street'
 'https://www.artprice.com/marketplace/728239/zygmunt-szreter-schretter/drawing-watercolor/the-gardener'
 'https://www.artprice.com/marketplace/728237/zygmunt-szreter-schretter/drawing-watercolor/woman-walking-in-hilly-landscape'
 'https://www.artprice.com/marketplace/517312/zygmunt-szreter-schretter/drawing-watercolor/still-life-with-apple-and-flowers'
 'https://www.artprice.com/marketplace/522048/bela-kadar/drawing-watercolor/boy-sitting-in-the-crowd'
 'https://www.artprice.com/marketplace/89156/antal-biro/drawing-watercolor/figures-in-yellow-background'
 'https://www.artprice.com/marketplace/1064924/bernard-morel/drawing-watercolor/modele'
 'https://www.artprice.com/marketplace/284218/gabriel-zendel/drawing-watercolor/pianiste-et-chien-couche'
 'https://www.artprice.com/marketplace/1061885/bertrand-mogniat-duclos/drawing-watercolor/nu-assis'
 'https://www.artprice.com/marketplace/917679/jules-pascin/drawing-watercolor/planche-etude-personnages-28double-face-29'
 'https://www.artprice.com/marketplace/660390/pierre-gastaud/drawing-watercolor/abstraction'
 'https://www.artprice.com/marketplace/1061415/bernard-morel/drawing-watercolor/peintre-et-modele'
 'https://www.artprice.com/marketplace/913395/jules-pascin/drawing-watercolor/22sur-la-plage-de-marseille-22'
 'https://www.artprice.com/marketplace/711731/ivan-kawun/drawing-watercolor/nu-femme'
 'https://www.artprice.com/marketplace/660392/andre-francois-breuillaud/drawing-watercolor/portrait-de-daniele-perre'
 'https://www.artprice.com/marketplace/743928/jean-montchougny/drawing-watercolor/22port-22'
 'https://www.artprice.com/marketplace/1030805/moritz-schwind-von/drawing-watercolor/22blumenstreuende-flora-22'
 'https://www.artprice.com/marketplace/1030847/friedrich-august-kaulbach-von/drawing-watercolor/der-bayerische-ministerprasident-graf-v-podewils-durnitz'
 'https://www.artprice.com/marketplace/188167/henri-paul-pecqueriaux/drawing-watercolor/le-cycliste-de-dieppe'
 'https://www.artprice.com/marketplace/1025864/donato-creti-il-donatino/drawing-watercolor/a-sheet-of-studies-of-female-busts-in-oval'
 'https://www.artprice.com/marketplace/1023743/leonor-fini/drawing-watercolor/the-dance'
 'https://www.artprice.com/marketplace/1023747/emile-othon-friesz/drawing-watercolor/nu-debout-252fstanding-nude'
 'https://www.artprice.com/marketplace/263131/gustave-florot/drawing-watercolor/3-personnages'
 'https://www.artprice.com/marketplace/82928/bernard-morel/drawing-watercolor/dessin-28le-modele-29'
 'https://www.artprice.com/marketplace/813815/pierre-belay-de/drawing-watercolor/le-proces-stavisky'
 'https://www.artprice.com/marketplace/999990/joseph-csaky/drawing-watercolor/2-femmes-courantes'
 'https://www.artprice.com/marketplace/999074/paul-lemagny/drawing-watercolor/le-cedre'
 'https://www.artprice.com/marketplace/999057/paul-lemagny/drawing-watercolor/danse-macabre'
 'https://www.artprice.com/marketplace/999060/paul-lemagny/drawing-watercolor/portrait-de-florent-schmitt-1950'
 'https://www.artprice.com/marketplace/1938100/juan-carlos-virgili/photography/punto-de-luz'
 'https://www.artprice.com/marketplace/1936637/thalie-b-vernet/photography/ecce-homo'
 'https://www.artprice.com/marketplace/1936640/thalie-b-vernet/photography/silentium'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935719/juan-carlos-virgili/photography/punto-de-luz'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1938919/dores-sacquegna/photography/il-libro-della-terra'
 'https://www.artprice.com/marketplace/1937995/paul-snell/photography/intersect-23-201803'
 'https://www.artprice.com/marketplace/1937794/paul-snell/photography/lumina-23-201603'
 'https://www.artprice.com/marketplace/1937791/paul-snell/photography/lumina-23-201601'
 'https://www.artprice.com/marketplace/1937629/elizerman/photography/botanica'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1864393/stephen-wilkes/photography/gramercy-park'
 'https://www.artprice.com/marketplace/1556040/tenesh-webber/photography/crossing-1'
 'https://www.artprice.com/marketplace/1912268/zbigniew-warpechowski/photography/ii-dialogue-with-fish'
 'https://www.artprice.com/marketplace/1912262/zbigniew-warpechowski/photography/champion-of-golgotha'
 'https://www.artprice.com/marketplace/1912259/zbigniew-warpechowski/photography/dialogue-with-death'
 'https://www.artprice.com/marketplace/1912076/vanessa-beecroft/photography/senza-titolo'
 'https://www.artprice.com/marketplace/1901735/thomas-demand/photography/kuchenreibe'
 'https://www.artprice.com/marketplace/1911670/giovanni-plozner/photography/no-title-28cat-n-c2-b0-6291-29'
 'https://www.artprice.com/marketplace/1911664/vincent-laceur/photography/no-title-28cat-n-c2-b0-6265-29'
 'https://www.artprice.com/marketplace/1860940/abbas-gharib/photography/couple-and-snow-white'
 'https://www.artprice.com/marketplace/1860931/abbas-gharib/photography/woman-at-bastioni-in-snow'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935731/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935737/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935695/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935701/juan-carlos-virgili/photography/tela-2c-pintura-2c-papel-3f'
 'https://www.artprice.com/marketplace/1935704/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f'
 'https://www.artprice.com/marketplace/1935728/juan-carlos-virgili/photography/papel-2c-tela-2c-pintura-3f']
1
[]
2
[]
3
[]
4
[]
5
[]
6
[]
7
[]
8
[]
9
[]
10
[]
11
[]
12
[]
13
[]
14
[]
15
[]
16
[<Response [302]>]
17
[]
18
[]
19
[]
20
[]
21
[]
22
[]
23
[]
24
[]
25
[]
26
[]
27
[]
28
[]
29
[]
30
[]
31
[]
32
[]
33
[]
34
[]
35
[]
36
[]
37
[]
38
[]
39
[]
40
[]
41
[]
42
[]
43
[]
44
[]
45
[]
46
[]
47
[]
48
[]
49
[]
50
[]
51
[]
52
[]
53
[]
54
[]
55
[]
56
[]
57
[]
58
[]
59
[]
60
[]
61
[]
62
[]
63
[<Response [302]>]
64
[]
65
[]
66
[]
67
[]
68
[]
69
[]
70
[]
71
[]
72
[]
73
[]
74
[]
75
[]
76
[]
77
[]
78
[]
79
[]
80
[]
81
[]
82
[]
83
[]
84
[<Response [302]>]
85
[<Response [302]>]
86
[<Response [302]>]
87
[<Response [302]>]
88
[<Response [302]>]
89
[<Response [302]>]
90
[]
91
[]
92
[]
93
[]
94
[]
95
[]
96
[]
97
[]
98
[]
99
[]
100
[<Response [302]>]
101
[]
102
[]
103
[]
104
[]
105
[]
106
[]
107
[]
108
[]
109
[]
110
[]
111
[]
112
[<Response [302]>]
113
[]
114
[]
115
[]
116
[]
117
[]
118
[]
119
[]
120
[]
121
[]
122
[]
123
[<Response [302]>]
124
[<Response [302]>]
125
[]
126
[]
127
[]
128
[]
129
[]
130
[]
131
[]
132
[]
133
[]
134
[]
135
[]
136
[]
137
[]
138
[<Response [302]>]
139
[]
140
[<Response [302]>]
141
[]
142
[]
143
[]
144
[]
145
[]
146
[]
147
[]
148
[]
149
[]
150
[]
151
[]
152
[]
153
[]
154
[]
155
[]
156
[]
157
[]
158
[<Response [302]>]
159
[]
160
[]
161
[]
162
[<Response [302]>]
163
[<Response [302]>]
164
[<Response [302]>]
165
[]
166
[<Response [302]>]
167
[]
168
[]
169
[]
170
[]
171
[]
172
[]
173
[]
174
[]
175
[]
176
[]
177
[]
178
[]
179
[]
180
[]
181
[]
182
[]
183
[]
184
[]
185
[]
186
[]
187
[]
188
[]
189
[]
190
[]
191
[]
192
[]
193
[]
194
[]
195
[<Response [302]>]
196
[<Response [302]>]
197
[]
198
[]
199
[]
200
[]
201
[]
202
[]
203
[]
204
[<Response [302]>]
205
[]
206
[]
207
[]
208
[]
209
[]
210
[<Response [302]>]
211
[]
212
[]
213
[<Response [302]>]
214
[<Response [302]>]
215
[<Response [302]>]
216
[]
217
[]
218
[]
219
[]
220
[]
221
[]
222
[]
223
[]
224
[]
225
[]
226
[<Response [302]>]
227
[<Response [302]>]
228
[]
229
[]
230
[]
231
[]
232
[<Response [302]>]
233
[]
234
[]
235
[<Response [302]>]
236
[]
237
[]
238
[]
239
[]
240
[<Response [302]>]
241
[<Response [302]>]
242
[<Response [302]>]
243
[<Response [302]>]
244
[<Response [302]>]
245
[<Response [302]>]
246
[<Response [302]>]
247
[<Response [302]>]
248
[<Response [302]>]
249
[<Response [302]>]
250
[<Response [302]>]
251
[<Response [302]>]
252
[<Response [302]>]
253
[<Response [302]>]
254
[<Response [302]>]
255
[<Response [302]>]
256
[<Response [302]>]
257
[<Response [302]>]
258
[]
259
[]
260
[]
261
[]
262
[]
263
[]
264
[]
265
[]
266
[]
267
[]
268
[]
269
[]
270
[]
271
[]
272
[]
273
[]
274
[]
275
[]
276
[]
277
[]
278
[]
279
[]
280
[<Response [302]>]
281
[]
282
[]
283
[]
284
[]
285
[]
286
[]
287
[]
288
[]
289
[]
290
[]
291
[]
292
[]
293
[]
294
[]
295
[]
296
[]
297
[]
298
[]
299
[<Response [302]>]
300
[]
301
[]
302
[]
303
[]
304
[]
305
[]
306
[]
307
[]
308
[]
309
[]
310
[]
311
[]
312
[]
313
[]
314
[]
315
[<Response [301]>]
316
[<Response [302]>]
317
[<Response [302]>]
318
[<Response [301]>]
319
[<Response [301]>]
320
[<Response [301]>]
321
[<Response [301]>]
322
[<Response [301]>]
323
[<Response [301]>]
324
[<Response [301]>]
325
[<Response [301]>]
326
[<Response [301]>]
327
[<Response [301]>]
328
[<Response [301]>]
329
[<Response [301]>]
330
[<Response [301]>]
331
[]
332
[]
333
[]
334
[]
335
[]
336
[<Response [301]>]
337
[<Response [301]>]
338
[<Response [301]>]
339
[<Response [301]>]
340
[<Response [301]>]
341
[<Response [301]>]
342
[<Response [301]>]
343
[<Response [301]>]
344
[<Response [301]>]
345
[<Response [301]>]
346
[<Response [301]>]
347
[<Response [301]>]
348
[<Response [301]>]
349
[<Response [301]>]
350
[<Response [301]>]
351
[<Response [301]>]
352
[<Response [301]>]
353
[<Response [301]>]
354
[<Response [301]>]
355
[<Response [301]>]
356
[<Response [301]>]
357
[<Response [301]>]
358
[<Response [301]>]
359
[<Response [301]>]
360
[<Response [301]>]
361
[<Response [301]>]
362
[<Response [301]>]
363
[<Response [301]>]
364
[<Response [301]>]
365
[<Response [301]>]
366
[<Response [301]>]
367
[<Response [301]>]
368
[<Response [301]>]
369
[<Response [301]>]
370
[<Response [301]>]
371
[<Response [301]>]
372
[<Response [301]>]
373
[<Response [301]>]
374
[<Response [301]>]
375
[<Response [301]>]
376
[<Response [301]>]
377
[<Response [301]>]
378
[<Response [301]>]
379
[<Response [301]>]
380
[<Response [301]>]
381
[<Response [301]>]
382
[<Response [301]>]
383
[<Response [301]>]
384
[<Response [301]>]
385
[<Response [301]>]
386
[<Response [301]>]
387
[<Response [301]>]
388
[<Response [301]>]
389
[<Response [301]>]
390
[<Response [301]>]
391
[<Response [301]>]
392
[<Response [301]>]
393
[<Response [301]>]
394
[<Response [301]>]
395
[<Response [301]>]
396
[<Response [302]>]
397
[]
398
[]
399
[]
400
[]
401
[]
402
[<Response [302]>]
403
[<Response [302]>]
404
[]
405
[<Response [302]>]
406
[<Response [302]>]
407
[<Response [301]>]
408
[<Response [301]>]
409
[<Response [301]>]
410
[<Response [301]>]
411
[<Response [301]>]
412
[<Response [301]>]
413
[<Response [301]>]
414
[<Response [301]>]
415
[<Response [301]>]
416
[<Response [301]>]
417
[<Response [301]>]
418
[<Response [301]>]
419
[<Response [301]>]
420
[<Response [301]>]
421
[<Response [301]>]
422
[<Response [301]>]
423
[<Response [301]>]
424
[<Response [301]>]
425
[<Response [301]>]
426
[<Response [301]>]
427
[<Response [301]>]
428
[<Response [301]>]
429
[<Response [301]>]
430
[<Response [301]>]
431
[<Response [301]>]
432
[<Response [301]>]
433
[<Response [301]>]
434
[<Response [301]>]
435
[<Response [301]>]
436
[<Response [301]>]
437
[<Response [301]>]
438
[<Response [301]>]
439
[<Response [301]>]
440
[<Response [301]>]
441
[<Response [301]>]
442
[<Response [301]>]
443
[<Response [301]>]
444
[<Response [301]>]
445
[<Response [301]>]
446
[<Response [301]>]
447
[<Response [301]>]
448
[<Response [301]>]
449
[<Response [301]>]
450
[<Response [301]>]
451
[<Response [301]>]
452
[<Response [301]>]
453
[<Response [301]>]
454
[<Response [301]>]
455
[<Response [301]>]
456
[<Response [301]>]
457
[<Response [301]>]
458
[<Response [301]>]
459
[<Response [301]>]
460
[<Response [301]>]
461
[<Response [301]>]
462
[<Response [301]>]
463
[<Response [301]>]
464
[<Response [301]>]
465
[<Response [301]>]
466
[<Response [301]>]
467
[<Response [301]>]
468
[<Response [301]>]
469
[<Response [301]>]
470
[<Response [301]>]
471
[<Response [301]>]
472
[<Response [301]>]
473
[<Response [301]>]
474
[<Response [301]>]
475
[<Response [301]>]
476
[<Response [301]>]
477
[<Response [301]>]
478
[<Response [301]>]
479
[<Response [301]>]
480
[<Response [301]>]
481
[<Response [301]>]
482
[<Response [301]>]
483
[<Response [301]>]
484
[<Response [301]>]
485
[<Response [301]>]
486
[<Response [301]>]
487
[<Response [301]>]
488
[<Response [301]>]
489
[<Response [301]>]
490
[<Response [301]>]
491
[<Response [301]>]
492
[<Response [301]>]
493
[<Response [301]>]
494
[<Response [301]>]
495
[<Response [301]>]
496
[<Response [301]>]
497
[<Response [301]>]
498
[<Response [301]>]
499
[<Response [301]>]
500
[<Response [301]>]
Joys-MacBook-Pro:Desktop JoyCowper$ Req = response.get('https://www.artprice.com')
-bash: syntax error near unexpected token `('
Joys-MacBook-Pro:Desktop JoyCowper$ python
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> Req = requests.get('https://www.artprice.com')
>>> Req
<Response [200]>
>>> Req.content
b'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" class="no-js" lang="en">\n<head>\n  <title>Art market, auction sales and artist\xe2\x80\x99s prices and indices - Artprice, the world leader of art market information.</title>\n  \n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<meta name="google-site-verification" content="uhQqRWH6T1tU_Gx_kpWWpAdqwa9TsZAyE58dKMCuirA">\n<meta http-equiv="pragma" content="private">\n<meta name="verify-v1" content="CBcAVemUjvx1B/FZMX9yV/Nlkp0zDvCF0HTwLVWwtA0=">\n<meta name="language" content="en-EN"/>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="baidu-site-verification" content="XGvsphXFPW"/>\n    <link rel="alternate" href="https://fr.artprice.com/" hreflang="fr"/>\n    <link rel="alternate" href="https://it.artprice.com/" hreflang="it"/>\n    <link rel="alternate" href="https://es.artprice.com/" hreflang="es"/>\n    <link rel="alternate" href="https://zh.artprice.com/" hreflang="zh"/>\n    <link rel="alternate" href="https://www.artprice.com/" hreflang="en"/>\n    <link rel="alternate" href="https://de.artprice.com/" hreflang="de"/>\n<LINK rel="schema.DC" href="http://purl.org/dc/elements/1.1/">\n    <link rel="canonical" href="https://www.artprice.com">\n          <meta name="DESCRIPTION" content="Artprice is the world leader of art market information. Artprice.com covers 30 million prices and indices for 700,000 artists, 6,300 auction houses and 126 millions artworks.">\n          <meta name="ROBOTS" content="INDEX, FOLLOW">\n          <meta name="AUTHOR" content="Thierry EHRMANN">\n\n  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />\n  <link rel="stylesheet" media="all" href="/packs/css/vendors-1d263983.chunk.css" />\n<link rel="stylesheet" media="all" href="/packs/css/bs-b531878d.chunk.css" />\n<link rel="stylesheet" media="all" href="/packs/css/react-f0bbfbfe.chunk.css" />\n\n  <script>\n    if (window && !window.Intl) {\n      document.write("<script src=\\"https://cdn.polyfill.io/v2/polyfill.min.js?features=Intl.~locale.en\\"><\\/script>");\n    }\n  </script>\n  <script src="/packs/js/runtime-154e4e9ee3ce8426d5b8.js"></script>\n<script src="/packs/js/vendors-96802b7d8bce65147bdf.chunk.js"></script>\n<script src="/packs/js/locales_en-be7ad52a972e76bb098b.chunk.js"></script>\n<script src="/packs/js/default-88c43ce3a8394ac3a6a2.chunk.js"></script>\n<script src="/packs/js/bs-d6621e1a5d3d27d420c6.chunk.js"></script>\n<script src="/packs/js/react-e51c6c5df6ce822c72ec.chunk.js"></script>\n\n    <script type="application/ld+json">\n    { \n       "@context": "http://schema.org",\n       "@type": "WebSite",\n       "url": "http://www.artprice.com/",\n       "potentialAction": {\n         "@type": "SearchAction",\n         "target": "http://www.artprice.com/artists/search?search={search_term_string}",\n         "query-input": "required name=search_term_string"\n       }\n    }\n  </script>\n\n    <script type="text/javascript">\n      (function(i, s, o, g, r, a, m) {\n        i[\'GoogleAnalyticsObject\'] = r;\n        i[r] = i[r] || function() {\n          (i[r].q = i[r].q || []).push(arguments)\n        }, i[r].l = 1 * new Date();\n        a = s.createElement(o),\n            m = s.getElementsByTagName(o)[0];\n        a.async = 1;\n        a.src = g;\n        m.parentNode.insertBefore(a, m)\n      })(window, document, \'script\', \'//www.google-analytics.com/analytics.js\', \'aa\');\n  \n      window.ga_trackers = [];\n        window.ga_trackers.push({ id: \'UA-8821659-2\', tracker: \'\', host: \'artprice.com\' });\n        window.ga_trackers.push({ id: \'UA-8821659-4\', tracker: \'tracker_en\', host: \'www.artprice.com\' });\n  \n        aa(\'create\', \'UA-8821659-2\', \'artprice.com\');\n    \n    \n          aa(\'send\', \'pageview\'\n              , {\n                \'page\': \'%2Fhome\',\n                \'title\': \'home\',\n                dimension1: \'prospect\',\n                dimension2: \'\',\n                dimension3: \'\',\n              }\n          );         \n        \n          aa(\'require\', \'GTM-5K8ZCX7\');\n    \n        aa(\'create\', \'UA-8821659-4\', \'www.artprice.com\', {\'name\': \'tracker_en\'});\n    \n    \n          aa(\'tracker_en.send\', \'pageview\'\n              , {\n                \'page\': \'%2Fhome\',\n                \'title\': \'home\',\n                dimension1: \'prospect\',\n                dimension2: \'\',\n                dimension3: \'\',\n              }\n          );         \n        \n          aa(\'require\', \'GTM-5K8ZCX7\');\n    \n    </script>\n\n  <style>\n    @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {\n      .body-container {\n        height: 100%;\n      }\n    }\n  </style>\n  <script type="text/javascript">window.geoIp = \'GB\'</script>\n</head>\n<body ng-app="artprice_app" ng-controller="ApplicationCtrl">\n  <noscript>\n  <div class="javascript_warning">\n    <div>\n      For full functionality of this site it is necessary to enable JavaScript. Here are the <a href=\'http://www.enable-javascript.com/\' target=\'_blank\'> instructions how to enable JavaScript in your web browser</a>.\n    </div>\n  </div>\n</noscript>\n\n  <div class="javascript_warning" class="ng-cloak" ng-show="!navigator.cookieEnabled" ng-cloak>\n    <div>\n      You must have cookies enabled to use this website.\n    </div>\n  </div>\n\n<div class="body-container">\n    <div class="body-header">\n      <div>\n  <div class="container" ng-cloak>\n    <artp-layouts-header\n      hidden-menu="false"\n      id-accountrole="1"\n      id-customertype="0"\n      />\n  </div>\n\n  <div class="header-no-js" ng-cloak ng-if="false">\n    <ul>\n      <li>\n        Auction databases\n        <ul>\n          <li>\n            <a href="/search">Search</a>\n          </li>\n          <li>\n            <a href="/artists/directory">Artist index</a>\n          </li>\n          <li>\n            <a href="/sales/futures">Upcoming auctions</a>\n          </li>\n          <li>\n            <a href="/artmarketinsight/reports#archives">Artprice Archives</a>\n          </li>\n        </ul>\n      </li>\n      <li>\n        Marketplace\n        <ul>\n          <li>\n            <a href="/marketplace">Ads/Auctions</a>\n          </li>\n          <li>\n            <a href="/marketplace/sell-an-artwork">Sell an artwork</a>\n          </li>\n          <li>\n            <a href="/subscription/store">Pricing</a>\n          </li>\n          <li>\n            <a href="/marketplace/ads-instructions-for-use">Auctions instructions for use</a>\n          </li>\n          <li>\n            <a target="pdf" href="/html/en/mode_emploi_store.pdf">Artprice Store instructions for use</a>\n          </li>\n        </ul>\n      </li>\n      <li>\n        Market news\n        <ul>\n          <li>\n            <a href="/artmarketinsight">ArtMarketInsight articles</a>\n          </li>\n          <li>\n            <a href="/artmarketinsight/reports">The reports</a>\n          </li>\n          <li>\n            <a href="/eventweb/past">Events</a>\n          </li>\n          <li>\n            <a href="/events/">Fairs</a>\n          </li>\n        </ul>\n      </li>\n      <li>\n        Services\n        <ul>\n          <li>\n            <a href="/subscription">Subscriptions</a>\n          </li>\n          <li>\n            <a href="/estimate">Estimate</a>\n          </li>\n          <li>\n            <a href="/subscription/store">Artprice Store</a>\n          </li>\n          <li>\n            <a href="/indexes/artinvestment">Econometric data</a>\n          </li>\n          <li>\n            <a href="/webapp#!/shop/list">Books</a>\n          </li>\n        </ul>\n      </li>\n    </ul>\n  </div>\n</div>\n\n    </div>\n    <div class="hidden-xs promote-sign-in-banner" onclick="window.location=\'/newcomer\';aa(\'send\', \'event\', \'top_banner\', \'newcomer\', \'/home/index\');">\n      <div class="container">\n          <div class="new-comer">\n            Sign up! Stay in the loop with free email updates on your favorite artists.\n          </div>\n      </div>\n    </div>\n  <div class="font font-14 site-content" >\n    <div class="container">\n      \n      \n\n\n      \n    </div>\n    \n    \n\n<div class="home ng-cloak" ng-controller="AilCtrl">\n\n  <div class="container">\n    <h1 class="text-center">\n      The Art Market\'s prices and images \n    </h1>\n    <div class="row">\n      <div class="col-xs-12 font font-16 pad pad-l-20">\n        <div ng-controller="ArtistSearchCtrl" ng-init="setKeywordPlaceholder(false);customerNoArtists=true" ng-cloak>\n  <script type="text/ng-template" id="artist_small.html">\n    <a class="no-pointer" ng-if="match.model.noHighlight" ng-bind-html="match.label"></a>\n    <a ng-if="!match.model.noHighlight" ng-bind-html="match.label | uibTypeaheadHighlight:query"></a>\n  </script>\n  <div id="artist_search" class="search-bar-artist hidden-print" ng-class="{\'expanded\': expanded}">\n    <div class="search-txt" ng-class="{\'full-width\': customerNoArtists || expanded}">\n      <form class="marg marg-b-0 pad pad-t-10" ng-submit="submitSearch($event)" action="/artists/search">\n        <label class="label-for-keyword animate-show-hide" ng-show="expanded">\n          Search artists and artworks\n        </label>\n        <div class="input-group">\n          <input name="keyword"\n                 value="{{keyword}}"\n                 id="sln_searchbar"\n                 ng-click="expanded=true"\n                 autocomplete="off"\n                 class="form-control"\n                 ng-model="keyword"\n                 typeahead-template-url="artist_small.html"\n                 typeahead-focus-first="false"\n                 typeahead-on-select="selectArtist($model)"\n                 typeahead-min-length="2"\n                 ng-model-options="{ debounce: 150 }"\n                 uib-typeahead="artist as artist.html for artist in perform_artist_search($viewValue, \'All records\')"\n                 placeholder="Search"\n          >\n          <span class="input-group-btn">          \n                <button class="btn btn-primary" id="sln_searchbar_commit" ng-disabled="!keyword">\n                  <span ng-hide="artistSelected"><i class="fa fa-search"></i></span>\n                  <span ng-show="artistSelected"><i class="fa fa-spinner fa-spin"></i></span>\n                </button>\n              </span>\n        </div>\n      </form>\n    </div>\n  </div>\n</div>\n\n        You can also view the <a href="/artists/all/A" ng-click="send_aa_event_now(\'artist_search_bar\', \'artist_directory\')">complete index</a> of the 714,330 artists listed by Artprice.com\n\n          <div class="row">\n            <div class="col-xs-12">\n              <h2>\n                Discover Artprice&copy; in Video\n              </h2>\n            </div>\n            <div class="col-xs-12">\n              <div class="container-video">\n    <iframe class="video" src="https://www.youtube.com/embed/Id_9iN-2gGA?rel=0&amp;controls=1&amp;showinfo=0" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>\n</div>\n\n            </div>\n          </div>\n      </div>\n    </div>\n    \n  </div>\n\n  <div class="container">\n    <div class="row">\n        <div class="col-xs-12 col-sm-6 col-md-4">\n    <div class="row">\n      <div class="col-xs-12">\n        <h2> Auction highlight</h2>\n      </div>\n    </div>\n    <div class="row">\n        <div class="ail-auction marg marg-t-20 col-xs-12">\n          <div class="col-xs-12" ng-init="viewAil(24801, 6)">\n            <div class="col-xs-6">\n              <img class="pointer img-responsive" src="https://imgprivate2.artprice.com/get/ail/5323/6c6d/71ca/2de1/650c/165f/d41d/8377/ad8a/3bda/140/170/ail-1561639166.jpeg" ng-click="clickAil(24801, 6, \'/sale/305844/paintings%2C+prints+and+sculpture\')">\n            </div>\n            <div class="col-xs-6" style="height: 170px;">\n              <strong>\n                Mainichi Auction Inc.\n              </strong>\n              <br>\n              <strong>\n                Paintings,...\n              </strong>\n              <br>\n              13 Jul 2019\n              <br>\n              <br>\n              Tokyo\n              <br>\n              Japan\n            </div>\n          </div>\n          <div class="pull-right links marg marg-t-20">\n            <h2>\n              <small>\n                <div class="pointer marg marg-t-10" ng-click="clickAil(24801, 6, \'/sale/305844/paintings%2C+prints+and+sculpture\')">\n                  <span class="badge"><i class="fa fa-chevron-right"></i></span>  View this sale\'s lots\n                </div>\n              </small>\n            </h2>\n          </div>\n        </div>\n    </div>\n  </div>\n\n      \n      <div data-react-class="HomePage/Events" data-react-props="{&quot;locals&quot;:{&quot;lang&quot;:&quot;en&quot;,&quot;key&quot;:&quot;10&quot;}}" data-hydrate="t"><div class="col-xs-12 col-sm-6 col-md-8"><div class="col-sm-12"><h2>Fairs</h2></div><div class="homepage-events marg marg-t-0 marg-b-0 col-sm-12"><div class="homepage-exposition-block col-xs-12 col-sm-6 col-md-4 col-lg-3"><a href="/events/8000/ARTESANTANDER/"><div class="card"><div class="justify-content-center marg marg-b-15"><img src="//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-168x140.gif" alt="Event Thumbnail" class="event-thumbnail card-img-top"/></div><div class="card-body"><div class="card-title"><h1 class="marg marg-t-0 marg-b-0 font font-28 text-center"><small>ARTESANTANDER</small></h1></div></div></div></a></div><div class="homepage-exposition-block col-xs-12 col-sm-6 col-md-4 col-lg-3"><a href="/events/8057/Art-Marbella/"><div class="card"><div class="justify-content-center marg marg-b-15"><img src="//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-168x140.jpg" alt="Event Thumbnail" class="event-thumbnail card-img-top"/></div><div class="card-body"><div class="card-title"><h1 class="marg marg-t-0 marg-b-0 font font-28 text-center"><small>Art Marbella</small></h1></div></div></div></a></div></div><div class="col-sm-12"><div class="pull-right links"><h2 class="marg marg-t-0 pad pad-t-0"><small><a href="/events/" class="pointer"><span class="badge marg marg-r-5"><i class="fa fa-chevron-right"></i></span>See all</a></small></h2></div></div></div></div>\n    </div>\n  </div>\n\n  <div class="container">\n      <div class="row">\n        <div class="col-xs-12">\n          <h2>Summer Bonus</h2>\n        </div>\n      </div>\n      <div class="row">\n        <div class="col-xs-12">\n          <a href="/subscription/payable">\n            <img class="center-block img-responsive visible-xs-block" src="https://imgprivate2.artprice.com/get/promo/2dd0/eacf/f1f5/d26f/2261/d54b/2ea1/896f/31cc/0ae1/400/133/artprice-img-1560523837.jpeg" alt="Artprice img 1560523837" />\n            <img class="center-block visible-sm-block" src="https://imgprivate2.artprice.com/get/promo/eff2/805f/ac10/a844/6a1c/8c8b/adb2/8410/fcb0/bd6d/720/133/artprice-img-1560523842.jpeg" alt="Artprice img 1560523842" />\n            <img class="center-block visible-md-block" src="https://imgprivate2.artprice.com/get/promo/065b/7aea/fc36/1646/8991/abea/de50/2760/c680/9cf4/940/133/artprice-img-1560523857.jpeg" alt="Artprice img 1560523857" />\n            <img class="center-block visible-lg-block" src="https://imgprivate2.artprice.com/get/promo/5b78/1a76/9386/2eda/4d89/8c8d/ffd5/33a3/61e5/af66/1100/133/artprice-img-1560523861.jpeg" alt="Artprice img 1560523861" />\n          </a>\n        </div>\n      </div>\n\n      <div class="row ">\n        <div class="col-xs-12">\n          <h2 class="custom">\n            Artprice\'s Latest Report\n          </h2>\n        </div>\n        <div class="col-xs-12 main-report">\n          <a href="/artprice-reports/the-art-market-in-2018">\n            <img alt="The art market in 2018" src="//imgpublic.artprice.com/img/wp/sites/113/2019/03/Bandeaux_web_rama2018_EN.jpg">\n          </a>\n          <div class="row">\n            <div class="col-xs-12">\n              <h2 style="border-bottom: none;float: right;margin: 0;">\n                <small>\n                  <a ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'reports\')" href="/artmarketinsight/reports" class="marg marg-l-20"><span class="badge"><i class="fa fa-chevron-right"></i></span> The Art Market Reports by Artprice.com\n                  </a>\n                </small>\n              </h2>\n            </div>\n          </div>\n        </div>\n      </div>\n\n    <div class="row">\n      <div class="col-xs-12  ">\n        \n\n<div class="row">\n  <div class="col-xs-12">\n    <h2>\n      On the Marketplace\n    </h2>\n  </div>\n</div>\n\n<div class="row marketplace">\n  <div class="col-xs-12">\n    <div class="classifieds-homepage">\n        <a href="/marketplace/1943123/aurelie-nemours/drawing-watercolor/e8-22re-rom-82-22">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/7076/2806/aee6/b4db/23bf/f4fd/ff8b/fcf5/b7be/235a/300/300/Aurelie-NEMOURS-E8--Re-Rom-82--1552897576.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1689643/tony-soulie/painting/hong-kong-238-28from-hong-kong-series-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/66ec/ad0e/ff0b/8fc4/bb72/4337/5e6c/f991/f83e/23d9/300/300/Tony-SOULIE-Hong-Kong--8---from-Hong-Kong-series--1505937911.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1955165/bengt-lindstrom/painting/tetti-di-parigi">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/f40d/b087/ac84/bd08/abbe/3342/59a7/ee52/75ac/69fa/300/300/Bengt-LINDSTROM-tetti-di-Parigi-1555503481.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1980817/jean-fautrier/painting/femme-assise-dans-un-cafe">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/920b/e263/d2d6/8e8d/8085/de2d/5ed7/79dd/539f/2a13/300/300/Jean-FAUTRIER-Femme-assise-dans-un-cafe-1561382422.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1824484/felix-labisse/painting/essas">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/6760/902b/c62a/3a30/7f5d/d817/f8b0/731d/5403/5b93/300/300/Felix-LABISSE-Essas-1527946623.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1656205/mr-brainwash/print-multiple/metro-polisa">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/0bd8/231d/8b43/023a/c172/44d5/d164/122a/e641/5d5f/300/300/MR-BRAINWASH-Metro-Polisa-1501076332.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1808969/tony-soulie/painting/dreamed-flower-xi">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/38e7/afa7/900e/c861/f20b/7e7f/ebcf/48fb/a384/d7eb/300/300/Tony-SOULIE-Dreamed-Flower-XI-------------------1524676748.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1873441/pierre-bonnard/sculpture-volume/baigneuse-assise-devant-un-rocher">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/730b/3a2a/13be/5bcf/e46e/195a/ee99/c35b/59e1/7260/300/300/Pierre-BONNARD-Baigneuse-assise-devant-un-rocher-1538644223.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1678039/mark-di-suvero/drawing-watercolor/untitled-28drawing-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/682c/626f/fd28/80f6/cc83/7030/6201/f760/124f/e349/300/300/DI-SUVERO-Mark-Untitled--drawing--1535142030.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1575558/patrick-cornillet/drawing-watercolor/sans-titre">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/7a48/34b6/4153/5685/a3df/455b/a0db/0411/991f/0583/300/300/Patrick-CORNILLET-Sans-titre--1490349617.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1669429/mimmo-paladino/sculpture-volume/acrobata-28sculpture-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/3983/d7c9/8b05/2a87/7ace/ea9f/3559/e752/75ee/0f22/300/300/Mimmo-PALADINO-Acrobata--sculpture----------------1535494143.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1825604/moise-kisling/painting/mimosas">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/13fb/3745/88b6/cf18/1824/57c1/816e/379f/bfce/2e06/300/300/Moise-KISLING-Mimosas-1554978075.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1721179/mark-di-suvero/print-multiple/magnetic-borealis">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/b1d4/dec4/dd7f/ad5e/9a20/10c0/218c/a8d4/79f7/6c7c/300/300/DI-SUVERO-Mark-Magnetic-Borealis--1535139145.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/733217/aurelie-nemours/painting/polychromie-28triptyque-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/fe4a/7e5e/8daf/a0a9/6b37/491e/6b86/4897/f395/25e0/300/300/Aurelie-NEMOURS-Polychromie--triptyque--1538125642.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1033048/salvador-dali/sculpture-volume/christ-of-st-john-of-the-cross-28cristo-de-san-juan-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/9b1e/a388/312f/f7e3/e5b7/4fdc/fa0e/00c6/121a/5931/300/300/Salvador-DALI-Christ-of-St--John-of-the-Cross--Cri-1535481574.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/576677/edward-cucuel/painting/dame-mit-kleid-2c-impressionist-2c-lady-with-dress">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/423e/cbc3/2c2a/fe6a/cd29/24ff/e461/5271/c41a/de49/300/300/Edward-CUCUEL-Dame-mit-Kleid--Impressionist---lady-1267519606.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1645765/philippe-pasqua/painting/stella">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/8969/14ef/57bb/956a/4c21/4afe/d4fb/7923/7059/a3fc/300/300/Philippe-PASQUA-Stella-1499626403.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1664803/tony-soulie/painting/untitled-san-francisco-28bridge-29">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/8eaf/a30c/ab31/6f0d/a02c/3351/c63f/a664/a102/7d34/300/300/Tony-SOULIE-Untitled---San-Francisco--bridge-----1535492144.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1955150/auguste-herbin/painting/chene-liege-a-vaison-la-romaine">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/68a7/95d3/293c/2816/2919/0a79/8355/37b2/bf38/3ecf/300/300/Auguste-HERBIN-Chene-liege-a-Vaison-la-Romaine-1555502221.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n        <a href="/marketplace/1738482/joan-miro/print-multiple/joan-miro-and-catalonia-7c-joan-miro-und-katalonien">\n          <img class="shadow" src="https://imgprivate2.artprice.com/get/classifieds/ea57/c774/4d17/94f0/5a02/32ca/da87/c5b7/380b/e6f4/300/300/Joan-MIRO-Joan-Miro-and-Catalonia---Joan-Miro-und--1513098750.jpg" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'picture\')">\n        </a>\n    </div>\n  </div>\n</div>\n\n<div class="pull-right links">\n  <h2>\n    <small>\n      <a href="/marketplace" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'list\')"><span class="badge"><i class="fa fa-chevron-right"></i></span>\n        Access the Marketplace</a>\n      <a href="/estimate" class="marg marg-l-20" ng-click="send_aa_event_now(\'click_home_page\', \'marketplace\', \'estimate\')"><span class="badge"><i class="fa fa-chevron-right"></i></span>\n        Submit an artwork for pricing</a>\n    </small>\n  </h2>\n</div>\n\n\n\n      </div>\n      \n    </div>\n      <div class="stores row">\n    <div class="col-xs-12">\n      <h2>\n        Artprice Stores\n      </h2>\n    </div>\n    <div class="col-xs-12">\n      <div data-react-class="marketplace/stores/Top" data-react-props="{&quot;displayH2&quot;:false}" data-hydrate="t"><div class="marketplace-stores-top"><div class="list"><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Villa-del-Arte-Galleries"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/00dd/1a43/b361/a6ba/b820/247b/4c57/8179/6a4e/500/500/e53d-1539942108.jpg" alt="Villa del Arte Galleries"/></a></div><div class="store-link"><a href="/store/Villa-del-Arte-Galleries">Villa del Arte Galleries</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/MA-GALERIE---Samuel-Le-Paire"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/a38c/7592/1f65/e632/5796/6a30/5086/1a7d/b26d/500/500/d61a-0.jpg" alt="MA GALERIE - Samuel Le Paire"/></a></div><div class="store-link"><a href="/store/MA-GALERIE---Samuel-Le-Paire">MA GALERIE - Samuel Le Paire</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Galerie-Bertrand-Gillig"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/9127/a413/c12e/f4dc/7f53/ee34/01b9/8ed1/69f9/500/500/939d-1528814509.jpg" alt="Galerie Bertrand Gillig"/></a></div><div class="store-link"><a href="/store/Galerie-Bertrand-Gillig">Galerie Bertrand Gillig</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/MODERN-ART-COLLECTION-SA"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/0950/1682/05ff/cbf7/ab4e/689d/444f/319b/32a6/500/500/d4ae-1555083694.jpg" alt="MODERN ART COLLECTION SA"/></a></div><div class="store-link"><a href="/store/MODERN-ART-COLLECTION-SA">MODERN ART COLLECTION SA</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Galerie-Kellermann"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/3316/84bd/6cd1/76d1/48a7/b8a5/fa3c/1adc/67a3/500/500/629a-1526556250.jpg" alt="Galerie Kellermann"/></a></div><div class="store-link"><a href="/store/Galerie-Kellermann">Galerie Kellermann</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/BEL-AIR-FINE-ART"><img class="shadow" src="https://imgprivate2.artprice.com//get/store/82da/b47b/fac8/5c30/b240/65e0/ac4d/c0e0/6c12/500/500/b6b8-1509709511.jpg" alt="BEL-AIR FINE ART"/></a></div><div class="store-link"><a href="/store/BEL-AIR-FINE-ART">BEL-AIR FINE ART</a></div></div></div></div></div></div>\n    </div>\n    <div class="col-xs-12 links text-right">\n      <h2>\n        <small>\n          <a href="/marketplace/store" ng-click="send_aa_event_now(\'click_home_page\', \'events\', \'see_all\')"><span class="badge"><i class="fa fa-chevron-right"></i></span>\n            See all</a>\n        </small>\n      </h2>\n    </div>\n  </div>\n\n    <div class="row">\n      <div class="col-xs-12 ">\n        <h2>\n  ArtMarket&reg; Insight - what\'s trending on the art market\n</h2>\n\n<div class="row artmarketinsight pad pad-l-15">\n      <div class="col-xs-12 col-lg-4 article">\n        <a class=\'font font-18\' ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'article\')" href="/artmarketinsight/artprice-com-is-changing-its-name-to-artmarket-com-to-become-a-global-player-in-the-art-market" title="Artprice.com is changing its name to Artmarket.com to become a global player in the Art Market">\n          Artprice.com is changing its name to Artmarket.com to become a global player in the Art Market\n          \n        </a>\n        <small>\n          (10 Jul 2019)\n        </small>\n      </div>\n      <div class="col-xs-12 col-lg-4 article">\n        <a class=\'font font-18\' ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'article\')" href="/artmarketinsight/francis-bacon-at-the-pompidou-centre-the-big-autumn-event-in-paris" title="Francis Bacon at the Pompidou Centre: the big autumn event in Paris">\n          Francis Bacon at the Pompidou Centre: the big autumn event in Paris\n          \n        </a>\n        <small>\n          (09 Jul 2019)\n        </small>\n      </div>\n      <div class="col-xs-12 col-lg-4 article">\n        <a class=\'font font-18\' ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'article\')" href="/artmarketinsight/flash-news-wols-the-mysterious-at-sothebys-cindy-sherman-in-london" title="Flash News: Wols \xe2\x80\x9cthe mysterious\xe2\x80\x9d at Sotheby\xe2\x80\x99s &#8211; Cindy Sherman in London">\n          Flash News: Wols \xe2\x80\x9cthe mysterious\xe2\x80\x9d at Sotheby\xe2\x80\x99s &#8211; Cindy Sherman in London\n          \n        </a>\n        <small>\n          (05 Jul 2019)\n        </small>\n      </div>\n</div>\n\n<div class="row">\n  <div class="col-xs-12">\n    <h2 style="border-bottom: none;float: right;margin: 0;">\n      <small>\n        <a id="sln_ami" ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'all\')" href="/artmarketinsight"><span class="badge"><i class="fa fa-chevron-right"></i></span>  Go to all the articles\n        </a>\n        <a ng-click="send_aa_event_now(\'click_home_page\', \'artmarketinsight\', \'reports\')" href="/artmarketinsight/reports" class="marg marg-l-20"><span class="badge"><i class="fa fa-chevron-right"></i></span> The Art Market Reports by Artprice.com\n        </a>\n      </small>\n    </h2>\n  </div>\n</div>\n\n      </div>\n    </div>\n\n  </div>\n</div>\n\n\n    \n  </div>\n  <footer class="bottom-bar">\n  <div class="container">\n      <div class="wechat-qr-code hidden" ng-show="weChatQRCode" ng-click="toggleWeChatQRCode()" ng-cloak>\n        <img src="https://imgpublic.artprice.com/img/wechat-artprice.png" alt="Wechat artprice" />\n      </div>\n      <div class="col-sm-3 col-xs-12">\n        <ul>\n          <li>\n            <div class="row marg marg-b-10">\n              <div class="col-xs-12">\n                <div class="social-network twitter">\n                  <a href="https://twitter.com/artpricedotcom?lang=en" onclick="javascript:aa(\'send\', \'event\', \'footer\', \'about_us\', \'twitter\');" target="_blank" rel="publisher">\n                    <i class="fa fa-lg fa-twitter"></i>\n                  </a>\n                </div>\n                <div class="social-network facebook">\n                  <a href="http://www.facebook.com/artpricedotcom" target="facebook" onclick="javascript:aa(\'send\', \'event\', \'footer\', \'about_us\', \'facebook\');">\n                    <i class="fa fa-lg fa-facebook" aria-hidden="true"></i>\n                  </a>\n                </div>\n              </div>\n            </div>\n          </li>\n          <li>\n            <a onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;footer&#39;, &#39;about_us&#39;, &#39;video&#39;);" class="invisiblelink" title="*ENGLISH VERSION: ARTPRICE OR THE REVOLUTION OF THE ART MARKET* " alt="ARTPRICE VIDEO : *ENGLISH VERSION: ARTPRICE OR THE REVOLUTION OF THE ART MARKET* " href="/videos/artprice">Discover Artprice&copy; in Video</a>\n          </li>\n            <li>\n              <a ng-click="send_aa_event_now(&#39;footer&#39;, &#39;usefull_links&#39;, &#39;jobs&#39;);" href="/editorial/artprice-is-hiring">Careers</a>\n            </li>\n          <li>\n            <a ng-click="send_aa_event_now(&#39;footer&#39;, &#39;about_us&#39;, &#39;artprice_presentation&#39;);" href="//imgpublic.artprice.com/img/wp/sites/11/2018/03/FactSheet_EN.pdf">Artprice presentation</a>\n          </li>\n        </ul>\n      </div>\n      <div class="col-sm-5 col-xs-12 col2">\n        <ul>\n          <li>\n            <a onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;footer&#39;, &#39;contact_us&#39;, &#39;phone&#39;);" href="/contact">FAQ</a>\n          </li>\n          <li>\n              <a target="amci" borser="0" onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;top_banner&#39;, &#39;amci&#39;, &#39;confidenceindex.png&#39;);" href="/amci">Artmarket Confidence Index by Artprice</a>\n                <a class="amciup" href="#" onclick="javascript:aa(\'send\', \'event\', \'top_banner\', \'amci\', \'amcivariance\');window.parent.location=\'https://www.artprice.com/amci\';">\n                  <img src="https://imgpublic.artprice.com/img/amciup.gif" alt="Amciup" />\n                  31.30\n                </a>\n          </li>\n          <li>\n            <a onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;footer&#39;, &#39;contact_us&#39;, &#39;auctioneers&#39;);" href="/auctioneer">Auction House Partner program</a>\n          </li>\n          <li>\n            <a onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;footer&#39;, &#39;contact_us&#39;, &#39;ail&#39;);" href="/ail">Advertising</a>\n          </li>\n        </ul>\n      </div>\n      <div class="col-sm-4 col-xs-12">\n        <ul>\n          <li>\n            <a href="http://serveur.serveur.com/Press_Release/pressreleaseen.htm" target=_blank onclick="javascript:aa(\'send\', \'event\', \'footer\', \'about_us\', \'press_release\');">Press Releases</a>\n          </li>\n          <li>\n            <a target="pdf" ng-click="send_aa_event_now(&#39;footer&#39;, &#39;usefull_links&#39;, &#39;ddc_opus_ix&#39;);" href="http://blog.ehrmann.org/pdf/demeureduchaos-abodeofchaos-opus-IX-2013.pdf">Abode of Chaos Opus IX</a>\n          </li>\n          <li>\n            <a target="inerpol" ng-click="send_aa_event_now(&#39;footer&#39;, &#39;usefull_links&#39;, &#39;interpol&#39;);" href="https://www.interpol.int/en/Crimes/Cultural-heritage-crime/Stolen-Works-of-Art-Database">INTERPOL\'s database on Stolen Works of Art</a>\n          </li>\n        </ul>\n      </div>\n    <div class="col-xs-12">\n      <div class="layout-bottom-copy ">\n\n  <a href="/">Artprice</a>\n  is listed on Eurolist by\n    <a target=\'euronext\' href="https://www.euronext.com/en/products/equities/FR0000074783-XPAR">Euronext Paris (Euroclear: 7478 - Bloomberg: PRC - Reuters: ARTF) </a>\n  - A company of\n  <a href="http://www.serveur.com">Groupe serveur</a>\n  <br>\n\n\n    <a ng-click="open_cgv();send_aa_event(\'footer\', \'bottom\', \'cgv_path\');" href="#"> Terms and conditions of use and sale </a>\n\n  -\n  <a target="pdf" href="https://imgpublic.artprice.com/pdf/retract_en.pdf">Withdrawal process</a>\n  -\n  <a data-toggle="modal" data-target="#base-modal" href="/block/privacypolicy?modal=true">Confidentiality and personal data protection charter</a>\n  -\n  <a data-toggle="modal" data-target="#base-modal" href="/block/copyright?modal=true">Copyright</a>\n\n  by \n  <a href="/">artprice.com</a>\n\n  &copy; <a target=_blank href=\'http://blog.ehrmann.org/\'>Thierry Ehrmann 1987-2019</a> All rights reserved </span>\n</div>\n\n    </div>\n  </div>\n</footer>\n\n</div>\n\n<!-- Need this for react drawers (see react portals) /> -->\n<div id="drawer-root"></div>\n\n<div class="modal fade" id="base-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n  <div class="modal-dialog modal-lg">\n    <div class="modal-content"></div>\n  </div>\n</div>\n<div class="modal fade" id="login_modal" tabindex="-1" role="dialog" aria-hidden="true" ng-controller=\'CustomerLoginCtrl\' ng-init="initialize_login_input()">\n  <form id="login_form" ng-submit="login_submit($event)" force-blur-before-submit="" action="/login/login?layout=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" />\n    <div class="modal-dialog">\n      <div class="modal-content">\n        <div class="modal-header">\n          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n          <h4 class="modal-title">Log in</h4>\n        </div>\n        <div class="modal-body" id="modal-login-body">\n          <div class="form-group">\n            <label for="login">Username</label>\n            <input type="text" ng-focus="error=null" ng-model="login" id="login" name="login" required class="form-control sln_login" placeholder="youremail@email.com"/>\n          </div>\n          <div class="form-group">\n            <label for="pass">Password</label>\n            <div class="input-group">\n              <input type="{{inputTypeModal}}" autocomplete="off" ng-model="pass" ng-focus="error=null" id="pass" name="pass" required class="form-control sln_pass" placeholder="Password"/>\n              <span class="input-group-btn">\n                <button ng-init="inputTypeModal = \'password\'" title="Display password" class="btn btn-default" type="button" ng-class="{\'active\': inputTypeModal == \'text\'}" ng-click="inputTypeModal = inputTypeModal == \'text\' ? \'password\' : \'text\'">\n                  <i title="Hide password" class="fa fa-eye" ng-if="inputTypeModal == \'text\'"></i>\n                  <i title="Show password" class=" fa fa-eye-slash" ng-if="inputTypeModal != \'text\'"></i>\n                </button>\n              </span>\n            </div>\n          </div>\n          <div class="alert alert-warning alert-dismissable" ng-show="error">\n            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\n            <strong>Note</strong> {{ error }}\n          </div>\n        </div>\n        <div class="modal-footer">\n          <div class="pull-left" style="text-align:left ;font-size:12px">\n            <a onclick="javascript:aa(&#39;send&#39;, &#39;event&#39;, &#39;login&#39;, &#39;cooked&#39;, &#39;forgot_password&#39;);" href="/account/forgot_password">Forgot your username and/or password?</a>\n              <br/>\n              <a href="/newcomer">Free express sign up</a>\n          </div>\n          <input type="submit" name="commit" value="Submit" class="btn btn-primary sln_post_login" />\n          <button class="btn btn-default" data-dismiss="modal" aria-hidden="true">Close</button>\n        </div>\n      </div>\n    </div>\n</form></div>\n\n  <div ng-controller="CookiesConsentController as $ctrl">\n    <div id="cookies_banner" ng-hide="$ctrl.hideCookieWarning" class="hidden-print">\n      By using this website, you accept the use of cookies for better analysis and relevance.\n      For more information, \n      <a data-toggle="modal" data-target="#base-modal" href="/block/privacypolicy?modal=true">Confidentiality and personal data protection charter</a>\n      <a id="sln_hcw" href="javascript:void(0)" ng-click="$ctrl.acceptCookies()" class="linkbutton btn btn-xs btn-primary" title="Click on OK to ignore this comment">OK</a>\n    </div>\n    <div style="height:30px" ng-hide="$ctrl.hideCookieWarning"></div>\n  </div>\n\n\n  <script>\n    window.__PRELOADED_STATE__ = {"events":{"store":{"loading":false,"data":{"8000":{"id":8000,"title":"ARTESANTANDER","dt_event_start":"2019-07-12T23:00:00.000+01:00","dt_event_expire":"2019-07-16T23:00:00.000+01:00","slug":"artesantander","idcountry":469},"8057":{"id":8057,"title":"Art Marbella","dt_event_start":"2019-07-29T23:00:00.000+01:00","dt_event_expire":"2019-08-02T23:00:00.000+01:00","slug":"art-marbella","idcountry":469},"8087":{"id":8087,"title":"Art International Z\xc3\xbcrich","dt_event_start":"2019-09-25T23:00:00.000+01:00","dt_event_expire":"2019-09-28T23:00:00.000+01:00","slug":"art-international-zurich-2019","idcountry":476},"8129":{"id":8129,"title":"ART FORMOSA","dt_event_start":"2019-08-21T23:00:00.000+01:00","dt_event_expire":"2019-08-24T23:00:00.000+01:00","slug":"art-formosa","idcountry":478}}},"events/HOME_PAGE":{"country#all&from#unset&to#unset":{"ids":[8000,8057,8129,8087],"loading":false}},"countries":{"469":{"loading":false,"data":{"fr":"ESPAGNE","en":"SPAIN","es":"ESPA\xc3\x91A","it":"SPAGNA","de":"Spanien","zh":"\xe8\xa5\xbf\xe7\x8f\xad\xe7\x89\x99"}},"476":{"loading":false,"data":{"fr":"SUISSE","en":"SWITZERLAND","es":"SUIZA","it":"SVIZZERA","de":"Schweiz","zh":"\xe7\x91\x9e\xe5\xa3\xab"}},"478":{"loading":false,"data":{"fr":"TA\xc3\x8fWAN","en":"TAIWAN","es":"TAIW\xc3\x81N","it":"TAIWAN","de":"Taiwan","zh":"\xe5\x8f\xb0\xe6\xb9\xbe"}}},"medias":{"437":{"loading":false,"data":{"id":437,"date":"2019-06-04T15:46:01.000+02:00","mime_type":"image/gif","media_type":"image","name":"180-x-150-px.gif","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px.gif","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-150x150.gif","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-168x140.gif","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-120x150.gif","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px.gif","height":150,"width":180}}}},"920":{"loading":false,"data":{"id":920,"date":"2019-06-20T08:55:09.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"52725434_2061848314108026_6870054731188797440_n-1.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-120x150.jpg","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1.jpg","height":150,"width":180}}}},"947":{"loading":false,"data":{"id":947,"date":"2019-06-20T09:45:13.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"Banner180x150.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-120x150.jpg","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150.jpg","height":150,"width":180}}}},"1898":{"loading":false,"data":{"id":1898,"date":"2019-07-03T12:57:34.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"Art-international-Z\xc3\xbcrich-Logo-180-x-150.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Z\xc3\xbcrich-Logo-180-x-150.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Z\xc3\xbcrich-Logo-180-x-150-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Z\xc3\xbcrich-Logo-180-x-150-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Z\xc3\xbcrich-Logo-180-x-150-120x157.jpg","height":157,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Z\xc3\xbcrich-Logo-180-x-150.jpg","height":157,"width":180}}}},"bySlug":{"artesantander":{"loading":false,"idmedia":437},"art-marbella":{"loading":false,"idmedia":947},"art-formosa":{"loading":false,"idmedia":920},"art-international-zurich-2019":{"loading":false,"idmedia":1898}}}},"indexes":{},"userContext":{"name":"","logged":false},"preferences":{"dimension":"cm","currency":"gbp","lang":"en","marketplaceItemsPerPage":1},"marketplace":{"searchbars":{"search":{"totalCount":0,"initialTotalCount":0,"loadingFacets":false,"facetsPathname":""}},"stores":{"top":{"loading":false,"result":[{"id":30787,"sitename":"Villa del Arte Galleries","url":"/store/Villa-del-Arte-Galleries","imageUrl":"https://imgprivate2.artprice.com//get/store/00dd/1a43/b361/a6ba/b820/247b/4c57/8179/6a4e/500/500/e53d-1539942108.jpg"},{"id":17492,"sitename":"MA GALERIE - Samuel Le Paire","url":"/store/MA-GALERIE---Samuel-Le-Paire","imageUrl":"https://imgprivate2.artprice.com//get/store/a38c/7592/1f65/e632/5796/6a30/5086/1a7d/b26d/500/500/d61a-0.jpg"},{"id":19323,"sitename":"Galerie Bertrand Gillig","url":"/store/Galerie-Bertrand-Gillig","imageUrl":"https://imgprivate2.artprice.com//get/store/9127/a413/c12e/f4dc/7f53/ee34/01b9/8ed1/69f9/500/500/939d-1528814509.jpg"},{"id":53,"sitename":"MODERN ART COLLECTION SA","url":"/store/MODERN-ART-COLLECTION-SA","imageUrl":"https://imgprivate2.artprice.com//get/store/0950/1682/05ff/cbf7/ab4e/689d/444f/319b/32a6/500/500/d4ae-1555083694.jpg"},{"id":29852,"sitename":"Galerie Kellermann","url":"/store/Galerie-Kellermann","imageUrl":"https://imgprivate2.artprice.com//get/store/3316/84bd/6cd1/76d1/48a7/b8a5/fa3c/1adc/67a3/500/500/629a-1526556250.jpg"},{"id":26069,"sitename":"BEL-AIR FINE ART","url":"/store/BEL-AIR-FINE-ART","imageUrl":"https://imgprivate2.artprice.com//get/store/82da/b47b/fac8/5c30/b240/65e0/ac4d/c0e0/6c12/500/500/b6b8-1509709511.jpg"}]}}},"ui":{}};\n  </script>\n\n</body>\n</html>\n\n\n'
>>> in Req.content:
  File "<stdin>", line 1
    in Req.content:
     ^
SyntaxError: invalid syntax
>>> find in Req.content
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'find' is not defined
>>> Req.response
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Response' object has no attribute 'response'
>>> Req.response()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Response' object has no attribute 'response'
>>> import bs4
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(Req.content)
/Users/JoyCowper/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <stdin>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

  markup_type=markup_type))
>>> soup = BeautifulSoup(Req.content, "lxml")
>>> soup
<!DOCTYPE html>
<html class="no-js" lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Art market, auction sales and artist’s prices and indices - Artprice, the world leader of art market information.</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="uhQqRWH6T1tU_Gx_kpWWpAdqwa9TsZAyE58dKMCuirA" name="google-site-verification"/>
<meta content="private" http-equiv="pragma"/>
<meta content="CBcAVemUjvx1B/FZMX9yV/Nlkp0zDvCF0HTwLVWwtA0=" name="verify-v1"/>
<meta content="en-EN" name="language"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<meta content="XGvsphXFPW" name="baidu-site-verification"/>
<link href="https://fr.artprice.com/" hreflang="fr" rel="alternate"/>
<link href="https://it.artprice.com/" hreflang="it" rel="alternate"/>
<link href="https://es.artprice.com/" hreflang="es" rel="alternate"/>
<link href="https://zh.artprice.com/" hreflang="zh" rel="alternate"/>
<link href="https://www.artprice.com/" hreflang="en" rel="alternate"/>
<link href="https://de.artprice.com/" hreflang="de" rel="alternate"/>
<link href="http://purl.org/dc/elements/1.1/" rel="schema.DC"/>
<link href="https://www.artprice.com" rel="canonical"/>
<meta content="Artprice is the world leader of art market information. Artprice.com covers 30 million prices and indices for 700,000 artists, 6,300 auction houses and 126 millions artworks." name="DESCRIPTION"/>
<meta content="INDEX, FOLLOW" name="ROBOTS"/>
<meta content="Thierry EHRMANN" name="AUTHOR"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon"/>
<link href="/packs/css/vendors-1d263983.chunk.css" media="all" rel="stylesheet"/>
<link href="/packs/css/bs-b531878d.chunk.css" media="all" rel="stylesheet"/>
<link href="/packs/css/react-f0bbfbfe.chunk.css" media="all" rel="stylesheet"/>
<script>
    if (window && !window.Intl) {
      document.write("<script src=\"https://cdn.polyfill.io/v2/polyfill.min.js?features=Intl.~locale.en\"><\/script>");
    }
  </script>
<script src="/packs/js/runtime-154e4e9ee3ce8426d5b8.js"></script>
<script src="/packs/js/vendors-96802b7d8bce65147bdf.chunk.js"></script>
<script src="/packs/js/locales_en-be7ad52a972e76bb098b.chunk.js"></script>
<script src="/packs/js/default-88c43ce3a8394ac3a6a2.chunk.js"></script>
<script src="/packs/js/bs-d6621e1a5d3d27d420c6.chunk.js"></script>
<script src="/packs/js/react-e51c6c5df6ce822c72ec.chunk.js"></script>
<script type="application/ld+json">
    {
       "@context": "http://schema.org",
       "@type": "WebSite",
       "url": "http://www.artprice.com/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "http://www.artprice.com/artists/search?search={search_term_string}",
         "query-input": "required name=search_term_string"
       }
    }
  </script>
<script type="text/javascript">
      (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
          (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
      })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'aa');

      window.ga_trackers = [];
        window.ga_trackers.push({ id: 'UA-8821659-2', tracker: '', host: 'artprice.com' });
        window.ga_trackers.push({ id: 'UA-8821659-4', tracker: 'tracker_en', host: 'www.artprice.com' });

        aa('create', 'UA-8821659-2', 'artprice.com');


          aa('send', 'pageview'
              , {
                'page': '%2Fhome',
                'title': 'home',
                dimension1: 'prospect',
                dimension2: '',
                dimension3: '',
              }
          );

          aa('require', 'GTM-5K8ZCX7');

        aa('create', 'UA-8821659-4', 'www.artprice.com', {'name': 'tracker_en'});


          aa('tracker_en.send', 'pageview'
              , {
                'page': '%2Fhome',
                'title': 'home',
                dimension1: 'prospect',
                dimension2: '',
                dimension3: '',
              }
          );

          aa('require', 'GTM-5K8ZCX7');

    </script>
<style>
    @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
      .body-container {
        height: 100%;
      }
    }
  </style>
<script type="text/javascript">window.geoIp = 'GB'</script>
</head>
<body ng-app="artprice_app" ng-controller="ApplicationCtrl">
<noscript>
<div class="javascript_warning">
<div>
      For full functionality of this site it is necessary to enable JavaScript. Here are the <a href="http://www.enable-javascript.com/" target="_blank"> instructions how to enable JavaScript in your web browser</a>.
    </div>
</div>
</noscript>
<div class="javascript_warning" ng-cloak="" ng-show="!navigator.cookieEnabled">
<div>
      You must have cookies enabled to use this website.
    </div>
</div>
<div class="body-container">
<div class="body-header">
<div>
<div class="container" ng-cloak="">
<artp-layouts-header hidden-menu="false" id-accountrole="1" id-customertype="0"></artp-layouts-header>
</div>
<div class="header-no-js" ng-cloak="" ng-if="false">
<ul>
<li>
        Auction databases
        <ul>
<li>
<a href="/search">Search</a>
</li>
<li>
<a href="/artists/directory">Artist index</a>
</li>
<li>
<a href="/sales/futures">Upcoming auctions</a>
</li>
<li>
<a href="/artmarketinsight/reports#archives">Artprice Archives</a>
</li>
</ul>
</li>
<li>
        Marketplace
        <ul>
<li>
<a href="/marketplace">Ads/Auctions</a>
</li>
<li>
<a href="/marketplace/sell-an-artwork">Sell an artwork</a>
</li>
<li>
<a href="/subscription/store">Pricing</a>
</li>
<li>
<a href="/marketplace/ads-instructions-for-use">Auctions instructions for use</a>
</li>
<li>
<a href="/html/en/mode_emploi_store.pdf" target="pdf">Artprice Store instructions for use</a>
</li>
</ul>
</li>
<li>
        Market news
        <ul>
<li>
<a href="/artmarketinsight">ArtMarketInsight articles</a>
</li>
<li>
<a href="/artmarketinsight/reports">The reports</a>
</li>
<li>
<a href="/eventweb/past">Events</a>
</li>
<li>
<a href="/events/">Fairs</a>
</li>
</ul>
</li>
<li>
        Services
        <ul>
<li>
<a href="/subscription">Subscriptions</a>
</li>
<li>
<a href="/estimate">Estimate</a>
</li>
<li>
<a href="/subscription/store">Artprice Store</a>
</li>
<li>
<a href="/indexes/artinvestment">Econometric data</a>
</li>
<li>
<a href="/webapp#!/shop/list">Books</a>
</li>
</ul>
</li>
</ul>
</div>
</div>
</div>
<div class="hidden-xs promote-sign-in-banner" onclick="window.location='/newcomer';aa('send', 'event', 'top_banner', 'newcomer', '/home/index');">
<div class="container">
<div class="new-comer">
            Sign up! Stay in the loop with free email updates on your favorite artists.
          </div>
</div>
</div>
<div class="font font-14 site-content">
<div class="container">
</div>
<div class="home ng-cloak" ng-controller="AilCtrl">
<div class="container">
<h1 class="text-center">
      The Art Market's prices and images
    </h1>
<div class="row">
<div class="col-xs-12 font font-16 pad pad-l-20">
<div ng-cloak="" ng-controller="ArtistSearchCtrl" ng-init="setKeywordPlaceholder(false);customerNoArtists=true">
<script id="artist_small.html" type="text/ng-template">
    <a class="no-pointer" ng-if="match.model.noHighlight" ng-bind-html="match.label"></a>
    <a ng-if="!match.model.noHighlight" ng-bind-html="match.label | uibTypeaheadHighlight:query"></a>
  </script>
<div class="search-bar-artist hidden-print" id="artist_search" ng-class="{'expanded': expanded}">
<div class="search-txt" ng-class="{'full-width': customerNoArtists || expanded}">
<form action="/artists/search" class="marg marg-b-0 pad pad-t-10" ng-submit="submitSearch($event)">
<label class="label-for-keyword animate-show-hide" ng-show="expanded">
          Search artists and artworks
        </label>
<div class="input-group">
<input autocomplete="off" class="form-control" id="sln_searchbar" name="keyword" ng-click="expanded=true" ng-model="keyword" ng-model-options="{ debounce: 150 }" placeholder="Search" typeahead-focus-first="false" typeahead-min-length="2" typeahead-on-select="selectArtist($model)" typeahead-template-url="artist_small.html" uib-typeahead="artist as artist.html for artist in perform_artist_search($viewValue, 'All records')" value="{{keyword}}"/>
<span class="input-group-btn">
<button class="btn btn-primary" id="sln_searchbar_commit" ng-disabled="!keyword">
<span ng-hide="artistSelected"><i class="fa fa-search"></i></span>
<span ng-show="artistSelected"><i class="fa fa-spinner fa-spin"></i></span>
</button>
</span>
</div>
</form>
</div>
</div>
</div>

        You can also view the <a href="/artists/all/A" ng-click="send_aa_event_now('artist_search_bar', 'artist_directory')">complete index</a> of the 714,330 artists listed by Artprice.com

          <div class="row">
<div class="col-xs-12">
<h2>
                Discover Artprice© in Video
              </h2>
</div>
<div class="col-xs-12">
<div class="container-video">
<iframe allow="encrypted-media" allowfullscreen="" class="video" frameborder="0" gesture="media" src="https://www.youtube.com/embed/Id_9iN-2gGA?rel=0&amp;controls=1&amp;showinfo=0"></iframe>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="container">
<div class="row">
<div class="col-xs-12 col-sm-6 col-md-4">
<div class="row">
<div class="col-xs-12">
<h2> Auction highlight</h2>
</div>
</div>
<div class="row">
<div class="ail-auction marg marg-t-20 col-xs-12">
<div class="col-xs-12" ng-init="viewAil(24801, 6)">
<div class="col-xs-6">
<img class="pointer img-responsive" ng-click="clickAil(24801, 6, '/sale/305844/paintings%2C+prints+and+sculpture')" src="https://imgprivate2.artprice.com/get/ail/5323/6c6d/71ca/2de1/650c/165f/d41d/8377/ad8a/3bda/140/170/ail-1561639166.jpeg"/>
</div>
<div class="col-xs-6" style="height: 170px;">
<strong>
                Mainichi Auction Inc.
              </strong>
<br/>
<strong>
                Paintings,...
              </strong>
<br/>
              13 Jul 2019
              <br/>
<br/>
              Tokyo
              <br/>
              Japan
            </div>
</div>
<div class="pull-right links marg marg-t-20">
<h2>
<small>
<div class="pointer marg marg-t-10" ng-click="clickAil(24801, 6, '/sale/305844/paintings%2C+prints+and+sculpture')">
<span class="badge"><i class="fa fa-chevron-right"></i></span>  View this sale's lots
                </div>
</small>
</h2>
</div>
</div>
</div>
</div>
<div data-hydrate="t" data-react-class="HomePage/Events" data-react-props='{"locals":{"lang":"en","key":"10"}}'><div class="col-xs-12 col-sm-6 col-md-8"><div class="col-sm-12"><h2>Fairs</h2></div><div class="homepage-events marg marg-t-0 marg-b-0 col-sm-12"><div class="homepage-exposition-block col-xs-12 col-sm-6 col-md-4 col-lg-3"><a href="/events/8000/ARTESANTANDER/"><div class="card"><div class="justify-content-center marg marg-b-15"><img alt="Event Thumbnail" class="event-thumbnail card-img-top" src="//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-168x140.gif"/></div><div class="card-body"><div class="card-title"><h1 class="marg marg-t-0 marg-b-0 font font-28 text-center"><small>ARTESANTANDER</small></h1></div></div></div></a></div><div class="homepage-exposition-block col-xs-12 col-sm-6 col-md-4 col-lg-3"><a href="/events/8057/Art-Marbella/"><div class="card"><div class="justify-content-center marg marg-b-15"><img alt="Event Thumbnail" class="event-thumbnail card-img-top" src="//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-168x140.jpg"/></div><div class="card-body"><div class="card-title"><h1 class="marg marg-t-0 marg-b-0 font font-28 text-center"><small>Art Marbella</small></h1></div></div></div></a></div></div><div class="col-sm-12"><div class="pull-right links"><h2 class="marg marg-t-0 pad pad-t-0"><small><a class="pointer" href="/events/"><span class="badge marg marg-r-5"><i class="fa fa-chevron-right"></i></span>See all</a></small></h2></div></div></div></div>
</div>
</div>
<div class="container">
<div class="row">
<div class="col-xs-12">
<h2>Summer Bonus</h2>
</div>
</div>
<div class="row">
<div class="col-xs-12">
<a href="/subscription/payable">
<img alt="Artprice img 1560523837" class="center-block img-responsive visible-xs-block" src="https://imgprivate2.artprice.com/get/promo/2dd0/eacf/f1f5/d26f/2261/d54b/2ea1/896f/31cc/0ae1/400/133/artprice-img-1560523837.jpeg"/>
<img alt="Artprice img 1560523842" class="center-block visible-sm-block" src="https://imgprivate2.artprice.com/get/promo/eff2/805f/ac10/a844/6a1c/8c8b/adb2/8410/fcb0/bd6d/720/133/artprice-img-1560523842.jpeg"/>
<img alt="Artprice img 1560523857" class="center-block visible-md-block" src="https://imgprivate2.artprice.com/get/promo/065b/7aea/fc36/1646/8991/abea/de50/2760/c680/9cf4/940/133/artprice-img-1560523857.jpeg"/>
<img alt="Artprice img 1560523861" class="center-block visible-lg-block" src="https://imgprivate2.artprice.com/get/promo/5b78/1a76/9386/2eda/4d89/8c8d/ffd5/33a3/61e5/af66/1100/133/artprice-img-1560523861.jpeg"/>
</a>
</div>
</div>
<div class="row ">
<div class="col-xs-12">
<h2 class="custom">
            Artprice's Latest Report
          </h2>
</div>
<div class="col-xs-12 main-report">
<a href="/artprice-reports/the-art-market-in-2018">
<img alt="The art market in 2018" src="//imgpublic.artprice.com/img/wp/sites/113/2019/03/Bandeaux_web_rama2018_EN.jpg"/>
</a>
<div class="row">
<div class="col-xs-12">
<h2 style="border-bottom: none;float: right;margin: 0;">
<small>
<a class="marg marg-l-20" href="/artmarketinsight/reports" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'reports')"><span class="badge"><i class="fa fa-chevron-right"></i></span> The Art Market Reports by Artprice.com
                  </a>
</small>
</h2>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-xs-12 ">
<div class="row">
<div class="col-xs-12">
<h2>
      On the Marketplace
    </h2>
</div>
</div>
<div class="row marketplace">
<div class="col-xs-12">
<div class="classifieds-homepage">
<a href="/marketplace/1943123/aurelie-nemours/drawing-watercolor/e8-22re-rom-82-22">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/7076/2806/aee6/b4db/23bf/f4fd/ff8b/fcf5/b7be/235a/300/300/Aurelie-NEMOURS-E8--Re-Rom-82--1552897576.jpg"/>
</a>
<a href="/marketplace/1689643/tony-soulie/painting/hong-kong-238-28from-hong-kong-series-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/66ec/ad0e/ff0b/8fc4/bb72/4337/5e6c/f991/f83e/23d9/300/300/Tony-SOULIE-Hong-Kong--8---from-Hong-Kong-series--1505937911.jpg"/>
</a>
<a href="/marketplace/1955165/bengt-lindstrom/painting/tetti-di-parigi">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/f40d/b087/ac84/bd08/abbe/3342/59a7/ee52/75ac/69fa/300/300/Bengt-LINDSTROM-tetti-di-Parigi-1555503481.jpg"/>
</a>
<a href="/marketplace/1980817/jean-fautrier/painting/femme-assise-dans-un-cafe">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/920b/e263/d2d6/8e8d/8085/de2d/5ed7/79dd/539f/2a13/300/300/Jean-FAUTRIER-Femme-assise-dans-un-cafe-1561382422.jpg"/>
</a>
<a href="/marketplace/1824484/felix-labisse/painting/essas">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/6760/902b/c62a/3a30/7f5d/d817/f8b0/731d/5403/5b93/300/300/Felix-LABISSE-Essas-1527946623.jpg"/>
</a>
<a href="/marketplace/1656205/mr-brainwash/print-multiple/metro-polisa">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/0bd8/231d/8b43/023a/c172/44d5/d164/122a/e641/5d5f/300/300/MR-BRAINWASH-Metro-Polisa-1501076332.jpg"/>
</a>
<a href="/marketplace/1808969/tony-soulie/painting/dreamed-flower-xi">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/38e7/afa7/900e/c861/f20b/7e7f/ebcf/48fb/a384/d7eb/300/300/Tony-SOULIE-Dreamed-Flower-XI-------------------1524676748.jpg"/>
</a>
<a href="/marketplace/1873441/pierre-bonnard/sculpture-volume/baigneuse-assise-devant-un-rocher">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/730b/3a2a/13be/5bcf/e46e/195a/ee99/c35b/59e1/7260/300/300/Pierre-BONNARD-Baigneuse-assise-devant-un-rocher-1538644223.jpg"/>
</a>
<a href="/marketplace/1678039/mark-di-suvero/drawing-watercolor/untitled-28drawing-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/682c/626f/fd28/80f6/cc83/7030/6201/f760/124f/e349/300/300/DI-SUVERO-Mark-Untitled--drawing--1535142030.jpg"/>
</a>
<a href="/marketplace/1575558/patrick-cornillet/drawing-watercolor/sans-titre">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/7a48/34b6/4153/5685/a3df/455b/a0db/0411/991f/0583/300/300/Patrick-CORNILLET-Sans-titre--1490349617.jpg"/>
</a>
<a href="/marketplace/1669429/mimmo-paladino/sculpture-volume/acrobata-28sculpture-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/3983/d7c9/8b05/2a87/7ace/ea9f/3559/e752/75ee/0f22/300/300/Mimmo-PALADINO-Acrobata--sculpture----------------1535494143.jpg"/>
</a>
<a href="/marketplace/1825604/moise-kisling/painting/mimosas">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/13fb/3745/88b6/cf18/1824/57c1/816e/379f/bfce/2e06/300/300/Moise-KISLING-Mimosas-1554978075.jpg"/>
</a>
<a href="/marketplace/1721179/mark-di-suvero/print-multiple/magnetic-borealis">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/b1d4/dec4/dd7f/ad5e/9a20/10c0/218c/a8d4/79f7/6c7c/300/300/DI-SUVERO-Mark-Magnetic-Borealis--1535139145.jpg"/>
</a>
<a href="/marketplace/733217/aurelie-nemours/painting/polychromie-28triptyque-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/fe4a/7e5e/8daf/a0a9/6b37/491e/6b86/4897/f395/25e0/300/300/Aurelie-NEMOURS-Polychromie--triptyque--1538125642.jpg"/>
</a>
<a href="/marketplace/1033048/salvador-dali/sculpture-volume/christ-of-st-john-of-the-cross-28cristo-de-san-juan-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/9b1e/a388/312f/f7e3/e5b7/4fdc/fa0e/00c6/121a/5931/300/300/Salvador-DALI-Christ-of-St--John-of-the-Cross--Cri-1535481574.jpg"/>
</a>
<a href="/marketplace/576677/edward-cucuel/painting/dame-mit-kleid-2c-impressionist-2c-lady-with-dress">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/423e/cbc3/2c2a/fe6a/cd29/24ff/e461/5271/c41a/de49/300/300/Edward-CUCUEL-Dame-mit-Kleid--Impressionist---lady-1267519606.jpg"/>
</a>
<a href="/marketplace/1645765/philippe-pasqua/painting/stella">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/8969/14ef/57bb/956a/4c21/4afe/d4fb/7923/7059/a3fc/300/300/Philippe-PASQUA-Stella-1499626403.jpg"/>
</a>
<a href="/marketplace/1664803/tony-soulie/painting/untitled-san-francisco-28bridge-29">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/8eaf/a30c/ab31/6f0d/a02c/3351/c63f/a664/a102/7d34/300/300/Tony-SOULIE-Untitled---San-Francisco--bridge-----1535492144.jpg"/>
</a>
<a href="/marketplace/1955150/auguste-herbin/painting/chene-liege-a-vaison-la-romaine">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/68a7/95d3/293c/2816/2919/0a79/8355/37b2/bf38/3ecf/300/300/Auguste-HERBIN-Chene-liege-a-Vaison-la-Romaine-1555502221.jpg"/>
</a>
<a href="/marketplace/1738482/joan-miro/print-multiple/joan-miro-and-catalonia-7c-joan-miro-und-katalonien">
<img class="shadow" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'picture')" src="https://imgprivate2.artprice.com/get/classifieds/ea57/c774/4d17/94f0/5a02/32ca/da87/c5b7/380b/e6f4/300/300/Joan-MIRO-Joan-Miro-and-Catalonia---Joan-Miro-und--1513098750.jpg"/>
</a>
</div>
</div>
</div>
<div class="pull-right links">
<h2>
<small>
<a href="/marketplace" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'list')"><span class="badge"><i class="fa fa-chevron-right"></i></span>
        Access the Marketplace</a>
<a class="marg marg-l-20" href="/estimate" ng-click="send_aa_event_now('click_home_page', 'marketplace', 'estimate')"><span class="badge"><i class="fa fa-chevron-right"></i></span>
        Submit an artwork for pricing</a>
</small>
</h2>
</div>
</div>
</div>
<div class="stores row">
<div class="col-xs-12">
<h2>
        Artprice Stores
      </h2>
</div>
<div class="col-xs-12">
<div data-hydrate="t" data-react-class="marketplace/stores/Top" data-react-props='{"displayH2":false}'><div class="marketplace-stores-top"><div class="list"><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Villa-del-Arte-Galleries"><img alt="Villa del Arte Galleries" class="shadow" src="https://imgprivate2.artprice.com//get/store/00dd/1a43/b361/a6ba/b820/247b/4c57/8179/6a4e/500/500/e53d-1539942108.jpg"/></a></div><div class="store-link"><a href="/store/Villa-del-Arte-Galleries">Villa del Arte Galleries</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/MA-GALERIE---Samuel-Le-Paire"><img alt="MA GALERIE - Samuel Le Paire" class="shadow" src="https://imgprivate2.artprice.com//get/store/a38c/7592/1f65/e632/5796/6a30/5086/1a7d/b26d/500/500/d61a-0.jpg"/></a></div><div class="store-link"><a href="/store/MA-GALERIE---Samuel-Le-Paire">MA GALERIE - Samuel Le Paire</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Galerie-Bertrand-Gillig"><img alt="Galerie Bertrand Gillig" class="shadow" src="https://imgprivate2.artprice.com//get/store/9127/a413/c12e/f4dc/7f53/ee34/01b9/8ed1/69f9/500/500/939d-1528814509.jpg"/></a></div><div class="store-link"><a href="/store/Galerie-Bertrand-Gillig">Galerie Bertrand Gillig</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/MODERN-ART-COLLECTION-SA"><img alt="MODERN ART COLLECTION SA" class="shadow" src="https://imgprivate2.artprice.com//get/store/0950/1682/05ff/cbf7/ab4e/689d/444f/319b/32a6/500/500/d4ae-1555083694.jpg"/></a></div><div class="store-link"><a href="/store/MODERN-ART-COLLECTION-SA">MODERN ART COLLECTION SA</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/Galerie-Kellermann"><img alt="Galerie Kellermann" class="shadow" src="https://imgprivate2.artprice.com//get/store/3316/84bd/6cd1/76d1/48a7/b8a5/fa3c/1adc/67a3/500/500/629a-1526556250.jpg"/></a></div><div class="store-link"><a href="/store/Galerie-Kellermann">Galerie Kellermann</a></div></div></div><div class="view-container"><div class="marketplace-stores-top-store"><div class="store-img"><a href="/store/BEL-AIR-FINE-ART"><img alt="BEL-AIR FINE ART" class="shadow" src="https://imgprivate2.artprice.com//get/store/82da/b47b/fac8/5c30/b240/65e0/ac4d/c0e0/6c12/500/500/b6b8-1509709511.jpg"/></a></div><div class="store-link"><a href="/store/BEL-AIR-FINE-ART">BEL-AIR FINE ART</a></div></div></div></div></div></div>
</div>
<div class="col-xs-12 links text-right">
<h2>
<small>
<a href="/marketplace/store" ng-click="send_aa_event_now('click_home_page', 'events', 'see_all')"><span class="badge"><i class="fa fa-chevron-right"></i></span>
            See all</a>
</small>
</h2>
</div>
</div>
<div class="row">
<div class="col-xs-12 ">
<h2>
  ArtMarket® Insight - what's trending on the art market
</h2>
<div class="row artmarketinsight pad pad-l-15">
<div class="col-xs-12 col-lg-4 article">
<a class="font font-18" href="/artmarketinsight/artprice-com-is-changing-its-name-to-artmarket-com-to-become-a-global-player-in-the-art-market" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'article')" title="Artprice.com is changing its name to Artmarket.com to become a global player in the Art Market">
          Artprice.com is changing its name to Artmarket.com to become a global player in the Art Market

        </a>
<small>
          (10 Jul 2019)
        </small>
</div>
<div class="col-xs-12 col-lg-4 article">
<a class="font font-18" href="/artmarketinsight/francis-bacon-at-the-pompidou-centre-the-big-autumn-event-in-paris" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'article')" title="Francis Bacon at the Pompidou Centre: the big autumn event in Paris">
          Francis Bacon at the Pompidou Centre: the big autumn event in Paris

        </a>
<small>
          (09 Jul 2019)
        </small>
</div>
<div class="col-xs-12 col-lg-4 article">
<a class="font font-18" href="/artmarketinsight/flash-news-wols-the-mysterious-at-sothebys-cindy-sherman-in-london" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'article')" title="Flash News: Wols “the mysterious” at Sotheby’s – Cindy Sherman in London">
          Flash News: Wols “the mysterious” at Sotheby’s – Cindy Sherman in London

        </a>
<small>
          (05 Jul 2019)
        </small>
</div>
</div>
<div class="row">
<div class="col-xs-12">
<h2 style="border-bottom: none;float: right;margin: 0;">
<small>
<a href="/artmarketinsight" id="sln_ami" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'all')"><span class="badge"><i class="fa fa-chevron-right"></i></span>  Go to all the articles
        </a>
<a class="marg marg-l-20" href="/artmarketinsight/reports" ng-click="send_aa_event_now('click_home_page', 'artmarketinsight', 'reports')"><span class="badge"><i class="fa fa-chevron-right"></i></span> The Art Market Reports by Artprice.com
        </a>
</small>
</h2>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<footer class="bottom-bar">
<div class="container">
<div class="wechat-qr-code hidden" ng-click="toggleWeChatQRCode()" ng-cloak="" ng-show="weChatQRCode">
<img alt="Wechat artprice" src="https://imgpublic.artprice.com/img/wechat-artprice.png"/>
</div>
<div class="col-sm-3 col-xs-12">
<ul>
<li>
<div class="row marg marg-b-10">
<div class="col-xs-12">
<div class="social-network twitter">
<a href="https://twitter.com/artpricedotcom?lang=en" onclick="javascript:aa('send', 'event', 'footer', 'about_us', 'twitter');" rel="publisher" target="_blank">
<i class="fa fa-lg fa-twitter"></i>
</a>
</div>
<div class="social-network facebook">
<a href="http://www.facebook.com/artpricedotcom" onclick="javascript:aa('send', 'event', 'footer', 'about_us', 'facebook');" target="facebook">
<i aria-hidden="true" class="fa fa-lg fa-facebook"></i>
</a>
</div>
</div>
</div>
</li>
<li>
<a alt="ARTPRICE VIDEO : *ENGLISH VERSION: ARTPRICE OR THE REVOLUTION OF THE ART MARKET* " class="invisiblelink" href="/videos/artprice" onclick="javascript:aa('send', 'event', 'footer', 'about_us', 'video');" title="*ENGLISH VERSION: ARTPRICE OR THE REVOLUTION OF THE ART MARKET* ">Discover Artprice© in Video</a>
</li>
<li>
<a href="/editorial/artprice-is-hiring" ng-click="send_aa_event_now('footer', 'usefull_links', 'jobs');">Careers</a>
</li>
<li>
<a href="//imgpublic.artprice.com/img/wp/sites/11/2018/03/FactSheet_EN.pdf" ng-click="send_aa_event_now('footer', 'about_us', 'artprice_presentation');">Artprice presentation</a>
</li>
</ul>
</div>
<div class="col-sm-5 col-xs-12 col2">
<ul>
<li>
<a href="/contact" onclick="javascript:aa('send', 'event', 'footer', 'contact_us', 'phone');">FAQ</a>
</li>
<li>
<a borser="0" href="/amci" onclick="javascript:aa('send', 'event', 'top_banner', 'amci', 'confidenceindex.png');" target="amci">Artmarket Confidence Index by Artprice</a>
<a class="amciup" href="#" onclick="javascript:aa('send', 'event', 'top_banner', 'amci', 'amcivariance');window.parent.location='https://www.artprice.com/amci';">
<img alt="Amciup" src="https://imgpublic.artprice.com/img/amciup.gif"/>
                  31.30
                </a>
</li>
<li>
<a href="/auctioneer" onclick="javascript:aa('send', 'event', 'footer', 'contact_us', 'auctioneers');">Auction House Partner program</a>
</li>
<li>
<a href="/ail" onclick="javascript:aa('send', 'event', 'footer', 'contact_us', 'ail');">Advertising</a>
</li>
</ul>
</div>
<div class="col-sm-4 col-xs-12">
<ul>
<li>
<a href="http://serveur.serveur.com/Press_Release/pressreleaseen.htm" onclick="javascript:aa('send', 'event', 'footer', 'about_us', 'press_release');" target="_blank">Press Releases</a>
</li>
<li>
<a href="http://blog.ehrmann.org/pdf/demeureduchaos-abodeofchaos-opus-IX-2013.pdf" ng-click="send_aa_event_now('footer', 'usefull_links', 'ddc_opus_ix');" target="pdf">Abode of Chaos Opus IX</a>
</li>
<li>
<a href="https://www.interpol.int/en/Crimes/Cultural-heritage-crime/Stolen-Works-of-Art-Database" ng-click="send_aa_event_now('footer', 'usefull_links', 'interpol');" target="inerpol">INTERPOL's database on Stolen Works of Art</a>
</li>
</ul>
</div>
<div class="col-xs-12">
<div class="layout-bottom-copy ">
<a href="/">Artprice</a>
  is listed on Eurolist by
    <a href="https://www.euronext.com/en/products/equities/FR0000074783-XPAR" target="euronext">Euronext Paris (Euroclear: 7478 - Bloomberg: PRC - Reuters: ARTF) </a>
  - A company of
  <a href="http://www.serveur.com">Groupe serveur</a>
<br/>
<a href="#" ng-click="open_cgv();send_aa_event('footer', 'bottom', 'cgv_path');"> Terms and conditions of use and sale </a>

  -
  <a href="https://imgpublic.artprice.com/pdf/retract_en.pdf" target="pdf">Withdrawal process</a>
  -
  <a data-target="#base-modal" data-toggle="modal" href="/block/privacypolicy?modal=true">Confidentiality and personal data protection charter</a>
  -
  <a data-target="#base-modal" data-toggle="modal" href="/block/copyright?modal=true">Copyright</a>

  by
  <a href="/">artprice.com</a>

  © <a href="http://blog.ehrmann.org/" target="_blank">Thierry Ehrmann 1987-2019</a> All rights reserved
</div>
</div>
</div>
</footer>
</div>
<!-- Need this for react drawers (see react portals) /> -->
<div id="drawer-root"></div>
<div aria-hidden="true" aria-labelledby="myModalLabel" class="modal fade" id="base-modal" role="dialog" tabindex="-1">
<div class="modal-dialog modal-lg">
<div class="modal-content"></div>
</div>
</div>
<div aria-hidden="true" class="modal fade" id="login_modal" ng-controller="CustomerLoginCtrl" ng-init="initialize_login_input()" role="dialog" tabindex="-1">
<form accept-charset="UTF-8" action="/login/login?layout=1" force-blur-before-submit="" id="login_form" method="post" ng-submit="login_submit($event)"><input name="utf8" type="hidden" value="✓"/>
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-hidden="true" class="close" data-dismiss="modal" type="button">×</button>
<h4 class="modal-title">Log in</h4>
</div>
<div class="modal-body" id="modal-login-body">
<div class="form-group">
<label for="login">Username</label>
<input class="form-control sln_login" id="login" name="login" ng-focus="error=null" ng-model="login" placeholder="youremail@email.com" required="" type="text"/>
</div>
<div class="form-group">
<label for="pass">Password</label>
<div class="input-group">
<input autocomplete="off" class="form-control sln_pass" id="pass" name="pass" ng-focus="error=null" ng-model="pass" placeholder="Password" required="" type="{{inputTypeModal}}"/>
<span class="input-group-btn">
<button class="btn btn-default" ng-class="{'active': inputTypeModal == 'text'}" ng-click="inputTypeModal = inputTypeModal == 'text' ? 'password' : 'text'" ng-init="inputTypeModal = 'password'" title="Display password" type="button">
<i class="fa fa-eye" ng-if="inputTypeModal == 'text'" title="Hide password"></i>
<i class=" fa fa-eye-slash" ng-if="inputTypeModal != 'text'" title="Show password"></i>
</button>
</span>
</div>
</div>
<div class="alert alert-warning alert-dismissable" ng-show="error">
<button aria-hidden="true" class="close" data-dismiss="alert" type="button">×</button>
<strong>Note</strong> {{ error }}
          </div>
</div>
<div class="modal-footer">
<div class="pull-left" style="text-align:left ;font-size:12px">
<a href="/account/forgot_password" onclick="javascript:aa('send', 'event', 'login', 'cooked', 'forgot_password');">Forgot your username and/or password?</a>
<br/>
<a href="/newcomer">Free express sign up</a>
</div>
<input class="btn btn-primary sln_post_login" name="commit" type="submit" value="Submit"/>
<button aria-hidden="true" class="btn btn-default" data-dismiss="modal">Close</button>
</div>
</div>
</div>
</form></div>
<div ng-controller="CookiesConsentController as $ctrl">
<div class="hidden-print" id="cookies_banner" ng-hide="$ctrl.hideCookieWarning">
      By using this website, you accept the use of cookies for better analysis and relevance.
      For more information,
      <a data-target="#base-modal" data-toggle="modal" href="/block/privacypolicy?modal=true">Confidentiality and personal data protection charter</a>
<a class="linkbutton btn btn-xs btn-primary" href="javascript:void(0)" id="sln_hcw" ng-click="$ctrl.acceptCookies()" title="Click on OK to ignore this comment">OK</a>
</div>
<div ng-hide="$ctrl.hideCookieWarning" style="height:30px"></div>
</div>
<script>
    window.__PRELOADED_STATE__ = {"events":{"store":{"loading":false,"data":{"8000":{"id":8000,"title":"ARTESANTANDER","dt_event_start":"2019-07-12T23:00:00.000+01:00","dt_event_expire":"2019-07-16T23:00:00.000+01:00","slug":"artesantander","idcountry":469},"8057":{"id":8057,"title":"Art Marbella","dt_event_start":"2019-07-29T23:00:00.000+01:00","dt_event_expire":"2019-08-02T23:00:00.000+01:00","slug":"art-marbella","idcountry":469},"8087":{"id":8087,"title":"Art International Zürich","dt_event_start":"2019-09-25T23:00:00.000+01:00","dt_event_expire":"2019-09-28T23:00:00.000+01:00","slug":"art-international-zurich-2019","idcountry":476},"8129":{"id":8129,"title":"ART FORMOSA","dt_event_start":"2019-08-21T23:00:00.000+01:00","dt_event_expire":"2019-08-24T23:00:00.000+01:00","slug":"art-formosa","idcountry":478}}},"events/HOME_PAGE":{"country#all&from#unset&to#unset":{"ids":[8000,8057,8129,8087],"loading":false}},"countries":{"469":{"loading":false,"data":{"fr":"ESPAGNE","en":"SPAIN","es":"ESPAÑA","it":"SPAGNA","de":"Spanien","zh":"西班牙"}},"476":{"loading":false,"data":{"fr":"SUISSE","en":"SWITZERLAND","es":"SUIZA","it":"SVIZZERA","de":"Schweiz","zh":"瑞士"}},"478":{"loading":false,"data":{"fr":"TAÏWAN","en":"TAIWAN","es":"TAIWÁN","it":"TAIWAN","de":"Taiwan","zh":"台湾"}}},"medias":{"437":{"loading":false,"data":{"id":437,"date":"2019-06-04T15:46:01.000+02:00","mime_type":"image/gif","media_type":"image","name":"180-x-150-px.gif","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px.gif","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-150x150.gif","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-168x140.gif","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px-120x150.gif","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/04/180-x-150-px.gif","height":150,"width":180}}}},"920":{"loading":false,"data":{"id":920,"date":"2019-06-20T08:55:09.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"52725434_2061848314108026_6870054731188797440_n-1.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1-120x150.jpg","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/52725434_2061848314108026_6870054731188797440_n-1.jpg","height":150,"width":180}}}},"947":{"loading":false,"data":{"id":947,"date":"2019-06-20T09:45:13.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"Banner180x150.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150-120x150.jpg","height":150,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/06/Banner180x150.jpg","height":150,"width":180}}}},"1898":{"loading":false,"data":{"id":1898,"date":"2019-07-03T12:57:34.000+02:00","mime_type":"image/jpeg","media_type":"image","name":"Art-international-Zürich-Logo-180-x-150.jpg","source":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Zürich-Logo-180-x-150.jpg","formats":{"thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Zürich-Logo-180-x-150-150x150.jpg","height":150,"width":150},"ami-thumbnail":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Zürich-Logo-180-x-150-168x140.jpg","height":140,"width":168},"cover":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Zürich-Logo-180-x-150-120x157.jpg","height":157,"width":120},"full":{"url":"//imgpublic.artprice.com/img/wp/sites/119/2019/07/Art-international-Zürich-Logo-180-x-150.jpg","height":157,"width":180}}}},"bySlug":{"artesantander":{"loading":false,"idmedia":437},"art-marbella":{"loading":false,"idmedia":947},"art-formosa":{"loading":false,"idmedia":920},"art-international-zurich-2019":{"loading":false,"idmedia":1898}}}},"indexes":{},"userContext":{"name":"","logged":false},"preferences":{"dimension":"cm","currency":"gbp","lang":"en","marketplaceItemsPerPage":1},"marketplace":{"searchbars":{"search":{"totalCount":0,"initialTotalCount":0,"loadingFacets":false,"facetsPathname":""}},"stores":{"top":{"loading":false,"result":[{"id":30787,"sitename":"Villa del Arte Galleries","url":"/store/Villa-del-Arte-Galleries","imageUrl":"https://imgprivate2.artprice.com//get/store/00dd/1a43/b361/a6ba/b820/247b/4c57/8179/6a4e/500/500/e53d-1539942108.jpg"},{"id":17492,"sitename":"MA GALERIE - Samuel Le Paire","url":"/store/MA-GALERIE---Samuel-Le-Paire","imageUrl":"https://imgprivate2.artprice.com//get/store/a38c/7592/1f65/e632/5796/6a30/5086/1a7d/b26d/500/500/d61a-0.jpg"},{"id":19323,"sitename":"Galerie Bertrand Gillig","url":"/store/Galerie-Bertrand-Gillig","imageUrl":"https://imgprivate2.artprice.com//get/store/9127/a413/c12e/f4dc/7f53/ee34/01b9/8ed1/69f9/500/500/939d-1528814509.jpg"},{"id":53,"sitename":"MODERN ART COLLECTION SA","url":"/store/MODERN-ART-COLLECTION-SA","imageUrl":"https://imgprivate2.artprice.com//get/store/0950/1682/05ff/cbf7/ab4e/689d/444f/319b/32a6/500/500/d4ae-1555083694.jpg"},{"id":29852,"sitename":"Galerie Kellermann","url":"/store/Galerie-Kellermann","imageUrl":"https://imgprivate2.artprice.com//get/store/3316/84bd/6cd1/76d1/48a7/b8a5/fa3c/1adc/67a3/500/500/629a-1526556250.jpg"},{"id":26069,"sitename":"BEL-AIR FINE ART","url":"/store/BEL-AIR-FINE-ART","imageUrl":"https://imgprivate2.artprice.com//get/store/82da/b47b/fac8/5c30/b240/65e0/ac4d/c0e0/6c12/500/500/b6b8-1509709511.jpg"}]}}},"ui":{}};
  </script>
</body>
</html>

>>> for link in soup.find_all("a")
  File "<stdin>", line 1
    for link in soup.find_all("a")
                                 ^
SyntaxError: invalid syntax
>>> for link in soup.find_all("a"):
...     print(link.get("href"))
...
http://www.enable-javascript.com/
/search
/artists/directory
/sales/futures
/artmarketinsight/reports#archives
/marketplace
/marketplace/sell-an-artwork
/subscription/store
/marketplace/ads-instructions-for-use
/html/en/mode_emploi_store.pdf
/artmarketinsight
/artmarketinsight/reports
/eventweb/past
/events/
/subscription
/estimate
/subscription/store
/indexes/artinvestment
/webapp#!/shop/list
/artists/all/A
/events/8000/ARTESANTANDER/
/events/8057/Art-Marbella/
/events/
/subscription/payable
/artprice-reports/the-art-market-in-2018
/artmarketinsight/reports
/marketplace/1943123/aurelie-nemours/drawing-watercolor/e8-22re-rom-82-22
/marketplace/1689643/tony-soulie/painting/hong-kong-238-28from-hong-kong-series-29
/marketplace/1955165/bengt-lindstrom/painting/tetti-di-parigi
/marketplace/1980817/jean-fautrier/painting/femme-assise-dans-un-cafe
/marketplace/1824484/felix-labisse/painting/essas
/marketplace/1656205/mr-brainwash/print-multiple/metro-polisa
/marketplace/1808969/tony-soulie/painting/dreamed-flower-xi
/marketplace/1873441/pierre-bonnard/sculpture-volume/baigneuse-assise-devant-un-rocher
/marketplace/1678039/mark-di-suvero/drawing-watercolor/untitled-28drawing-29
/marketplace/1575558/patrick-cornillet/drawing-watercolor/sans-titre
/marketplace/1669429/mimmo-paladino/sculpture-volume/acrobata-28sculpture-29
/marketplace/1825604/moise-kisling/painting/mimosas
/marketplace/1721179/mark-di-suvero/print-multiple/magnetic-borealis
/marketplace/733217/aurelie-nemours/painting/polychromie-28triptyque-29
/marketplace/1033048/salvador-dali/sculpture-volume/christ-of-st-john-of-the-cross-28cristo-de-san-juan-29
/marketplace/576677/edward-cucuel/painting/dame-mit-kleid-2c-impressionist-2c-lady-with-dress
/marketplace/1645765/philippe-pasqua/painting/stella
/marketplace/1664803/tony-soulie/painting/untitled-san-francisco-28bridge-29
/marketplace/1955150/auguste-herbin/painting/chene-liege-a-vaison-la-romaine
/marketplace/1738482/joan-miro/print-multiple/joan-miro-and-catalonia-7c-joan-miro-und-katalonien
/marketplace
/estimate
/store/Villa-del-Arte-Galleries
/store/Villa-del-Arte-Galleries
/store/MA-GALERIE---Samuel-Le-Paire
/store/MA-GALERIE---Samuel-Le-Paire
/store/Galerie-Bertrand-Gillig
/store/Galerie-Bertrand-Gillig
/store/MODERN-ART-COLLECTION-SA
/store/MODERN-ART-COLLECTION-SA
/store/Galerie-Kellermann
/store/Galerie-Kellermann
/store/BEL-AIR-FINE-ART
/store/BEL-AIR-FINE-ART
/marketplace/store
/artmarketinsight/artprice-com-is-changing-its-name-to-artmarket-com-to-become-a-global-player-in-the-art-market
/artmarketinsight/francis-bacon-at-the-pompidou-centre-the-big-autumn-event-in-paris
/artmarketinsight/flash-news-wols-the-mysterious-at-sothebys-cindy-sherman-in-london
/artmarketinsight
/artmarketinsight/reports
https://twitter.com/artpricedotcom?lang=en
http://www.facebook.com/artpricedotcom
/videos/artprice
/editorial/artprice-is-hiring
//imgpublic.artprice.com/img/wp/sites/11/2018/03/FactSheet_EN.pdf
/contact
/amci
#
/auctioneer
/ail
http://serveur.serveur.com/Press_Release/pressreleaseen.htm
http://blog.ehrmann.org/pdf/demeureduchaos-abodeofchaos-opus-IX-2013.pdf
https://www.interpol.int/en/Crimes/Cultural-heritage-crime/Stolen-Works-of-Art-Database
/
https://www.euronext.com/en/products/equities/FR0000074783-XPAR
http://www.serveur.com
#
https://imgpublic.artprice.com/pdf/retract_en.pdf
/block/privacypolicy?modal=true
/block/copyright?modal=true
/
http://blog.ehrmann.org/
/account/forgot_password
/newcomer
/block/privacypolicy?modal=true
javascript:void(0)
>>>
