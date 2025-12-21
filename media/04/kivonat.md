# Törzsszolgálati Ismeretek - Közérthető Kivonat

*Ez a kivonat a törzsszolgálati ismeretek tananyag legfontosabb fogalmait magyarázza el közérthető módon, majd megadja a precíz definíciókat.*

---

## 1. Katonai Műveletek Szintjei

### Mi ez egyszerűen?

Képzeljük el a hadműveletet úgy, mint egy vállalat működését:
- A **stratégiai szint** olyan, mint az igazgatóság: ők döntik el, milyen üzletágakat célozzunk meg (háborús célok)
- A **hadműveleti szint** olyan, mint a középvezetés: ők tervezik meg a kampányokat és koordinálják az osztályokat
- A **harcászati szint** olyan, mint a terepen dolgozó csapatok: ők hajtják végre a konkrét feladatokat

```mermaid
flowchart TD
    subgraph "🏛️ STRATÉGIAI SZINT"
        S1[Politikai-katonai döntéshozatal]
        S2[Háborús célok meghatározása]
        S3[Erőforrások elosztása]
    end

    subgraph "⚔️ HADMŰVELETI SZINT"
        H1[Hadjáratok tervezése]
        H2[Hadműveletek összehangolása]
        H3[Erők koordinálása]
    end

    subgraph "🎯 HARCÁSZATI SZINT"
        T1[Csaták és ütközetek]
        T2[Alegységek közvetlen harca]
        T3[Feladatok végrehajtása]
    end

    S1 --> H1
    H1 --> T1

    style S1 fill:#E8F4FD,stroke:#4A90A4
    style S2 fill:#E8F4FD,stroke:#4A90A4
    style S3 fill:#E8F4FD,stroke:#4A90A4
    style H1 fill:#FDF2E8,stroke:#D4A574
    style H2 fill:#FDF2E8,stroke:#D4A574
    style H3 fill:#FDF2E8,stroke:#D4A574
    style T1 fill:#E8FDE8,stroke:#74A474
    style T2 fill:#E8FDE8,stroke:#74A474
    style T3 fill:#E8FDE8,stroke:#74A474
```

### Pontos definíciók

> **Stratégiai szint:** A legmagasabb szint, ahol a politikai és katonai vezetés meghatározza a háború céljait, mozgósítja az erőforrásokat, és összehangolja a nemzeti erőfeszítéseket a stratégiai célkitűzések elérése érdekében.

> **Hadműveleti szint:** A közbenső szint, ahol a hadműveleti parancsnokságok megtervezik és végrehajtják a hadjáratokat és nagyobb hadműveleteket a stratégiai célok elérése érdekében.

> **Harcászati szint:** A legalsó szint, ahol a csapatok közvetlenül harcolnak az ellenséggel. Itt történnek a csaták, ütközetek és harcászati feladatok végrehajtása.

---

## 2. A Törzs és Szervezete

### Mi ez egyszerűen?

A törzs olyan, mint egy vállalat központi irodája, ahol különböző osztályok dolgoznak együtt a vezető támogatására. Minden osztálynak (részlegnek) megvan a saját szakterülete:

- **G1/S1** - "HR osztály" → személyügyek, állomány
- **G2/S2** - "Piackutató" → hírszerzés, ellenség figyelése
- **G3/S3** - "Operatív igazgató" → hadműveletek tervezése
- **G4/S4** - "Logisztikai osztály" → ellátás, szállítás
- **G5/S5** - "Stratégiai tervező" → jövőbeli tervezés
- **G6/S6** - "IT osztály" → híradás, informatika
- **G7/S7** - "Oktatási központ" → kiképzés
- **G8/S8** - "Pénzügyi osztály" → költségvetés
- **G9/S9** - "PR és Kapcsolatok" → civil együttműködés

A "G" betű a magasabb szintű parancsnokságokat jelöli, az "S" az alacsonyabbakat.

```mermaid
flowchart LR
    subgraph "TÖRZS FELÉPÍTÉSE"
        PK[👨‍✈️ PARANCSNOK]
        TF[📋 TÖRZSFŐNÖK]

        subgraph "Koordináló törzs"
            G1[G1 Személyügy]
            G2[G2 Felderítés]
            G3[G3 Hadműveletek]
            G4[G4 Logisztika]
            G5[G5 Tervezés]
            G6[G6 Híradás]
        end

        subgraph "Különleges törzs"
            G7[G7 Kiképzés]
            G8[G8 Pénzügy]
            G9[G9 CIMIC]
        end
    end

    PK --> TF
    TF --> G1
    TF --> G2
    TF --> G3
    TF --> G4
    TF --> G5
    TF --> G6
    TF --> G7
    TF --> G8
    TF --> G9

    style PK fill:#FFE4E1,stroke:#CD5C5C
    style TF fill:#E6E6FA,stroke:#9370DB
    style G1 fill:#F0FFF0,stroke:#90EE90
    style G2 fill:#F0FFF0,stroke:#90EE90
    style G3 fill:#FFF0F5,stroke:#FFB6C1
    style G4 fill:#F0FFF0,stroke:#90EE90
    style G5 fill:#F0FFF0,stroke:#90EE90
    style G6 fill:#F0FFF0,stroke:#90EE90
    style G7 fill:#FFFACD,stroke:#F0E68C
    style G8 fill:#FFFACD,stroke:#F0E68C
    style G9 fill:#FFFACD,stroke:#F0E68C
```

### Pontos definíciók

> **Törzs:** A parancsnok vezetési tevékenységét támogató szervezet, amely szakértőkből áll, és biztosítja a döntés-előkészítést, tervezést, szervezést és az ellenőrzést.

> **G részlegek:** A dandár és magasabb szintű parancsnokságok koordináló és különleges törzsrészlegei, amelyeket számokkal (G1-G9) jelölnek, és specifikus szakterületekért felelősek.

> **S részlegek:** A zászlóalj és ezred szintű parancsnokságok törzsrészlegei, hasonló szakterületi felosztással, mint a G részlegek.

---

## 3. Vezetési Pontok

### Mi ez egyszerűen?

A vezetési pontok olyan helyszínek, ahol a parancsnok és törzse tartózkodik és irányítja a hadműveletet. Három fő típusa van:

- **FHP (Előretolt Harcálláspont)** - Olyan, mint egy mobil irodabusz a terepen. A parancsnok innen követi a harcot közelről, gyors döntéseket hozhat.

- **MHP (Fő Harcálláspont)** - Ez a "központi iroda", ahol a törzs nagy része dolgozik. Itt történik a részletes tervezés és koordináció.

- **FIH (Mögöttes Információs Központ)** - A "hátsó iroda", ahol a logisztikát és utánpótlást irányítják, valamint tartalék vezetési lehetőséget biztosít.

```mermaid
flowchart TB
    subgraph "HARCMEZŐ"
        E[☠️ Ellenség]

        subgraph "VEZETÉSI PONTOK"
            FHP[🚐 FHP<br/>Előretolt Harcálláspont<br/>Mobil, gyors döntések]
            MHP[🏢 MHP<br/>Fő Harcálláspont<br/>Tervezés központ]
            FIH[📦 FIH<br/>Mögöttes Központ<br/>Logisztika, tartalék]
        end

        CS[🎖️ Harcoló csapatok]
    end

    E <-.-> CS
    FHP --> CS
    MHP --> FHP
    FIH --> MHP

    style E fill:#FFCCCB,stroke:#FF6B6B
    style FHP fill:#E8F4FD,stroke:#4A90A4
    style MHP fill:#FFF3E0,stroke:#FFB74D
    style FIH fill:#E8F5E9,stroke:#66BB6A
    style CS fill:#E3F2FD,stroke:#42A5F5
```

### Pontos definíciók

> **FHP (Előretolt Harcálláspont):** Kis létszámú, mobil vezetési pont, ahonnan a parancsnok közvetlenül irányíthatja a harcot. Jellemzően a hadszíntéren, az eseményekhez közel helyezkedik el.

> **MHP (Fő Harcálláspont):** A parancsnokság fő vezetési pontja, ahol a törzs jelentős része tevékenykedik. Itt történik a hadműveletek részletes tervezése, szervezése és végrehajtásának irányítása.

> **FIH (Mögöttes Információs Központ):** Mögöttes területen elhelyezett vezetési pont, amely biztosítja a logisztikai irányítást és szükség esetén átveheti a vezetést, ha az MHP megsemmisül.

---

## 4. A Katonai Döntéshozatali Folyamat (MDMP)

### Mi ez egyszerűen?

Az MDMP egy 7 lépéses módszer arra, hogy a katonai vezetők jó döntéseket hozzanak. Olyan, mint egy recept, amit követve szisztematikusan végiggondolhatjuk a problémát és megtalálhatjuk a legjobb megoldást.

Képzeljük el, hogy egy esküvőt szervezünk:
1. **Feladat vétele** → Megkapjuk a feladatot: "Szervezz esküvőt!"
2. **Küldetés elemzése** → Elemezzük: ki a pár, mennyi vendég, mikor, hol
3. **Változatok kidolgozása** → Opciók: étterem? kert? kastély?
4. **Változatok elemzése** → Minden opciót végiggondolunk (költség, kapacitás, időjárás)
5. **Változatok összehasonlítása** → Döntési táblázatban hasonlítjuk össze
6. **Döntés** → A pár dönt a legjobb opció mellett
7. **Parancs elkészítése** → Részletes tervet írunk és kiosztjuk a feladatokat

```mermaid
flowchart TD
    subgraph "MDMP - 7 LÉPÉS"
        L1[1️⃣ Feladat vétele<br/>Megkapjuk a feladatot]
        L2[2️⃣ Küldetés elemzése<br/>Mit kell tennünk?]
        L3[3️⃣ Változatok kidolgozása<br/>Hogyan tehetjük?]
        L4[4️⃣ Változatok elemzése<br/>Hadijáték végrehajtása]
        L5[5️⃣ Változatok összehasonlítása<br/>Melyik a legjobb?]
        L6[6️⃣ Döntés<br/>Parancsnok elhatároz]
        L7[7️⃣ Harcparancs elkészítése<br/>Feladatok kiosztása]
    end

    L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7

    style L1 fill:#FFEBEE,stroke:#EF5350
    style L2 fill:#FFF3E0,stroke:#FF9800
    style L3 fill:#FFFDE7,stroke:#FFEB3B
    style L4 fill:#E8F5E9,stroke:#4CAF50
    style L5 fill:#E3F2FD,stroke:#2196F3
    style L6 fill:#EDE7F6,stroke:#673AB7
    style L7 fill:#FCE4EC,stroke:#E91E63
```

### Az MDMP lépései részletesen

#### 1. lépés: Feladat vétele (Receipt of Mission)

Egyszerűen: Megkapjuk a parancsot az elöljárótól, és megértjük, mit vár tőlünk.

> **Definíció:** Az a folyamat, amelynek során a parancsnok és a törzs megkapja, feldolgozza és értelmezi az elöljáró parancsát vagy intézkedését.

**Fő tevékenységek:**
- Elöljáró szándékának megértése
- Időszámvetés készítése
- Előzetes intézkedés kiadása

#### 2. lépés: Küldetés elemzése (Mission Analysis)

Egyszerűen: Alaposan átgondoljuk, mit kell tennünk, milyen akadályok vannak, és milyen erőforrásaink állnak rendelkezésre.

> **Definíció:** A tervezési folyamat azon lépése, amely során a törzs meghatározza a kötelezően végrehajtandó és a következtetett feladatokat, elemzi a körülményeket, és meghatározza a kritikus információigényeket.

**Kulcselemek:**
- **HFÉ (IPB)** - Harcmező Felderítő Értékelés: Az ellenség és a terep elemzése
- **CCIR** - Parancsnok Kritikus Információigénye: Amit tudnunk kell a döntéshez
- **PIR** - Elsődleges Információigény: Az ellenségről szükséges információk
- **FFIR** - Saját erőkkel kapcsolatos információigény
- **EEFI** - Rejtendő információk (amit az ellenségnek nem szabad megtudnia)

#### 3. lépés: Cselekvési változatok kidolgozása (COA Development)

Egyszerűen: Különböző opciókat dolgozunk ki a feladat megoldására.

> **Definíció:** Kreatív folyamat, amelynek során a törzs több lehetséges megoldási módot dolgoz ki a küldetés végrehajtására.

**Egy jó cselekvési változat:**
- Megvalósítható (van rá elég erőnk)
- Elfogadható (az áldozatok arányban vannak a céllal)
- Megfelelő (eléri a célt)
- Megkülönböztethető (valóban más, mint a többi opció)

#### 4. lépés: Változatok elemzése - Hadijáték (Wargaming)

Egyszerűen: Eljátsszuk fejben (vagy térképen), mi történne, ha végrehajtanánk az egyes opciókat.

> **Definíció:** Szisztematikus elemzési folyamat, amely során a törzs szimulált környezetben vizsgálja a cselekvési változatok végrehajtását az ellenség valószínű reakcióival szemben.

```mermaid
flowchart LR
    subgraph "HADIJÁTÉK SZEREPLŐI"
        PK[👨‍✈️ Parancsnok<br/>Irányít]
        TF[📋 Törzsfőnök<br/>Facilitál]
        G2[🔍 G2<br/>Ellenséget játssza]
        G3[⚔️ G3<br/>Saját erőket mozgatja]
        REC[📝 Rögzítő<br/>Jegyzetel]
    end

    PK --> TF
    TF --> G2
    TF --> G3
    G2 <-.Harc.-> G3
    G3 --> REC
    G2 --> REC

    style PK fill:#FFE4E1,stroke:#CD5C5C
    style TF fill:#E6E6FA,stroke:#9370DB
    style G2 fill:#FFCCCB,stroke:#FF6B6B
    style G3 fill:#E8F4FD,stroke:#4A90A4
    style REC fill:#FFFACD,stroke:#DAA520
```

**Hadijáték technikák:**
- **Öv-technika:** Arcvonal mentén haladunk
- **Doboz-technika:** Fontosabb körletekre fókuszálunk
- **Folyosó-technika:** Fő mozgási útvonalat követjük

#### 5. lépés: Változatok összehasonlítása (COA Comparison)

Egyszerűen: Döntési mátrixban összehasonlítjuk az opciókat kritériumok alapján.

> **Definíció:** A hadijáték során szerzett információk alapján a cselekvési változatok objektív összehasonlítása meghatározott kritériumok szerint.

#### 6. lépés: Döntés (COA Approval)

Egyszerűen: A parancsnok kiválasztja a legjobb opciót és elmondja szándékát.

> **Definíció:** A parancsnok jóváhagyja a javasolt cselekvési változatot és kihirdeti elhatározását, amely tartalmazza szándékát és útmutatását.

#### 7. lépés: Harcparancs elkészítése (Orders Production)

Egyszerűen: Részletes parancsot írunk, amely mindenki feladatát tartalmazza.

> **Definíció:** A döntés dokumentálása harcparancs (OPORD) formájában, amely tartalmazza a helyzetet, küldetést, végrehajtási utasításokat, támogatást és vezetési rendet.

---

## 5. Parancsnoki Információigények

### Mi ez egyszerűen?

A parancsnoknak folyamatosan információkra van szüksége a jó döntésekhez. Ezeket kategóriákba soroljuk:

```mermaid
flowchart TD
    subgraph "PARANCSNOKI INFORMÁCIÓK"
        CCIR[📊 CCIR<br/>Parancsnok Kritikus<br/>Információigénye]

        PIR[🔍 PIR<br/>Ellenségről<br/>szóló info]
        FFIR[👥 FFIR<br/>Saját erőkről<br/>szóló info]
        EEFI[🔒 EEFI<br/>Rejtendő<br/>információk]
    end

    CCIR --> PIR
    CCIR --> FFIR
    CCIR -.-> EEFI

    style CCIR fill:#E8F4FD,stroke:#4A90A4
    style PIR fill:#FFCCCB,stroke:#FF6B6B
    style FFIR fill:#E8F5E9,stroke:#66BB6A
    style EEFI fill:#FFF3E0,stroke:#FFB74D
```

### Pontos definíciók

> **CCIR (Commander's Critical Information Requirements):** A parancsnok kritikus információigénye - azok az információk, amelyek nélkülözhetetlenek a parancsnok időszerű döntéshozatalához.

> **PIR (Priority Intelligence Requirements):** Elsődleges hírszerzési igények az ellenségről és a hadműveleti környezetről.

> **FFIR (Friendly Force Information Requirements):** Saját erőkkel kapcsolatos információigények (pl. harckészültség, veszteségek).

> **EEFI (Essential Elements of Friendly Information):** Saját erőkről szóló rejtendő információk, amelyeket meg kell védeni az ellenségtől.

---

## 6. Gyakorlattervezési Eljárás (EP)

### Mi ez egyszerűen?

A katonai gyakorlatok (pl. NATO hadgyakorlatok) tervezése és végrehajtása rendkívül összetett folyamat. Az EP (Exercise Planning Process) 4 fő szakaszból áll, ami akár 2-3 évig is tarthat egy nagy gyakorlatnál.

Gondoljunk rá úgy, mint egy nagy filmforgatásra:
1. **0. szakasz (Initiation)** - Döntés: milyen filmet forgatunk
2. **1. szakasz (Specification)** - Forgatókönyv és költségvetés készítése
3. **2. szakasz (Planning)** - Részletes forgatási terv, szereplőválasztás
4. **3. szakasz (Conduct)** - Maga a forgatás és utómunka

```mermaid
flowchart LR
    subgraph "GYAKORLATTERVEZÉS 4 SZAKASZA"
        S0[0️⃣ INITIATION<br/>Kezdeményezés<br/>Mit gyakorolunk?]
        S1[1️⃣ SPECIFICATION<br/>Specifikáció<br/>Milyen lesz?]
        S2[2️⃣ PLANNING<br/>Tervezés<br/>Hogyan csináljuk?]
        S3[3️⃣ CONDUCT<br/>Végrehajtás<br/>Hajrá!]
    end

    S0 --> S1 --> S2 --> S3

    style S0 fill:#E8F4FD,stroke:#4A90A4
    style S1 fill:#FFF3E0,stroke:#FFB74D
    style S2 fill:#E8F5E9,stroke:#66BB6A
    style S3 fill:#FCE4EC,stroke:#E91E63
```

### Kulcs szervezetek

> **EXCON (Exercise Control):** A gyakorlat irányító szervezete, amely vezeti és értékeli a gyakorlatot.

> **HICON (Higher Control):** Magasabb szintű irányítás, amely a résztvevők felettes parancsnokságát szimulálja.

> **LOCON (Lower Control):** Alacsonyabb szintű irányítás, amely az alárendelt alegységeket szimulálja.

### Kulcs dokumentumok

> **EXSPEC (Exercise Specification):** A gyakorlat specifikációja, amely meghatározza a célokat, résztvevőket, időkeretet.

> **EXPLAN (Exercise Plan):** A gyakorlat részletes terve.

> **MEL/MIL (Master Event List/Master Incident List):** Fő esemény és incidens lista - a gyakorlat forgatókönyve.

---

## 7. NATO Jelek és Szimbólumok (APP-6)

### Mi ez egyszerűen?

A NATO szimbólumok egy nemzetközi "képnyelv", amelyet minden szövetséges ország katonái megértenek. Ez olyan, mint a közlekedési táblák - mindenhol ugyanazt jelentik.

### Alapszínek és jelentésük

```mermaid
flowchart TD
    subgraph "NATO SZÍNKÓDOK"
        KK[🔵 KÉK = Barát/Saját]
        PP[🔴 PIROS = Ellenség]
        ZZ[🟢 ZÖLD = Semleges]
        SS[🟡 SÁRGA = Ismeretlen]
    end

    style KK fill:#E3F2FD,stroke:#2196F3
    style PP fill:#FFEBEE,stroke:#F44336
    style ZZ fill:#E8F5E9,stroke:#4CAF50
    style SS fill:#FFFDE7,stroke:#FFEB3B
```

### Hovatartozás

> **Kék szín:** Barát erők (saját és szövetséges)
> **Piros szín:** Ellenséges erők
> **Zöld szín:** Semleges erők
> **Sárga szín:** Ismeretlen hovatartozású

### Kötelékméret jelölések

A katonai egységek méretét függőleges vonalak jelölik a szimbólum tetején:

| Jel | Kötelék | Angol | Létszám (kb.) |
|-----|---------|-------|---------------|
| • | Tűzfészek | Team | 2-5 |
| •• | Raj | Squad | 8-12 |
| ••• | Szakasz | Platoon | 30-50 |
| I | Század | Company | 100-200 |
| II | Zászlóalj | Battalion | 400-800 |
| III | Ezred/Csoport | Regiment | 1000-3000 |
| X | Dandár | Brigade | 3000-5000 |
| XX | Hadosztály | Division | 10000-20000 |
| XXX | Hadtest | Corps | 30000-50000 |
| XXXX | Hadsereg | Army | 80000+ |

### Szimbólum felépítése

```mermaid
flowchart TD
    subgraph "SZIMBÓLUM ÖSSZETEVŐI"
        K[KÖRVONAL<br/>Hovatartozás]
        KIT[KITÖLTÉS<br/>Harctéri dimenzió]
        IK[IKON<br/>Csapatnem/Funkció]
        MOD[MÓDOSÍTÓK<br/>Kiegészítő info]
    end

    K --> KIT --> IK --> MOD

    style K fill:#E8F4FD,stroke:#4A90A4
    style KIT fill:#FFF3E0,stroke:#FFB74D
    style IK fill:#E8F5E9,stroke:#66BB6A
    style MOD fill:#FCE4EC,stroke:#E91E63
```

### Harctéri dimenziók

| Szín | Dimenzió |
|------|----------|
| Világoskék | Űr |
| Kék | Levegő |
| Zöld | Szárazföld |
| Zöldeskék | Víz felszíni |
| Világoszöld | Víz alatti |

---

## 8. Harcászati Grafikai Jelek

### Mi ez egyszerűen?

Ezek a térképeken használt rajzok, amelyek a hadműveletek terveit mutatják: határvonalak, mozgások, célpontok stb.

### Határvonalak típusai

```mermaid
flowchart TD
    subgraph "HATÁRVONALAK"
        OH[OLDALSÓ HATÁRVONAL<br/>Szomszédos egységek között]
        EH[ELÜLSŐ HATÁRVONAL<br/>Az ellenség felé]
        MH[MÖGÖTTES HATÁRVONAL<br/>A hátország felé]
        FLOT[FLOT<br/>Előretolt saját csapatok vonala]
    end

    MH --> OH
    OH --> EH
    EH --> FLOT

    style OH fill:#E8F4FD,stroke:#4A90A4
    style EH fill:#FFCCCB,stroke:#FF6B6B
    style MH fill:#E8F5E9,stroke:#66BB6A
    style FLOT fill:#FFF3E0,stroke:#FFB74D
```

### Pontos definíciók

> **FLOT (Forward Line of Own Troops):** Előretolt saját csapatok vonala - az a vonal, amelyen túl már nincs saját erő.

> **FEBA (Forward Edge of the Battle Area):** A harcterület elülső széle.

### Fontos pontok

> **Checkpoint (Ellenőrző pont):** Mozgásszabályozásra, tűzhelyesbítésre vagy helymeghatározásra használt pont.

> **Linkup Point (Csatlakozási pont):** Könnyen azonosítható hely, ahol két erő érintkezik egymással.

> **Passage Point (Áthaladási pont):** Megjelölt hely, ahol egységek áthaladnak egymáson.

---

## 9. Harci Okmányok Rendszere

### Mi ez egyszerűen?

A harci okmányok a katonai "hivatalos papírok", amelyekkel a parancsokat, terveket és jelentéseket rögzítik és továbbítják. Olyanok, mint egy vállalat belső levelezése és dokumentációja - csak itt emberéletek múlnak a pontosságon.

### Okmányok típusai

```mermaid
flowchart TD
    subgraph "HARCI OKMÁNYOK TÍPUSAI"
        V[📋 VEZETÉSI<br/>Parancsok, tervek]
        B[📊 BESZÁMOLÓ<br/>Jelentések]
        T[📖 TÁJÉKOZTATÓ<br/>Információk]
    end

    subgraph "VEZETÉSI"
        OPORD[OPORD<br/>Harcparancs]
        WNGO[WNGO<br/>Előzetes intézkedés]
        FRAGO[FRAGO<br/>Kiegészítő parancs]
    end

    subgraph "BESZÁMOLÓ"
        ELH[Elhatározás]
        JEL[Jelentések]
        NAP[Hadműveleti napló]
    end

    V --> OPORD
    V --> WNGO
    V --> FRAGO
    B --> ELH
    B --> JEL
    B --> NAP

    style V fill:#E8F4FD,stroke:#4A90A4
    style B fill:#FFF3E0,stroke:#FFB74D
    style T fill:#E8F5E9,stroke:#66BB6A
    style OPORD fill:#FCE4EC,stroke:#E91E63
    style WNGO fill:#E3F2FD,stroke:#42A5F5
    style FRAGO fill:#F3E5F5,stroke:#AB47BC
```

### Harci okmányok követelményei

Minden harci okmánynak meg kell felelnie az alábbi követelményeknek:

1. **Időszerűség** - A késve elkészített okmány értéktelen
2. **Rövidség** - Tömören, szaknyelven megfogalmazva
3. **Érthetőség** - Egyértelműen, félreérthetetlenül
4. **Megbízhatóság** - Csak ellenőrzött adatok
5. **Szemléletesség** - Könnyű feldolgozni
6. **Szabványosság** - NATO előírások szerint

---

## 10. Az OPORD (Harcparancs) Felépítése

### Mi ez egyszerűen?

Az OPORD (Operation Order) a katonai parancsok "királya" - ez tartalmazza mindazt, amit a csapatoknak tudniuk kell a feladat végrehajtásához. 5 fő részből áll, amelyeket mindig ugyanabban a sorrendben írnak.

```mermaid
flowchart TD
    subgraph "OPORD 5 PONTJA"
        P1[1️⃣ HELYZET<br/>Mi a helyzet?]
        P2[2️⃣ KÜLDETÉS<br/>Mi a feladat?]
        P3[3️⃣ VÉGREHAJTÁS<br/>Hogyan csináljuk?]
        P4[4️⃣ MŰVELETTÁMOGATÁS<br/>Mi kell hozzá?]
        P5[5️⃣ VEZETÉS ÉS HÍRADÁS<br/>Ki irányít?]
    end

    P1 --> P2 --> P3 --> P4 --> P5

    style P1 fill:#FFEBEE,stroke:#EF5350
    style P2 fill:#FFF3E0,stroke:#FF9800
    style P3 fill:#E8F5E9,stroke:#4CAF50
    style P4 fill:#E3F2FD,stroke:#2196F3
    style P5 fill:#EDE7F6,stroke:#673AB7
```

### Az 5 pont részletesen

#### 1. HELYZET
- Ellenség helyzete, ereje, szándéka
- Saját erők, szomszédok
- Terep és időjárás hatásai
- Civil tényezők

#### 2. KÜLDETÉS
- **Ki** hajtja végre?
- **Mit** kell tenni?
- **Mikor** kell végrehajtani?
- **Hol** történik?
- **Miért** (milyen célból)?

> **Fontos:** A 2. pont NEM tartalmazhat alpontokat - egy tömör mondatban kell megfogalmazni!

#### 3. VÉGREHAJTÁS
- Parancsnok szándéka
- Művelet elgondolása
- Alárendeltek feladatai
- Koordinációs utasítások

#### 4. MŰVELETTÁMOGATÁS
- Logisztika (ellátás, szállítás)
- Személyügy
- Egészségügy

#### 5. VEZETÉS ÉS HÍRADÁS
- Vezetési pontok helye
- Parancsnoklási sorrend
- Híradás rendje

### Kiegészítő okmányok

> **WNGO (Warning Order - Előzetes intézkedés):** Előzetes figyelmeztetés a várható feladatról, amely segíti az alárendeltek felkészülését.

> **FRAGO (Fragmentary Order - Kiegészítő intézkedés):** Rövidített parancs a változások közlésére, amely csak a megváltozott részeket tartalmazza.

---

## Összefoglaló Táblázat

| Fogalom | Egyszerűen | Definíció |
|---------|------------|-----------|
| **MDMP** | 7 lépéses döntési recept | Katonai Döntéshozatali Folyamat |
| **OPORD** | A fő parancs | Harcparancs (Operation Order) |
| **CCIR** | Amit a parancsnoknak tudnia kell | Parancsnok Kritikus Információigénye |
| **PIR** | Ellenségről szóló kérdések | Elsődleges Hírszerzési Igények |
| **FHP** | Mobil iroda a fronton | Előretolt Harcálláspont |
| **MHP** | Központi iroda | Fő Harcálláspont |
| **G3** | Hadműveleti főnök | Hadműveleti törzsrészleg |
| **HFÉ/IPB** | Ellenség és terep elemzése | Harcmező Felderítő Értékelés |
| **EXCON** | Gyakorlat irányítói | Exercise Control |
| **APP-6** | NATO "képnyelv" | Katonai szimbólumrendszer |

---

*Ez a kivonat a "Törzsszolgálati ismeretek" tananyag közérthető összefoglalása. A precíz definíciók és részletes szabályok az eredeti dokumentumban találhatók.*
