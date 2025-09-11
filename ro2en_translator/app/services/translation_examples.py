SYSTEM_INSTRUCTIONS = """
You are an expert translator. I am going to give you one or more example pairs of text \
snippets where the first is in Romanian and the second is a translation of the first \
snippet into English. The sentences will be written
Romanian: <first sentence>
English: <translated first sentence>
After the example pairs, I am going to provide another sentence in Romanian and I want you to translate it \
into English. Give only the translation, and no extra commentary, formatting, or chattiness. Translate the \
text from Romanian to English.

Romanian: Ei bine, trebuie să-mi clătesc ochiul şi vreau să-ţi mulţumesc din nou.
English: Well, I must bathe my eye. Thank you again, you've been awfully sweet.
Romanian: Nimic.
English: Mistake.
Romanian: Si la lucrusoare pe care le foloseai sa faci
English: ♪ AND THE LITTLE THINGS YOU USED TO DO ♪
Romanian: Exact, Henry.
English: That's right, Henry.
Romanian: Dar nu pot să plec la Veneţia.
English: But I can not go to Venice.
Romanian: Trebuie să mă confesez ca nu am fost pregătit să vă d această viziune a frumusetţii.
English: I must confess, I was not quite prepared to see such a vision of loveliness.
Romanian: - La revedere.
English: - Auf wiedersehen.
Romanian: Mulţimile se transformă repede în jefuitori.
English: Mobs quickly turn to looting.
Romanian: - Bună!
English: - Hello.
Romanian: Nu, dragul meu Reggie, era un elefant.
English: No, my dear Reggie. It was an elephant.
Romanian: Parte om!
English: - Part man!
Romanian: # Sunt îndrăgostit # # Şi mă simt minunat #
English: I'm in love And feelin' high
Romanian: Da, îl iubesc!
English: "So you love him? '
Romanian: Haide !
English: Come on!
Romanian: Nu le-am văzut în viaţa mea.
English: I never saw them.
Romanian: Mai faceti dragoste?
English: - Do you still screw?
Romanian: - Mi-e foame.
English: - I'm hungry.
Romanian: Urcă pe catarg.
English: Get aloft.
Romanian: E gata să vorbească.
English: She's ready to talk.
Romanian: - Spune-i că sunt Nora.
English: - Tell him it's Nora.
Romanian: Ei bine, nu domnule... nu tocmai.
English: Well, no sir .. not exactly.
Romanian: Capturarea lui e inevitabilă.
English: I assure you we will capture him.
Romanian: Dacă i-ai distrus viața sorei mele, te voi face să plăteşti.
English: If you've wrecked my sister's life, I'll make you pay for this.
Romanian: Singurul pe care l-am cunoscut.
English: The only one I've ever met.
Romanian: Da, excelenţă.
English: Yes, Your Excellency.
Romanian: Mai întâi îi dau drumul.
English: First, I let her go.
Romanian: Sheila, Sheila, Ken la telefon.
English: Sheila, Sheila, Ken speaking.
Romanian: Haide, așază-te, Nick.
English: Come on, sit in, Nick.
Romanian: Bine.
English: Good.
Romanian: Liniste!
English: Quiet!
Romanian: Nu mergem mii de mile.
English: Here's the island we're looking for.
Romanian: Îți spun să-l eliberezi.
English: I tell you to release him.
Romanian: Da, va fi bine.
English: Yes, he'll be all right.
Romanian: Citește!
English: See for yourselves.
Romanian: Orcine, care-l ia regulat, nicodata nu tuşeşte.
English: Anyone taking it regularly will never cough.
Romanian: Fă-ţi munca pe vas şi te vei întoarce acasă plin de glorie.
English: Do your spit and polish and you'll come home with the seals following in admiration.
Romanian: O lege care să pună armele în acelaşi context ca drogurile şi rasismul.
English: A law that puts the gun in the same class as drugs and white slavery.
Romanian: - Dragul meu, dl Blake... cum mă poţi ierta vreodată că m-am îndoit de integritatea ta?
English: - My dear Mr. Blake... how can you ever forgive me for doubting your integrity?
Romanian: Baumann ?
English: Baumann?
Romanian: Acum, criminalul pene umbrela pe cos.
English: Now, the killer wedges the umbrella up the chimney.
Romanian: - Erau împreună când...
English: They were together when-
Romanian: - Dar draga mea, eu...
English: - But. my dear. I...
Romanian: Este teribil sa te trezeşti dimineaţa si sa fi avut visuri despre traznete.
English: It's terrible to wake up at dawn dreaming of thunder.
Romanian: N-a fost chiar o minciună.
English: Well, it... It wasn't untrue exactly.
Romanian: Și Ați cunoscut-o de la bun început.
English: And You've Known It From The Very Beginning.
Romanian: Legea şi ordinea în San Francisco.
English: Law and order in San Francisco.
Romanian: Nu vreau să am de-a face cu tine.
English: I'll have nothing to do with you.
Romanian: Acum știu ce îmi doresc.
English: I know my own mind now.
Romanian: Pentru numele lui Dumnezeu, gândeşte-te la ceea ce spui.
English: For God's sake, man, think what you're saying.
Romanian: Cred că ar fi trebuit să te implor să mă ierţi.
English: I suppose I ought to beg you to forgive me.
Romanian: Aș prefera să ne vedem în altă parte.
English: I'd prefer to meet you somewhere else.
Romanian: Nu aş vrea să îmi asum răspunderea, dle Smith.
English: I don't like to take the responsibility, Mr. Smith.
Romanian: Daca-mi puteti acorda o clipa.
English: If you could just give me a moment.
Romanian: A cui a fost ideea?
English: Whose idea?
Romanian: Inteleg.
English: -I understand.
Romanian: Nu e corect ce-ai făcut. Pe viitor n-o să mă mai încred în marsiliezi.
English: I'll never trust a Marseillais again.
Romanian: Te duci la Curte.
English: You're going to court.
Romanian: Liftul nu mai merge.
English: The lift isn't working.
Romanian: - Am auzit-o pe prietena lui lătrând azi noapte.
English: - I heard his lady friend howling last night.
Romanian: Spune-o.
English: Say it.
Romanian: E treabă importantă.
English: This is important business.
Romanian: Cu placere.
English: With pleasure.
Romanian: O sa ma sinucid!
English: So help me, I'll kill myself!
Romanian: - A mai rămas putin în sticlă.
English: - There's another little drink in the bottle.
Romanian: Şi pot spune, că sunt bine informat.
English: I'm in a position to know, believe me.
Romanian: Cine e?
English: Who is it?
Romanian: Este pentru pamantul natal.
English: It's for the fatherland.
Romanian: Ce lucru prostesc!
English: It was the silliest, silliest thing!
Romanian: - Experimentele.
English: His experiments.
Romanian: - 255!
English: -255!
Romanian: Ce-a patit fetita mea?
English: Oh! Why, what's wrong with my little girl?
Romanian: - Sigur că da!
English: - Yes, of course!
Romanian: Nu este totul unilateral.
English: It's not all one-sided like that.
Romanian: - Treci acolo!
English: - Get out here!
Romanian: La revedere.
English: Goodbye.
Romanian: - Ciao, Lil.
English: - Hello, Lil.
Romanian: Haide!
English: Come on.!
Romanian: E pe aici pe undeva.
English: It's around here somewhere.
Romanian: Da, domnule.
English: Yes, sir.
Romanian: - Primăria e coruptă.
English: Well, that's the idea. The city government is full of graft and corruption.
Romanian: Se zvoneste ca, la intoarcerea din Europa,
English: It is rumored that, on her return from Europe,
Romanian: Marturiseste ca ai ucis-o!
English: Confess that you killed her !
Romanian: Dă-mi să văd.
English: Let me look at that.
Romanian: - Da, foarte mult.
English: - Yes, very much.
Romanian: Ştii ce s-a întâmplat.
English: You know what happened.
Romanian: Dar dacă vorbim suficient de tare, poate ne va auzi.
English: But if we speak loudly enough, perhaps he can hear us.
Romanian: Scuză-mă.
English: Excuse me.
Romanian: Mi-am depus deja candidatura în oraşul ăsta.
English: - Often? Say, I'm already runnin' for office in this town.
Romanian: Eu mă duc la culcare.
English: I'm going to bed.
Romanian: Tu nu l-ai luat să-şi facă plimbarea azi dimineaţă.
English: You didn't take him for his walk this morning.
Romanian: "Albert, mama ta se simte bine?"
English: Tell her that I shall do my best to see her sometime today.
Romanian: - Maiuses le-a luat pe cele mai bune.
English: The Maiuses got better ones.
Romanian: Trebuie să avem în vedere vântul, curenţii de apă...
English: We must consider winds and currents...
Romanian: - Ordinele căpitanului Bligh.
English: - Captain Bligh's orders.
Romanian: Fiule drag, moartea mamei tale ne-a făcut relaţia mai apropiată, decât relaţia tată-fiu şi de aceea, parcă pot vorbi cu un prieten.
English: Dear son, Since the death of your mother our relation was more that of comrades than that of father and son, and that is why I can now speak to you as a friend.
Romanian: Acum încă o dată, te rog să-i convingi pe aceşti oameni drăguţi că nu a fost o întâmplare.
English: Now another, please - to convince these nice people that it wasn't a fluke.
Romanian: -Ce?
English: - What?
Romanian: - În faţa cortului, să fii marele şef.
English: In front of the tent, the big boss.
Romanian: Cele mai multe necazuri din această lume vin de la oameni care au convingeri.
English: Most trouble comes from people with convictions.
Romanian: Vă rog!
English: Ready.
Romanian: Mi-am făcut socotelile.
English: I did a few calculations.
Romanian: Aici e presa.
English: Here are the press.
Romanian: Locotenentul ALEXIS a fost trimis unităţii dvs. ca pedeapsă.
English: Lieutenant ALEXIS has been sent to your unit as punishment.
Romanian: Suntem acadele elegante.
English: We're the old-fashioned cookies
Romanian: A fost si el acolo?
English: Was he there too?
Romanian: - Cine e?
English: - Who's that?
Romanian: Încercaţi să vă frângeţi gâturile?
English: What are you trying to do, break your necks?
Romanian: - Ai luptat cu ei ?
English: - Did you fight?
Romanian: Atunci vei aranja un interviu... când?
English: Then you will arrange interview... when?
Romanian: Trebuia să sosească o telegramă de la mama ta.
English: There should have been a cable from your mother.
Romanian: Rămâi cu bine, draga mea.
English: Good-bye, darling.
Romanian: Poate că da.
English: Maybe so.
Romanian: E vorba despre un turneu scandinav.
English: It's for a Scandinavian tour.
Romanian: Ei bine... o fată arendașă.
English: Well .. a tenant girl.
Romanian: - Mergem să adoptăm un copil.
English: We're going to adopt a baby.
Romanian: - Ţi-am spus să chemi un taxi.
English: - I told you to get me a taxi.
Romanian: Îmi dai o ţigară?
English: May I have a cigarette?
Romanian: Bună seara, Marie.
English: Hello, Marie.
Romanian: Să ascultăm
English: Let's hear it.
Romanian: Scuzați-mă, domnișoară, Arizona Jim se vinde bine?
English: Excuse me... Does this "Arizona Jim" sell much?
Romanian: Vă vor oferi preţul aurului.
English: Would offer the price of gold.
Romanian: Ceea ce aţi spus poate fi adevărat, dar copilul nostru este în pericol.
English: What you've said may be true, but our child's in danger.
Romanian: Ce s-a întâmplat?
English: What's wrong?
Romanian: Vă rog să nu vă supăraţi pe mine.
English: "Please don't be angry with me.
Romanian: - Și tu o să cânți. Imposibil.
English: Impossible.
Romanian: Este mai linişte aici, nu-i aşa ?
English: Kind of quiet around here, ain't it?
Romanian: Se prezintă ca un reformist însă e un om obişnuit!
English: He may be running on the Reform ticket... but believe me, he's a regular feller!
Romanian: Sa ma joc de-a circul cu voi?
English: Must mama take you horsy-back ride?
Romanian: Poftim.
English: There you are.
Romanian: - Nu ai nevoie de curaj pentru asta.
English: You don't need any courage for this job.
Romanian: Este casa de comoară a Estului.
English: It's the treasure house of the East.
Romanian: Camera dumneavoastră, domnişoară.
English: Your room, senorita.
Romanian: Aşa o încheiem?
English: Is this how we end up?
Romanian: Ei bine, națiunile sunt ca oamenii, Joe, iar oamenii nu se înțeleg ?
English: Well, uh, nations are like people,Joe, and do people get together?
Romanian: Vă mulţumesc pentru oferta de protecţie, Col. Cobb... Dar nu cred că voi avea nevoie.
English: Thank you for your offer of protection, Col. Cobb but I don't think I shall need it.
Romanian: Eu întotdeauna am crezut că acest talent există.
English: I've always thought there was.
Romanian: Nu voi suporta aşa ceva.
English: I ain't gonna stand for that.
Romanian: Acum o tragem peste cap...
English: Now, we'll just slip this right over your head.
Romanian: Am salvat fiecare bănuţ.
English: Saving every bob.
Romanian: Te iubesc, Sonia.
English: I love you, Sonia.
Romanian: Mort?
English: Dead?
Romanian: - O să ştii şi tu cum e! - Biciuieşte-l!
English: - We'll let you know what it feels like!
Romanian: Ceva îmi spune că Golden Harvest
English: Something tells me that Golden Harvest
Romanian: E Pepel.
English: It's Pépel.
Romanian: - Spuneți, care dintre voi...
English: - Say, which one of you-
Romanian: Guzzi!
English: Guzzi!
Romanian: Mă duc să le aduc.
English: I'll get it.
Romanian: Atunci unul dintre voi va muri.
English: You'll die, then.
Romanian: Lăsând-o pe mătuşa ta cu o povară.
English: Leaving you a charge on your old aunt.
Romanian: - Luke!
English: Luke!
Romanian: Are de-a face, cu faptul de-a lua atitudine față de soția lui.
English: IT HAS TO DO WITH STANDING UP TO HIS WIFE.
Romanian: Dragă Mary.
English: Mary, darling.
Romanian: - Jur, Robert!
English: - I promise, Robert.
Romanian: Apropo, de ce eraţi supărat în noaptea când aţi părăsit Elveţia ?
English: By the way, why were you so upset the night you left Switzerland?
Romanian: Mi-e greu să nu o fac.
English: You're making it difficult for me not to.
Romanian: Aterizare plăcută.
English: Well, happy landing.
Romanian: În alt tur de forţă ca grevă?
English: Another stunt like the strike ?
Romanian: Uf și ție.
English: Woof to you.
Romanian: Şi cine crezi că va veni şchiopătând, pentru slujba asta cine altul decât bătrânul Long John Silver?
English: And who do you think would come hobbling along for that berth but old Long John Silver?
Romanian: Atunci a încetat să fie om.
English: That's where she ceased to be human.
Romanian: Îmi pare rău dar trebuie să ne despărţim. Mi-a ajuns!
English: "I'm sorry, but we must part.
Romanian: Dar, draga mea... Şşş
English: But, my dear...
Romanian: Mă aşteaptă.
English: They're waiting for me
Romanian: - Nu-i pasă.
English: - She doesn't care.
Romanian: - Daţi-mi un trabuc.
English: - Give me a cigar.
Romanian: Sunt şeful tău?
English: Am I your manager?
Romanian: Trebuie să şoptim ceea ce toată Roma mormăie?
English: Must we whisper what all Rome growls?
Romanian: Te rog, Frieda! Nu-mi spune ce sa fac!
English: Please, Frieda, don't tell me what I do!
Romanian: Vreau să te văd mai târziu.
English: I want to see you later, then...
Romanian: Mergea prea repede.
English: He was going too fast.
Romanian: Nu te îngrijora pentru mine.
English: - Oh, don't worry about me.
Romanian: Tu ești partenerul meu.
English: You're my partner.
Romanian: Bine...
English: Very well.
Romanian: Dar aş dori să te pot săruta.
English: I wish I could kiss you.
Romanian: Ai insigna pe faţa ta... nu sub haina ta.
English: You've got your badge on your face, not under your coat.
Romanian: Lăsaţi-l jos.
English: Let him down.
Romanian: De ce nu vii şi să mă iei de aici ?
English: Why don't you come and take me away from here?
Romanian: - Nu.
English: - No.
Romanian: Vezi dacă-ţi place.
English: See if you like him.
Romanian: Ar fi trebuit să spun da.
English: I ought to have said yes
Romanian: Nu-i frumos.
English: That's too bad.
Romanian: Şi asta-i toată grozăvia, dle.
English: And that's the whole awful story, sir.
Romanian: Astfel grăi Mime, meşterul fierar:
English: Thus spake Mime, the artful blacksmith:
Romanian: Aş vrea tare mult să nu fim nevoiţi să ne mai întoarcem la Lloydsboro.
English: I do wish I didn't have to go back home to Lloydsboro.
Romanian: - Da.
English: - Yes.
Romanian: Pearl.
English: Pearl.
Romanian: Doamne, pentru ce a mai trăit?
English: Lord, why did she even live?
Romanian: Îmi ştii numele ?
English: You know my name?
Romanian: Dacă aş fi în locul tău, aş fi, atât de fericit.
English: If I were you, I would be, oh, so happy.
Romanian: Cunosti un jad bun cand vezi unul?
English: Do you know good jade when you see it?
Romanian: Ne-am dus vitele la Marsilia pentru a-ţi vinde cruciaţi, pe aur, nu pe promisiuni.
English: We drove our cattle down to Marseille to sell to you Crusaders for gold not promises.
Romanian: Poate că ţie nu, dar mie sigur mi s-ar părea ciudat.
English: Well, maybe you wouldn't, but it would certainly feel very queer to me.
Romanian: O mică atenţie de Crăciun.
English: Just a bit of a Christmas gift.
Romanian: Am avut asistente, guvernante, bone... până şi bodyguarzi.
English: Nurses, governesses, chaperones, even bodyguards.
Romanian: Nu te grăbi.
English: Don't be in a hurry.
Romanian: "Mă bucur mult, că ai venit, doctore."
English: "I'm so glad you've come, Doctor."
Romanian: - M-am gândit că ai vrea să ştii.
English: - Thought you might like to know.
Romanian: - Nu poţi s-o faci, Richard!
English: - You cannot, Richard.
Romanian: Cunoaştem prea bine viaţa.
English: We know too much of life.
Romanian: Dar întotdeauna mi se par atât de reci.
English: But they always seem so cold to me.
Romanian: în Anglia...
English: In England...
Romanian: De ce, eu...?
English: Why, I....!
Romanian: - Obraznic! - Seară bună!
English: - Well, cheek.
Romanian: "Nu accept chervoneţi!"
English: "I don't give scrip."
Romanian: - Da, domnule..
English: - Yes, sir.
Romanian: Poate ne vedem după-amiază.
English: Perhaps I shall see you this afternoon.
Romanian: - Ei bine, un tip pe linie ...
English: - Well, a fella down the line...
Romanian: - Da, trebuie.
English: Yes, l have to.
Romanian: - Gata, gata !
English: There, there.
Romanian: Oh, tu încă nu ai niciun jeton, Nick.
English: Oh, you ain't got any chips yet, Nick.
Romanian: De acum încolo, mă voi duce peste tot, în oras,
English: My dear, words fail me.
Romanian: Dă-mi germenii de sânge, dă-mi şobolanii, puricii de şobolan, micii purici săltăreţi.
English: Give me blood germs. give me rats. rat fleas. little jumpy fleas.
Romanian: Da, sunt considerată o bucătăreasă excelentă.
English: Yes, I'm considered a very excellent cook.
Romanian: Şi încearcă să nu loveşti nimic.
English: And listen -don't hit anything.
Romanian: Nu te obosi, Rosie.
English: Nix cracking, Rosie.
Romanian: Cu condiţia să fie folosit cu măsură.
English: - Providing, of course, it's used sparingly.
Romanian: Pentru că va trebui.
English: Because you're going to.
Romanian: - Bine, dacă vrei.
English: - All right, you'll do.
Romanian: Renunt.
English: I give up.
Romanian: Mulţumesc.
English: Thank you.
Romanian: Numai...
English: I only...
Romanian: Dormi,baiatul meu.
English: Sleep, my boy.
Romanian: Marcus Superbus... prins în sfârşit de o creştină zburdalnică.
English: Marcus Superbus... caught at last by a Christian wanton.
Romanian: Nu, nu, nu.
English: - Then there's... - No, no, no, no.
Romanian: Cezar... sunt vorbe mânioase care spun că tu ai dat foc oraşului.
English: Caesar... there are angry rumors that you set fire to the city.
Romanian: Este o iertare pentru tine și un mandat de moarte pentru Carston.
English: It's a pardon for you and a death warrant for Carston.
Romanian: Trimite-l înapoi!
English: Send him aloft again!
Romanian: Asta e prima data cand tu...
English: This is the first time you...
Romanian: El trebuie să fie epuizat.
English: He must be worn out.
Romanian: Repede!
English: Come, quick!
Romanian: - Da, O.J.
English: - Yes, O.J.
Romanian: Totuși, presupun că vor fi câțiva polițiști care vor da târcoale.
English: Still, I suppose there'll be a couple of cops snooping around.
Romanian: lată vine clipa mea cea mare.
English: Here goes my big moment.
Romanian: Nu-şi poate şterge trecutul.
English: He cannot rub out his past.
Romanian: - Nu pricepuşi ?
English: - You don't get it?
Romanian: Vreau ca cele trei zile să fie fericite pe nava asta.
English: I want our three days of happiness on this ship.
Romanian: - Nu.
English: - No.
Romanian: Dar ai terminat cu porcăria asta.
English: But you're through with that bunch.
Romanian: Şi totul e o mare plictiseala, nu ?
English: It's all just a great bore, isn't it, darling?
Romanian: Nu te-ai culcat, văd lumină !
English: You're still up. We can see your light.
Romanian: El singur, dintre toţi, şi-a realizat visul, iar tu-mi ceri să-l alung, să ţi-l trimit înapoi ţie şi măruntei tale iubiri muritoare.
English: He alone, of all men, has realized that dream, And you ask me to send him away, to send him back to you... - and your little mortal love.
Romanian: Nu e nici în teugă.
English: He ain't in the forecastle.
Romanian: De-a lungul timpului... în care reclamanta a fost logodită cu pârâtul, domnul Clayton... aţi fost prietenos cu ea ?
English: During the time... the plaintiff was engaged to the defendant, Mr. Clayton... were you friendly with her?
Romanian: Dacă pleacă, pleacă.
English: If they goes, they goes.
Romanian: - El este?
English: - Is he in?
Romanian: Chiar pe covorul tău, sergent.
English: Right on your carpet, Sarge.
Romanian: În Marsilia, dle Brun, nimic nu e mai neplăcut ca munca.
English: In Marseille, nothing comes harder than work.
Romanian: - La revedere, Felice.
English: Au revoir, Felice.
Romanian: Nu neg responsabilitatea.
English: I don't deny the responsibility.
Romanian: Mă uit şi eu pe aici.
English: Oh. Just looking.
Romanian: Ai înţeles asta?
English: You got what?
Romanian: În schimb joacă
English: Starring
Romanian: Situatia e grea in Kham Po Shian.
English: There's a bad case in Kham Po Shian.
Romanian: Prostii, treci inapoi in pat.
English: Nonsense, you get right back into bed.
Romanian: Bine, Jimmy.
English: Okay, Jimmy.
Romanian: Ia-l de aici, fă-l să-şi vândă ferma, plecaţi de aici.
English: Take him away, make him sell the ranch, leave here.
Romanian: - Acum ceva muzică, vă rog.
English: - Now some music, please!
Romanian: Haide, grabiti-va.
English: Come on, hurry up.
Romanian: - Ce faci aici ?
English: - What are you doing here?
Romanian: - Aseară ?
English: ─ Last night?
Romanian: Este localul La Rueda?
English: This La Rueda?
Romanian: Pălăria.
English: Hat.
Romanian: - Ce-i asta?
English: - What is this?
Romanian: Mă tem că va trebui să mai aveţi răbdare câteva zile.
English: I'm afraid we'll have to be patient a few days longer.
Romanian: Da, știu.
English: Yes, I know, but uh...
Romanian: Da, Elanul Negru mi-a spus că este aproape sigur... - Ca indienii Cheyenne vor începe un război.
English: Yeah, Black Elk tells me that it's almost certain that the Cheyennes will declare war later.
Romanian: Nu ştiu.
English: I don't know.
Romanian: Cine e cine?
English: Who is who?
Romanian: Nu te deranjează dacă nu mă îmbrac?
English: You don't mind if I'm not dressed?
Romanian: Acum, să fim clari, Martin, vei munci aici şi nu vei avea pe nimeni decât pe tine însuţi de satisfăcut.
English: Now. let us be clear. Martin. You will do your own work here and have no one but yourself to satisfy.
Romanian: Dacă asta nu înseamnă mai mult decât a comanda cina, precum prietena ta, madam...
English: If that isn't more than knowing how to order dinner as your friend the madam...
Romanian: Stai aici cu mine.
English: - Aw, sit here with me.
Romanian: Dacă furtuna asta creşte aşa cum sper, vei avea motive să-ţi fie frică în noaptea asta.
English: If this storm develops as I hope, you will have plenty to be afraid of before the night's over.
Romanian: E profesor la liceul local.
English: Ηe's the boys' professor.
Romanian: "scoala naturii"
English: dNature's school dBut one thing there is lacking in the picture
Romanian: - Slavă Domnului.
English: - Thank heavens. - Yes.
Romanian: Crainquebille ar fi mărturisit, dacă ar fi ştiut, ce trebuia să mărturisească.
English: Now Crainquebille would have confessed had he known what he had to confess to.
Romanian: - Mai spune o dată.
English: Say that again, kinda slow like.
Romanian: Ce icerci să spui ?
English: What are you trying to say?
Romanian: Trăiască, trăiască Freedonia
English: Hail, hail Freedonia
Romanian: Și s-a pornit o furtună crâncenă.
English: Suddenly, a storm broke out.
Romanian: - Îmi permiteţi?
English: May I?
Romanian: Le accept. Totuşi, venirea asta senzaţională cu cătuşe, jandarmi, şi tot tacâmul, dau un efect deplorabil asupra populaţiei provinciale.
English: - I accept them wholeheartedly, but these spectacular entrances, with handcuffs policemen and all this ruckus, have a regrettable impact on the minds of rural populations.
Romanian: Aş bea o bere. O bere rece.
English: I'll have some beer, cold beer.
Romanian: Ele perie.
English: They brush.
Romanian: Precis sunteţi buni.
English: Well, I'll bet you're good.
Romanian: Hai să-i doborâm.
English: Let's go get 'em.
Romanian: Dar cele mai multe dintre ele nu erau la nivel tău.
English: But most of them weren't on the level.
Romanian: Nu mai avem unde dormi, nu mai avem de mâncare...
English: No place to sleep and no food.
Romanian: - Da.
English: - Yeah.
Romanian: Caporale, Bell.
English: Corporal Bell.
Romanian: Şi totul e de la Dragostea osândita.
English: And it's all from Doomed Love.
Romanian: Sună adunarea.
English: They're sounding assembly.
Romanian: Şi ne-am strâns tare.
English: We pressed tightly together.
Romanian: Ei sunt ca pocnitori tare.
English: They're like loud firecrackers.
Romanian: - Smitty, doar ce l-am văzut mergând printre vagoane... Arăta ca Barton.
English: Smitty, just saw him walking' down the track...
Romanian: - Mie îmi face mai multă plăcere.
English: - Much pleasure to see you.
Romanian: Ce?
English: What?
Romanian: Cu mine e altceva.
English: With me it's different.
Romanian: Cu dublura ei, care va duce piesa de râpă.
English: The understudy, and she'll put the show right back on track for Keynes warehouse.
Romanian: Cum e cotletul de porc a la Pompadour?
English: What's this pork chop à la Pompadour?
Romanian: Ce vor?
English: What do they want?
Romanian: - Unul dintre sclavii mei?
English: - What? One of my slaves?
Romanian: Ai fost amestecat în mai multe aventuri deocheate cu femei.
English: You've been mixed up in several messy affairs with women.
Romanian: Din cauză că ti-a fost dor de mine.
English: That's only because you've been missing me.
Romanian: Merg să-i spun.
English: I tell her.
Romanian: Trebuie să găsim o cale de scăpare, să facem o plută sau ceva.
English: We're gonna move on and find some way out of this, make a raft or something.
Romanian: Bijuteriile.
English: Jewels.
Romanian: Trebuie sa-l gasesti!
English: You've got to find him!
Romanian: Asta apartine unui tip numit Kirkwood, mare avocat in centru.
English: This belongs to a guy named Kirkwood, big lawyer downtown.
Romanian: N-am mai mâncat aşa mult de multă vreme.
English: Yes, sir, you know... I can't remember when I've enjoyed eating so much.
Romanian: Părerea ta, mi se pare prea sentimentală.
English: Your opinion seems too sentimental.
Romanian: Da, pentru asta am venit.
English: Yes, that's what I came for.
Romanian: Oh, nu puteam să stau singur.
English: Oh, I couldn't stand it myself.
Romanian: Ei bine, vom pleca, Franz.
English: Well, we'll be going, Franz.
Romanian: Din depărtări
English: # Far away ##
Romanian: Mamă, simt cum sângele mi se scurge din inimă!
English: Mother, I feel as if the blood is draining from my heart!
Romanian: Tot ce are nevoie este de putere și de o pereche de pantofi, iar eu le-am primit.
English: All he needs is strength and a pair of boots, And I got them.
Romanian: Bietul de el, te-a vizitat si in ziua mortii sale.
English: The poor fellow even visited you on the day of his death.
Romanian: Ah, prăpăditule.
English: Ah, you rascal.
Romanian: El e foarte nerăbdător să te vadă.
English: He's terribly anxious to see you.
Romanian: De ce nu te întinzi linistit si să dormi ?
English: Why don't you lie still and go to sleep?
Romanian: Ar fi călărit mai greu.
English: Why, he would've been riding bareback.
Romanian: Oricum ai grijă si încuie-ti banii.
English: Anyway, you be careful, and lock your money up.
Romanian: - Hellcat, Mary, groapa de calcar!
English: - Hellcat, Mary- the chalk pit!
Romanian: Dragă copilă!
English: "Dear child! ...
Romanian: - Amici, domnisoara Fields.
English: - Fellas, Miss Fields.
Romanian: Chiar mai galant.
English: More gallant still.
Romanian: să-mi găsesc propriile greşeli.
English: looking for my own mistakes.
Romanian: - Te căsătoreşti cu Dan Morgan ?
English: - Marry Dan Morgan?
Romanian: Amin.
English: Amen.
Romanian: Dacă, dai de necaz.
English: If you get in trouble.
Romanian: Credeam că ei vor fi simpli, cruzi, și barbari și nu îmi va plăcea, dar acolo am văzut anumite acțiuni precise care îmi va da sentimentul de viață și moarte la care lucram eu.
English: I thought they would be simple and barbarous and cruel and that I would not like them, but that I would see certain definite action which would give me the feeling of life and death that I was working for.
Romanian: Oricine e de acord cu tine e drăguţ.
English: Anyone's nice who gives in to you.
Romanian: E prea târziu, domnule.
English: Too late, sir.
Romanian: Ce pot face pentru tine, domnule Chan?
English: What can I do for you, Mr. Chan?
Romanian: Oh, bine, bine, o să vin și o să văd a cui a fost vina.
English: Oh, all right, all right, I'll come down and see whose fault it was.
Romanian: Gata?
English: Ready?
Romanian: - Unde te duci?
English: - Where are you going?
Romanian: Şi eu i-am dat o mamă de bătaie!
English: I got a few licks in, too!
Romanian: Putem fi impreuna, nu doar acum ci mereu
English: We can be together, not only now, but always.
Romanian: Vrea să intre într-o transă juju.
English: He's working himself into a juju.
Romanian: Cei care câștigă sub 100 de dolari pe săptămână nu sunt niciodată încântați.
English: People who make under $100 a week are never delighted.
Romanian: Ar putea sa moara.
English: He may be dying.
Romanian: Oh, mulţumesc băiete.
English: Oh, thanks, lad.
Romanian: Spune-i că insist să vină.
English: Tell him I want him.
Romanian: - Eşti un tip ciudat.
English: - You're a peculiar chap.
Romanian: - Ia loc!
English: - Sit down.
Romanian: Nu, eu doar...
English: No, I was only...
Romanian: La un bal ţinut în cinstea lui, îi oferă mâna ei.
English: At a ball given in his honour, she offers him her hand.
Romanian: Mai ţii minte când Mickey se târa şi încercă să se caţere pe el ?
English: Remember the time when Mickey first climbed over the side and crawled?
Romanian: Nu miscati!
English: Keep quiet.
Romanian: Nu uita: In copacul gaunos de langa stanci.
English: Now don't forget in the hollow of a tree down by the forks...
Romanian: Nu, e a dvs. Eu am luat bucata dinainte.
English: No, that's yours. I had the last piece.
Romanian: Era să ne mai cunoaştem odată, nu-i aşa?
English: We almost met once before, did we not, you and I?
Romanian: O să facem skanderbeg.
English: Us two are gonna arm-wrestle.
Romanian: Pimenov?
English: Pimenov?
Romanian: M-a angajat.
English: He's hired me.
Romanian: - Soţia mea, săraca.
English: - My wife, poor girl.
Romanian: Vine, vine, vine.
English: Here he is, here he is, here he is.
Romanian: Este mare păcat.
English: That's too bad.
Romanian: O să mă credeţi când o să stau alături de voi în arenă.
English: You'll believe me when I stand beside you in the arena.
Romanian: Antrenorul. E atât de dur ca se râde cu torţa.
English: The head coach ... so tough he shaves with a blow-torch.
Romanian: Francoise.
English: Francoise.
Romanian: Nu voi mai fi niciodată asistentă, George.
English: I'm never going back to it, George.
Romanian: Ştiţi cine-s făptaşii, nu?
English: You weren't at the ball, were you?
Romanian: In schimb, voi avea grija de nepoata ta.
English: -And in return for this, I will take good care of your granddaughter.
Romanian: Adică ai renunţa la viaţa cu mine şi ai muri pentru o credinţă, pentru ceva nesigur...
English: You mean you'd give up life with me... and would rather die for a belief, for some vague...
Romanian: ştiţi că este încă interzis să te lupţi... luptă... luptă!
English: You Know that fighting is prohibited yet you fight... fight... fight!
Romanian: - Şmecherule...
English: - You dirty, low...
Romanian: "Dar o făcea să sufere"
English: And he was doing her wrong
Romanian: Eu sunt Joe Stevens, de la WQL.
English: This is Joe Stevens over at wql.
Romanian: Dar el te cunoaşte, dragă.
English: Well, he knows you, dearie.
Romanian: Stimulează apetitul.
English: They say it's great for the appetite.
Romanian: Nu e om.
English: He ain't a man.
Romanian: Vreau să auziți asta. A fost seara de dinainte de Shiloh, iar ordinele trebuiau să ajungă peste râu la gen.
English: I want you to hear this. 'Twas the eve before Shiloh... and them orders had to get across the river to General Beauregard.
Romanian: Nu pot trece.
English: I can't pass.
Romanian: - Talgav.
English: - Talgav.
Romanian: Dacă nu voi turna, o va face altcineva, ceva va apărea într-una din aceste zile și te vor acuza... - Și știi asta.
English: If I don't squeal, it doesn't have to be me, something will pop up one of these days and get you... and you know it.
Romanian: Şi acum... sunt atât de slab.
English: And now... I'm so weak.
Romanian: Si Saul a aruncat sulita.
English: And Saul threw the spear.
Romanian: Vreau o ţigară.
English: I want a cigarette.
Romanian: În documentele căpitanului Grant apare paralela 37.
English: Our documents say that Grant is on parallel 37.
Romanian: Bine.
English: All right.
Romanian: Nu m-am asteptat la asta.
English: I didn't anticipate that.
Romanian: Ce înseamnă sindrofia asta ?
English: "What's the meanin' of this jamboree?"
Romanian: Cere-mi ce vrei, dar asta...
English: You can ask anything of me, but not that!
Romanian: Anne, asculta-ma.
English: Anne, listen to me.
Romanian: Iată un model elegant.
English: Here's a neat little model.
Romanian: Toți bărbații râdeau.
English: They all laughed
Romanian: O... împuşcătură?
English: A... shot? !
Romanian: Trebuie să plec acum.
English: I have to go now.
Romanian: Ce face soția?
English: How's your wife?
Romanian: As vrea o cafea înainte sa mor, în compania linistitoare a ta, daca se poate.
English: I should like some coffee before I die... and in your soothing company, if possible.
Romanian: Numai trei ?
English: Oh, certainly.
Romanian: Spune-i cine deţine tronul Angliei.
English: Tell him who holds the throne of England.
Romanian: Nu mi le mai aminti, acum seara !
English: Don't remind me of it tonight.
Romanian: Mama.
English: Mother.
Romanian: - Ești îndrăgostită de Gaerste?
English: - In love with Gaerste?
Romanian: În cinstea ta!
English: Cheers!
Romanian: - Helen. - Ia te uită, este bătrânul Roy.
English: - Well, if it isn't old Roy.
Romanian: Prieteni... suntem cu toţii mineri !
English: Comrades! All of us here are miners.
Romanian: - Nu, nu încă.
English: -No, not just yet.
Romanian: Vreți să așteptați?
English: Do you want to wait?
Romanian: Aşa sper.
English: I hope so.
Romanian: Cand completam actele?
English: When shall we draw up the papers?
Romanian: Tu habar n-ai !
English: You weren't there.
Romanian: Aici, Angus.
English: Here, Angus.
Romanian: De ce e trist ?
English: What is his sorrow?
Romanian: "... deci, mă iubeşti ?
English: "...so, are you in love?
Romanian: - Nu, eu...
English: No.
Romanian: Ce drăguţ...
English: How lovely...
Romanian: - Pe cine aşteptai, dragule ?
English: - Who were you expecting, darling?
Romanian: - Da.
English: - Yes.
Romanian: Despre viața lor de familie, relațiile ... date, fapte, zvonuri, chiar și cele mai mici detalii.
English: I wish to know them as intimately as I know myself. And as I know my weaknesses, I shall discover theirs. And then,
Romanian: O mare recompensă.
English: A big reward.
Romanian: Cu cateva ore inainte sa-i arunce trupul in piscina, cineva a inecat-o si a imbracat-o.
English: You see, a couple of hours before her body was dropped into the pool, somebody drowned her and somebody dressed her.
Romanian: Ce se întâmplă ?
English: Here, what's going on?
Romanian: Să vă purtaţi frumos cu copiii de aici!
English: You need to get along with the local kids.
Romanian: Suntem pe zero cu el pentru prima dată în viața noastră.
English: We're square with him for the first time in our lives.
Romanian: Al meu !
English: Mine!
Romanian: Sună bine.
English: Sound great.
Romanian: Spune-mi, încearcă să te agate si pe tine în piesă aceasta infantilă?
English: Tell me, are they trying to rope you into this putrid show too?
Romanian: Molâi stângace!
English: Left-handed moths!
Romanian: Omul ăla de jos mi-e cel mai mare duşman.
English: That man downstairs is my greatest enemy.
Romanian: Nu fi prostuţ.
English: Don't be so silly.
Romanian: Unde-s duşmanii noştri ?
English: Where's our sworn enemy?
Romanian: Şi acesta este Captain Li, ajutorul meu.
English: And this is Ceptein Li, my eide.
Romanian: Eu plec.
English: I'm leaving.
Romanian: Caii pentru mâine, ai făcut o afacere bună.
English: Those horses for tomorrow... -...you made a good deal.
Romanian: Repede !
English: Hurry!
Romanian: "Mai bine un domn decât un ţăran !"
English: - She prefers the lord to the peasant!
Romanian: Cum îi vrei de data asta:
English: How do you want them this time:
Romanian: Eu nu m-am uitat niciodată la...
English: - What am I to do with her?
Romanian: Cum e Adriano?
English: How is Adriano?
Romanian: -Obiectie respinsa.
English: - Objection overruled.
Romanian: Impuscati-l!
English: Give him another one.
Romanian: Nu te poţi hotărî cum îl vrei?
English: Can't you make up your mind which way you want him?
Romanian: Hei, vizitiu !
English: Hey, driver!
Romanian: Da,intr-adevar.
English: Yes, indeed.
Romanian: - Bună ziua, dle.
English: - Morning, sir.
Romanian: Mă voi întoarce la tine în ambalajul original.
English: I will be returned to you in the original package.
Romanian: În sfârșit, fericirea s-a întors la noi.
English: At long last happiness has returned to us.
Romanian: - Mă bucur să vă văd.
English: - Glad to see you.
Romanian: Repede, trebuie sa fie in partea cealalta.
English: Hurry up. She must be up ahead here.
Romanian: Cea adevarata e in gheata mea.
English: I left the real one on my boot.
Romanian: Brandt Dl. Ce este aceasta?
English: Mr. Brandt. What is it?
Romanian: Ai milă!
English: Mercy!
Romanian: Ce s-a intamplat?
English: What happened?
Romanian: Ah!
English: Ah!
Romanian: - E posibil să fie rău, dle Smith.
English: - He's liable to get tough, Mr. Smith.
Romanian: Valdemar Christensen (1898-1971) şi Allan Lynge
English: Valdemar Christensen (1898-1971) and Allan Lynge
Romanian: Da, domnule.
English: - Yes, sir.
Romanian: Reţinem camerele acum.
English: We're holding the rooms now.
Romanian: Dar este ceea ce își dorește Julia, iar eu mă bucur să fac conform dorinței ei.
English: But it's what Julia wishes, and I'm glad to defer to her wish.
Romanian: Pot să-mi port singură de grijă.
English: I can take care of myself.
Romanian: O sa trec peste asta.
English: I'll get over it.
Romanian: O, ia-i!
English: No, take it!
Romanian: Vă zic că el este nebun.
English: I tell you he's mad.
Romanian: Nu !
English: No!
Romanian: O sa-ti dau cuvantul meu... si tu stii ca niciodata nu mi l-am incalcat.
English: I'll give you my word... and you know that I never break my word.
Romanian: - Am bănuit că vei apărea.
English: I thought I'd be hearing from you real soon.
Romanian: Maestrul e pe moarte.
English: The Master is dying.
Romanian: - Nu pot să te concedieze fără motiv.
English: - Why, thy can't let you out for nothing. - No.
Romanian: Nu, uh, ne-am familiarizat așa bine în acea zi la Ritz, domnule Taylor, că m-am gândit să-mi iau libertatea de a vă aduce la cunoștință acest bilet.
English: We, uh, got so well acquainted that day at the Ritz, Mr. Taylor, that I thought I'd take the liberty of bringing this item to you.
Romanian: Bine?
English: Well?
Romanian: Dacă tu şi iubita ta nu sunteţi de acord,
English: ~ If you and your beloved can't agree ~
Romanian: Murat intră în Moscova.
English: Murat enters Moscow.
Romanian: Vorbeşti ca o nebună.
English: You're talking like a crazy person.
Romanian: Ce s-a întâmplat?
English: What's the matter?
Romanian: - Nu.
English: - No.
Romanian: Ştii că mama ta nici măcar nu ne-a chemat?
English: Do you know your mother hasn't even called on Chloe?
Romanian: Care-i treaba?
English: - What's the matter?
Romanian: - Și atunci, ce importanță are?
English: Then what difference does it make?
Romanian: Este o petrecere minunată, domnule Easton,
English: This is a wonderful party, Mr. Easton.
Romanian: Nu-i zi de la Dumnezeu să nu mi se cotrobăiască prin ce am.
English: I get robbed every single day.
Romanian: - Cum aş putea să uit?
English: How could I ever forget?
Romanian: Lasă-mă jos!
English: Put me down!
Romanian: Wentworth?
English: Wentworth?
Romanian: - Da.
English: I mean mama.
Romanian: Va fi Marcus aici sau nu ?
English: Will Marcus be here or not?
Romanian: Oh, draga, nunta mea este distrusa.
English: Oh, dear, my wedding is all spoiled.
Romanian: Bună, George.
English: Hello George.
Romanian: Sunt sigură că nu eu am făcut-o.
English: I'm sure I didn't.
Romanian: Este intolerabil!
English: This is unbearable.
Romanian: El este cel care ne-a adus în această țară a decăderii și a morții!
English: He is the one who brought us into this land of decay and death!
Romanian: Annie, nu voi permite asta.
English: Annie, I won't allow that.
Romanian: - Ne mai vedem.
English: -I'll see you.
Romanian: Dar încă mă îngrijorez.
English: But I am still concerned.
Romanian: De ce nu?
English: Why not ?
Romanian: Crezi ca aceasta noapte va fi ca toate celelalte, nu-i asa?
English: You think this night will be like all the others, don't you?
Romanian: Nimic.
English: Well, nothing.
Romanian: - Da.
English: - Yes.
Romanian: Hamlet trăieşte ?
English: Hamlet lives?
Romanian: Vreau să-ţi spun.
English: I want to tell you.
Romanian: Pentru că e o chestiune de familie.
English: Because it's a family affair.
Romanian: Oare?
English: Do I?
Romanian: Dar vă mulțumesc mult.
English: But thank you so much.
Romanian: Regelui îi pasă de "văduvă"
English: A king worrying about a widow.
Romanian: Dar eu te iubesc, Pascual.
English: But I love you, Pasqual.
Romanian: D-le Barr, nu vreţi sã luaţi loc ?
English: Oh, Mr. Barr, won't you sit down?
Romanian: Undeva, cândva.
English: Somewhere, someday.
Romanian: - Mulţumesc, domnule Baron.
English: - Thank you, Baron.
Romanian: Te-am văzut înregistrându-te azi dimineaţă, dar erai în lift înainte să ajung la tine.
English: I saw you register this morning. You was in the elevator before I could get you.
Romanian: L-am găsit pe Sleepy Sam, șefule.
English: We found Sleepy Sam, chief.
Romanian: Să așteptăm aici până se întunecă.
English: - That is the Pharaon, isn't it? - Yes. What can a mother do with a daughter?
Romanian: - Te-au căutat peste tot. - Ei ?
English: - They've been looking for you all over.
Romanian: Îsi iubesc copiii la fel cum ma iubesti tu pe mine.
English: They love their children as much as you love me.
Romanian: Ce a avut de spus ?
English: Yeah? What did he have to say?
Romanian: De ce nu faci ceva în privința asta?
English: Why don't you do something about it?
Romanian: Mergem pe drumul lung, mai interesant.
English: We will take the long way, it is more picturesque.
Romanian: Nu putem sta aici fără să facem nimic, când el ne ucide pe rând.
English: We can't stay here and do nothing while he picks us off one by one.
Romanian: Cumpără-ți o cutie de bomboane.
English: Buy yourself a box of candy.
Romanian: Tenor.
English: A tenor.
Romanian: N-ai de ce.
English: That's nothing.
Romanian: Floarea dragostei nu şi-a putut găsi un loc mai romantic în care să înflorească decât în această Grădină de Vis a poetului.
English: The Flower of Love could find no more romantic spot in which to blossom than in this poet's Dream Garden.
Romanian: Terenul ăla e al nostru de drept, iar noi îl vrem înapoi.
English: That land rightfully belongs to us, and we mean to have it.
Romanian: Vă interesează cumva Krotov Tătarul?
English: Does Krotov the Tartar interest you?
Romanian: Tom?
English: Oh, Tom?
Romanian: - Totul creşte.
English: - All's more expensive!
Romanian: - Un milion de dolari.
English: - A million dollars.
Romanian: - Banii fac bani, ştii.
English: Money goes to money, you know.
Romanian: Ma întreb daca te vei simti la fel intr-o zi.
English: I wonder whether you'll feel the same way some day.
Romanian: Spuneți-mi, pentru câți voi pregăti cina?
English: Say, how many will I set the table for?
Romanian: N-a vrut decat sa-mi joace o farsa.
English: He was doing a trick with me.
Romanian: - Nu, draga.
English: - No, dear.
Romanian: La revedere.
English: Goodbye.
Romanian: De ce nu l-ai legat?
English: Why hasn't it been done?
Romanian: - Da.
English: - Yes.
Romanian: Asta-i tot.
English: That's all.
Romanian: Nu primesti mancare mai buna in nici o inchisoare "chain gang" din state.
English: You can't get better food on any chain gang in the state.
Romanian: - Nu e sezonul lor.
English: ─ Well, you're out of season.
Romanian: Nu suport politistii- Toţi sunt nişte brute.
English: I can't stand cops -- they're all brutes.
Romanian: Maria e moartă şi ai putea arde !
English: Maria drowned to death and you burned up!
Romanian: Da, având în vedere că nu ştii să conduci.
English: Yes, considering you can't drive.
Romanian: Salutare!
English: Well, hello!
Romanian: Dar nu era chiar o scrisoare.
English: But there wasn't much of a letter.
Romanian: Dar dacă Tira se întoarce înainte să plec de acolo.
English: But suppose Tira gets back before we spring it.
Romanian: Dă-te jos !
English: Get down!
Romanian: - Nu. Nu cu străini.
English: Not with strangers.
Romanian: - Am sau nu dreptate ?
English: - Am I right?
Romanian: Bazat pe novela lui Ilya Ehrenbourg.
English: Screenplay:
Romanian: El trebuie să fie regele vostru !
English: He is your King!
Romanian: Aşteptaţi.
English: - She's on duty.
Romanian: Să mă schimb cumva sau voi înnebuni.
English: Change somehow or I'll go mad.
Romanian: Şi datorită tăriei voastre nordice, specifică acestor locuri, Vikingii au dominat Europa.
English: And from all your northern fastness here, the Viking spirit has dominated Europe.
Romanian: - Și... acestea?
English: - And, uh, these?
Romanian: - Bună, bună.
English: - Well, hello.
Romanian: Îmi răspunzi ?
English: Will you answer?
Romanian: Da, domnule Chan.
English: Yes, Mr. Chan.
Romanian: - L-am prins.
English: - Ah, we've got him. We've got him.
Romanian: Nu pot să-ti dau ce nu ti-am dat.
English: I can't give you what I haven't got.
Romanian: Am avut din nou porţia săptămânală de râs.
English: I passed up my weekly laugh once more.
Romanian: Mi s-a adus la cunoştinţă că deţineţi un copil pentru care nu aveţi niciun drept legal.
English: It has come to my attention that you have a child to which you have no legal right.
Romanian: Ăsta nu-i visul unui copil.
English: That's not a child's dream.
Romanian: Oh, o clipă, vă rog.
English: Oh, one moment please.
Romanian: Întotdeauna te-am iubit şi întotdeauna te voi iubi.
English: I always have and I always will.
Romanian: Ei bine?
English: Well?
Romanian: Vreau să vă prezint tuturor pe vărul meu, Buddy Reeves, din Hoppersville, Tippecanoe, Indiana, USA.
English: Listen, folks, I want the whole crowd of you to meet my cousin, my good little old cousin Buddy Reeves from Hoopersville, Tippecanoe County, Indiana, USA.
Romanian: Frank Strobel
English: Frank Strobel
Romanian: Nu ştiu, să auzim din nou...
English: - I don't know.
Romanian: Înțeleg.
English: I see.
Romanian: Nu sunt ca...
English: They're just not like...
Romanian: - Ce faci? - Relaxează-te.
English: - What are you doing?
Romanian: - Ce vrei sa spui, luna?
English: - What do you mean, the moon?
Romanian: O să-i sun. O să le spun să-l aducă înapoi.
English: l'll get them on the telephone. l'll make them bring it back.
Romanian: "Valul trece
English: The swell passes
Romanian: Bună, Frances, plecăm.
English: Hello, Frances, we're leaving.
Romanian: Asculta, tu!
English: Listen, you!
Romanian: Ce aromă?
English: What flavour?
Romanian: - Ei bine?
English: - Well?
Romanian: Eşti un domn, în adevăratul sens al cuvântului.
English: Gentleman, in every sense of the word.
Romanian: Ai găsit ceva?
English: Find anything?
Romanian: Nu esti suparata pe mine, nu ? Te rog !
English: You aren't mad at me, are you?
Romanian: Atunci de ce nu ma lasi sa plec?
English: Why don't you let me go, then?
Romanian: Dupa cum e regula, confirm ca presedintele fiecarei organizatii din uniune este reprezentat. Presupun ca toti puteti vota in numele membrilor vostri.
English: According to regulations, I confirm that the leadership of every organization in our union is represented l assume you are all authorized to vote on behalf of your members
Romanian: Nu știu pe nimeni care să fi jucat biliard fără ele.
English: Well, never heard of nobody playing pool without 'em.
Romanian: La revedere.
English: Goodbye.
Romanian: E minunat de frumoasă.
English: That's beautiful.
Romanian: - Mă condamnă şi pe mine.
English: - It condemns me too.
Romanian: Eu sunt cea pe care ei...
English: It's me that they...
Romanian: De ce, în clipa în care te-ai pus în mâinile mele iubito, interesele tale sunt mai aproape de mine, decât eu însumi?
English: Why, the minute you put yourself in my hands, baby... your interests are closer to me than my own. Get me?
Romanian: - "Dlor duri" pentru tine.
English: Mr. Bozos to you. All right, Mr. Bozo.
Romanian: - Nu sunt multe de spus.
English: Well, there's really nothing much to tell.
Romanian: - În ciuda voastră.
English: In spite of you all.
Romanian: O s-o găsesc chiar de va trebui să întorc casa cu fundul în sus.
English: I'm going to get hold of it!
Romanian: Mă gândeam.
English: Just a thought.
Romanian: "Fericită ?"
English: "Happy?"
Romanian: La dreapta.
English: On the right.
Romanian: Oh, dl Beckert...
English: Oh, Mr. Beckert...
Romanian: De ce te-ai oprit?
English: Why did you stop?
Romanian: Nu te las să-i mai vânezi banii!
English: I won't have you hounding him for any more money!
Romanian: Şi tu ai fost minunat în felul tău.
English: You've been kind of wonderful yourself.
Romanian: Da, tati.
English: Yes, daddy.
Romanian: Himmelstoss.
English: Himmelstoss.
Romanian: Ne revedem curând.
English: I'm going to see you again soon.
Romanian: - Şi bune şi rele.
English: - Good and bad.
Romanian: - Mocasinii ăştia sunt rupţi.
English: These moccasins are torn.
Romanian: Uite, am o însãrcinare acum care mã va face cel mai mare poliţist din New York.
English: Look, I got an assignment today that will make me the biggest cop in New York.
Romanian: Dacă nu le-am spus despre mine, de ce să le spun de tine?
English: I didn't tell him about myself, so why should tell him about you?
Romanian: - Cu siguranţă.
English: - Can you?
Romanian: - E bun?
English: Is it good?
Romanian: - Trebuie să intru.
English: -That's my cue.
Romanian: Dacă ţi-ai da seama...
English: If you'd only realize...
Romanian: Taras inainte!
English: Crawl forward!
Romanian: Să răpună un câine turbat, un lup hămesit!
English: To put down a mad dog - a ravenous wolf!
Romanian: Cum Siegfried a răpus balaurul.
English: How Siegfried Slew the Dragon.
Romanian: "Închide ușa!"
English: "Close the door!"
Romanian: - Nu mă scoţi aşa uşor din pat.
English: You're not gonna get me off this bed.
Romanian: Da, George.
English: - Yes, George.
Romanian: Louis.
English: Louis.
Romanian: Nu.
English: No.
Romanian: Vă rog amabil să-mi eliberaţi prietenul.
English: Kindly release my dear friend.
Romanian: - Da.
English: - Yes.
Romanian: Dacă cânți "Mărșăluind prin Georgia", mă alătur linșorilor.
English: If you play "Marching Through Georgia", I'll join the lynchers.
Romanian: "Nu ştiu" şi "Nu-mi amintesc".
English: 'I don't know' and 'I don't remember'.
Romanian: - Trage-te de mustăţi, Sandy.
English: - Pull in your whiskers, Sandy.
Romanian: Şi în cinstea buzelor tale, cu sărutările lor drăgăstoase.
English: And to your lips, with their warm kisses.
Romanian: Buna iubitule.Buna
English: - Hello, honey. - Hello.
Romanian: Porcilor!
English: Pigs!
Romanian: Întotdeauna am știut că acest loc este un cuib de hoți.
English: I always knew this place was a nest of thieves.
Romanian: Lumea ar fi mai bună pentru copii dacă părinţii ar trebui să mănânce spanac.
English: The world would be better for children if the parents had to eat the spinach.
Romanian: De ce nu aş fi fericită?
English: Why shouldn't I be happy?
Romanian: - Plecăm în Franţa peste 15 zile.
English: We go to France in two weeks.
Romanian: Îţi aduci aminte ziua în care ai venit să mă vezi?
English: You remember that first day you came to see me?
Romanian: Oh, bine, contesă.
English: Oh, all right, countess.
Romanian: Prindeţi-I !
English: Catch him, men.
Romanian: V-am spus că calul ne va duce unde trebuie.
English: I told you the horse would bring you to the right place.
Romanian: Nu trebuie sa dai mare atentie unui obuz ca asta.
English: That kind of shell you don't have to pay much attention to.
Romanian: India.
English: India.
Romanian: "Dle profesor, nu dau greş niciodată...
English: "Professor, I never fail...
Romanian: "Prietenul meu de la şcoală...
English: This is my schoolmate, Mormon minister Andrew Larsson.
Romanian: - Da.
English: Yes.
Romanian: Col. Mărcuş Aurelius Cobb este numele meu, domnilor.
English: Col. Marcus Aurelius Cobb is the name, gentlemen.
Romanian: De cei care vă periclitează viaţă şi bunurile.
English: That'd endanger your property or your lives.
Romanian: Ce sa inchida?
English: Going to close what?
Romanian: - Haide, Marvin.
English: Come on, Marvin.
Romanian: Hans.
English: Hans.
Romanian: - Nu vreau să aud despre asta.
English: - I don't want to hear about that.
Romanian: Verificam schiţa să văd cum se deschide fereastra.
English: I was looking at the blueprint, trying to open the window!
Romanian: Lasă-mă să dansez Până restaurantul se închide.
English: Let me dance till the restaurant's close.
Romanian: După o săptămână, Serviciul de Informaţii l-a trimis pe soţul meu într-o misiune.
English: I hadn't been more than a week with my husband... when he was sent away on intelligence work.
Romanian: Oh, majestate...
English: Oh, Grace...
Romanian: Oh, d-na Bernard, vi-l prezint pe d-nul Spencer, d-nul Roy Spencer.
English: Oh, Miss Bernard, meet Mr. Spencer, Mr. Roy Spencer.
Romanian: Asa se rezolva treaba.
English: There's the works.
Romanian: - Dle. Wallace ! - Salut !
English: Mr. Wallace.
Romanian: Destul de târziu.
English: Late enough.
Romanian: O să mă descurc eu.
English: I'll catch on.
Romanian: Sire, locul meu e alături de tine.
English: - Sire, my place is with you.
Romanian: - Nu!
English: - No!
Romanian: - Dă-mi pelerina!
English: Give me my cape.
Romanian: - Sigur.
English: - Sure.
Romanian: Am vorbit cu mai mulţi oameni interesaţi.
English: I've talked to more people that are interested.
Romanian: Du-mă acolo.
English: - Oh, let me go too.
Romanian: Mamă, a doua noastră, Ossi este gata!
English: Mother, our second Ossi is finished!
Romanian: - Arată-ne stilul de dans.
English: - Give us an idea of the dance.
Romanian: Escadra a lovit crucişătorul.
English: The squadron draws near!
Romanian: Repede!
English: Quick, to arms.
Romanian: Ne vedem mai târziu.
English: See you later.
Romanian: Te va vindeca.
English: He'll cure you.
Romanian: - Am eşuat, dle. ambasador.
English: - I have failed, ambassador.
Romanian: Fata?
English: The girl?
Romanian: - O grămadă.
English: - Lots.
Romanian: "de scriere expozitivă...
English: "OF EXPOSITORY WRITING...
Romanian: Poate pentru tine, dar nu pentru mine.
English: Maybe for you, but not for me.
Romanian: Deci vrei ca eu sa devin un spion.
English: So you wish me to become a spy.
Romanian: Nu pot să nu-l iubesc.
English: I can't help loving him.
Romanian: Pardon!
English: I beg your pardon!
Romanian: Da, dar el n-a apărut.
English: - Yes, but he didn't show up.
Romanian: Ar trebui să-ţi fie ruşine de dumneata.
English: You should be ashamed of yourselves.
Romanian: Doreşte femeile tinere şi cele mai bune.
English: He wants his women young and picked.
Romanian: Marvin, arată-le camerele lor din spate, vrei?
English: Marvin, show them around to their rooms in the back, will you.
Romanian: Nunta de la Castelul Chanterelle.
English: Wedding at Castle Chanterelle.
Romanian: Întotdeauna am vrut să merg acolo.
English: I have always wanted to go.
Romanian: - Ba da !
English: - Yes, you are.
Romanian: "Nu accept mai puţin de 100!"
English: "Nothing less than a hundred."
Romanian: Aş vrea să am şi eu acest crez al tău, Arhiepiscope.
English: I wish I had your confidence, Archbishop.
Romanian: Mi-e foarte bine aici.
English: I'm quite happy here.
Romanian: Nu-mi plac escrocii.
English: I don't like crooks.
Romanian: Toţi din partea lui tata suntem aşa.
English: We're all like that on my father's side.
Romanian: V-ati făcut debutul în societate!
English: I see you're breaking into society.
Romanian: Nu mi-am imaginat ca ti-ar placea.
English: I didn't dream you'd like it.
Romanian: - E ieftin.
English: - It's cheap.
Romanian: Vorbiţi în şoaptă şi ascultaţi.
English: Keep your voice low and listen.
Romanian: - Veţi fi bine plătiţi.
English: -You will be well-paid.
Romanian: - Atâta tot.
English: - That's all.
Romanian: - Se spune că e bântuit de o fantomă.
English: It's said to have a ghost. - Said to have?
Romanian: - V-a spus cineva ceva sigur până acum?
English: - Anyone wise to you yet?
Romanian: Cine, Iris ?
English: Who, Iris?
Romanian: Regele George?
English: King George?
Romanian: Dacă pot să vă dau o mână de ajutor ca să reîncepeţi de unde v-aţi oprit, apelaţi la mine oricând.
English: Anything that I can do to help you start where you left off, call on me at any time.
Romanian: După tot ce s-a întâmplat?
English: After everything that's happened ?
Romanian: John.
English: John.
Romanian: Mulţumesc foarte mult.
English: I appreciate it a lot.
Romanian: Nu cred că e de mare ajutor.
English: Very helpful, I don't think.
Romanian: Tocmai m-am uitat.
English: I've just looked myself.
Romanian: - Poate ai dreptate.
English: I've just got to bring you back together again. Well, maybe you're right.
Romanian: Prânzul e la unu, acum e ora unu.
English: Luncheon's at one, and it's one now!
Romanian: Zicea că mă ucide, dar eu n-am făcut nimic.
English: He said he'd kill me and I wasn't doing anything.
Romanian: Acum, aici, acest mic bec...
English: Now, in here, this little bulb...
Romanian: Nu mă interesează restul.
English: I came to find out for myself.
Romanian: - Da, draga mea.
English: Success seems so empty.
Romanian: Suntem pregătiți în ziua și la ora stabilite.
English: We are ready on the day and at the time set.
Romanian: Nu ai putea să trimiţi pe cineva...
English: Couldn't you send someone -
Romanian: Par avion.
English: Air mail.
Romanian: Apropo de gândaci...
English: Creepy, it's true...
Romanian: Soţului meu o să i se spună de noi.
English: - My husband will be told.
Romanian: Doctorul Jaipur este cu el acum în camera de oaspeți.
English: Dr. Jaipur is with him now in the guest room.
Romanian: Ce am de pierdut
English: What have I got to lose
Romanian: Dar îmi vorbeşti limba.
English: - But you speak my language.
Romanian: Ei bine, hai sa spunem au existat trei saci pentru ca am întâmpla sa aiba trei saci aici.
English: Well, let's just say there were three sacks because I happen to have three sacks here.
Romanian: Deloc.
English: Nothing like that.
Romanian: Ooo, deci ai gardieni din nou, fricosule!
English: Oh, so you got guards again, you big sissy!
Romanian: "Sunteţi arestat."
English: "You are under arrest."
Romanian: Domnul Maurice a fost cu mine în taxi în acea noapte când mi-am pierdut diamantele.
English: Sir Maurice was with me in the taxi that night when I lost my diamonds.
Romanian: Sigur.
English: Well, of course.
Romanian: - De ce?
English: - Why?
Romanian: - Eşti în regulă şi aşa.
English: - You look alright the way you are.
Romanian: - Da?
English: - Yeah?
Romanian: Te dai bătut ?
English: Give up?
Romanian: Da fapt, e o singură mină.
English: This is one pit.
Romanian: Nu te mai afli, în serviciul diplomatic.
English: You're not in the diplomatic service now.
Romanian: Perlele moștenite de la mama, diamantele pe care mi le-ai dat la nuntă, inelul cu diamant de la Clas...
English: The pearls used to be Mummy's. ...the brilliants I got from you and the diamond ring from Claes.
Romanian: Adu-mi o ghioagă.
English: Here, fetch me a mace.
Romanian: Da.
English: Yeah.
Romanian: Bună ziua.
English: How do you do?
Romanian: Ea mă iubeşte chiar dacă hainele mele sunt vechi şi urâte.
English: She loves me, even if my clothes are old and ugly.
Romanian: - Cu cât mă gândesc mai mult la asta, cu atât mai mult mi se pare că Welford a fost terminat.
English: Murder? The more I think of it, the more it looks to me like Welford was knocked off.
Romanian: Dacă vă prind numai că vă uitaţi la nevastă-mea, am să te lovesc aşa de tare ca o să-l doară şi pe el.
English: lf l ever catch you even looking at my wife again, l'll hit you so hard that he'll feel it.
Romanian: Oricum, doar să lucrăm separat şi să facem lucrurile separat.
English: Either way. But let's work separately and do things separately.
Romanian: In regula, haide.
English: All right, come on.
Romanian: Nu stiu.
English: I don't know.
Romanian: N-ar face-o fericită pe Sheila dacă aş rezolva asta ?
English: Wouldn't it make Sheila happy if l could work this thing out;
Romanian: - Vin să vorbesc cu el.
English: He wants to see you. - l'll go and see him.
Romanian: Nu, mergi înainte. Foarte bine, domnule.
English: We'll go ahead.
Romanian: 20 de goguti !
English: Twenty francs!
Romanian: Ţine-o, Holt!
English: Hold her, Holt!
Romanian: E în regulă.
English: It's okay.
Romanian: Detectiv Dolan.
English: Detective Dolan.
Romanian: E în regulă.
English: It's all right.
Romanian: Uită-te ce-am tras.
English: Look at what I drew.
Romanian: În regulă.
English: All right.
Romanian: Vreau să uit toate astea.
English: I want to forget all that.
Romanian: Atunci de ce m-ai întrebat?
English: Why did you ask me then?
Romanian: Vino înapoi...
English: Get back...
Romanian: - Nu, trebuie să sosească mâine.
English: - We're expecting it tomorrow.
Romanian: Adică De fapt, a fost concediată?
English: You Mean You Actually Got Fired?
Romanian: - De ce nu?
English: - Why not?
Romanian: Sunt foarte formali.
English: They're all very formal.
Romanian: Ca au vazut-o pe fata de aur.
English: He says, look at the golden woman.
Romanian: Dacă mă auzi, răspunde, te rog.
English: lf you can hear me, come back, please.
Romanian: Dar locul pare parasit.
English: But the place looks deserted.
Romanian: Hadley Richardson.
English: How exciting you are.
Romanian: - Așteaptă-mă, Lew!
English: - Wait, Lew!
Romanian: Fata patiserului ?
English: I mean the baker's daughter.
Romanian: - M-am plimbat.
English: I've been taking a walk.
Romanian: Spune-i.
English: Tell him.
Romanian: Dar, doamnă, a fost ieri, mă uit la înregistrări.
English: But, madame, it was yesterday. I'm looking at the records.
Romanian: Marian, mai bine te duci la Emmy.
English: Marian, you'd better go to Emmy's.
Romanian: - Nu, regret, sunt încă pe-aici pe undeva.
English: No, sir. I'm sorry. They're still out there.
Romanian: Cer ca astea să nu fie luate în consideraţie.
English: I move to strike it from record.
Romanian: - Îmi pare rău.
English: - I'm sorry.
Romanian: Profesore, ajuta-ma sa testez atmosfera !
English: Professor, please, help me with the air-sample!
Romanian: Multumesc.
English: Thank you.
Romanian: Cred că Eddie a spus că era la transmisiuni.
English: I think Eddie said he was with the Signal Corps. Sure, that's it.
Romanian: Numai o clipă!
English: Wait a minute. Wait a minute.
Romanian: - Foarte bine.
English: Very good, sir.
Romanian: Este mai uşor acum, dar nu va mai fi când zăpezile vor cădea.
English: It's easy going now, but it won't be when the heavy snows come on.
Romanian: - Nu mi-aţi auzit trubadurul, nu?
English: You have not heard my troubadour, have you?
Romanian: Muffat e nebun după tine.
English: "Muffat is crazy about you.
Romanian: Oh, e atât de tânar si de sarac...
English: Oh, he's so young and so poor.
Romanian: Da, domnişoară, vă aşteaptă.
English: Yes, mademoiselle, he's expecting you.
Romanian: Adunaţi-vă familiile şi bunurile!
English: Get your families and your goods together!
Romanian: Căsătoria merge foarte bine.
English: That marriage is working out all right.
Romanian: - Tu, in seara asta.
English: - You, tonight.
Romanian: Dacã ar fi fãcut-o, l-aş fi pãlmuit.
English: If he had, I'd have slapped his face.
Romanian: - De ce?
English: - Why?
Romanian: - Sunt în regulă, dle...
English: - I'm all right, sir.
Romanian: Da, si aliniază-le chiar aici.
English: Yeah, and line them up right here.
Romanian: Doar sărbătoreşti...
English: Oh, uh, just celebrating...
Romanian: Ţi-ar place să vi şi să trăieşti cu mine?
English: Well, would you like to come and live with me?
Romanian: Astea sunt plătite?
English: Are these paid for?
Romanian: Miscă-te.
English: Get a move on.
Romanian: Nici nu am prins-o, idiotule.
English: - Why didn't you keep her when you had her? We never had her, you lassoed fool!
Romanian: Aveți vreme minunată.
English: It's been great here.
Romanian: Haide, şefu.
English: Go on, boss.
Romanian: - Nu o să ştii vreodată.
English: You'll never know.
Romanian: Faust!
English: Faust...
Romanian: Cred că ar fi mai bine să rămâi Cleopatra.
English: I think you'd better stay as Cleopatra.
Romanian: E cineva în cămară şi cred că tu eşti, căpitane.
English: There's somebody in that closet, and I think it's you, Captain.
Romanian: Ce vrei?
English: What do you want?
Romanian: ...
English: ...
Romanian: - Da.
English: - Yes.
Romanian: Serios, îmi place de tine, Anne.
English: I like you, Anne, really.
Romanian: - Iar?
English: - Again?
Romanian: Spuneţi-mi ceva despre dumneavoastră!
English: "Tell me something about yourself."
Romanian: - Serios!
English: - Really!
Romanian: Ihoşka, servitoarea preferată a Aelitei.
English: Ihoshka, Aelita's favorite maidservant.
Romanian: Uite, vrei să-ţi arăt?
English: Look, do you want me to show it to you?
Romanian: O imitație aproape bună.
English: Nearly good imitation.
Romanian: - Lucrează aici?
English: Does she work here?
Romanian: Tocmai am aflat că mai cunt cinci oameni blocaţi, dar în viaţă.
English: I've been told that there are five men still alive and trapped in the engine room.
Romanian: se furisau spre vrajitor unde li se ungea spatele cu "ulei fermecat".
English: sneaked away to the sorcerer where they could have their backs smeared with "witch ointment".
Romanian: Oare o femeie onorabilă nu poate fi văzută la orice oră?
English: Isn't an honorable woman always decent?"
Romanian: - Pa!
English: -Goodbye.
Romanian: Cu prima ocazie, am să-l împuşc, căpitan sau nu.
English: First chance I get, I'll shoot him dead, captain or not.
Romanian: De ce?
English: Why?
Romanian: Cu orgoliul rănit şi într-o izbucnire de mânie de o clipă,
English: But of wounded vanity, in the flare of a moment"s anger, -
Romanian: Acum, în cazul în care locuiești?
English: Now, where do you live?
Romanian: Într-o biserică...
English: In a church.
Romanian: Bani n-am găsit.
English: - Money? We found no money.
Romanian: Permite-mi.
English: Allow me.
Romanian: Un cal.
English: A horse.
Romanian: Domnilor... domnilor.
English: Gentlemen .. gentlemen.
Romanian: Nu înţelegi?
English: Don't you see?
Romanian: ♪ Și se văd toate razele lui aurii ♪
English: ♪ To capture all its golden beams ♪
Romanian: Beakman 3-8-4-6.
English: Beakman 3-8-4-6.
Romanian: Înţelepciunea Sa, medicul...
English: His Learnedness, the physician.
Romanian: Aşteaptă, nu vreau să te mişti.
English: Wait, I don't want you to move.
Romanian: Nu, doamnă.
English: No, madame. No, madame.
Romanian: Atunci mergem şi noi la New York dar nu aveam bani aşa că ne-am ascuns în cufăr.
English: We want to go to New York, too. But we got no money, so we hide in the trunk.
Romanian: - Ar fi mai rezonabil daca ne continuam drumul.
English: It would be more reasonable to move forward.
Romanian: La ce te aştepţi de la o femeie pe care o întâlneşti pe străzi?
English: What do you expect from a woman you meet in the streets?
Romanian: - De unde ştiu asta ?
English: - How do I know that?
Romanian: Imnul oficial al NSDAP şi, neoficial, imnul naţional
English: the NSDAP hymn and unofficial German National Anthem after Deutschland Über Alles.
Romanian: Dragi prieteni americani, iertaţi-mă dacă vorbesc mai prost deoarece nu sunt obişnuită să ţin discursuri în limba engleză.
English: Dear American friends, forgive me if I speak bad, as I am not accustomed to making speeches in English.
Romanian: Ce mai face Fifi, d-na Cole ?
English: How is Fifi, Mrs. Cole?
Romanian: Hai, puştiule.
English: NlCK: Go on, kid.
Romanian: - Niciuna.
English: - Nothing.
Romanian: Vrei să rămâi cu el ?
English: Alas, ifs not for love's sake
Romanian: - Da, Your Majesty.
English: - Yes, Your Majesty.
Romanian: Bine, ia-o mai ușor.
English: Alright, take it easy.
Romanian: Gaston!
English: Gaston!
Romanian: Trebuie să obții bilete pentru vasul cu aburi.
English: - Must get steamship tickets.
Romanian: În cele câteva săptămâni de când sunt aici, am deprins şi eu acelaşi lucru.
English: In the few weeks I've been here, I've learned it myself.
Romanian: Sire, am scotocit palatul din turn şi până-n temniţe.
English: Sire, we've searched the palace from tower to vault.
Romanian: Dar, trebuie să-ţi aminteşti, că l-ai iubit pe Geoffrey când l-ai acceptat.
English: But you must remember that you loved Geoffrey when you accepted him.
Romanian: Simţind că sfârşitul îi e aproape, Gabriel, bătrânul ţăran, îi spune secretul său lui Betty, care a crescut în casa sa.
English: Feeling his end, Gabriel, the old peasant tell his secret to Betty, grown up in his house.
Romanian: Nu poţi fi niciodată sigur că o femeie va fii la timp - chiar şi pentru nunta ei.
English: You can never be sure a woman will be on time -- even for her wedding.
Romanian: L-a prins !
English: He's got him. Look, he's got him.
Romanian: Nu am sete în seara asta.
English: I've no thirst tonight.
Romanian: Marele domn își așteaptă fiica.
English: The Great Lord awaits his daughter.
Romanian: Daţi-mi... caietul de hotărâri. Poftiţi, dle general.
English: Here it is, general.
Romanian: Imaginativ ?
English: Imaginative?
Romanian: - Ia spune-mi, eu n-am văzut nicio barză.
English: Say, I didn't see no stork. - Shush.
Romanian: Acuma, nu începe să plângi, Judy.
English: Now, don't start to cry, Judy.
Romanian: Alta n-are.
English: I can't get a new one.
Romanian: Egiptenii credeau că amuleta asta îi apără de forţele răului, forţele care l-au răpus pe tatăl tău.
English: That amulet, the Egyptians believed, was a charm against evil sendings, such as struck down your father.
Romanian: Adică ?
English: How so?
Romanian: Întâi o să-ţi povestesc cum I-am întâInit pe tip.
English: First, I'll tell you how I met the guy.
Romanian: Să ne fie mereu la fel de bine ca astăzi.
English: May they never be less happy than they are at this moment.
Romanian: Vă spun că nu mint.
English: I tell you I'm not lying.
Romanian: Doamnă Dowling.
English: Mrs. Dowling.
Romanian: - Cum e posibil?
English: - How is that possible?
Romanian: Să-i înveselesc.
English: Make them laugh.
Romanian: Așezați-vă.
English: Sit down. Thank you.
Romanian: Ai grijă !
English: Watch out!
Romanian: Greutate: 86 kg.
English: Weight, 190 pounds.
Romanian: Cum mai merge, Frank ? Nu prea rău, Pete.
English: - How's everything been, Frank?
Romanian: Doar tu mă poţi ajuta.
English: You're the only one who could help us now.
Romanian: Priveşte!
English: Look.
Romanian: Sau supără-te cât vrei.
English: Oh, be as angry as you like.
Romanian: Nu trebuie.
English: My dear, you don't need to.
Romanian: Pune-i pe loc repaos, te rog.
English: Stand them at ease, please.
Romanian: Ce s-a întâmplat ?
English: What's happened?
Romanian: Dar undeva interesant"
English: But somewhere with a mixed clientele.
Romanian: Nu le-am văzut niciodată aşa de aproape.
English: I've never seen them so close.
Romanian: La urma urmei, ce petrecere de logodnă e asta, fără logodnic ?
English: After all, what's an announcement party without a fiancé?
Romanian: Sunt sigur ca habar nu are.
English: I'm sure she has no idea.
Romanian: O bancnotă de 1.000 de dolari.
English: A thousand dollar bill.
Romanian: "Ieşi din teren şi nu te mai întoarce niciodată !"
English: "Get off this field ... AND DONO'T COME BACK !"
Romanian: Dar ar putea cobori intr-un minut sau altul.
English: But they can get off at any time.
Romanian: Omul puternic al trupei de acrobaţi.
English: The strong man of the acrobatic troupe.
Romanian: Acum, nu trebuie să te îngrijorezi pentru nimic, doar să dormi puțin.
English: Now, you're not to worry about anything except getting a little sleep.
Romanian: Alții ar putea cenzura manierele rurale ale judecătorului Priest în tribunal.
English: Others may censure the homespun manners ofJudge Priest on the bench.
Romanian: Numai dacă am putea face-o şi pe mătuşa Katherine să dispară...
English: Now if we could just get Aunt Katherine to disappear...
Romanian: În regulă, continuă-ţi treaba.
English: All right, keep on the job.
Romanian: Mulţumesc.
English: Thank you.
Romanian: Crezi că te-a turnat cineva, uriaşule ?
English: You think somebody turned you in, Big?
Romanian: - Da, tată, asa-i.
English: Yes Father, I suppose I did.
Romanian: - Bine, Joe.
English: Okay,Joe.
Romanian: Ce s-a întâmplat cu tine în seara asta, Brown?
English: What happened to you, Brown?
Romanian: - Oricum, cam asa a început totul.
English: - Anyway, that's how it all began.
Romanian: Bună, tinere! Bună ziua.
English: -hey, young man.
Romanian: S-o terminăm.
English: Finishing it.
Romanian: - Da.
English: - Well, yes.
Romanian: Mai durează un minut.
English: iii only be another minute.
Romanian: Ca şi Tintin.
English: Like Tintin.
Romanian: - Îl aveţi, nu-i aşa?
English: - You have your deed, of course?
Romanian: O clipă.
English: Just a moment.
Romanian: Ce ma nelinisteste este OPTUL.
English: What's bothering me is the eight.
Romanian: Ar putea fi un spărgător.
English: It might be a burglar.
Romanian: Mulțumesc.
English: THANKS.
Romanian: Că te-ai împuşcat.
English: That you shot yourself.
Romanian: Ceva are nevoie de atenţia mea, ceva foarte personal.
English: Something needs my attention, something very personal.
Romanian: Este un moment decisiv.
English: This is a decisive moment.
Romanian: Salonul de muzică al castelului Chambord.
English: The music room of chambord castle.
Romanian: - Bună dimineaţa, d-na.
English: Good morning, Madame.
Romanian: Interzis cu caini
English: THE GREEN LANTERN NO DOGS ALLOWED
Romanian: Când un bărbat îşi ruinează viaţa pentru ea, dragostea lui e adevărată.
English: When a man ruins his life for something, it's liable to be pretty real.
Romanian: Pentru că prefer carnea de vită şi varză?
English: Because I like corned beef and cabbage?
Romanian: Eu?
English: Oh, it's a silly hoax.
Romanian: - Refrenul în fa diez.
English: - The chorus in F-sharp.
Romanian: Hai să ne întoarcem.
English: Let's turn back.
Romanian: Oricum, mă bucur că te-ai întors şi ai respectat înţelegerea... şi sper că te vei menţine mereu aşa.
English: Anyway, I'm glad you're back and squared your account... and I hope you'll always keep it that way.
Romanian: Pe cine?
English: Who?
Romanian: Nu poți pleca așa.
English: You can't walk out like this.
Romanian: Trei saptamini repetitii si doua saptamini de lucru, daca am noroc.
English: Three weeks rehearsal and two weeks work if I'm lucky.
Romanian: A fost ţinut timp de un an, dar a evadat de la azil.
English: They've had him away for over a year but he escaped from the asylum.
Romanian: - "Comunică cu Herbert MacCaulay."
English: - "Communicate with Herbert MacCaulay."
Romanian: Raskolnikov.
English: Raskolnikov.
Romanian: - Destul, Janice.
English: - Cut it out, Janice.
Romanian: Nu ma intereseaza.
English: I'm not interested. How much?
Romanian: Minunat, nu-i aşa ?
English: Lovely, isn't it?
Romanian: Cât ți-am promis pentru un mic document ca acesta?
English: How much did I promise you for a little document like this?
Romanian: Si tinerii casatoriti trebuie sa aiba bune maniere.
English: Even newlywed, you know must have good manners.
Romanian: E-n regula,Pete.
English: Now, that's all right, Pete.
Romanian: Zizzi.
English: Zizzi.
Romanian: Nu crezi că aş putea să o iau pe doamna şi să plecăm de aici ?
English: Come on, you don't think I'm going to take the lady away from you?
Romanian: Vă cer scuze, doamnă, dar vă caută o tânără de la agenția de ocupare a forței de muncă.
English: I beg your pardon, madam, the young woman from the employment agency.
Romanian: La care dană, domnule?
English: "What pier, sir?"
Romanian: Aşa face tot timpul, parcă ar fi un predicator negru.
English: He goes on that way all the time like a Negro preacher.
Romanian: Adună-te.
English: [Whistle Blows] [Man Yells Orders]
Romanian: Bună Gottlieb ! Mereu o dai în bălării !
English: Hi, Gottlieb, always beating around the bush.
Romanian: Nu îți place duminica după-amiază?
English: Don't you just love Sunday afternoons?
Romanian: Ia du-te şi vezi dacă-s pe la grajduri.
English: Go to the stables and see if I'm there.
Romanian: Luaţi ceva de băut?
English: Get yourself a drink. Won't you?
Romanian: Dna Walker.
English: Mrs Walker.
Romanian: - Dra Docto r.
English: Fräulein Doktor.
Romanian: Mackie !
English: Good heavens, Mackie!
Romanian: - E o tusă de iarnă.
English: It's a winter cough.
Romanian: Ba sunt căsătoriţi.
English: They're married, all right.
Romanian: Hai să-ţi arăt ce-am ales eu.
English: Let me show you what I picked out.
Romanian: Ar fi bine să te agăți de acel contrabandist al tău.
English: You better hang on to that bootlegger of yours.
Romanian: - Da. Am nevoie de bani.
English: I'll need money.
Romanian: Dacă un astfel de bărbat eşti, mai bine mai duce acasă.
English: Well, if that's the kind of a man you are, you can take me home.
Romanian: Ţi-ai jucat rolul în această piesă!
English: Your role played out!
Romanian: - Petrie este mort?
English: Is Petrie dead? ─ Petrie?
Romanian: Pur și simplu aleg un număr și pariez pe el, iar dacp câștig, colectez.
English: I just pick a number and bet on it and then when it wins, I collect.
Romanian: Apropo, dle Evans. De ce vrei să știi ce au zis soții Dryden?
English: By the way, Mr Evans, What made you ask what the Drydens said when they heard the news?
Romanian: Ce mai faceţi, oameni buni ?
English: How do you do, everybody?
Romanian: Poți să înțelegi ce spune sau ai uitat?
English: Can you understand what he says or have you forgotten?
Romanian: Mai ia-l o singură dată.
English: One more snoop.
Romanian: Ma sufoc.
English: I need fresh air.
Romanian: Haide.
English: Come on.
Romanian: Ascultă, Potpot.
English: Now, listen, Potpot.
Romanian: - Dumneata ești om cumsecade.
English: You're a good man.
Romanian: Iar tu vei avea o casă bună aici, dacă te porţi frumos.
English: And you'll have a good home here if you behave.
Romanian: In mod evident facuta de un anumit tip de bisturiu folosit pentru operatii pe creier.
English: Obviously made by some type of scalpel used for brain dissecting.
Romanian: - Mă iubeşti?
English: - You love me?
Romanian: Da.
English: Oh, yes.
Romanian: - Esti inca un clovn.
English: - You are still a clown.
Romanian: - Noapte buna, Bob.
English: - Goodnight, Bob.
Romanian: Indiferent ce ai crezut că ştii, Thursby nu l-a omorât pe Archer.
English: Well, if you thought that you were right, Thursby never killed Archer.
Romanian: Dar nu am trimis acel bilet, dacă asta vrei să spui.
English: But I didn't send that note, if that's what you mean.
Romanian: Este vorba despre doi irlandezi, Pat și Mike!
English: It concerns two irishmen, pat and Mike!
Romanian: Trebuie să vă mărturisesc ceva, Înălţimea Voastră.
English: "I must confess to something to His Highness"
Romanian: De aceea nu pot sa incep raportul.
English: That's why I can't start the report.
Romanian: De la fam.
English: The Mallorys.
Romanian: Ştii, nu irosi toată dragostea pe iarbă şi lucruri.
English: You know, I won't have you squandering all that love on grass and things.
Romanian: Marinarul care a vazut cum a fost ucisa femeia de serviciu in seara asta spune ca ucigasul a avut o fata desfigurata oribila.
English: That sailor who saw the scrubwoman killed tonight says the murderer had a face that was horribly disfigured.
Romanian: "Este o domnişoară, pe numele de Florence Forster."
English: She is called Miss Florence Forster.
Romanian: Îmi spune Maloney.
English: Can you imagine calling me Maloney?
Romanian: Nu, n-aş putea face asta!
English: No, I couldn't do that!
Romanian: Şi să te ţină, mamă...
English: " Mother "
Romanian: "Ai o soţie draguţă !"
English: "You have a fetching wife!"
Romanian: Dacă există curent, înseamnă că apa provine din Nil.
English: If there's a current, that means this water comes from the Nile.
Romanian: Acum e jos.
English: He's downstairs now.
Romanian: -Vrei sa-ti faci ziarul acolo?
English: - Gonna start your newspaper there? - Yeah.
Romanian: O să ratez genul de tortură prin care treci tu acum.
English: I'LL HAVE MISSED THE KIND OF TORTURE YOU'RE GOING THROUGH NOW.
Romanian: Vândută pentru 125 de dolari! Vă mulţumesc, oameni buni, pentru bunătatea voastră!
English: Sold for 125 dollars and l thank you for your kind attention.
Romanian: Spuneţi-mi...
English: Tell me.
Romanian: Oricum, aflu că ai o soţie şi 2 copii.
English: Now I find out you have a wife and two children.
Romanian: Supă minunată. Minunată.
English: Beautiful soup, beautiful...
Romanian: - Acesta este ultimul pai !
English: - This is the last straw!
Romanian: Am făcut o mică greşeală.
English: We've made a little mistake.
Romanian: Vezi, Lilli?
English: You see, Lilli?
Romanian: Da, sigur...
English: Here you go.
Romanian: "FOUR INFANTRYMEN ON THE WESTERN FRONT"
English: "FOUR INFANTRYMEN ON THE WESTERN FRONT"
Romanian: Am participat la acel jaf armat.
English: I was in on that bank stick-up.
Romanian: Tocmai am venit din Berlin.
English: - No. I just came from Berlin.
Romanian: - O clipă.
English: - Just a minute.
Romanian: - Annie!
English: - Annie!
Romanian: Spune-le aşa:
English: Tell them:
Romanian: - Mulţumesc!
English: - Thanks.
Romanian: - Despre ce vorbeşti ?
English: - What are you talking about?
Romanian: N-am mai simţit niciodată sentimentele pe care le nutresc acum.
English: Never before I'm feel such terrifical vibrations as I am feel now.
Romanian: - Alo?
English: - Hello?
Romanian: Poate că mă înşel.
English: Maybe I'm wrong.
Romanian: Merităm partea noastră de fericire, nu crezi?
English: We deserve a little happiness, don't you think?
Romanian: Păi... poate e totul în regulă.
English: - Well, maybe you're right.
Romanian: - Saidi!
English: - Saidi!
Romanian: Aduceţi-l aici imediat !
English: Bring him in immediately!
Romanian: Ca să fie ucişi cu sânge rece. Oh, nu, nu, nu!
English: - To be shot down in cold blood.
Romanian: Nu te cunosc eu mai bine decât te cunoşti chiar tu?
English: Don't I know you better then you do yourself?
Romanian: O, uite!
English: Oh, look!
Romanian: - Sunt ocupat.
English: - I'm busy.
Romanian: Cât ceri pe el... 30.000 de dolari?
English: What are you asking for it... $30,000?
Romanian: Nimic.
English: Nothing.
Romanian: Cum pot să aştept, Louis ?
English: How can I wait, Louis?
Romanian: Unde îţi este musafirul?
English: Where's your visitor?
Romanian: M-ai sunt multe lucruri de făcut înainte ca Ali Bey să aibă încredere în mine.
English: There's still a lot of work to be done before Ali Bey feels he can trust me.
Romanian: Buck
English: Buck.
Romanian: Se vede limpede că sunteţi mişcat.
English: I can see you care.
Romanian: Am uitat.
English: Oh, now, I must have forgotten it.
Romanian: - Cum ajung în avion?
English: - How do I get on the plane now?
Romanian: Acel om mi-a adus, doar insulte !
English: That man has covered me with insults!
Romanian: Bravo. Bravissimo.
English: Bravo, bravissimo.
Romanian: Mulţumesc!
English: Thanks...
Romanian: Ești nebun?
English: Are ya crazy?
Romanian: Bătrânii Bunding au murit de mult, iar Joe cântă din nou într-un circ ambulant.
English: The old Bundings passed away long ago, and Joe is back performing with a touring circus.
Romanian: Vin mâine. - Ce e cu ordinul ăsta?
English: - What's this writ?
Romanian: Ciudatul om pe care-l numiţi monstru, e mort.
English: This strange man you call a monster is dead.
Romanian: - Nu ?
English: - No?
Romanian: Sună bine pentru mine.
English: - That sounds good to me.
Romanian: Ei bine, atât timp cât pare să fie o aventură de familie, aș putea la fel de bine să îți spun asta.
English: Well, as long as this seems to be a family affair, I might as well tell you.
Romanian: Eu... uh, tocmai ce-am venit de la Crawling Stone Flats.
English: I just came in from Crawling Stone Flats.
Romanian: Dar!
English: But!
Romanian: Le place să se joace în valuri... înotul este foarte popular vara, când temperatura creşte peste zero.
English: They dearly love to play in the waves for surf bathing is very popular in the summer-time when the temperature rises above Zero.
Romanian: Să-i permiți Lindei ?
English: Permit Linda?
Romanian: Dar acum înţeleg.
English: But now I see.
Romanian: Îmi placi.
English: I like you.
Romanian: Voi fi acolo.
English: I'll be there.
Romanian: Avem aceleași șanse ca și altele.
English: We stand as big a chance as anybody else.
Romanian: Vinde mii de peri pe an.
English: He sells thousands of brushes a year.
Romanian: Ia-ţi mâinile de pe bijuterii.
English: Hands off jewelry.
Romanian: L-am văzut în seara aceasta.
English: I saw him tonight.
Romanian: - Monstrul, el a luat-o !
English: The monster, he's got her!
Romanian: Mă duc până la frontiera Arabă ca să cumpăr o hoardă de cai.
English: I'm going up on the Arabian frontier to buy a pack of horses.
Romanian: Într-o schemă ca asta?
English: In a racket like this?
Romanian: Şi asta este tot ce îmi amintesc.
English: And that's all I remember.
Romanian: Mănăstirea poate fi foarte atrăgătoare, nu-mi pot decât imagina... O să aibă nevoie de o mulţime de reparaţii.
English: The abbey could be very attractive, but I should imagine... it would need quite extensive repairs.
Romanian: - N-am găsit niciuna, dle.
English: - Couldn't find any, sir.
Romanian: - Îți doresc noroc.
English: - Wish you luck.
Romanian: Criminalul nu a fost prins.
English: Murderer not apprehended."
Romanian: H-3.
English: H.3.
Romanian: Nu, prietene.
English: No, my friend.
Romanian: Am dreptate, Gypo?
English: Am I right, Gypo?
Romanian: Este sora ta.
English: It's your sister.
Romanian: Vei fi senzaţia sezonului.
English: You'll be the season's sensation.
Romanian: Oricând va voi să plece. De ce întrebaţi ?
English: Whenever she wants to go.
Romanian: Nepoata mea, Excelenţă?
English: My niece, Excellency?
Romanian: Că veni vorba, cum este germana ta?
English: By the way, how's your German?
Romanian: Accesul interzis până săptămâna viitoare.
English: No admittance until week after next. Why...
Romanian: Contacteaza sediul central, Colonele, si informeaza-i ca l-am capturat pe H-14, din Serviciul Secret Rus,
English: Wire headquarters at once, Colonel, and inform them of the capture of H-14, of the Russian Secret Service,
Romanian: - Robert!
English: - Robert!
Romanian: Imaginea insasi a puritatii.
English: The image of purity.
Romanian: - Noi nu credem ca cineva are o pshihoza pe termen lung.
English: – We don't believe that anybody has a long term psychosis.
Romanian: Acelaşi traseu ca Malaezia.
English: The same voyage as The Malaisie.
Romanian: "Palatele oraşelor necunoscute,
English: The palaces of unknown cities,
Romanian: Eu sunt cazat la hotelul Palace.
English: Ah. I am staying at the Palace Hotel.
Romanian: - Vrea să se căsătorească cu tine, nu?
English: He wants to marry you, eh?
Romanian: - Ł20.
English: - Ј20.
Romanian: - Bine. Minunat.
English: Hold a minute.
Romanian: Ce ai de data asta?
English: What have you got this time ?
Romanian: Asta o să-mi placă.
English: You'll love this, Barb.
Romanian: - Doar puţin obosită.
English: - Just a little tired, that's all.
Romanian: Pe ce nume să-l scriu?
English: How shall I make it out?
Romanian: Eu, unul... aş prefera cu langustă.
English: I'd rather have some crayfish.
Romanian: Nu ar avea rost!
English: It would be no use!
Romanian: Trebuie, Drexler.
English: It must be done, Drexler.
Romanian: A luat slujba asta în locul altei fete pentru că era într-o situaţie precară.
English: She took this job in place of another girl... because she was hungry.
Romanian: N-ai aflat?
English: You haven't heard ?
Romanian: "Soţii noştri trebuie să moară pentru că Regele vrea să construiască o trezorerie ? "
English: Because the king wants to build his treasure house. for that, our men must die?
Romanian: - Stai puţin.
English: - Wait a minute.
Romanian: Unul dintre cei mai buni.
English: One of the greatest.
Romanian: Conversaţia noastră s-ar fi putut termina de mult.
English: Why didn't I think of it? Our conversation could have been over long ago.
Romanian: E o păcăleală.
English: I thank you.
Romanian: Dar nu vad nici unul suficient de lung pentru camaradul Tjaden.
English: But I don't see any long enough for our comrade Tjaden.
Romanian: Oh, Jerry,
English: Oh, Jerry,
Romanian: - 176?
English: - 176?
Romanian: De ce a fost execuţia oprită ?
English: Why was this execution stopped?
Romanian: Prizonierii vor veni cu mine în cealaltă barcă.
English: Prisoners go with me in the other boat.
Romanian: Pe la ora 9 voi alerga aici... să ne revedem...
English: But around 9 o'clock, I will run here ... to see you again!
Romanian: Aşa cum spui.
English: Just as you say.
Romanian: Care vrea să fie singură.
English: Who wishes to be alone.
Romanian: - Iară e liliacul acela.
English: - There's that bat again.
Romanian: ... întreaga lume s-a schimbat.
English: the very world did change.
Romanian: - Ai ceva cap, nu-i aşa?
English: - You've got a brain.
Romanian: - Desigur.
English: - Of course.
Romanian: "În legătură cu ce, Generale ?"
English: What about, General?
Romanian: Anunţaţi-o pe Prinţesa ca moştenitoare a tronului şi oamenii vor crede că e un băiat !
English: Announce the Princess as the heir to the throne and the people will believe it is a boy!
Romanian: Sus!
English: Up!
Romanian: Nu îţi vrem răul.
English: We don't mean you any harm.
Romanian: Am doar 17 cenţi.
English: I've only got 17 cents.
Romanian: Credeam că ai suflet...
English: "I thought you had a heart.
Romanian: Ce s-a întâmplat ?
English: What happened?
Romanian: De ce vrei asta?
English: Why do you want to?
Romanian: Intră acolo.
English: Get in there.
Romanian: Nu este momentul sau locul pentru eroism.
English: This isn't the time or the place for heroics.
Romanian: Încearcă din răsputeri.
English: She tries hard enough.
Romanian: I-am spus același lucru de multe ori, dar nu m-a ascultat.
English: I told him the same thing many a-time, but he wouldn't listen to me.
Romanian: Totul s-a dus.
English: Everything's gone.
Romanian: - Chiar aşa?
English: - Is that so?
Romanian: Am spus ora 9.
English: I said 9 o'clock.
Romanian: DO NOT TURN A DEAF EAR TO MlSFORTUNE
English: DO NOT TURN A DEAF EAR TO MISFORTUNE
Romanian: Tâmpit, dacă m-ai întreba pe mine.
English: Stupid, if you ask me.
Romanian: Căci suntem drăgălaşi.
English: We're naughty, but we're nice
Romanian: Copoiul de la Criminalistică.
English: The crime commission buzzard.
Romanian: Spune-le să nu mai tureze motoarele peste 1900 de rotaţii.
English: Tell them to stop turning up the motors over 1900 revolutions.
Romanian: Cine nu este ?
English: Who isn't?
Romanian: Esti asa de buna.
English: You're so kind.
Romanian: Spune că a studiat agronomia în Brno şi vrea să studieze şi aici.
English: Now, he says that he went to a farming school in Brno. 'And he also want to go to school here.'
Romanian: - Eşti Jean?
English: - Are you Jean?
Romanian: Aşa am să fac.
English: I will.
Romanian: Cu toate că nu este treaba nimănui, îţi spun, dacă promiţi să nu zici nimănui. Bineînţeles că nu o să spun.
English: Although its nobody´ss affair but mine, I might tell you if you promise not to repeat it.
Romanian: [Suspine]
English: [Sobbing]
Romanian: O declaraţie despre reforme.
English: How about a statement for the papers? Yeah, give us the lowdown on the Reform racket.
Romanian: Asta a fost un adevărat succes.
English: That was an achievement.
Romanian: Era destul de dur.
English: Plenty tough, too.
Romanian: Acel loc este capătul extrem al Pământului...
English: That spot is the uttermost end of the earth...
Romanian: Da, doamnă.
English: Yes, ma'am.
Romanian: Cât de mulți dintre ei râd de mine?
English: And how many of them are laughing at me?
Romanian: Dragă, și doream să-l văd.
English: Oh, dear, and I wanted to see him.
Romanian: - Sper că nu.
English: - I hope not.
Romanian: - Nu mă deranjează.
English: I don't mind. When will you come?
Romanian: De unde știi care este partea mea a gardului ?
English: How do you know what my side of the fence is?
Romanian: Ştiu o scurtătură!
English: "I know a short cut...
Romanian: - Mary?
English: - Mary?
Romanian: Nu am ce să-ţi ofer. Sunt măritată.
English: You see, I'm not my own to give.
Romanian: La revedere, Bill.
English: Goodbye, Bill.
Romanian: Ei sunt cei care ar trebui sa fie in lanturi, nu eu!
English: They're the ones that should be in chains, not me!
Romanian: Vrei să-l încerci?
English: Would you like to try it?
Romanian: Vreți să spuneți că acest om mi-a folosit mașina?
English: You mean to say that this man used my car?
Romanian: Cum ?
English: How?
Romanian: Apoi, pentru a ascunde corpul, l-a târât în ​​dulap.
English: Then, to hide the body, he dragged it into the closet.
Romanian: Iată-ne din nou înpreună, ca o mare familie fericită.
English: Here we are all together again, just like one big, happy family.
Romanian: Poate pleca sau nu?
English: Hey, can he go or not?
Romanian: Mașina mea e mai importantă pentru mine decât nepoata ta !
English: My car is more important to me than your niece!
Romanian: Pe aici.
English: Right this way.
Romanian: - Helen, te rog.
English: Oh, now, Helen, please.
Romanian: - Nu, încă nu.
English: NO, NOT QUITE.
Romanian: Știi că tata lucrează în fiecare miercuri seara.
English: You know daddy works every Wednesday night.
Romanian: Ești bine acum?
English: Are you alright, now?
Romanian: - Cu mare plăcere.
English: - Oh, we'd be very glad to.
Romanian: Au trecut atâţia ani.
English: So many years ago.
Romanian: Despre ce vorbeai cu Young la telefon?
English: What were you and Young talking about on the telephone?
Romanian: Veniti aici, oameni buni! Avem o adevarata atractie!
English: Over here, over here, over here, folks, we have a free attraction.
Romanian: - O pot vedea în ochii tăi.
English: I can see it in your eyes.
Romanian: Amaratul, normal in toate celelalte momente, este obligat sa traiasca pe scena actiunii care l-au condus in primul rand spre nebunie.
English: The poor devil, sane at all other times, is forced to live over the scene of the action that first drove him mad.
Romanian: Adolphe...
English: Adolphe.
Romanian: Dar el pe tine te cunoaşte.
English: But he knows you.
Romanian: Mai aveti o ipoteză!
English: Maybe you have a hypothesis?
Romanian: De ceva timp, am ştiut că am greşit unindu-mi viata cu a ta.
English: For some time... For some time, I have known that in uniting my life to yours, I have made a mistake.
Romanian: - Haide, mâncătorule de muşte.
English: - On your way, old fly eater.
Romanian: Scoate-ţi pantalonii.
English: Drop your trousers.
Romanian: Ai auzit doar o reproducere mecanica.
English: You only heard a mechanical reproduction of it.
Romanian: De asta îmi e şi teamă.
English: - That's just what I'm afraid of.
Romanian: - Lasă-mă să încerc.
English: - Please let me try. It's worth it, Harry.
Romanian: Bineînțeles, că nu.
English: No, of course not.
Romanian: Dar a o îmbrăca este o problemă.
English: But getting her dressed is a problem.
Romanian: Hai!
English: Hurry up!
Romanian: Gerald nu trebuie să le vadă Înainte de căsătorie.
English: Gerald should not see him before the wedding.
Romanian: A multumit cerului ca e? ti în viata.
English: She blessed the saints that you're alive.
Romanian: Te vei simţi mai bine.
English: You'll feel better.
Romanian: O superstiţie periculoasă, Tigellinus... spune că cel blând va moşteni ce aparţine celui puternic... care acceptă alt Dumnezeu în locul meu.
English: A dangerous superstition, Tigellinus... that teaches that the meek shall inherit that which belongs to the mighty... that accepts another god in place of myself.
Romanian: Voi şterge orice răutate de pe pământ şi toate femeile vor învăţa să nu o imite.
English: That's how I'll put an end to all the evil on earth and all the women will learn not to imitate their abominations!
Romanian: Şi ce-i cu asta?
English: Well, what about it? !
Romanian: Fecioarele erau duse la "Piaţa Căsătoriilor"
English: Maidens chosen for the marriage market.
Romanian: - O să plec acum.
English: I'm off.
Romanian: Ce fel de geantă era?
English: What kind of a bag was it?
Romanian: Baron, aţi ieşit afară?
English: Baron, are you out?
Romanian: Atunci, fii atent !
English: I mean no, captain.
Romanian: Îmi amintesc odată când zburam în Omaha cu o femeie şi cu fiul ei care avea dureri de dinţi.
English: MAN: l remember one time l was flying an old girl who had a son in Omaha with a toothache.
Romanian: Bineînţeles că pot
English: Of course I cen.
Romanian: Cartile astea intinse peste tot.
English: Αll these books lying about.
Romanian: - 2,500 neacoperiti.
English: - 2,500 uncovered.
Romanian: Nu cât n-are un tată!
English: Not as long as she ain't got no pa!
Romanian: Nu-i nevoie, șefule.
English: It's all right, guvnor. It's all right.
Romanian: - Da, Smitty ar vrea asta.
English: Yeah, Smitty'd like that.
Romanian: Nu poate sa scape usor.
English: -Yeah.
Romanian: - Aşteaptă aici.
English: -You wait here.
Romanian: Ajutor!
English: Help!
Romanian: I-am spus că greşeşte tratându-şi astfel fiul, dar fără nici un rezultat.
English: I told him how wrong it is to hold a grudge against his own son. It's useless.
Romanian: Trebuie să-i pese! Dacă are conştiinţă.
English: He must, when it's put to him, if he has any decent feeling.
Romanian: şi că e pe drum.
English: And that's on its way.
Romanian: Te-ai distrat?
English: Did you have a good time?
Romanian: Mă voi simti mai bine după ce trecem dincolo.
English: I'll feel much better when we've put all this behind us.
Romanian: În regulă, voi termina până la cină.
English: All right, I'll be over for dinner.
Romanian: Odată era o fată drăguță
English: Once there was the sweetest girl
Romanian: Nu arată prea bine ?
English: Not an attractive crowd, eh?
Romanian: Aşteptaţi puţin, să vă ajut.
English: Just a moment. Maybe I can help you.
Romanian: O să-ți pară rău.
English: You'll be sorry.
Romanian: Vino, vino...
English: Come, come, come...
Romanian: La telefon Samuel Dodsworth.
English: This is Samuel Dodsworth speaking.
Romanian: Sunt asistenta d-lui Julian de Lussac.
English: This is Mr. Julian de Lussac's trained nurse.
Romanian: Nu o s-o vezi.
English: You're not going to see her.
Romanian: Taci...
English: Don't...
Romanian: - Whiskey?
English: ─ Whiskey?
Romanian: Îţi cumpăr eu ceva de băut.
English: I buy you a drink.
Romanian: O uşă zăvorâta nu este prea prietenoasă.
English: A bolted door isn't very friendly.
Romanian: Vila din deșert a șeicului Ahmed Ben Hassan, renumitul tată al tânărului Ahmed.
English: "The desert villa of Sheik Ahmed Ben Hassan, young Ahmed's famous father."
Romanian: - Nu, a fost uşor.
English: - No, it was easy.
Romanian: - Mulţumesc.
English: - Thank you. Yeah.
Romanian: - HENRIETTA
English: -HENRIETTA
Romanian: Ia o pauză, fumează o ţigară.
English: Go on, get yourself a smoke.
Romanian: Aveţi de gând să veniţi la petrecere în seara asta?
English: You planning to come to the party tonight?
Romanian: Vrea să omoare pe toată lumea...
English: He wants to kill the whole world ...
Romanian: Nu lipsesc mult, dragule.
English: I shan't be long, darling.
Romanian: Nu ai ascuns o Katherine Howard care a jucat împotriva reginei mele?
English: - Oh, you knew about that all the time.
Romanian: Nu trage !
English: No shooting!
Romanian: Mai tarziu, o sa fim distrati de niste cantarete.
English: Later on, we'll be entertained by some singsong girls.
Romanian: Regi ai Cruciadei, ăsta-i răspunsul lor la mesajul nostru.
English: Kings of the Crusade, this is their answer to our herald.
Romanian: - Aveţi de gând să-i încasaţi?
English: - Are you going to cash that?
Romanian: M-am chinuit mult aseara, dupa ce am plecat, sa obtin niste informati despre tine.
English: I took a lot of trouble last night, after I left, to obtain some information about you.
Romanian: Și ultima dată nu au fost suficient de mari. Știu.
English: And the last time they wasn't big enough.
Romanian: Fa-o chiar si daca nu o intelegi, si iti promit, sunt asa de sigura,
English: Do it even blindly if you must, and I promise you, I'm so sure of it,
Romanian: - Multumesc, draga.
English: - Thank you, dear.
Romanian: "Nu-mi pasă ce crede lumea"
English: "I don't care what people say"
Romanian: S-ar putea chiar să găsești o altă tumoră sacrococcigiană, care să te mângâie.
English: You may even find another sacrococcygeal tumour to comfort you.
Romanian: Venim din lumi diferite.
English: We come from different worlds.
Romanian: Obţine bijuteriile de la Ducele de Buckingham şi întoarce-te cu toate grabă.
English: Get the jewels from the Duke of Buckingham and return in all haste.
Romanian: Îţi face rău.
English: It's bad for you.
Romanian: Multumesc.
English: - Thank you.
Romanian: Șaizeci si cinci.
English: 65.
Romanian: Oraşul ăsta e diferit, de când a plecat.
English: This town's different than when he left.
Romanian: Contele Muffat, şambelanul împărătesei.
English: Count Muffat, the Empress's Chamberlain.
Romanian: Nu voi uita niciodată.
English: I shall never forget it.
Romanian: Deci nu credeţi că o dată am împuşcat un leu?
English: So you don't believe I got a lion once?
Romanian: Au plecat ?
English: They've gone.
Romanian: Nu-mi răspunde la telefon de două zile !
English: I haven't been able to get through to him for two days!"
Romanian: Și ție... cum îți plac schițele mele îndrăznețe, draga mea?
English: And you... How do you like my bold strokes, my darling?
Romanian: Pe tine te vrem, Brant!
English: We want you, Brant.
Romanian: - Esti casatorita?
English: -Are you married?
Romanian: - Aici e unul pe care nu-l poti face.
English: - Here's one you can't do.
Romanian: Misca.
English: Move.
Romanian: Îmi dau seama de risc.
English: I know the risk.
Romanian: Nu ştiu.
English: I don't know.
Romanian: - Du-te, Clodia.
English: - Go, Clodia.
Romanian: Aş vrea să-mi lumineze viaţa.
English: I wish she'd take a shine to me.
Romanian: În realitate, sunt deţinute de un grup mic, format din şase-şapte persoane.
English: As a matter of fact, it's very closely held. Only six or seven people in all.
Romanian: Cineva vine încoace, d-le.
English: Someone's coming this way, sir.
Romanian: - Cine-i ?
English: - Who's that?
Romanian: Vino, Stan. Unde vrei să pleci?
English: Come, Stanley.
Romanian: Intoxicată de bucurie a alergat, ca şi cum ar avea aripi...
English: Overjoyed, she ran as if on wings...
Romanian: Suntem aglomeraţi.
English: We're snowed under.
Romanian: Nu o înțeleg
English: I don't understand it
Romanian: Sportivul multidisciplinar Georges André, cunoscut ca
English: Multi-disciplined athlete Georges André, known as
Romanian: - Fata are bani?
English: - Has the girl money?
Romanian: 55?
English: 55?
Romanian: Când ai venit?
English: When did you get here?
Romanian: - Calul meu!
English: - My horse!
Romanian: Ai ordonat uciderea lui Mah-Li.
English: You've ordered the murder of Mah-Li.
Romanian: Scuzaţi-mă.
English: Excuse me.
Romanian: Toți ceilalți din familia mea sunt, cu excepția lui Arthur, care s-a înșelat.
English: Everyone else in my family is, unless Arthur was mistaken.
Romanian: Si am nevoie de ajutorul vostru.
English: And I want your help.
Romanian: E minunat.
English: It's so wonderfully beautiful here.
Romanian: Lasă-mă, mă răneşti..
English: Let go of my arm. You're hurting me.
Romanian: Poftim!
English: Here.
Romanian: Şi vizavi de comodă...
English: On the other side...
Romanian: - Să mă răneşti.
English: - Ha. Hurt me.
Romanian: Nu avem timp de astea acum.
English: There ain't no time for that now.
Romanian: Purtându-si frumoasele picioare de-a lungul sălii de dans
English: To drag her very weary feet around the ballroom
Romanian: Va fi în port peste o oră.
English: He's had his trial.
Romanian: Un film produs de
English: THE FILM OF
Romanian: Baby ai spus că este târziu, dar asta-i doar o aparenţă.
English: You say it's late, and I'm here to tell you, it only feels that way.
Romanian: Ei bine, imaginaţi-vă stând pe resturile morii.
English: Well, then, imagine yourselves standing by the wreckage of the mill.
Romanian: - Atât de mult timp?
English: - Out of his...? All that time?
Romanian: Le-aş numi "ariengarda".
English: I would call them the rear-guard.
Romanian: Cred că devin prea nervos.
English: I guess I'm getting jumpy.
Romanian: Acum cheam-o pe Nicole!
English: Now go and get Nicole.
Romanian: Marcus.
English: Marcus.
Romanian: - Este foarte simplu.
English: - You see, it's very simple.
Romanian: De ce nu a intrat?
English: Why doesn't he come in?
Romanian: Ce-i cu Péman?
English: What about Péman?
Romanian: Nu vor să ştie unde sunt.
English: I don't want them to know where I am.
Romanian: Spune-mi ce stii.
English: And not me going to say?
Romanian: Nu a apărut.
English: He no show up.
Romanian: Cinci mii de dolari, doar pentru mine?
English: - Yeah? - $5,000, all for me?
Romanian: O ştiu.
English: I know it.
Romanian: Ştie de petrecerea de ziua ei de mâine seară?
English: Does she know about her birthday party tomorrow night?
Romanian: Da.
English: Yes.
Romanian: Dacă pleacă toţi, ridicăm ancora şi fugim cu corabia.
English: If they all go, we up anchor and run with the ship.
Romanian: Răutate ce eşti! Dacă mai fugi de acasă, te bat!
English: You ran away from home... and I'm gonna spank you.
Romanian: Am deturnat fonduri!
English: I have embezzled funds!
Romanian: - O, deci mă recunoşti?
English: - Oh, so you recognize me?
Romanian: Fii atent cum il depasesc cu fumul ala puturos.
English: Watch me pass this mud turtle.
Romanian: Ai prieteni aici? - Nu.
English: Well, uh... no.
Romanian: Astea pentru ce-s?
English: What's this for?
Romanian: Intră!
English: Come in!
Romanian: - Transporta o turmă de tăuraşi.
English: Shipping a bunch of steers.
Romanian: Nu sunt ata de tampita.
English: I'm not that stupid for that.
Romanian: Ai vazut vreodata un tip ducandu-se la scaunul electric?
English: Did you ever see a guy go to the chair?
Romanian: Împreună ați făcut din petrecerea mea un mare succes.
English: TOGETHER, YOU'VE MADE MY PARTY THE GREATEST SUCCESS.
Romanian: Am să dansez pentru toată lumea, dar nu şi pentru femeia aia!
English: I'll dance for the whole world, but not for that woman!
Romanian: Este...
English: It's...
Romanian: - Hedrick, te rog să te porți frumos.
English: - Hedrick, please behave.
Romanian: Oh, deci asta e jocul tău.
English: Oh, so that's your game.
Romanian: Ce pete mici şi drăguţe aveţi acolo.
English: Charming little spot you have here.
Romanian: Ce e?
English: Yes, what is it? !
Romanian: - Copii.
English: - About children.
Romanian: Eu mă gândesc cum să-i fac pe alţii să danseze.
English: I'm figuring on making other people dance.
Romanian: Nu pot muri încă !
English: I cannot die yet!"
Romanian: O să tragă şi ai noştri.
English: Just keep on going. Aim towards the back.
Romanian: Nu-i suficient.
English: Oh, that's not enough.
Romanian: Nu!
English: No!
Romanian: - Philip, îmi pare rău că am întârziat.
English: Philip, I'm sorry I'm late.
Romanian: E ca și cum el a schimbat tot mobilierul din cameră, nu? Și toți trebuie să stăm așa cam--știi tu, am putea sta la marginea unui fotoliu, pe brațul fotoliului sau să facem altceva, dar, știi, el a schimbat tot mobilierul din cameră.
English: You can't do this without putting in the bad and the ugly, as well as what is beautiful, because if it is all beautiful you can't believe in it.
Romanian: Oricum ai da-o şi oricum ai întoarce-o,
English: No matter how you try to twist and turn it
Romanian: Nu pot să vin la călărie azi.
English: I cannot ride today.
Romanian: - Oh...
English: - Oh...
Romanian: Foarte interesant!
English: Very interesting!
Romanian: "Da...
English: "Yes.
Romanian: Spectatorilor noştri nu le place cum joacă în ultima vreme.
English: Our audiences do not like her work lately
Romanian: Dar amintiți-vă să nu confundați fata cu bătrânul.
English: I'll get the boys started on the drive.
Romanian: - Aşa cred, că ar fi bine.
English: - I think you'd better.
Romanian: Exact!
English: Exactly!
Romanian: Weisskopf a identificat ceasul purtat de ucigaș.
English: Mr Weiskopf's identified the watch worn by the murderer.
Romanian: Iată-i că vin pe dragii mei părinţi! Ar trebui să fiu prezent la tratatul de pace...!
English: "They are coming, my dear parents, I should like to be present at the Peace-treaty..."
Romanian: Vrei să vezi meniul, doamnă ?
English: Would you like to see the menu, ma'am?
Romanian: Uite-i că au venit!
English: Here they are!
Romanian: Ştii ce s-ar întâmpla cu însetatul, dacă n-ar mai primi apă?
English: Did you know what would happen to that thirst if it were denied water?
Romanian: Adică...
English: - You mean-
Romanian: FRANKENSTEIN
English: FRANKENSTEIN
Romanian: Lasă-mă să ghicesc unde sunt ascunşi.
English: Well... Well, let me guess where it's hidden.
Romanian: Cred că îl pot opri.
English: I think perhaps I can stop it.
Romanian: - De ce ?
English: - Why?
Romanian: Se spune că un bărbat trebuie mereu să doarmă pe partea stângă.
English: They say that a man should always sleep on his left side.
Romanian: Negativul B era probabil pentru piaţa germană.
English: The B negative was probably for the German market.
Romanian: Ce prostie din partea mea să fac o asemenea greșeală.
English: How stupid of me to make such a silly mistake.
Romanian: Mai bine vii data viitoare, Marvin, deoarece unii devin bănuitori foarte ușor.
English: You better come the next time, Marvin, as some folk get suspicious mighty easy.
Romanian: A spus că ar trebui să ne pregătim paşapoartele şi mergem pe peron.
English: He said we should get our passports and go outside.
Romanian: Oh, nu-i nimic.
English: Oh, that's all right.
Romanian: - Da, înțeleg, înțeleg.
English: - Yes, I understand, I understand.
Romanian: Sunt cu adevarat foarte rau.
English: I'm really terribly sorry.
Romanian: Mi-ar plăcea atât de mult să văd acel loc din spatele şemineului.
English: I would so like to see that little bit just behind the fireplace.
Romanian: Nu-i treaba ta.
English: None of your business.
Romanian: Nu, nu?
English: No. No?
Romanian: - Te voi găsi.
English: I will find you.
Romanian: Da, draga mea.
English: Yes, dear.
Romanian: A făcut ca Rosa să fie concediată !
English: He's get Rosa fired.
Romanian: - Vrei să salvezi barca?
English: - Want to salvage that boat?
Romanian: L-ai chemat pe fiul meu, fiindcă-ţi pare rău de mine?
English: So you sent for my son because you feel sorry for me, is that it?
Romanian: - Ce e aici, un chef?
English: - What is this, a pinch?
Romanian: Oh, piciorul meu !
English: Oh, my leg!
Romanian: Mi se va întâmpla ceva, știu asta.
English: Somethin' gonna happen to me, I know.
Romanian: Studsy cum mai e?
English: How is Studsy?
Romanian: D-na Strong... ştiu că nu-i momentul potrivit pentru a discuta despre bani... dar dacă ai nevoie de ceva, te rog să mă suni oricând, da ?
English: Mrs. Strong, I... I know this is hardly the time to discuss money... but if you need me, please reach me here any time, will you?
Romanian: Asta e.
English: - That's it.
Romanian: Crezi că aceste lucruri sunt în regulă ?
English: Think these things are all right?
Romanian: - Suntem toti nebuni.
English: - We're all crazy.
Romanian: Xavier, porneste luminile!
English: Xavier, turn on the lights!
Romanian: "Adorat."
English: "Precious."
Romanian: Dormitoare... să vedem.
English: Bedrooms. Now, let me see.
Romanian: Pentru ca vreau sa ma astepti afara.
English: Because I want you to wait for me outside.
Romanian: Dar, doctore, gândeşte-te la aspectele profunde ale problemei şi ia în considerare punctele vitale ale lucrării mele.
English: But, Doctor, please reflect on the profound aspects of the matter and consider the vital points of my thesis.
Romanian: Când eram copil, obişnuiam să înot în jurul unui dig ca acesta.
English: When I was a kid, I used to swim around a pier like that.
Romanian: - Pentru ce ?
English: For what?
Romanian: - m-a scutit de durere de cap.
English: - Riding with you gave me a swelled head.
Romanian: - Las-o sa plece.
English: - Don't do anything stupid.
Romanian: - O să ajungeţi la Londra.
English: - You'll get to London all right.
Romanian: Perfect, desigur.
English: Fine, of course.
Romanian: Imi faceam si eu griji despre asta.
English: I've been worrying about it too.
Romanian: Da, Sam.
English: Yes, Sam.
Romanian: Altceva ?
English: - Anything else?
Romanian: Caută pe cineva şi mă bucur că nu au nimic cu mine.
English: They´rre after somebody and they´vve got nothing on me.
Romanian: Niciodată nu l-ai mai făcut, nu?
English: You've never done that before, have you?
Romanian: Doi câte doi!
English: Two by two!
Romanian: Bine.
English: All right.
Romanian: Zău aşa !
English: Really.
Romanian: De fapt Taj Mahal nu este în China, dar nu contează.
English: Of course. The Taj Mahal isn't in China. But that wouldn't make any difference.
Romanian: Haideţi, băieţi. De să ne pese de generali ?
English: Guys, what do we care about generals?
Romanian: Bani, haine, flori.
English: Money, clothes, flowers.
Romanian: Unde-i Barbara?
English: Where is Barbara?
Romanian: Spaţiu.
English: Space.
Romanian: Asta este calomnie!
English: That's slander!
Romanian: Totul e bine.
English: Everything's all right.
Romanian: "dar toate acestea vin de la Pauline.
English: "BUT THEY ALL REALLY COME FROM PAULINE.
Romanian: - Poftim?
English: ?
Romanian: Eşti teafără.
English: There. You're all right, dear.
Romanian: Ei bine, nu am nicio pretenție de la tine.
English: Well, I have no claim on you.
Romanian: Pune lanterna pe asta.
English: Get a flash of that.
Romanian: Dacă vrei, o voi face.
English: If you do, I will.
Romanian: Nu înțeleg.
English: I don't understand.
Romanian: Drept înainte.
English: Straight ahead.
Romanian: Nici măcar...
English: Not one...
Romanian: Şi de ce ar trebui să mă tem?
English: And what's there to be afraid of?
Romanian: - Tarzan.
English: - Tarzan.
Romanian: Prieteni, eu n-am să vă duc în Eden... Sunteţi prea deştepţi.
English: "My friends, I will not take you to Eden --- you are too clever.
Romanian: Dii !
English: Hyah!
Romanian: Şi când te gândeşti... Câteva troiene de zăpadă ne-ar fi putut ţine despărţiţi pentru totdeauna.
English: And to think... a few snowdrifts might have separated us forever.
Romanian: - Ei bine, mă interesează.
English: WELL, IT INTERESTS ME,
Romanian: Tăcere!
English: Silence!
Romanian: Trebuie să vă mărturisesc, este un lucru foarte agreabil.
English: I must confess, it's very agreeable.
Romanian: Iar in aceasta, vrajeste incaltarile unui om.
English: In the following image a witch has bewitched a man's shoe.
Romanian: Îmi amintesc lampa, ţin minte noptieră... şi îmi amintesc de acea noapte.
English: I remember the lamp, I remember the night table... and I remember the night.
Romanian: Aveti cumva apa?
English: Do you have any water ?
Romanian: - Nimic de făcut, mă voi ocupa de asta..
English: - Nothing doing. I'll attend to this now.
Romanian: Moralul ?
English: How's the morale?
Romanian: Eu n-am probleme cu apetitul.
English: You see, there's nothing wrong with my appetite. No?
Romanian: Nu aş privi lucrurile chiar aşa.
English: I shouldn't put it quite like that.
Romanian: Da.
English: Si.
Romanian: Scuip-o, te rog.
English: Spit it out, please.
Romanian: Ai vreun partener sau lucrezi singur ?
English: Have you got a partner or do you work alone?
Romanian: Vino să cinezi cu noi mâine.
English: Come and dine with us tomorrow.
Romanian: "Si mama Annei, sotia tipografului, cea care imi doreste o moarte ingrozitoare -"
English: "And Anna's mother, the wife of the Printer, who wished me a scalding death -"
Romanian: Şi ai descoperit toate astea singur?
English: You figured that out all by yourself?
Romanian: Da, în patul nostru!
English: Yes, on our bed!
Romanian: Nu mă pot opri acum.
English: I cannot stop now.
Romanian: Mergeţi amândoi.
English: You two run along.
Romanian: Sunt doar o fată mare și puternică care are nevoie de câteva aspirine, asta-i tot.
English: I'm just a big strong girl that needs a couple of aspirins, that's all.
Romanian: Castenega e încă în libertate.
English: Now this Castenega is still at large.
Romanian: Este nerabdatoare sa devina actrită, sefule.
English: She's anxious to become an actress, governor. I didn't know young women anxious to become actresses took the trouble to learn.
Romanian: - Nu spunem nimanui, Harris.
English: -We're not telling anybody, Harris.
Romanian: Nu sunt marele lup rău cum credeai că sunt.
English: I'm not the big bad wolf you thought I was.
Romanian: Domnişoara Smith, daţi asta pacientului din camera 22.
English: Miss Smith, give this to the patient in room 22.
Romanian: - Ce-i cu gondola?
English: But what's the idea of the gondola?
Romanian: - Urmatorul martor. - De sigur. Daca ascultati un daltonist!
English: -Of course, Inspector if you listen to a color-blind man!
Romanian: - Da.
English: - Yes.
Romanian: Du-mă la apartamentul lui Jerry Strong.
English: Get me up to Jerry Strong's apartment.
Romanian: PREŞEDINTELE Roman de Emil Franzos
English: THE PRESIDENT A novel by Karl Emil Franzos
Romanian: Acolo, uite!
English: There we are!
Romanian: Cum se numesc acei oameni care au grijă de bunăstarea copiilor?
English: WHAT DO THEY CALL THE PEOPLE THAT LOOK AFTER THE WELFARE OF CHILDREN?
Romanian: - Ai spus să fiu aici la miezul nopţii.
English: - You told me to be here at 12.
Romanian: N-am vrut să par cu nasul pe sus.
English: I didn't want him to think I was high-hatting him.
Romanian: Ce fel de bărbat ţi-ar plăcea, Libby ?
English: What kind of men do you like, Libby?
Romanian: Ai impresia că-i cunoşti pe toţi.
English: You think you've met everybody that you see. Yes? Really?
Romanian: - Ai dreptate, domnule guvernator.
English: - You're right, governor.
Romanian: Bine.
English: - Oh, can't you see?
Romanian: Fără glumă. N-am mai văzut-o de mult.
English: I haven't laid eyes on her since I got out of reform school!
Romanian: - Și cazul North cu mașină-bombă.
English: - And the North car bomb case.
Romanian: - Ai citit-o?
English: - Have read?
Romanian: Este soţia lui Poelzig.
English: She is Poelzig's wife.
Romanian: - Într-o casă cu chirie.
English: - In a flophouse.
Romanian: Nu sunt gata ?
English: Aren't they finished yet?
Romanian: Știi cât ne costă să ungem politicienii pentru a ne permite să acționăm în acest vechi hambar?
English: Do you know how much to grease the politicians to allow us to operate in this old barn?
Romanian: Ce mai e şi asta ? Ce-i asta ?
English: What's the matter with this shirt...
Romanian: Ce faci aici?
English: - What are you doing here?
Romanian: În 1935, Hemingway a publicat
English: IN 1935, HEMINGWAY PUBLISHED
Romanian: Aş prefera junglă.
English: I'd advise the jungle.
Romanian: Da sunt german-american.
English: You know. An American German/American.
Romanian: - Sigur.
English: Sure.
Romanian: Ce au avut de spus?
English: One of them pressed him, we knew.
Romanian: Nu, nu se poate să-l luaţi!
English: No, you can't take him!
Romanian: - Nu ți-a făcut nimic.
English: - He hasn't done anything to you.
Romanian: - Câţi bani risipiţi!
English: - What a waste of money.
Romanian: Nu.
English: No.
Romanian: Încărcătura e încărcătura.
English: - Cargo is cargo.
Romanian: Dacă nu sunt dur cu ei...
English: If I'm not hard with them...
Romanian: Aveţi de grijă să se simtă cât mai, comfortabil, deocamdată.
English: See that he is quite comfortable, for the present.
Romanian: S-a produs o eroare teribilă.
English: A terrible mistake has occurred.
Romanian: Prietenul meu Bradford i-a condus pe toți direct la castel.
English: My friend Bradford led them all right into the castle.
Romanian: - Fanny ! - Fata cu scoicile ?
English: Is it that cockle girl?
Romanian: Taci!
English: Shut up, I tell you.
Romanian: Ce s-a întâmplat, te supăra piciorul?
English: What's the matter?
Romanian: "Mama ta a venit să spună că plângi după mine."
English: "Your mother said you cried, et cetera."
Romanian: Că doar n-ai zburat !
English: You ain't no eagle. Hey! Help me!
Romanian: - Mă duc la ferma Walton.
English: I'm going out to Walton ranch.
Romanian: Război?
English: War?
Romanian: - Doamnă Higgins...
English: Mrs. Higgins...
Romanian: Totuși, am avut momente prostești, doar că nu l-am lăsat niciodată pe Chris să bănuiască că avea o soție geloasă.
English: STILL, I'VE HAD FOOLISH MOMENTS, ONLY I'VE NEVER LET CHRIS SUSPECT THAT HE HAD A JEALOUS WIFE.
Romanian: Vă rog să nu vă apropiați.
English: Please don't come any closer.
Romanian: Trebuie să te gândeşti repede.
English: You'll have to make up your mind quick.
Romanian: Nu vreau să-l caut.
English: I don't want to look for it.
Romanian: Atingerea de aur este a mea.
English: The golden touch is mine.
Romanian: - Huh?
English: - Huh?
Romanian: De ani de zile aştept să cresc ca să devin soţia ta.
English: I longed to grow up to become your wife.
Romanian: Ei bine, dacă ea continuă așa cum o face acum, o vei vedea.
English: Well, if she keeps on going the way she is now, You will.
Romanian: Stanga, stanga, stanga.
English: Left, left, left.
Romanian: Motor !
English: Action!
Romanian: Nu i-ai spus despre noi?
English: Haven't you told her about us?
Romanian: - Nu contează.
English: That doesn't matter.
Romanian: - O, asta e nouă, nu?
English: Oh, fresh, huh?
Romanian: Aceste flamuri nu sunt doar un semn exterior, ele reprezintă o obligaţie vie.
English: These flags are not merely an outward sign... but represent a living obligation.
Romanian: - Acasa.
English: -Home.
Romanian: Scoate-o!
English: Take it off.
Romanian: Avem multe să vorbim, nu, Phil?
English: We've a lot to talk over, eh Phil?
Romanian: În cazul în care v-aţi dori că frumuseţea voastră să fie mai intensă decât ar putea fi îndeplinită în aceste emisiuni, v-aş sugera un diagnostic personal.
English: Should your beauty needs be greater than can be met by these broadcasts, I would suggest a personal diagnosis.
Romanian: Promisiuni măreţe.
English: Big promises.
Romanian: - Cum rămâne cu muniţia?
English: - What about ammo?
Romanian: Ochii  o, ochii cam aşa.
English: Eyes o, eyes like this.
Romanian: Isus i-a spus:
English: and Jesus said:
Romanian: Eşti incorigibilă.
English: You're incorrigible.
Romanian: Ce părere ai de inelul ăsta de logodnă ?
English: How will that do for an engagement ring, huh?
Romanian: Spune, vrei sa-ti scriu un cec, nu-i asa?
English: Say, you want to draw another paycheck, don't you?
Romanian: Delegaţii Facţiunii Menşevicilor, Camera 16
English: The meeting of the Menshevik fraction is in Room 16
Romanian: Si eu cu ce ma aleg?
English: It's nothing but a headache.
Romanian: Am reuşit!
English: We're in!
Romanian: D-ta nu ?
English: Don't you?
Romanian: "O să-ţi slujesc... , ... eu şi toate celelalte duhuri ale lampii!"
English: "I am your servant. I and all the spirits of the lamp!"
Romanian: Ah, mama!
English: Aw, mama!
Romanian: Da, Martin.
English: Yes. Martin.
Romanian: [Continua]
English: ¿¿ [Continues]
Romanian: - Sigur, a renunţat.
English: Sure, he quit!
Romanian: - Pune-le în buzunar.
English: - Put them in your pocket.
Romanian: - Bine.
English: - Fine.
Romanian: A murit... pentru că sunt o piază-rea.
English: She wasn't killed... 'cause I'm a Jonah.
Romanian: Domnişoara Wonderly mai are de luat nişte notiţe, încă n-am terminat.
English: Miss Wonderly is taking some notes that I haven't finished as yet.
Romanian: Acum micuţule, vom aştepta...
English: And now little Elmer.. We shall see.
Romanian: Vorbeste pentru tine, tarfa! M-ai pacalit!
English: Speak for yourself, bitch!
Romanian: Vă mulţumesc mult, doctore, ce agitaţie a mai fost.
English: Thank ye kindly, doctor, and quite a squall it were.
Romanian: Unde vrei tu.
English: Whatever you like.
Romanian: Aici erai.
English: Here you are.
Romanian: Deja jumătate din vaci îmi sunt moarte.
English: - Yeah. Half my cows is dead already.
Romanian: Cum trebuie?
English: Properly?
Romanian: În China?
English: China?
Romanian: Să plecăm de aici.
English: Let's get out of here.
Romanian: - Ce ţi-ar place cel mai mult?
English: What would you like to do best of all?
Romanian: Și noi suntem oamenii care fac ca țara să meargă.
English: And we're the people who keep the country going.
Romanian: De atunci inainte, mai mult de un sfert de film a fost considerat pierdut.
English: From that time onward, more than a quarter of the film was assumed to have been lost.
Romanian: Cine ?
English: - They? Who?
Romanian: Pentru asta, mă aştept ca să plângi foarte mult când voi pleca.
English: For that, I shall expect you to cry a good deal as I go.
Romanian: ADMINISTRATOR "Economiseşte hârtia"
English: BUSINESS MANAGER 'Conserve paper! '
Romanian: Tu tot intri şi ieşi de aici, trebuie să-l fi cunoscut.
English: You're in and out of here, you must've known him.
Romanian: Hei tu, da-i drumul.
English: Hey, you, get to work.
Romanian: Desfa covorul fermecat.
English: Spread the flying carpet.
Romanian: La naiba, poate că ne-am înşelat.
English: Organdy, perhaps we're wrong.
Romanian: Salutare!
English: Oh, hello there.
Romanian: - Absolut totală.
English: - All the difference in the world.
Romanian: Da.
English: Yeah.
Romanian: - Intră acolo.
English: - Get in there. - Jane.
Romanian: Loopy!
English: Loopy!
Romanian: Tu pleci în Canada.
English: You're off to Canada.
Romanian: Dacă am putea ieşi şi să lăsăm vasul în voia valurilor ar pune punct poveştii cu tunul.
English: If we could only get out and cut that ship adrift that'd put an end to the cannon.
Romanian: - Cecul?
English: - His check?
Romanian: - E înspăimântător.
English: - Oh, it's frightening.
Romanian: Just aş well we didn't.
English: Just as well we didn't.
Romanian: Îndată, domnule.
English: Right away, sir.
Romanian: Bună seara, doamna.
English: Good evening, madame.
Romanian: - Ollie!
English: -Ollie.
Romanian: De ce ești aici?
English: Why Are You In Here?
Romanian: N-ai făcut-o?
English: Didn't you?
Romanian: Du-te şi găseşte-i!
English: Go find them!
Romanian: L-am ucis pe Charlie Roark ca să te am!
English: I killed Charlie Roark to get you!
Romanian: - Bună, drăguţo!
English: - Hello, cutie?
Romanian: Ce mai faci, comodore?
English: How are you, Commodore?
Romanian: E garda regală !
English: The royal guard is presenting arms.
Romanian: Ei bine, am toate motivele să strig.
English: Well, I have every reason for shouting.
Romanian: Ai putea să te duci să o trezești pe Marianne.
English: You might go up and waken Marianne.
Romanian: - Ascultaţi, Alteţă...
English: - Now listen, Your Highness...
Romanian: Nu-ţi plac florile delicate?
English: Don't you like wallflowers?
Romanian: Aşa că, de ce să nu fi scris despre monştri ?
English: So why shouldn't I write of monsters?
Romanian: Ce zici de o partida de poker ca sa vedem cine cere de mancare.
English: How about some poker to see who bums the handout?
Romanian: Nu, nu!
English: No, no!
Romanian: - Bine, şefule.
English: - Okay, Chief.
Romanian: Căpitanul navei spune că ajungem în Cape Town cam în 10 zile.
English: The head man on the ship says we reach Cape Town in about 10 days.
Romanian: # Petrecere la Hollywood #
English: Hollywood party
Romanian: - Luaţi arzătorul şi topiţi lacătul.
English: - Get the blowtorch and melt the lock off.
Romanian: Eşti beat?
English: Are you drunk?
Romanian: Ce mai faci, Ebba?
English: How are you, Ebba?
Romanian: Regele iudeilor!
English: The King of the Jews!
Romanian: Cine ar face un asemenea lucru?
English: Who could do such a thing?
Romanian: - Le-a ascuns.
English: Here .. she needs one.
Romanian: "E uşor să spui asta. "
English: "That's easy for you to say."
Romanian: Da?
English: Yeah?
Romanian: Sunt cel mai bun magician stradal.
English: I am the best street magician there is.
Romanian: Nu ştiu dacă îţi dai seama, dar aveam influenţă asupra ei.
English: I don't know whether you realize but I've had an influence with her.
Romanian: Oh, te iubesc.
English: Oh, I love you.
Romanian: - Henry ?
English: - Henry?
Romanian: Crezi că vrea să-şi vadă mama împodobită cu colierul ghilotinei ?
English: do you think she wants herself or her mother adorned   with the collar of the guillotine?
Romanian: - E periculos?
English: - Is he dangerous?
Romanian: - Mamă, ce vrea să spună?
English: It means my dear..
Romanian: Nu-ţi face griji.
English: Don't worry.
Romanian: Bună, Halifax.
English: Hello, Halifax.
Romanian: Asta s-ar putea dovedi eficient.
English: That might prove effective.
Romanian: Este doar 9:30, doamna.
English: It's just 9:30, madam.
Romanian: Nu-mi place să văd oamenii care muncesc că pierd atâţia bani.
English: I hate to see working man lose so much money.
Romanian: "Dacă te grăbeşti, lasă-mă să te iau, o parte din drum."
English: "If you're in a hurry, let me take you part of the way."
Romanian: Și la început, el i-a încurajat munca ei.
English: AND AT FIRST, HE ENCOURAGED HER WORK.
Romanian: Ce părere aveţi despre a sluji regele?
English: What do you say to serving the King?
Romanian: E nu am ştiut niciodată să urăsc.
English: I never could hate properly.
Romanian: Ei bine, mi s-a cerut să le livrez astăzi.
English: Well, I've been ordered to deliver them today.
Romanian: Nu poţi s-o condamni.
English: You can't blame her.
Romanian: - Unde-i?
English: - Where is she?
Romanian: Aşa cred.
English: I think so.
Romanian: Ti-am adus lucrurile, vezi?
English: We brought your things for you. See?
Romanian: - Îl voi ţine pe Parker aici.
English: He's already attracted.
Romanian: Sena coteşte, vine şi iar pleacă.
English: The Seine turns, comes and then leaves again.
Romanian: Spune le celorlalţi ca m am retras.
English: Tell the others I've retired.
Romanian: - A fost o călătorie nemaipomenită, dle.
English: - It was a wondrous ride, sir.
Romanian: Da.
English: Yes.
Romanian: Oriunde am fi.
English: No matter where we are
Romanian: - Da, chiar aşa.
English: - Yeah, that's so.
Romanian: Vă descurcaţi destul de bine, nu-i aşa, d-le Dorrington?
English: You do yourself pretty well, don't you, Mr. Dorrington?
Romanian: Sergent, sunt un contabil public certificat.
English: Sergeant, I'm a certified public accountant.
Romanian: Ai anunţat-o pe soţia lui Archer, Sam ?
English: Did you break the news to Archer's wife, Sam?
Romanian: Ascultă, Sheila, 25000 de dolari sunt o căruţă de bani.
English: Listen, Sheila, $25,000 is a lot of tablets, baby.
Romanian: - O ţigară? - Mulţumesc.
English: - Cigarette, Colonel?
Romanian: Dragă Mizzi.
English: Dearest Mizzi.
Romanian: E şeful, s-a deghizat.
English: It's the boss. He's got a disguise.
Romanian: - Da... mă grăbesc.
English: - Yes. I'm in a hurry.
Romanian: Acesta este dormitorul ei. Ce caută acest om aici?
English: This is her bedroom.
Romanian: Nu m-au lăsat să trec, şi trebuia să vin să te văd.
English: They wouldn't let me pass, and I had to see you.
Romanian: Dar foarte curând am început să vreau lucruri, lucruri frumoase.
English: But very soon I began to want things, beautiful things.
Romanian: Derek Stewart.
English: Derek Stewart.
Romanian: Aş vrea să vorbesc cu tine, Murray.
English: I'd like to talk to you, Murray.
Romanian: Ei bine, asta nu-i din tablă.
English: Well, this ain't tin.
Romanian: Este bine educat, are maniere frumoase.
English: He's well-educeted, hes lovely menners.
Romanian: Mai întâi e camera pe care poţi s-o vezi în oglindă.
English: First, there's the room you can see through the glass.
Romanian: Apă caldă.
English: The hot water.
Romanian: Am pornit în jurul lumii băieţi.
English: We're off around the world, boys.
Romanian: Ma, o să stau aici o zi, două, apoi vreau o maşină.
English: Ma, I'm gonna stay here a day or two, then I want a car.
Romanian: - Am Henry Clay sau Corona-Corona.
English: I've got, I've got Henry Clay... - or Corona, Corona?
Romanian: Este o nouă echipă care se remarcă şi fiecare băiat cu banii pentru arme va încerca să îi calce pe urmă.
English: There's a new crew coming out and every guy with money for a gun is gonna try to step into his place. You see?
Romanian: Mai bine v-as spune imediat.
English: I would rather not wait.
Romanian: Scuza-ma, inspectore.
English: Excuse me, Inspector.
Romanian: Ai milă de noi !
English: Send us here on earth
Romanian: Nu, am o idee mai bună.
English: No, I got a better idea.
Romanian: Haidem !
English: ─ Ha .. come on.
Romanian: Zacamantul acela de la Bear Creek e o minciuna sfruntata.
English: That Bear Creek pool is a whopper.
Romanian: Anumite indicii ne fac sa credeam ca acest criminal este acelasi care a ucis deja opt copii.
English: Certain evidence leads us to believe that the murderer is the same one who has already killed eight children
Romanian: Ce încerci să faci ?
English: What are you trying to do?
Romanian: Sa castigam bani?
English: -You mean, make some money?
Romanian: Tații, mamele și prietenii voștri pot să fie mândrii de curajul vostru, de hotărârea voastră, de voința voastră de a reuși.
English: Your fathers and mothers and your friends May well be proud of your courage, your determination, Your will to succeed.
Romanian: Dragul meu băiat...
English: My dear old boy...
Romanian: Ai trusa de scule, tinere ?
English: Got your repair kit?
Romanian: Țineți-le cozile.
English: Wag your tail.
Romanian: Doctorul a spus că s-ar putea să faci pneumonie.
English: The doctor said you might get pneumonia.
Romanian: - Si dacă le urăsti?
English: - And if you hate them?
Romanian: Să mă trăsnească aici dacă am fost!
English: I hope to die right here if I was.
Romanian: - Ce a urmat?
English: - And then?
Romanian: Lăsându-ne pentru o lungă, lungă călătorie.
English: Leaving us for a long, long journey.
Romanian: Nu vom ceda nimic, niciodată
English: So we were born like this
Romanian: Magazinul universal sau mica prăvălie...
English: The big department store vs. the little shop.
Romanian: Unde te duci?
English: - Where are you going?
Romanian: Doamnă, înainte să termin cu tine, vei avea motive de divorţ şi soţia mea la fel.
English: Madam, before I get through with you, you will have a clear case for divorce... and so will my wife.
Romanian: Bună dimineața, domnilor.
English: Buenos dias, señores.
Romanian: Probabil e o indigestie.
English: It's probably indigestion.
Romanian: - Mulțumesc.
English: - Thank you.
Romanian: Dar nu ne putem întoarce în trecut din nou?
English: But can't we find those old selves again?
Romanian: Vezi, acum n-o să mai ai probleme cu ei.
English: You see, you'll have no more trouble with them now.
Romanian: De ce nu trimiţi pe cineva la el?
English: Why don't you send a messenger?
Romanian: Ii chemi la telefon.
English: You're wanted on the phone.
Romanian: Pentru asta am venit.
English: That's what I dropped in for.
Romanian: Ultimul conducător aproape că a ruinat tara asta, nu ştia ce sa facă cu ea dacă credeţi ca o duceţi rău acum staţi sa vedeţi când termin eu cu voi
English: The last man nearly ruined this place, he didn't know what to do with it If you think this country's bad off now just wait 'til I get through with it The country's taxes must be fixed and I know what to do with it
Romanian: Te temi de politie.
English: You are afraid of the police!
Romanian: Hei, dă-mi timp să mă acomodez, bine ?
English: Hey, let me learn to fly this ship, will you;
Romanian: - Nu vreau să te aud vorbind deloc.
English: - I don't want to hear you talk at all.
Romanian: Baronul de Chanterelle, dorind că descendenţa sa, să nu se stingă, convoacă toate tinerele din regiune în piaţă, pentru ca nepotul şi moştenitorul său, să-şi aleagă una dintre ele, drept soţie.
English: The Baron von Chanterelle does not wish for his lineage to die out and therefore invites all of the region's maidens to gather in the marketplace so that his nephew, the sole heir, may choose a fitting maiden to take as his wife.
Romanian: - Nu face pe prostul !
English: - Be quiet! Don't be a fool!
Romanian: Crezi că norocul orb te-a adus aici ?
English: - You think blind chance brought you here?
Romanian: "De ce ai făcut asta ?"
English: "Why did you do that?"
Romanian: Amah.
English: Amah.
Romanian: Eu bănuiesc că Eddie îl protejează pe Larry.
English: Now I figure that Eddie's protecting Larry.
Romanian: - Pe ăsta?
English: - That?
Romanian: Oh, ne-am agitat de cateva ori la ferestre.
English: Oh, we waved a couple of times from the window.
Romanian: Chiar fetiţa e la mijloc.
English: There's the child herself.
Romanian: - Serios? E greu pentru voi în sudul Suediei?
English: Looks like you have a bit to worry about.
Romanian: Ce vrei să spui, afară ?
English: What do you mean, out?
Romanian: Nu, eu îl găsesc foarte bun.
English: No, but I thought it was very good.
Romanian: Când e premieră?
English: When is the premiere?
Romanian: Ochiul tău drept, spune "da" Ochiul tău stâng, spune "nu"
English: Your right eye says yes and your left eye says no.
Romanian: Am fost inselati.
English: I'm not that dumb.
Romanian: - Ce anume? Am toate explicațiile de care am nevoie.
English: No explanation is required!
Romanian: Nu mai e nimic de spus.
English: There is nothing more to say.
Romanian: Să încheiem afacerea.
English: - Let's make a deal.
Romanian: De ce, e așa de urâtă.
English: Why, that dumb cluck!
Romanian: - Mă bucur să vă văd. Frank...
English: Will you get me that script?
Romanian: - Pune asta pe tine.
English: -Here, put this around you.
Romanian: Locotenente.
English: Lieutenant.
Romanian: Termină cu absurditatea asta.
English: Stop that nonsense.
Romanian: Nu mai am nevoie de ea.
English: I won't need it anymore.
Romanian: Cum a putut ?
English: How could she?
Romanian: Trebuie să zâmbim, ca tati să creadă că suntem fericiţi.
English: We've got to smile, so Daddy will think we're happy.
Romanian: Vino, Lily.
English: Come, Lily.
Romanian: Îşi dă cuvântul, cuvântul ni prinţ.
English: Why, he gives his word, the word of a prince.
Romanian: - Pa!
English: Goodbye, Mrs. Cardes
Romanian: Țineți minte ce vă spun!
English: Remember that, Mr Friis.
Romanian: Puteţi să vă întrerupeţi giugiuleală... cât schimb o vorbă cu Paula ?
English: Do you suppose you two could stop billing and cooing just long enough... for me to have a little word with Paula?
Romanian: Bună treabă, Rollo.
English: Nice work, Rollo.
Romanian: Are gusturi vulgare.
English: She has vulgar tastes.
Romanian: E prietenul meu şi un bun soldat...
English: He is my friend and a good soldier.
Romanian: - Sunt surprins... că tu nu ai recunoscut simptomele pe care le-ai descris atât de clar, doctore.
English: - Surprised... you did not recognize the symptoms... which you described so clearly, Doctor.
Romanian: Priviţi acum ieşirea supravieţuitorilor orgiilor criminale din castelul Selliny!
English: Here are the survivors of these orgies, leaving the Château de Selliny.
Romanian: Puneti-le sub pat.
English: Put 'em under the bed.
Romanian: - Amândoi au fost omorâți. Unul la Paris. Celălalt, la Praga.
English: You were secretary to two previous presidents of the world peace conference.
Romanian: Să ai grijă de ele! Uite, o să-ți arăt.
English: Here, I'll show you.
Romanian: Parcă se renova acolo.
English: I thought they were painting up there.
Romanian: Vacanta este singura ocazie in care Pot sa-si faca munca lor de cercetare.
English: Vacation period is the only opportunity they have to do their personal research work.
Romanian: Este acelasi omulet.
English: It's the same little man.
Romanian: Să mă arestez.
English: Frame it myself.
Romanian: Domnul Archibald MacMurray.
English: Sir Archibald MacMurray.
Romanian: Lâmgă trecătoare?
English: The pass?
Romanian: Viata nu e decat un lung sir De pierderi a celor pe care-i iubim.
English: Life is but a long loss of those we love.
Romanian: Susie !
English: Susie!
Romanian: Erai în gardă.
English: Last month, at the powder magazine,
Romanian: Franz Schubert a coborât aici.
English: Franz Schubert. I brought him down here.
Romanian: Poate am greşit.
English: - Oh, maybe I'm a mistake.
Romanian: Am facut deja acest lucru, domnisoara.
English: I have already done so, miss.
Romanian: Inima în piept
English: Heart in chest
Romanian: Când vrei să te căsătoreşti, devii suspect.
English: The minute a fellow wants to get married they become suspicious of him right away.
Romanian: Nu pot citi scrisul dintr-o perioadă aşa de îndepărtată.
English: I cannot read the writing of a period so remote.
Romanian: Ce părere ai despre felul în care te-a tratat această femeie ?
English: What construction did you place upon this woman's treatment of you?
Romanian: Teribil.
English: Terrible.
Romanian: Cum a fost acasă ?
English: Well, how was it back home?
Romanian: Şi ce?
English: So what?
Romanian: Nu e o piesă de spiritism.
English: This isn't a play about spiritualism.
Romanian: - L-au reperat.
English: -They put a mark on him
Romanian: Sunt obosit.
English: I'm tired.
Romanian: Fără dinamită aici !
English: No dynamite here!
Romanian: Operaţii estetice, transfuzii de sânge, Extracte de glande.
English: With plastic surgery, blood transfusions... gland extracts, with ray baths.
Romanian: - Ce probleme ai? - Nu ştiu.
English: What do you think is the matter with you?
Romanian: Chiar aşa?
English: Is that so?
Romanian: - N-ai văzut afişele ?
English: - Haven't you seen the wanted posters?
Romanian: Ce mai ţară.
English: Lets have a drink.
Romanian: Stai puţin!
English: Wait a minute! Glenda!
Romanian: Ştii despre cine e vorba?
English: Know who that is?
Romanian: Ești agitat?
English: Nervous?
Romanian: - Şi cum sunt micuţele gemene ?
English: And how are the little twins? Little?
Romanian: Uite-ți rufele!
English: Here is your linen
Romanian: Dar avem nevoie de 20.000 de franci pentru decoruri şi costume.
English: We just need 20,000 francs for sets and costumes.
Romanian: Vincey ?
English: Vincey.
Romanian: Li se pun întrebări.
English: They ask them questions.
Romanian: "Permiteţi-mi să mă prezint:
English: "Please allow me to introduce myself.
Romanian: Taci.
English: Shut up.
Romanian: El.
English: He did.
Romanian: Planuisem altceva pentru mine.
English: I'd planned a very different programme for myself.
Romanian: Si asta ce e?
English: -Well, what the heck is this?
Romanian: - Am înţeles, domnule.
English: Aye, aye, sir.
Romanian: Să înceapă petrecerea!
English: Let the festivities proceed.
Romanian: - Mă îndoiesc ca o va face.
English: - I doubt he will.
Romanian: Ce ar fi viața fără iubire?
English: What would life be without love?
Romanian: Căutaţi-i!
English: Find 'em now!
Romanian: Dă-i 100 de franci pentru hotel.
English: Give him 100 francs for a hotel.
Romanian: Dar laşi asta să ţi se amestece cu cariera şi e fatal.
English: But you're letting it interfere with your career, and that is fatal.
Romanian: - Măi să fie, şi ea şi-a împuşcat soţul.
English: - By golly, she shot her husband, too.
Romanian: Dar noi trebuie să punem în aplicare regulamentele noastre.
English: But we must enforce our regulations.
Romanian: Uneori mă plictisesc de el.
English: I just get tired of him sometimes.
Romanian: Săraca.
English: That's too bad.
Romanian: De ce mai anesteziat în tren?
English: Why did you drug me on the trein?
Romanian: - Unul dintre tâlhari?
English: - One of the robbers?
Romanian: Nu mă poate plictisii.
English: That would ever bore me.
Romanian: Tu esti povara barbatului tau!
English: You are the white man's burden!
Romanian: E un tip aici care e de pe piuliţă lui.
English: There's a guy here who's off his nut.
Romanian: Nu, nu e normal.
English: Oh, no, that ain't right.
Romanian: Este acasa Dr. Fane?
English: Is Dr. Fane home ?
Romanian: Se vede că-i scrisă de bărbați.
English: The law was clearly written by men!
Romanian: Nu înţelegi, iubitule, că vreau să fac călătoria asta cu tine?
English: Don't you see, dear, I want to take this trip with you.
Romanian: Cumpărată ieri.
English: Bought it yesterday.
Romanian: Ei bine, mare mahăr.
English: Well, big shot.
Romanian: Ei bine, n-a luat.
English: Well, it wasn't.
Romanian: Ei bine... suntem căsătoriţi.
English: Well... we're married.
Romanian: Vă explic imediat.
English: I beg your pardon.
Romanian: Ar fi perfectă pentru pagina femeilor.
English: It'll be lovely for the woman's page.
Romanian: Dacă ai putea face o notificare telegrafistului să ascundă unele informaţii din ziarul de dimineaţă.
English: If you'll give me a note to your wireless operator to hold back some news in your morning paper.
Romanian: Numărul 5 câştigă.
English: = number five wins.
Romanian: - La treabă!
English: - Then get started.
Romanian: Te uiţi la mine ca o găină care-a dat peste un cuţit.
English: You look like a chicken that's just seen a knife.
Romanian: Dar cine vrea să fie şobolan ?
English: But who wants to be a rat?
Romanian: Sunt prins ca un şoarece-n capcană.
English: I'm trapped like a rat.
Romanian: Așa cum d-na Bradford Meade, Deținând Jumătate Compania.
English: As Mrs. Bradford Meade, Owning Half The Company.
Romanian: - Închide ușa.
English: - Shut the door.
Romanian: În aceste condiții, medalia de aur pare să revină Franței, care a zdrobit-o
English: In these conditions, the gold medal looks set to go to France, who crushed the
Romanian: Deci nu vrei să mă sfătuieşti ?
English: So you won't advise me?
Romanian: Da, jur pe Coran.
English: I swear it upon the Koran.
Romanian: O sa ne vedem in tribunale.
English: I'll see you in court
Romanian: Cred că acest lucru vă va ajuta, domnişoară.
English: I think this will help you, Miss.
Romanian: - Da, Nick.
English: - Yes, Nick.
Romanian: Nu ești, până nu primesc cheia și biletul.
English: 'You don't, until I get that key and the note.'
Romanian: Asta e, ţi le-a furat.
English: That's it, he's pinched them.
Romanian: Ce a zis?
English: What did he say then?
Romanian: Nu pleci din cauza mea, nu?
English: You're not going on account of me, are you?
Romanian: Fiica mea exagerează. Ted și cu ea sunt prieteni de mai bine de cinci ani.
English: Confound that daughter of mine, she and Ted have been gone ages.
Romanian: Crezi că ai putea scrie și imnuri?
English: Do you suppose you could write hymns?
Romanian: Mda.
English: Yeah.
Romanian: Sau noaptea de lângă oază, când citeam în ochii tăi... lucrurile pe care nu îndrăznești să le spui?
English: Or the night by the oasis, when I read in your eyes... the things that you dare not speak?
Romanian: - Doar 8.000 de coroane. - De data asta nu.
English: Not a chance.
Romanian: Păi, vom discuta despre, dacă aşa doreşti, dar nu cred că vrei aşa ceva.
English: Well, we'll go into that if you do, but I don't think you will.
Romanian: - Bineînțeles! Am venit să te resuscitez!
English: I've come to revive you!
Romanian: E vreun pericol?
English: Is he dangerous?
Romanian: - Da?
English: - Yeah?
Romanian: - Ia, fugi după asta.
English: - Here, chase this.
Romanian: Ai să mă vezi aici mâine dimineaţă.
English: You'll see me here in the morning.
Romanian: Alipiţi umărul drept.
English: To the right, I said.
Romanian: Rapid !
English: I can't stand that guy.
Romanian: Am observat " asta", aseară.
English: Well, I noticed it last night.
Romanian: Nu vreau.
English: I don't.
Romanian: - Da.
English: - Yes.
Romanian: Vă conduc la o barcă, dar nu fără aurul lui Marcus.
English: I'll lead you to a ship, but not without Marcus' gold.
Romanian: - Foarte bine.
English: Just fine.
Romanian: Dle Martin, permiteti-mi să vă spun că hainele dv nu sunt potrivite pentru o întrunire stiintifică precum aceasta.
English: Mr. Martin, if you don't mind my saying so, I don't think that costume is quite appropriate to a serious scientific meeting like this.
Romanian: - Un moment.
English: - Oh, now, just a minute--
Romanian: Le-am adus, domnule.
English: Here we are sir.
Romanian: - Da. Flem, uite-o că vine.
English: Oh, Flem, here she comes.
Romanian: Oh, nu.
English: Oh, no.
Romanian: Ridicol.
English: - Ridiculous.
Romanian: # E minunat #
English: Feelin' high
Romanian: Nu poţi câştiga.
English: You can't beat it.
Romanian: Eu sunt Don Antonio José Miguel de Prado, Conte Pimentel...
English: I am Don Antonio José Miguel de Prado, Count Pimentel...
Romanian: Minunat!
English: Splendid.
Romanian: Colonelul, domnilor.
English: The Colonel, gentlemen.
Romanian: Acum ești de partea dreaptă, Marvin.
English: You are on the right side now, Marvin.
Romanian: Regina!
English: The Queen!
Romanian: Nu ai multa încredere în mine, nu-i asa ?
English: You haven't much faith in me, have you?
Romanian: La bazaruri.
English: To the bazaars.
Romanian: Din localul ăsta?
English: From this place here?
Romanian: Campionul neînvins din Valea Ciuboţicii Cucului va concura cu tanti Martha Hubbard, campioana neînvinsă din Arcul Frânt.
English: Valley will contest against Aunt Martha Hubbard, undefeated champion of Broken Bow.
Romanian: Am uitat că nu-i ştii numele de familie.
English: Oh, I forgot you didn't know her last name.
Romanian: - Attunci păstrează-l.
English: - Then keep it.
Romanian: - Aţi vrut să vă uitaţi peste astea ?
English: - You wanted to look these over?
Romanian: V-ar deranja preliminar pentru interior doar un moment, domnule?
English: Would you mind stepping inside for just one moment, sir?
Romanian: A dispărut evidența contabilă?
English: The accounts gone?
Romanian: Cum de ştii?
English: How do you know?
Romanian: - N-am isprăvit, domnule!
English: - I'm not finished!
Romanian: Nu se poate.
English: It's not possible.
Romanian: Te aştepţi să mă pun în genunchi şi să te implor?
English: Do you expect me to get down on my knees and beg ?
Romanian: - Din patru motive.
English: Four very distinct reasons.
Romanian: Oh, stai aici, Case.
English: Oh, sit here, Case.
Romanian: Nu ştiu.
English: Oh, I don't know.
Romanian: Am venit să te iau la meciul de polo, joacă Teddy.
English: By the way, I'll take you take to the polo match. Teddy's playing.
Romanian: Nu mi-aş dori să las impresia că sunt doar o aventurieră.
English: I shouldn't want you to get the impression that I'm just an adventuress.
Romanian: Scrisorile mele.
English: My letters.
Romanian: De ce nu săpaţi puţin mai adânc, băieţi?
English: Why don't you dig a little deeper, lads.
Romanian: Şefu'. O ştire bombă.
English: Hey, chief, fresh story.
Romanian: Creşte mai repede decât ar trebui.
English: It keeps growing much faster than it should!
Romanian: Cum adică?
English: What are you saying?
Romanian: Știi că mă gândeam să deschid aici și un magazin de parfumuri.
English: You know, I was thinking Of putting in a perfume shop here.
Romanian: Omoară unul, şi va trebui să-i omorâm pe toţi.
English: Kill one, and we'll have to kill all.
Romanian: Vom vedea. Amesteca-le.
English: Shuffle them.
Romanian: Aşa sunt eu.
English: That's me.
Romanian: Iti pierzi timpul cu mine.
English: I'm a wreck.
Romanian: Nu pare sa stie ce-i apartine si ce nu!
English: He don't seem to know what belongs to him and what doesn't.
Romanian: Bine.
English: Okay.
Romanian: Tot ce mă interesează e doar să fie corect.
English: All I'm interested in is its accuracy.
Romanian: - Alo, tu ești, Black?
English: - Hello, is that you, Black?
Romanian: Nu ai timp să vorbeşti cu mine?
English: "Don't you have time to talk to me?"
Romanian: Anck-es-en-Amon.
English: Anck-es-en-Amon.
Romanian: Păi n-ar trebui să fie aşa complicat.
English: Well, it shouldn't be difficult.
Romanian: Cum să o spun?
English: How shall I put it?
Romanian: Nu voi putea iubi alt bărbat.
English: I can't ever love another man.
Romanian: - Priviţi, pământ la orizont!
English: - Land ho, sir!
Romanian: Baieti, am mers destul de departe.
English: Well, boys, this has gone far enough. I'll just call that $2 bet.
Romanian: - Bună, Alma-Rose.
English: - Hello, Alma-Rose.
Romanian: - Îţi place asta, Swan ?
English: - Do you like this, Swan?
Romanian: Prieteni,e un leu pe strazile din Osage.
English: Friends, there's a lion in the streets of Osage.
Romanian: O perla penru fiecare gardian.
English: A pearl to every guard.
Romanian: Îmi pare rău.
English: I'm sorry.
Romanian: Arestaţi-l pe acest om, dle poliţist.
English: Ηim, Officer!
Romanian: Noi am încercat să nu.
English: We tried not to.
Romanian: Acum, ascultă-mă, băiete, eu sunt prietenul tău.
English: Now, listen, boy, I'm your friend.
Romanian: - Nu pot, mulţumesc.
English: - I can't do anything.
Romanian: - Billali ?
English: Billali?
Romanian: De unde ştie el?
English: How does he know?
Romanian: Domnilor,un suflet nepieritor a fost torturat la cazna... Si va cer,ca oameni cu sange in vene... Care aveti femei neajutorate la casele voastre...
English: Gentlemen, an immortal soul has been tortured on the rack... and I ask you as men with blood in your veins... who have helpless women in your own homes... to think of one of your innocent, dear ones... wronged and oppressed, like this poor defenseless woman.
Romanian: - Grăbiţi-vă !
English: He knows better. - Hurry up.
Romanian: - Atunci urmati-ma.
English: - Then follow me.
Romanian: Deschide uşa!
English: Open the door!
Romanian: A spus ca ma suna mai tarziu.
English: Said he'd tell me later today.
Romanian: Haide, prostuţo, mănâncă-ţi supa.
English: Come on, silly, eat your soup.
Romanian: Pun la cale o surpriză mare pentru el.
English: I'm planning a big surprise for him.
Romanian: Ce mai faceţi ?
English: How do you do?
Romanian: Ministrul de Interne
English: Minister of Interior
Romanian: Ei, Mr. Jaffe, arată frumos.
English: Say, Mr. Jaffe, it looks like a knockout.
Romanian: Ei bine, tinere, te-ai hotărât în ​​sfârșit să te trezești, nu?
English: Well young man, you've finally decided to get up, eh?
Romanian: Abia în 1928 Grecia a deschis fiecare paradă.
English: It was not until 1928 that Greece opened each parade.
Romanian: - Ce te-a făcut să renunți?
English: - What made you quit?
Romanian: Multumesc, domnule Newsome!
English: thanks Mister Newsome, that will be fine.
Romanian: Părinţii i-au trimis scrisori bătrânului director
English: Parents have sent letters to the old principal
Romanian: Dacă-ţi deschizi gura îţi scot un dinte.
English: You open your mouth and I'll pop a tooth out of it.
Romanian: Erezia!
English: Heresy!
Romanian: Da, ştiu.
English: Yes, I know.
Romanian: - E prima data cand eu...
English: It's the first time I-- You mean that?
Romanian: Domnul, glumeşte.
English: The gentleman is only fooling.
Romanian: Putea s-o facă unchiul tău
English: His uncle could have done it.
Romanian: - lmposibil!
English: - Impossible.
Romanian: Doar suntem la Ritz și ești prea mare și prea puternic ca să accepți păcăleli.
English: I on my part would undertake to produce Mrs. Drummond. Uh huh. Well, after all we are in the Ritz and you're too big and strong a man to allow any horseplay.
Romanian: - Da !
English: - Yes!
Romanian: Da, domnule.
English: Yes, sir.
Romanian: E mai bine!
English: That's better!
Romanian: Nu vine Richard?
English: Isn't Richard coming?
Romanian: - Mulţumesc.
English: Thanks.
Romanian: Trebuie să continuăm împreună.
English: We've got to keep going along together.
Romanian: M-ar împuşca.
English: He'd shoot me.
Romanian: Te iubesc.
English: I love you.
Romanian: Ce importanţă are, Rico?
English: What's the difference, Rico?
Romanian: A doua zi întâlnesc, cea mai frumoasă femeie din lume.
English: Next day you find yourself alone with the most beautiful woman in the world.
Romanian: O idee dragă lui Pierre de Coubertin.
English: An idea dear to Pierre de Coubertin.
Romanian: Hai să ne căsătorim.
English: Let's get married.
Romanian: COLIN CU MAMA SA, DOAMNA BEAN
English: COLIN WITH MA BEANS, HIS MOTHER
Romanian: Și nu uita, să-i spui.
English: And don't forget, tell him.
Romanian: Nu inteleg domnule.
English: I don't follow, sir.
Romanian: În ziua aceea, ucenicii au venit la Isus şi L-au întrebat:
English: But on this day the disciples had come to Jesus and asked im:
Romanian: I-as spune că îl iubesc.
English: I would tell him that I love him.
Romanian: Haide, uită de toate, iar eu mă întorc într-un minut.
English: Come on, you forget about it all and I'll be back in just a minute.
Romanian: L-am văzut pe Baigneur ieri și am jucat marea scenă a dezonoarei.
English: I saw Baigneur yesterday and played the big dishonor scene
Romanian: Ce le-ar putut causa, Profesore ?
English: What could have caused them, Professor?
Romanian: Sal...
English: I'll tell you the truth.
Romanian: - Eu nu cred...
English: - I don't think...
Romanian: "Şi lichior de mentă pentru că am întâlnit-o la poarta"
English: And then she gave me crme de menthe for meeting her at the gate
Romanian: Voi demonstra cu pipeta.
English: Will demonstrate with eyedropper.
Romanian: Dar vom fi arestaţi.
English: Why, we'd be arrested.
Romanian: Oh, la revedere, Egbert. Ştii, divorţurile mă fac să devin aşa sentimentală.
English: Oh, goodbye Egbert, you know, divorces make me so sentimental.
Romanian: - Nicole, te...
English: - Oh Nicole, I...
Romanian: - Adu barca înapoi. - Nu.
English: - Call back the boat.
Romanian: Dar, desigur, acum...
English: Oh, but of course, now...
Romanian: - Andrews.
English: - 'Andrews.'
Romanian: - Prima pacientă.
English: - First patient.
Romanian: Sa iesim!
English: Let's get out of here!
Romanian: Să vă spun eu ce cred despre omul vostru invizibil: e o făcătură.
English: I'll tell you what I think of your invisible man: it's a hoax.
Romanian: - Desigur.
English: - Naturally.
Romanian: - Absolut nimic.
English: - Not a thing!
Romanian: Regele a avut un fiu de la prima soţie?
English: No! Did the king have a son by his second wife?
Romanian: Dl Thornton va risipi aurul.
English: Mr. Thornton would only squander the gold.
Romanian: Păi am văzut-o pe soţia mea.
English: Well, I've seen my wife.
Romanian: - Roșcato.
English: - Red.
Romanian: Da, cred că este un bătrân prost.
English: Yes, I guess he is an old fool.
Romanian: Oh, tu eşti!
English: Oh, it's you!
Romanian: - Să deranjeze?
English: -Mind?
Romanian: Mă iertaţi, d-le, dar ordinele spun... că dacă semnaţi, nu va mai pot servi mâncare.
English: Excuse me, but my orders are... if you sign for it, I cannot serve any more food here.
Romanian: A comis o crimă când s-a căsătorit cu tânărul Hornblower fără să-i spună că provine dintr-un alt fel de anturaj.
English: - She committed her real crime when she married young Hornblower without telling him she came out of a certain world to do it.
Romanian: - Dar nu înţelegeţi...
English: But you don't understand.
Romanian: "Lăsaţi-ne să ne facem datoria de bună voie.
English: "Let us choose to do our duty willingly.
Romanian: Spitalul catolic, Albert.
English: Catholic hospital, Albert.
Romanian: Tine-te.
English: Hold on.
Romanian: Dar, nicio vorbă către el...
English: But not a word to him...
Romanian: Vă rog, nu spuneţi asta.
English: Please don't say that.
Romanian: Sigur.
English: Sure.
Romanian: Nu, nu cred.
English: No, not really.
Romanian: Și dacă nu îmi place? Am să te trag la bord.
English: Sailing into harbor with what for cargo?
Romanian: Ce era să fac?
English: What could I do?
Romanian: Așa că l-am dus la Frank Valentini de pe a treia stradă.
English: So, I run him over to Frank Valentini's speak over on third street.
Romanian: Ce-i va spune Navarra acestui mire?
English: Oh, what will Navarre say to this bridegroom?
Romanian: Mâna !
English: Mina!
Romanian: Inca un lucru.
English: One thing more.
Romanian: Păi...
English: Well...
Romanian: Probabil ca singurul lucru pe care-I puteam face ca sa ajung...
English: I guess the only thing I could have done if I'd gone to the gas station--
Romanian: Baronul este obosit?
English: Is the Baron tired?
Romanian: În plus, atâta exercițiu merită un julep.
English: Besides, that, uh, exertion calls for a julep.
Romanian: - Ah, fiule, viața m-a făcut dificil.
English: - Ah, son, it's life that's made me hard.
Romanian: O să facă mai mult bine decât contemplarea templelor.
English: It'll do you a lot more good than ruined temples.
Romanian: Şi acum unde mergem ?
English: Now where?
Romanian: Păi, am luat asta înainte să promit.
English: Well, I took that before I promised.
Romanian: - Ţi-a murdărit caracterul ?
English: - Slandered your character?
Romanian: Actul 5
English: ACT FIVE
Romanian: E ca şi cum ai căuta acul într-o căpiţă cu fân.
English: ♪ It's just like looking for a needle In a haystack. ♪
Romanian: Vi-I prezint pe Larry Renault, d-le Stengel.
English: This is Larry Renault, Mr. Stengel.
Romanian: Ne mai vedem.
English: See you often.
Romanian: - Multumesc că ati venit.
English: - How do you do?
Romanian: Nu mi-ai mai adus garniturile.
English: You didn't bring me any washers.
Romanian: Număra până la cinci sute şi nu te mişca!
English: "Count five hundred... and HOLD STILL!"
Romanian: Tu te ţii de planul tău, Louis.
English: You stick to your racket, Louis.
Romanian: M-am trezit tipând, crezând ca ma urmareste politia.
English: I'd wake up screaming thinking the police were after me.
Romanian: - Cum ?
English: What?
Romanian: "La Paris, poate.
English: "In Paris, perhaps.
Romanian: Nu mă cunoașteți, dle Duvalle.
English: You don't know me, Monsieur Duvalle.
Romanian: Băieţii s-au baricadat în pod.
English: Sir, the boys have barricaded themselves in the attic.
Romanian: Poate.
English: Maybe.
Romanian: E frig acolo sus noaptea.
English: Cold up here in the night patrol.
Romanian: Căţăraţi-vă pe zid.
English: Climb over the wall.
Romanian: - Bună dimineaţa.
English: - Good morning.
Romanian: - Eşti salvat?
English: - Are you saved?
Romanian: Poate ca nu.
English: Maybe not.
Romanian: Haide !
English: Come on.
Romanian: - Te-a refuzat?
English: - He did?
Romanian: Dar nu-mi plac mamele din această Curte şi nu ştiu unde să mai caut !"
English: But I don't like the mothers in this Court an' I don't know where else to look!"
Romanian: Nu vrea să spună, cine-i tatăl !
English: "She doesn't want to say who the father is."
Romanian: Noi scotocim subsolul.
English: We'll search the basement.
Romanian: Da, am început cu cele tinere.
English: Yeah, I started with the young ones, too.
Romanian: Ia uite ce avem aici!
English: Look at what we got here!
Romanian: Îl vede în sfârșit pe Stallard.
English: He sees Stallard at last.
Romanian: Ce scrie în ziar?
English: What does it say in the paper?
Romanian: Gerry...
English: Oh, Gerry...
Romanian: Aud o voce.
English: I hear a voice.
Romanian: Aşa şi este!
English: - He is.
Romanian: Probabil ai dreptate.
English: Yes, I guess you're right
Romanian: Sigur că vreau o prezentare dar nu aşa. Vreau o prezentare drăguţă. De genul...
English: He used big words and said such good things about him.
Romanian: - Salut, Crocker.
English: Hello Crocker.
Romanian: Hei, vino aici.
English: Hey. Come here.
Romanian: Oh.
English: Oh.
Romanian: Au cotit de pe strada Rodney Avenue pe autostrada 17.
English: They turned from Rodney Avenue into Highway 17.
Romanian: - Pa, Susie.
English: - Bye, Susie.
Romanian: El e un mare ceva si nu-i un politician.
English: He's a big something, and it ain't a politician.
Romanian: Voi s-au imaginind pentru escroc-mă de nişte bani?
English: You guys were figuring to gyp me out of some dough?
Romanian: Ce vrei să spui?
English: What do you mean?
Romanian: O sa fim ruinati pana atunci.
English: -We'll be ruined before then
Romanian: - Aşează-te, dle Dodsworth.
English: - Sit down, Mr. Dodsworth.
Romanian: Tom !
English: Tom.
Romanian: - Nu v-aţi simţi datoare stând aici, nu ?
English: You wouldn't feel obligated if you stayed, would you?
Romanian: Nu ar trebui să te descurajezi.
English: As a matter of fact, I liked you at rehearsals.
Romanian: Nu-i place să-i facă pe pasageri să aştepte.
English: He hates keeping passengers waiting.
Romanian: Vrei sa verifici oricum?
English: Well, check it anyway, would you?
Romanian: La pământ!
English: Get down!
Romanian: Bună seara, mama Durând.
English: Good evening, Mother Durand.
Romanian: - Ce mai faci, Will?
English: - How are you, Will?
Romanian: Ce mi se întâmplă ?
English: What's the matter with me?
Romanian: De ce filmele în special?
English: Why the movies particularly?
Romanian: Eu cunosc doar caii.
English: All I know is horses.
Romanian: Florence!
English: Florence!
Romanian: Nu-ţi mai aminteşti nimic ?
English: Don't you remember at all;
Romanian: Nu, n-avem de ce, cu excepţia lui Welch.
English: Oh, no. Not a thing... except Welch.
Romanian: Hai, eşti în regulă.
English: Come on, you're all right.
Romanian: - Da, si generalii.
English: - Yeah, generals too.
Romanian: Permiteti-mi sa va întreb ceva, domnule.
English: Let me ask you something, sir.
Romanian: Am primit scrisoarea doamnei şi sincer mulţumesc.
English: I have received your letter, madam, for which I am most grateful.
Romanian: - Pregatiti-va de ridicat ancora.
English: - We're off.
Romanian: Împreună cu o mică lăcustă, îi cântau cu tandreţe dulci imnuri de primăvară.
English: With a little grasshopper, tenderly, They sang her sweet hymns of spring.
Romanian: "Cum poţi suporta?"
English: "How can you stand it?"
Romanian: E bolnav.
English: He's sick.
Romanian: El cum arată ?
English: What's he look like?
Romanian: Îl aveţi sau nu?
English: Well, have you got it or haven't you got it?
Romanian: Şi nu am ce face.
English: I can't help it.
Romanian: Pentru că și tu îmi placi.
English: Because I like you a good deal too.
Romanian: Păcatele mele ! Sfântă Fecioară, cu ce ţi-am greşit ?
English: Holy Virgin, what have I done?
Romanian: Ei, ăsta da început de an nou.
English: Well, this is a fine way to start the New Year.
Romanian: Stai cât de mult doreşti.
English: Stay as long as you like.
Romanian: Lasă-te jos!
English: Get down from there!
Romanian: Numeşti asta discuţie?
English: You call that an argument?
Romanian: Dar aşa s-a întâmplat.
English: But it happened.
Romanian: Poliţia leagă această crimă cu omorul din cazul Landis.
English: Police link this murder with the Landis killing.
Romanian: Nu mergem fără tine.
English: We don't wanna go without you.
Romanian: Îmi place numele ăsta.
English: I like that name.
Romanian: Aruncați o privire la astea.
English: Take a look at these.
Romanian: Tată !
English: "Father!"
Romanian: - Ce mai faci, Baggs?
English: How are you, Baggs?
Romanian: Bine... Bine.
English: Fine... fine.
Romanian: Puteţi lucra pentru mine oricând.
English: You can work for me any time.
Romanian: Nu.
English: No.
Romanian: Dar, v-am spus, a dispărut.
English: But, I've been telling you, she vanished.
Romanian: Vei face aceasta?
English: Will you do it?
Romanian: Chiar dacă ţi se va spune să nu mai vii?
English: Even though they tell you not to?
Romanian: Da.
English: Yeah.
Romanian: Salutare, Dusty !
English: -Hi there, Dusty.
Romanian: Îmi amintesc acum,
English: l remember now,
Romanian: "Faimosul misionar s-a întors din China ca să-şi reformeze oraşul natal."
English: "Famous missionary returns from China... "to clean up his home town."
Romanian: Ei bine, cred că nu știe despre Dick.
English: I guess he doesn't know about Dick.
Romanian: Şi totuşi nu pot rămâne.
English: And yet I can't stay.
Romanian: Vreau s-o laşi în pace.
English: I want you to let her alone.
Romanian: - Ai cui oameni sunt ăştia?
English: Whose men are these?
Romanian: Bună ziua, domnule B. Era şi vremea să te întorci.
English: Well, hello Mr B. About time you were getting back.
Romanian: Ce veşti ai, aliatule arab?
English: What news from our ally? Bad news, sahib.
Romanian: Oricând pot culege noroi la fel de ușor asemeni caiilor de vreme frumoasă.
English: Say, I can pick mudders just as easily as fair weather horses anytime.
Romanian: Ai putea vorbi cu Goldberg.
English: You could fix it with Goldberg.
Romanian: Nu sunteţi aşteptaţi mâine?
English: Aren't you due tomorrow?
Romanian: Nu e treaba ta!
English: It's not your business!
Romanian: De ce, care este problema?
English: Why, what's the matter?
Romanian: Eram mai mult morţi decât vii !
English: We were dead.
Romanian: Te lasă să-i bagi mâna în gura lui, de ce nu şi capul ?
English: He'll let you stick your hand in, why not your head?
Romanian: Ce ?
English: What?
Romanian: Apoi se intimpla diverse lucruri.
English: Them things will happen.
Romanian: - Daca nu a fost acel mare babun(peste mare).
English: - if it wasn't for that big baboon.
Romanian: - Da.
English: - Sure.
Romanian: - Noroc!
English: -Cheers.
Romanian: Yvonne, eşti bine?
English: Yvonne, are you all right?
Romanian: Buna dimineata.
English: Morning.
Romanian: Morgan este mut.
English: Morgan is dumb.
Romanian: Pare că totuşi o face.
English: It looks like it though.
Romanian: - Doar un minut.
English: - Just a minute.
Romanian: "pentru a fi bogata si prospara, o natiune trebuie sa isi poata asigura aprovizionarea cu lemne."
English: "to be reach and prosperous, a nation must have a safe secure supply of wood"
Romanian: Există mulţi marinari cu un singur picior?
English: Are there many one-legged seafaring men?
Romanian: Găsesc apa aşa de curată C-am intrat să fac baie.
English: I found the water so clear That I went in to bathe
Romanian: Bună, Julie?
English: Hello, Julie?
Romanian: Nu cred că e posibil acum.
English: I don't think that's possible right now.
Romanian: Si o sa-i spun mamei tale ca tu n-ai fost in China - c-ai fost in puscarie.
English: And I'll tell your mother that you weren't in China- that you were in jail.
Romanian: - Ăla de este afacerist !
English: I told you about him. He's in business.
Romanian: - Mmm.
English: - Mmm.
Romanian: E minunat!
English: It's beautiful!
Romanian: Care este experimentul ?
English: What is the experiment?
Romanian: Apoi, ca un răspuns la rugaciunea unei copile, veni la Oak Grove frumoasa Bebe Blair.
English: like the answer to a maiden's prayer there came to Oak Grove, Beautiful Bebe Blair.
"""