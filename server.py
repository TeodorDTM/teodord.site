from flask import Flask, request, jsonify, send_from_directory # pyright: ignore[reportMissingImports]

app = Flask(__name__, static_folder='.', static_url_path='')

# ============================================================
#   MENIU PRINCIPAL
# ============================================================

MENIU_PRINCIPAL = [
    '1. Matrici',
    '2. Generarea Matricelor',
    '3. Subprograme',
    '4. Siruri de Caractere',
    '5. Struct',
    '6. Recursivitate',
    '7. Mesajul de final al clasei a X-a',
    '8. Exit',
]

# ============================================================
#   TEORIE
# ============================================================

def teorie_capitol_1():
    return {
        'titlu': 'Matrici',
        'definitii': [
            {
                'termen': 'Matrice',
                'definitie': 'Un tablou bidimensional de elemente de acelasi tip, organizat pe linii si coloane, accesat prin doi indici: linia si coloana.'
            },
            {
                'termen': 'Element a[i][j]',
                'definitie': 'Elementul de pe linia i si coloana j al matricei. In C++, indicii pornesc de la 0.'
            },
            {
                'termen': 'Matrice patratica',
                'definitie': 'Matrice cu acelasi numar de linii si coloane (n x n).'
            },
            {
                'termen': 'Diagonala principala',
                'definitie': 'Elementele pentru care i == j (de la coltul stanga-sus la dreapta-jos).'
            },
            {
                'termen': 'Diagonala secundara',
                'definitie': 'Elementele pentru care i + j == n - 1 (de la dreapta-sus la stanga-jos).'
            },
        ],
        'explicatii': [
            {
                'titlu': '1.1.1 Ce sunt matricile?',
                'text': 'O matrice este o structura de date bidimensionala — un tabel cu linii si coloane. In C++ o reprezentam ca un array de arrays. Fiecare element este identificat unic prin doua coordonate: linia (i) si coloana (j). Sunt folosite pentru probleme cu grile, imagini, grafuri reprezentate prin matrice de adiacenta etc.'
            },
            {
                'titlu': '1.1.2 Declararea unei matrici',
                'text': 'In C++ declarati o matrice specificand tipul elementelor si dimensiunile maxime: int a[NMAX][NMAX]. Puteti initializa cu 0 folosind int a[100][100] = {0}. Dimensiunile reale n si m se citesc de la tastatura si trebuie sa fie mai mici sau egale cu NMAX.'
            },
            {
                'titlu': '1.1.3 Citirea si afisarea matricilor',
                'text': 'Citirea se face cu doua for-uri imbricate: primul parcurge liniile (i de la 0 la n-1), al doilea parcurge coloanele (j de la 0 la m-1). La afisare, dupa fiecare linie completa se afiseaza endl sau "\\n" pentru a trece pe randul urmator.'
            },
            {
                'titlu': '1.1.4 Operatii cu matrici',
                'text': 'Operatiile clasice includ: suma a doua matrici (element cu element), transpusa (a[i][j] devine a[j][i]), inmultirea matricilor (necesita trei for-uri imbricate, complexitate O(n^3)), cautarea unui element, suma pe linii/coloane/diagonale.'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Declararea unei matrici in C++',
                'cod': 'int a[100][100];   // matrice de maxim 100x100\nint n, m;          // dimensiuni reale\n\n// Matrice patratica n x n\nint a[20][20];\nint n;'
            },
            {
                'descriere': 'Citirea si afisarea unei matrici',
                'cod': '// Citire\nfor (int i = 0; i < n; i++)\n    for (int j = 0; j < m; j++)\n        cin >> a[i][j];\n\n// Afisare\nfor (int i = 0; i < n; i++) {\n    for (int j = 0; j < m; j++)\n        cout << a[i][j] << " ";\n    cout << endl;\n}'
            },
            {
                'descriere': 'Suma elementelor de pe diagonala principala',
                'cod': 'int suma = 0;\nfor (int i = 0; i < n; i++)\n    suma += a[i][i];   // i == j pe diagonala principala\ncout << suma;'
            },
            {
                'descriere': 'Transpusa unei matrici',
                'cod': 'int t[100][100];\nfor (int i = 0; i < n; i++)\n    for (int j = 0; j < m; j++)\n        t[j][i] = a[i][j];\n// Acum t este transpusa lui a'
            },
        ],
        'exemple': [
            {
                'descriere': 'Suma tuturor elementelor dintr-o matrice',
                'cod': 'int a[3][3] = {{1,2,3},{4,5,6},{7,8,9}};\nint suma = 0;\nfor (int i = 0; i < 3; i++)\n    for (int j = 0; j < 3; j++)\n        suma += a[i][j];\ncout << suma;  // Output: 45'
            },
            {
                'descriere': 'Maximul dintr-o matrice',
                'cod': 'int maxim = a[0][0];\nfor (int i = 0; i < n; i++)\n    for (int j = 0; j < m; j++)\n        if (a[i][j] > maxim)\n            maxim = a[i][j];\ncout << maxim;'
            },
        ],
    }


def teorie_capitol_2():
    return {
        'titlu': 'Generarea Matricelor',
        'definitii': [
            {
                'termen': 'Matrice generata',
                'definitie': 'Matrice ale carei elemente sunt calculate dupa o regula matematica, fara a fi citite de la tastatura.'
            },
            {
                'termen': 'Matrice identitate',
                'definitie': 'Matrice patratica cu 1 pe diagonala principala si 0 in rest.'
            },
            {
                'termen': 'Matrice spirala',
                'definitie': 'Matrice umpluta cu numere consecutive urmand un traseu in spirala (dreapta, jos, stanga, sus).'
            },
            {
                'termen': 'Numerotare de la 1',
                'definitie': 'Conventie in care liniile si coloanele incep de la 1 in loc de 0; necesita ajustarea indicilor in cod.'
            },
        ],
        'explicatii': [
            {
                'titlu': '2.1.1 Generarea elementelor unei matrici',
                'text': 'In loc sa citim elementele de la tastatura, le calculam printr-o formula. Parcurgem pozitiile cu doua for-uri si atribuim valoarea calculata. De exemplu a[i][j] = i * m + j + 1 numeroteaza elementele de la 1 in ordine linie cu linie.'
            },
            {
                'titlu': '2.1.2 Tipuri de matrici generate',
                'text': 'Matricea identitate: 1 pe diagonala, 0 in rest. Matricea cu numere pe diagonale paralele. Matricea in spirala: se tine evidenta directiei curente si se schimba directia cand se iese din matrice sau se intalneste o celula deja completata. Matricea cu linii pare/impare cu ordine diferita de umplere (stanga-dreapta vs dreapta-stanga).'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Generarea matricei identitate',
                'cod': 'int a[100][100] = {0};\nfor (int i = 0; i < n; i++)\n    a[i][i] = 1;\n// Restul elementelor raman 0'
            },
            {
                'descriere': 'Generare cu linii impare stanga-dreapta, linii pare dreapta-stanga',
                'cod': 'int val_impar = 1, val_par = 2;\nfor (int i = 1; i <= 2*n; i++) {\n    if (i % 2 == 1) {  // linie impara: stanga -> dreapta\n        for (int j = 1; j <= 2*n; j++) {\n            a[i][j] = val_impar;\n            val_impar += 2;\n        }\n    } else {           // linie para: dreapta -> stanga\n        for (int j = 2*n; j >= 1; j--) {\n            a[i][j] = val_par;\n            val_par += 2;\n        }\n    }\n}'
            },
        ],
        'exemple': [
            {
                'descriere': 'Matricea identitate 3x3',
                'cod': '1 0 0\n0 1 0\n0 0 1'
            },
            {
                'descriere': 'Rezultatul pentru n=2 (problema din acest capitol)',
                'cod': 'Intrare: n = 2\n\n 1  3  5  7\n 8  6  4  2\n 9 11 13 15\n16 14 12 10\n\nLiniile impare (1,3): umplute cu numere impare, stanga->dreapta\nLiniile pare  (2,4): umplute cu numere pare,   dreapta->stanga'
            },
        ],
    }


def teorie_capitol_3():
    return {
        'titlu': 'Subprograme',
        'definitii': [
            {
                'termen': 'Subprogram',
                'definitie': 'Bloc de cod cu nume propriu care indeplineste o sarcina specifica si poate fi apelat din alte parti ale programului.'
            },
            {
                'termen': 'Functie',
                'definitie': 'Subprogram care returneaza o valoare. Se defineste cu un tip de retur (int, double, etc.) si foloseste instructiunea return.'
            },
            {
                'termen': 'Procedura (void)',
                'definitie': 'Subprogram care nu returneaza o valoare. Se defineste cu tipul void. Efectueaza actiuni (afisare, modificare parametri etc.).'
            },
            {
                'termen': 'Parametru formal',
                'definitie': 'Variabila din definitia subprogramului care primeste valoarea la apel.'
            },
            {
                'termen': 'Parametru actual',
                'definitie': 'Valoarea sau variabila transmisa la apelul subprogramului.'
            },
            {
                'termen': 'Transmitere prin valoare',
                'definitie': 'O copie a valorii este transmisa subprogramului. Modificarile din functie nu afecteaza variabila originala.'
            },
            {
                'termen': 'Transmitere prin referinta',
                'definitie': 'Se transmite adresa variabilei (int &x). Modificarile din functie afecteaza variabila originala.'
            },
        ],
        'explicatii': [
            {
                'titlu': '3.1.1 Functii',
                'text': 'O functie in C++ are: tip_retur, nume, lista de parametri si corp. Tipul de retur poate fi int, double, bool, string etc. Instructiunea return opreste executia functiei si returneaza valoarea. O functie poate fi apelata in expresii: int r = patrat(5);'
            },
            {
                'titlu': '3.1.2 Proceduri (void)',
                'text': 'Procedurile au tipul void si nu returneaza nimic. Se folosesc pentru actiuni cu efecte secundare: afisare, citire, modificarea unor variabile prin referinta. Apelul este o instructiune de sine statatoare: afiseazaMatrice(a, n);'
            },
            {
                'titlu': '3.1.3 Parametrii',
                'text': 'Parametrii prin valoare (int x) — functia primeste o copie, originalul nu se modifica. Parametrii prin referinta (int &x) — functia lucreaza direct cu variabila originala. Array-urile se transmit intotdeauna prin referinta (adresa primului element). Parametrii impliciti pot fi specificati in declaratie: void f(int x, int y = 0).'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Definirea unei functii care returneaza int',
                'cod': 'int patrat(int x) {\n    return x * x;\n}\n\n// Apel\nint rezultat = patrat(5);  // rezultat = 25'
            },
            {
                'descriere': 'Procedura void cu parametru prin referinta',
                'cod': 'void dubleaza(int &x) {\n    x = x * 2;\n}\n\n// Apel\nint a = 5;\ndubleaza(a);\ncout << a;  // Output: 10'
            },
            {
                'descriere': 'Functie care primeste un array',
                'cod': 'int suma(int v[], int n) {\n    int s = 0;\n    for (int i = 0; i < n; i++)\n        s += v[i];\n    return s;\n}\n\n// Apel\nint v[] = {1, 2, 3, 4};\ncout << suma(v, 4);  // Output: 10'
            },
        ],
        'exemple': [
            {
                'descriere': 'Functie care verifica daca un numar este par',
                'cod': 'bool estePar(int n) {\n    return n % 2 == 0;\n}\n\ncout << estePar(4);  // 1 (true)\ncout << estePar(7);  // 0 (false)'
            },
            {
                'descriere': 'Functie care calculeaza CMMDC (recursiv)',
                'cod': 'int cmmdc(int a, int b) {\n    if (b == 0) return a;\n    return cmmdc(b, a % b);\n}\n\ncout << cmmdc(12, 8);  // Output: 4'
            },
        ],
    }


def teorie_capitol_4():
    return {
        'titlu': 'Siruri de Caractere',
        'definitii': [
            {
                'termen': 'Sir de caractere (string)',
                'definitie': 'Secventa de caractere stocata fie ca array de char terminat cu \'\\0\', fie ca obiect de tip std::string.'
            },
            {
                'termen': 'Caracterul nul (\\0)',
                'definitie': 'Caracterul cu codul ASCII 0, care marcheaza sfarsitul unui sir de tip char[].'
            },
            {
                'termen': 'ASCII',
                'definitie': 'Standard de codificare a caracterelor. \'A\'=65, \'a\'=97, \'0\'=48. Literele mari si mici difera prin 32.'
            },
            {
                'termen': 'strlen(s)',
                'definitie': 'Functie din <cstring> care returneaza lungimea sirului s (fara caracterul \'\\0\').'
            },
            {
                'termen': 'strcpy(dest, src)',
                'definitie': 'Copiaza sirul src in dest.'
            },
            {
                'termen': 'strcmp(s1, s2)',
                'definitie': 'Compara doua siruri. Returneaza 0 daca sunt egale, negativ daca s1 < s2, pozitiv daca s1 > s2.'
            },
        ],
        'explicatii': [
            {
                'titlu': '4.1.1 Notiuni generale',
                'text': 'In C++ avem doua moduri de a lucra cu siruri: stilul C (char s[100]) si clasa string (#include <string>). Stilul C foloseste functii din <cstring>. Clasa string ofera operatori intuitivi (+, ==, <) si metode ca .length(), .substr(), .find(). Pentru citirea unui sir cu spatii folosim getline(cin, s).'
            },
            {
                'titlu': '4.1.2 Functii din biblioteca <cstring>',
                'text': 'strlen(s) — lungimea sirului. strcpy(d, s) — copiere. strcat(d, s) — concatenare (adauga s la finalul lui d). strcmp(s1, s2) — comparare. strchr(s, c) — cauta caracterul c in sir. strstr(s, sub) — cauta un subsir. Atentie: aceste functii nu verifica depasirea bufferului, deci asigurati-va ca array-ul destinatie este suficient de mare.'
            },
            {
                'titlu': '4.1.3 Parcurgerea sirurilor',
                'text': 'Cu char s[]: for (int i = 0; s[i] != \'\\0\'; i++) sau for (int i = 0; i < strlen(s); i++). Cu string: for (int i = 0; i < s.length(); i++) sau for (char c : s). Caracterele pot fi verificate cu functii din <cctype>: isdigit(c), isalpha(c), isupper(c), islower(c), toupper(c), tolower(c).'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Declarare si citire siruri de caractere',
                'cod': '#include <string>\n\n// Stilul C\nchar s[100];\ncin >> s;           // citeste pana la spatiu\ngets(s);            // citeste linia intreaga (vechi)\n\n// Clasa string\nstring str;\ncin >> str;         // citeste pana la spatiu\ngetline(cin, str);  // citeste linia intreaga'
            },
            {
                'descriere': 'Functii uzuale <cstring>',
                'cod': '#include <cstring>\n\nchar s1[50] = "Hello";\nchar s2[50] = "World";\n\ncout << strlen(s1);      // 5\nstrcpy(s2, s1);          // s2 devine "Hello"\nstrcat(s1, " World");    // s1 devine "Hello World"\ncout << strcmp(s1, s2);  // 0 daca sunt egale'
            },
            {
                'descriere': 'Parcurgerea unui sir caracter cu caracter',
                'cod': 'string s = "Informatica";\nint nr_vocale = 0;\nfor (int i = 0; i < s.length(); i++) {\n    char c = tolower(s[i]);\n    if (c==\'a\'||c==\'e\'||c==\'i\'||c==\'o\'||c==\'u\')\n        nr_vocale++;\n}\ncout << nr_vocale;  // Output: 5'
            },
        ],
        'exemple': [
            {
                'descriere': 'Inversarea unui sir de caractere',
                'cod': 'string s = "abcde";\nint n = s.length();\nfor (int i = 0; i < n / 2; i++)\n    swap(s[i], s[n - 1 - i]);\ncout << s;  // Output: edcba'
            },
            {
                'descriere': 'Numararea aparitiilor unui caracter',
                'cod': 'string s = "banana";\nchar c = \'a\';\nint cnt = 0;\nfor (char ch : s)\n    if (ch == c) cnt++;\ncout << cnt;  // Output: 3'
            },
        ],
    }


def teorie_capitol_5():
    return {
        'titlu': 'Struct',
        'definitii': [
            {
                'termen': 'struct',
                'definitie': 'Tip de date definit de utilizator care grupeaza mai multe campuri (membri) de tipuri diferite sub un singur nume.'
            },
            {
                'termen': 'Camp (membru)',
                'definitie': 'O variabila din interiorul unei structuri, accesata prin operatorul punct: variabila.camp.'
            },
            {
                'termen': 'Vector de structuri',
                'definitie': 'Array in care fiecare element este o structura. Permite stocarea mai multor inregistrari de acelasi tip.'
            },
            {
                'termen': 'Operatorul . (punct)',
                'definitie': 'Operator de acces la campurile unei structuri: elev.medie, elev.cod.'
            },
        ],
        'explicatii': [
            {
                'titlu': '5.1.1 Definirea unei structuri',
                'text': 'Cuvantul cheie struct urmat de numele tipului si intre acolade lista campurilor. Definitia se face inaintea functiei main(). Dupa acolade se pune punct si virgula. Tipul creat poate fi folosit ca orice alt tip: Elev e; sau Elev elevi[40];'
            },
            {
                'titlu': '5.1.2 Declararea variabilelor de tip struct',
                'text': 'Dupa definirea structurii, se declara variabile ca pentru orice tip: NumeStruct variabila;. Campurile se acceseaza cu punctul: variabila.camp = valoare. Structurile pot fi transmise ca parametri la functii (prin valoare sau prin referinta).'
            },
            {
                'titlu': '5.1.3 Vectori de structuri',
                'text': 'Un vector de structuri stocheaza mai multe inregistrari: Elev elevi[40]; Accesul la campul unui element: elevi[i].medie. Vectorii de structuri pot fi sortati cu sort() din <algorithm> folosind o functie de comparare personalizata.'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Definirea si folosirea unei structuri',
                'cod': 'struct Elev {\n    int cod;\n    int medie;\n    int absente;\n};\n\n// Declarare si initializare\nElev e;\ne.cod = 101;\ne.medie = 9;\ne.absente = 3;\n\ncout << e.cod << " " << e.medie;'
            },
            {
                'descriere': 'Vector de structuri — citire si afisare',
                'cod': 'Elev elevi[40];\nint n;\ncin >> n;\nfor (int i = 0; i < n; i++)\n    cin >> elevi[i].cod >> elevi[i].medie >> elevi[i].absente;\n\nfor (int i = 0; i < n; i++)\n    cout << elevi[i].cod << " "\n         << elevi[i].medie << " "\n         << elevi[i].absente << endl;'
            },
            {
                'descriere': 'Sortarea unui vector de structuri',
                'cod': '#include <algorithm>\nusing namespace std;\n\nbool compAbsente(Elev a, Elev b) {\n    if (a.absente != b.absente)\n        return a.absente > b.absente; // descrescator dupa absente\n    return a.cod < b.cod;             // crescator dupa cod\n}\n\nsort(elevi, elevi + n, compAbsente);'
            },
        ],
        'exemple': [
            {
                'descriere': 'Media clasei calculata din vector de structuri',
                'cod': 'int suma = 0;\nfor (int i = 0; i < n; i++)\n    suma += elevi[i].medie;\ncout << suma / n;  // partea intreaga a mediei'
            },
            {
                'descriere': 'Numarul de elevi cu media 10',
                'cod': 'int cnt = 0;\nfor (int i = 0; i < n; i++)\n    if (elevi[i].medie == 10)\n        cnt++;\ncout << cnt;'
            },
        ],
    }


def teorie_capitol_6():
    return {
        'titlu': 'Recursivitate',
        'definitii': [
            {
                'termen': 'Recursivitate',
                'definitie': 'Tehnica prin care o functie se apeleaza pe ea insasi cu parametri mai mici/simplificati, pana ajunge la un caz de baza.'
            },
            {
                'termen': 'Cazul de baza',
                'definitie': 'Conditia de oprire a recursiei — un caz simplu rezolvat direct, fara apel recursiv. Fara el, functia s-ar apela la infinit.'
            },
            {
                'termen': 'Apel recursiv',
                'definitie': 'Apelul functiei catre ea insasi cu un parametru modificat (mai mic, mai simplu) care converge spre cazul de baza.'
            },
            {
                'termen': 'Stiva de apeluri',
                'definitie': 'Zona de memorie unde se salveaza starea fiecarui apel recursiv activ. Recursivitatea prea adanca poate produce Stack Overflow.'
            },
        ],
        'explicatii': [
            {
                'titlu': '6.1.1 Ce este recursivitatea',
                'text': 'O functie recursiva rezolva o problema mai mare reducand-o la aceeasi problema cu date mai mici. De exemplu factorial(n) = n * factorial(n-1). Fiecare apel asteapta rezultatul urmatorului. Recursivitatea este eleganta dar poate fi mai lenta decat iteratia din cauza overhead-ului stivei.'
            },
            {
                'titlu': '6.1.2 Cazul de baza',
                'text': 'Primul lucru intr-o functie recursiva: verifica daca ai ajuns la cazul simplu si returneaza direct. Exemplu: if (n == 0) return 1; pentru factorial. Fara cazul de baza corect, functia se apeleaza la infinit pana apare Stack Overflow.'
            },
            {
                'titlu': '6.1.3 Apelul recursiv',
                'text': 'Dupa cazul de baza, functia se apeleaza cu un parametru mai apropiat de cazul de baza. Pentru sir de cifre: apelam cu n/10 (stergem ultima cifra). Pentru factorial: apelam cu n-1. Parametrul trebuie sa convearga obligatoriu spre cazul de baza.'
            },
            {
                'titlu': '6.1.4 Functii recursive de tip int',
                'text': 'Returneaza o valoare calculata din rezultatele apelurilor recursive. Exemple: factorial, fibonacci, cmmdc, suma cifrelor, cel mai mare divizor patrat perfect. Folosesc return pentru a propaga valoarea inapoi prin lantul de apeluri.'
            },
            {
                'titlu': '6.1.5 Functii recursive de tip void',
                'text': 'Nu returneaza valori, dar produc efecte: afisare, modificarea unor variabile globale. Exemple: afisarea cifrelor unui numar, parcurgerea unui arbore, generarea permutarilor. Apelul recursiv este o instructiune, nu o expresie.'
            },
        ],
        'sintaxa': [
            {
                'descriere': 'Factorial recursiv',
                'cod': 'int factorial(int n) {\n    // Cazul de baza\n    if (n == 0) return 1;\n    // Apel recursiv\n    return n * factorial(n - 1);\n}\n\ncout << factorial(5);  // Output: 120'
            },
            {
                'descriere': 'Suma cifrelor unui numar (recursiv)',
                'cod': 'int sumaCifre(int n) {\n    if (n == 0) return 0;          // caz de baza\n    return n % 10 + sumaCifre(n / 10); // ultima cifra + restul\n}\n\ncout << sumaCifre(1234);  // Output: 10'
            },
            {
                'descriere': 'Afisarea cifrelor unui numar (void recursiv)',
                'cod': 'void afisCifre(int n) {\n    if (n == 0) return;  // caz de baza\n    afisCifre(n / 10);   // afiseaza mai intai cifra mai semnificativa\n    cout << n % 10 << " ";\n}\n\nafisCifre(1234);  // Output: 1 2 3 4'
            },
        ],
        'exemple': [
            {
                'descriere': 'Sir Fibonacci recursiv',
                'cod': 'int fib(int n) {\n    if (n <= 1) return n;  // fib(0)=0, fib(1)=1\n    return fib(n-1) + fib(n-2);\n}\n\nfor (int i = 0; i < 8; i++)\n    cout << fib(i) << " ";\n// Output: 0 1 1 2 3 5 8 13'
            },
            {
                'descriere': 'CMMDC recursiv (algoritmul lui Euclid)',
                'cod': 'int cmmdc(int a, int b) {\n    if (b == 0) return a;       // caz de baza\n    return cmmdc(b, a % b);     // apel recursiv\n}\n\ncout << cmmdc(48, 18);  // Output: 6'
            },
        ],
    }



# ============================================================
#   PROBLEME
# ============================================================

def probleme_capitol_1():
    return {
        'titlu': 'Matrici',
        'probleme': [
            {
                'sursa': 'Olimpiada de Informatica',
                'enunt_original': 'Scrieteti un program care citeste un numar natural n si elementele unui tablou bidimensional n x n cu numere naturale. Programul afiseaza numarul de elemente strict mai mari decat toti vecinii directi (sus, jos, stanga, dreapta).',
                'enunt_reformulat': 'Intr-un oras cu strazi dispuse in grila n x n, fiecare intersectie are o inaltime. O intersectie este "varf" daca este mai inalta decat toate cele cu care se invecineaza direct (nu diagonal). Cati varfuri are orasul?',
                'intrare': '4\n1 5 1 1\n2 1 2 3\n1 3 4 2\n2 1 2 1',
                'iesire': '5',
                'cod_cpp': '#include <iostream>\nusing namespace std;\n\nint a[25][25];\n\nint main() {\n    int n;\n    cin >> n;\n    for (int i = 0; i < n; i++)\n        for (int j = 0; j < n; j++)\n            cin >> a[i][j];\n\n    // directiile: sus, jos, stanga, dreapta\n    int di[] = {-1, 1, 0, 0};\n    int dj[] = {0, 0, -1, 1};\n\n    int cnt = 0;\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n; j++) {\n            bool varf = true;\n            for (int d = 0; d < 4; d++) {\n                int ni = i + di[d];\n                int nj = j + dj[d];\n                if (ni >= 0 && ni < n && nj >= 0 && nj < n)\n                    if (a[ni][nj] >= a[i][j]) {\n                        varf = false;\n                        break;\n                    }\n            }\n            if (varf) cnt++;\n        }\n    }\n    cout << cnt << endl;\n    return 0;\n}',
                'explicatie': 'Pentru fiecare element, verificam cei 4 vecini (sus, jos, stanga, dreapta). Folosim vectorii de directie di[] si dj[] pentru a evita 4 if-uri separate. Inainte de a accesa un vecin, verificam ca indicii sunt in limitele matricei (ni >= 0 && ni < n etc.). Daca toti vecinii existenti sunt strict mai mici, elementul este un varf si incrementam contorul.'
            },
        ]
    }


def probleme_capitol_2():
    return {
        'titlu': 'Generarea Matricelor',
        'probleme': [
            {
                'sursa': 'Bacalaureat Informatica',
                'enunt_original': 'Cititi n si construiti o matrice 2n x 2n astfel incat liniile impare sa contina numerele impare din [1, 4n^2] in ordine crescatoare stanga-dreapta, iar liniile pare sa contina numerele pare tot in ordine crescatoare dar dreapta-stanga.',
                'enunt_reformulat': 'Intr-o scoala cu 2n randuri de banci, randurile impare sunt ocupate de elevi cu numere de ordine impare (1,3,5...) asezati de la stanga la dreapta. Randurile pare sunt ocupate de elevi cu numere pare (2,4,6...) asezati insa de la dreapta la stanga. Construieste planul scolii!',
                'intrare': '2',
                'iesire': '1 3 5 7\n8 6 4 2\n9 11 13 15\n16 14 12 10',
                'cod_cpp': '#include <iostream>\nusing namespace std;\n\nint a[25][25];\n\nint main() {\n    int n;\n    cin >> n;\n    int dim = 2 * n;\n\n    int impar = 1;   // primul numar impar\n    int par   = 2;   // primul numar par\n\n    for (int i = 1; i <= dim; i++) {\n        if (i % 2 == 1) {\n            // linie impara: stanga -> dreapta cu numere impare\n            for (int j = 1; j <= dim; j++) {\n                a[i][j] = impar;\n                impar += 2;\n            }\n        } else {\n            // linie para: dreapta -> stanga cu numere pare\n            for (int j = dim; j >= 1; j--) {\n                a[i][j] = par;\n                par += 2;\n            }\n        }\n    }\n\n    // Afisare\n    for (int i = 1; i <= dim; i++) {\n        for (int j = 1; j <= dim; j++)\n            cout << a[i][j] << " ";\n        cout << endl;\n    }\n    return 0;\n}',
                'explicatie': 'Tinem doi contori separati: impar (porneste de la 1, creste cu 2) si par (porneste de la 2, creste cu 2). Pentru liniile impare parcurgem coloanele de la 1 la dim si asignam valori impare crescatoare. Pentru liniile pare parcurgem coloanele de la dim la 1 (dreapta-stanga) si asignam valori pare crescatoare. Astfel fiecare linie para apare in ordine crescatoare de la dreapta la stanga.'
            },
        ]
    }


def probleme_capitol_3():
    return {
        'titlu': 'Subprograme',
        'probleme': [
            {
                'sursa': 'Bacalaureat Informatica 2024',
                'enunt_original': 'Subprogramul diviz are un singur parametru n prin care primeste un numar natural. Subprogramul returneaza cel mai mare divizor al lui n care este patrat perfect.',
                'enunt_reformulat': 'Un colectionar de timbre numara timbrelele in grupuri patrate perfecte (1, 4, 9, 16...). El vrea sa stie in ce cel mai mare grup patrat perfect poate imparti colectia sa de n timbre exact. Ajuta-l sa gaseasca cel mai mare patrat perfect care divide n!',
                'intrare': 'n = 72',
                'iesire': '36',
                'cod_cpp': 'int diviz(int n) {\n    int rezultat = 1;\n    // Verificam toate patratele perfecte pana la n\n    for (int i = 1; (long long)i * i <= n; i++) {\n        int patrat = i * i;\n        if (n % patrat == 0)\n            rezultat = patrat;\n    }\n    return rezultat;\n}\n\n// Exemple:\n// diviz(72)  -> 36  (36 = 6^2, 72/36 = 2)\n// diviz(16)  -> 16  (16 = 4^2, 16/16 = 1)\n// diviz(15)  -> 1   (1 = 1^2, niciun patrat > 1 nu divide 15)',
                'explicatie': 'Un patrat perfect este de forma i*i. Parcurgem i de la 1 in sus si verificam daca i*i divide n (n % (i*i) == 0). Daca da, actualizam rezultatul (cel mai mare patrat perfect gasit pana acum). Ne oprim cand i*i > n (nu mai pot exista patrate perfecte mai mari care sa divida n). Solutia are complexitate O(sqrt(n)).'
            },
        ]
    }


def probleme_capitol_4():
    return {
        'titlu': 'Siruri de Caractere',
        'probleme': [
            {
                'sursa': 'Clasa a X-a, Evaluare',
                'enunt_original': 'Se da o matrice cu n linii si m coloane cu elemente numere naturale. Determinati suma valorilor pare din matrice.',
                'enunt_reformulat': 'Intr-un depozit cu n randuri si m rafturi, fiecare raft contine un numar de produse. Un inspector vrea sa stie cate produse sunt in total pe rafturile cu numar par de produse (pentru o oferta speciala). Calculeaza suma!',
                'intrare': '4 6\n4 20 15 23 18 9\n1 8 23 22 14 18\n17 15 13 18 12 15\n3 18 8 20 12 5',
                'iesire': '192',
                'cod_cpp': '#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, m;\n    cin >> n >> m;\n\n    long long suma = 0;\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < m; j++) {\n            int x;\n            cin >> x;\n            if (x % 2 == 0)\n                suma += x;\n        }\n    }\n\n    cout << suma << endl;\n    return 0;\n}',
                'explicatie': 'Citim elementele pe rand (nu trebuie sa le stocam, le procesam imediat). Pentru fiecare element verificam daca este par (x % 2 == 0). Daca da, il adaugam la suma. Folosim long long pentru suma deoarece n, m <= 100 si elemente < 10000, deci suma maxima poate fi 100*100*10000 = 100.000.000, care incape in int, dar long long e mai sigur.'
            },
        ]
    }


def probleme_capitol_5():
    return {
        'titlu': 'Struct',
        'probleme': [
            {
                'sursa': 'pbinfo.ro — Clasa a X-a',
                'enunt_original': 'Se dau n elevi cu cod, medie informatica si numar absente. a) Memorati intr-un vector de structuri. b) Afisati numarul elevilor cu media 10. c) Afisati media clasei (partea intreaga). d) Afisati primii doi elevi cu cele mai multe absente (la egalitate, dupa cod crescator).',
                'enunt_reformulat': 'Diriginta clasei a X-a B trebuie sa faca un raport de sfarsit de an. Are datele a n elevi si trebuie sa afle: cati au media maxima, care este media generala a clasei, si care sunt cei mai absenteisti doi elevi (pentru a-i contacta parintii). Ajut-o!',
                'intrare': '3\n1 10 3\n2 8 1\n3 8 5',
                'iesire': '1\n8\n3 8 5\n1 10 3',
                'cod_cpp': '#include <iostream>\n#include <algorithm>\nusing namespace std;\n\nstruct Elev {\n    int cod, medie, absente;\n};\n\nbool cmp(Elev a, Elev b) {\n    if (a.absente != b.absente)\n        return a.absente > b.absente; // descrescator dupa absente\n    return a.cod < b.cod;             // crescator dupa cod\n}\n\nint main() {\n    int n;\n    cin >> n;\n    Elev elevi[40];\n\n    for (int i = 0; i < n; i++)\n        cin >> elevi[i].cod >> elevi[i].medie >> elevi[i].absente;\n\n    // b) nr elevi cu media 10\n    int cnt10 = 0;\n    for (int i = 0; i < n; i++)\n        if (elevi[i].medie == 10) cnt10++;\n    cout << cnt10 << endl;\n\n    // c) media clasei (partea intreaga)\n    int suma = 0;\n    for (int i = 0; i < n; i++) suma += elevi[i].medie;\n    cout << suma / n << endl;\n\n    // d) primii 2 dupa absente\n    sort(elevi, elevi + n, cmp);\n    for (int i = 0; i < min(2, n); i++)\n        cout << elevi[i].cod << " "\n             << elevi[i].medie << " "\n             << elevi[i].absente << endl;\n\n    return 0;\n}',
                'explicatie': 'Definim struct Elev cu cele 3 campuri. Citim toti elevii intr-un vector de structuri. Pentru b) parcurgem si numaram cei cu medie == 10. Pentru c) calculam suma mediilor si impartim la n (impartire intreaga). Pentru d) sortam cu o functie de comparare care prioritizeaza absentele descrescator, iar la egalitate codul crescator, apoi afisam primii min(2,n) elevi.'
            },
        ]
    }


def probleme_capitol_6():
    return {
        'titlu': 'Recursivitate',
        'probleme': [
            {
                'sursa': 'Bacalaureat Informatica',
                'enunt_original': 'Sa se scrie o functie C++ recursiva care primind ca parametru un numar natural n returneaza 0 daca numarul de cifre pare este egal cu numarul de cifre impare, sau o valoare nenula in caz contrar. Numele functiei va fi FPareImpare.',
                'enunt_reformulat': 'Un joc de echilibru: un numar este "echilibrat" daca are exact la fel de multe cifre pare cat cifre impare. De exemplu 1234 are 2 cifre pare (2,4) si 2 cifre impare (1,3) — echilibrat! Scrie o functie recursiva care verifica daca un numar este echilibrat.',
                'intrare': 'FPareImpare(1234)\nFPareImpare(13508)',
                'iesire': '0  (echilibrat: 2 pare, 2 impare)\n1  (neechilibrat: 2 pare, 3 impare)',
                'cod_cpp': '// Varianta 1: returneaza diferenta (pare - impare)\n// 0 = echilibrat, nenul = neechilibrat\nint FPareImpare(int n) {\n    // Caz de baza: numar cu o singura cifra\n    if (n < 10) {\n        if (n % 2 == 0) return 1;  // cifra para\n        else return -1;            // cifra impara\n    }\n    // Apel recursiv: cifra curenta + restul numarului\n    int cifra = n % 10;\n    int contributie = (cifra % 2 == 0) ? 1 : -1;\n    return contributie + FPareImpare(n / 10);\n}\n\n// FPareImpare(1234) = 1 + (-1) + 1 + (-1) = 0  -> echilibrat\n// FPareImpare(13508) = 1 + (-1) + 1 + 1 + (-1) = 1 -> neechilibrat',
                'explicatie': 'Strategia: in loc sa numaram separat parele si imparele, calculam o diferenta. Fiecare cifra para contribuie cu +1, fiecare cifra impara cu -1. Daca suma finala e 0, avem la fel de multe din fiecare. Cazul de baza: numarul are o singura cifra (n < 10) — returnam +1 sau -1 direct. Apelul recursiv: extragem ultima cifra (n % 10), calculam contributia ei, si o adaugam la rezultatul recursiv pentru restul cifrelor (n / 10).'
            },
        ]
    }




# ============================================================
#   PROCESAREA MESAJELOR CHAT
# ============================================================

sessions = {}

def get_state():
    return {'step': 'AWAIT_CHAPTER', 'chapter': None}

def process_message(session_id, user_input):
    if session_id not in sessions:
        sessions[session_id] = get_state()

    state = sessions[session_id]
    user_input = user_input.strip()

    # ECHIVALENT: while (question != '8')
    if user_input == '8':
        sessions[session_id] = get_state()
        return {
            'messages': [{'text': 'Program inchis. La revedere! Mult succes la bacalaureat!'}],
            'buttons': [],
            'step': 'DONE'
        }

    if state['step'] == 'AWAIT_CHAPTER':

        if user_input == '1':
            state['chapter'] = '1'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 1 — Matrici</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=1'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=1'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '2':
            state['chapter'] = '2'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 2 — Generarea Matricelor</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=2'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=2'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '3':
            state['chapter'] = '3'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 3 — Subprograme</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=3'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=3'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '4':
            state['chapter'] = '4'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 4 — Siruri de Caractere</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=4'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=4'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '5':
            state['chapter'] = '5'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 5 — Struct</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=5'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=5'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '6':
            state['chapter'] = '6'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': 'Ai ales <strong>Capitol 6 — Recursivitate</strong>.'},
                    {'text': 'Ce vrei sa faci?'}
                ],
                'buttons': [
                    {'text': '📖 Teorie',   'href': 'teorie.html?capitol=6'},
                    {'text': '✏️ Probleme', 'href': 'probleme.html?capitol=6'},
                ],
                'step': 'AWAIT_CHOICE'
            }

        elif user_input == '7':
            state['chapter'] = '7'
            state['step'] = 'AWAIT_CHOICE'
            return {
                'messages': [
                    {'text': '🎓 <strong>Felicitări pentru finalizarea clasei a X-a!</strong>'},
                    {'text': 'Ai parcurs un an plin de provocări și realizări. Ai învățat să lucrezi cu <strong>matrici</strong>, să generezi structuri complexe, să scrii <strong>subprograme</strong> elegante, să manipulezi <strong>șiruri de caractere</strong>, să organizezi date cu <strong>struct</strong> și să gândești recursiv.'},
                    {'text': '💡 Toate aceste concepte sunt fundamentele pe care se construiește programarea avansată. În clasa a XI-a te așteaptă <strong>backtracking</strong>, <strong>programare dinamică</strong> și <strong>teoria grafurilor</strong> — algoritmi cu care vei putea rezolva probleme cu adevărat complexe.'},
                    {'text': '🏆 Câteva sfaturi pentru drumul înainte:<br>→ Exersează zilnic pe <strong>pbinfo.ro</strong> și <strong>infoarena.ro</strong><br>→ Citește cu atenție enunțurile și testează pe exemple mici<br>→ Nu te descuraja când un algoritm nu merge — depanarea face parte din proces<br>→ Încearcă să înțelegi <em>de ce</em> funcționează o soluție, nu doar să o memorezi'},
                    {'text': '🚀 <strong>Mult succes la bacalaureat și la olimpiadă!</strong> Ești pregătit pentru ce urmează. 💪'},
            ],
            'buttons': [],
            'step': 'AWAIT_CHOICE'
        }

        else:
            return {
                'messages': [{'text': 'Numar invalid. Tasteaza un numar de la <strong>1 la 7</strong> sau <strong>8</strong> pentru exit.'}],
                'buttons': [],
                'step': 'AWAIT_CHAPTER'
            }

    elif state['step'] == 'AWAIT_CHOICE':
        return {
            'messages': [{'text': 'Apasa unul din butoanele de mai sus: <strong>📖 Teorie</strong> sau <strong>✏️ Probleme</strong>.'}],
            'buttons': [],
            'step': 'AWAIT_CHOICE'
        }

    elif state['step'] == 'DONE':
        return {
            'messages': [{'text': 'Sesiunea s-a incheiat. Apasa <strong>Reseteaza Chat</strong> pentru a relua.'}],
            'buttons': [],
            'step': 'DONE'
        }


# ============================================================
#   RUTE FLASK
# ============================================================

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/api/welcome', methods=['GET'])
def welcome():
    meniu = ''.join([f'<div style="padding:2px 0">  {linie}</div>' for linie in MENIU_PRINCIPAL])
    return jsonify({
        'messages': [
            {'text': 'Buna! Sunt <strong>EduBot</strong>.'},
            {'text': 'Tasteaza numarul capitolului pe care vrei sa il parcurgi:'},
            {'text': meniu}
        ]
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    user_input = data.get('message', '').strip()
    if not user_input:
        return jsonify({'error': 'mesaj gol'}), 400
    return jsonify(process_message(session_id, user_input))

@app.route('/api/reset', methods=['POST'])
def reset():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    if session_id in sessions:
        del sessions[session_id]
    meniu = ''.join([f'<div style="padding:2px 0">  {linie}</div>' for linie in MENIU_PRINCIPAL])
    return jsonify({
        'status': 'ok',
        'messages': [
            {'text': 'Chat resetat! Tasteaza numarul capitolului (1-7, 8=exit):'},
            {'text': meniu}
        ]
    })

@app.route('/api/teorie/<capitol>', methods=['GET'])
def get_teorie(capitol):
    if capitol == '1':
        return jsonify(teorie_capitol_1())
    elif capitol == '2':
        return jsonify(teorie_capitol_2())
    elif capitol == '3':
        return jsonify(teorie_capitol_3())
    elif capitol == '4':
        return jsonify(teorie_capitol_4())
    elif capitol == '5':
        return jsonify(teorie_capitol_5())
    elif capitol == '6':
        return jsonify(teorie_capitol_6())
    else:
        return jsonify({'eroare': 'Capitol inexistent'}), 404

@app.route('/api/probleme/<capitol>', methods=['GET'])
def get_probleme(capitol):
    if capitol == '1':
        return jsonify(probleme_capitol_1())
    elif capitol == '2':
        return jsonify(probleme_capitol_2())
    elif capitol == '3':
        return jsonify(probleme_capitol_3())
    elif capitol == '4':
        return jsonify(probleme_capitol_4())
    elif capitol == '5':
        return jsonify(probleme_capitol_5())
    elif capitol == '6':
        return jsonify(probleme_capitol_6())
    else:
        return jsonify({'eroare': 'Capitol inexistent'}), 404


# ============================================================
if __name__ == '__main__':
    print('=' * 50)
    print('  EduBot Server — http://localhost:5000')
    print('  CTRL+C pentru a opri')
    print('=' * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)