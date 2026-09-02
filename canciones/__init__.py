from cs50 import SQL

import check50
import sqlparse


BD = "canciones.db"


@check50.check()
def exists():
    """Archivos SQL existen"""
    for i in range(1, 16):
        check50.exists(f"{i}.sql")
    check50.include(BD)


@check50.check(exists)
def test1():
    """1.sql lista los álbumes estrenados en 2018"""
    check_single_col(
        run_query("1.sql"),
        {
            "Beautiful (feat. Camila Cabello) [Bazzi vs. EDX's Ibiza Sunrise Remix]",
            'Better',
            'Creed II: The Album',
            'FEFE (feat. Nicki Minaj & Murda Beatz)',
            'Goodbye (feat. Nicki Minaj & Willy William)',
            'Happier (Remixes Pt. 2)',
            "Hearts Ain't Gonna Lie (Remixes, Pt. 1)",
            'LM5 (Deluxe)',
            'Love Lies (with Normani)',
            'MyBoi (TroyBoi Remix)',
            'No Candle No Light (feat. Nicki Minaj)',
            'OTW',
            'Promises (with Sam Smith) [Remixes]',
            'Queen',
            'Ruin My Life (Remixes)',
            'Say My Name (feat. Bebe Rexha & J Balvin) [Lucas & Steve Remix]',
            'Side Effects - Remixes',
            'Signs (Eden Prince Remix)',
            'Skin (Rinzen Remix)',
            'Suncity',
            'Sweet but Psycho',
            'Sweetener',
            'The Beatles',
            'Woman Like Me (feat. Nicki Minaj)',
            'lovely (with Khalid)',
            "when the party's over",
        },
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql lista las canciones de más de 7 minutos"""
    check_single_col(
        run_query("2.sql"),
        {
            'Disco Eterno',
            'El Rito - Remasterizado 2007',
            'Hey Jude - Remastered 2009',
            'Let It Happen',
            'Mirrors',
            'Not over Yet - Perfecto Edit',
            'Open Eye Signal',
            'Open Over Us (Live)',
            'Skin - Rinzen Remix',
            'Spit Out the Bone',
            'Tumba La Casa (Remix) [feat. Daddy Yankee, Nicky Jam, Farruko, Arcangel, De La Ghetto, Zion & Ñengo Flow]',
        },
        ordered=False,
    )


@check50.check(exists)
def test3():
    """3.sql determina el tipo de agrupación de Chino & Nacho"""
    check_single_cell(run_query("3.sql"), "duo")


@check50.check(exists)
def test4():
    """4.sql lista las canciones bailables, energéticas y positivas"""
    check_single_col(
        run_query("4.sql"),
        [
            'Beat It - Single Version',
            'Donde Estan Las Gatas (feat. Nicky Jam)',
            'En La Cama (feat. Daddy Yankee)',
            'Happier - Matt Medved Remix',
            'Harder',
            "Hips Don't Lie (feat. Wyclef Jean)",
            'LLC',
            'La Negra Tiene Tumbao',
            'P.Y.T. (Pretty Young Thing)',
            'Poker Face',
            'Remember The Time',
            'Remember the Time',
            'Ride It',
            'Rie y Llora',
            'Spicy - Majestic Remix',
            'Tu Angelito',
            'Whenever, Wherever',
            'Woman Like Me (feat. Nicki Minaj)',
            'Woman Like Me (feat. Nicki Minaj)',
        ],
        ordered=True,
    )


@check50.check(exists)
def test5():
    """5.sql cuenta las canciones con popularidad mayor o igual a 90"""
    check_single_cell(run_query("5.sql"), "6")


@check50.check(exists)
def test6():
    """6.sql lista los álbumes de Metallica en orden cronológico"""
    check_double_col(
        run_query("6.sql"),
        [
            {'Metallica', '1991'},
            {'Metallica', '1991'},
            {'Metallica', '1991'},
            {'Reload', '1997'},
            {'Hardwired…To Self-Destruct', '2016'},
        ],
        ordered=True,
    )


@check50.check(exists)
def test7():
    """7.sql lista las canciones de 2019 y su popularidad"""
    check_double_col(
        run_query("7.sql"),
        [
            {'Tusa', '98'},
            {'everything i wanted', '97'},
            {'RITMO (Bad Boys For Life)', '96'},
            {'bad guy', '95'},
            {'Ride It', '94'},
            {'Lose Control', '91'},
            {'Higher Love', '87'},
            {'Up All Night', '87'},
            {'bury a friend', '87'},
            {'Turn Me On (feat. Vula)', '86'},
            {'all the good girls go to hell', '86'},
            {"Don't Call Me Up", '85'},
            {'i love you', '85'},
            {'you should see me in a crown', '84'},
            {'El Favor (with Nicky Jam & Sech, feat. Farruko, Zion & Lunay)', '83'},
            {'bad guy (with Justin Bieber)', '83'},
            {'xanny', '83'},
            {'Talk (feat. Disclosure)', '82'},
            {'my strange addiction', '82'},
            {'ilomilo', '81'},
            {'listen before i go', '81'},
            {'8', '80'},
            {'Loco Contigo (with J. Balvin & Ozuna feat. Nicky Jam, Natti Natasha, Darell & Sech) - REMIX', '80'},
            {'Hot Girl Summer (feat. Nicki Minaj & Ty Dolla $ign)', '79'},
            {'Bonita', '78'},
            {'Right Back (feat. A Boogie Wit Da Hoodie)', '77'},
            {'goodbye', '77'},
            {'Bad To You (with Normani & Nicki Minaj)', '76'},
            {'Dime tú', '75'},
            {'Outta My Head (with John Mayer)', '75'},
            {'Me Rehúso', '74'},
            {'All the Time - Don Diablo Remix', '70'},
            {'Right Back', '70'},
            {'Solito (Lonely) [feat. Nicky Jam & Akon]', '68'},
            {'Solo Pienso En Ti (feat. De La Ghetto & Justin Quiles)', '68'},
            {'Memories - Dillon Francis Remix', '67'},
            {"I Don't Care (with Justin Bieber) - Loud Luxury Remix", '66'},
            {'Harder', '62'},
            {'Call You Mine - Keanu Silva Remix', '60'},
            {'Kitipun', '60'},
            {'Talk - Disclosure VIP', '60'},
            {'Come Together - 2019 Mix', '59'},
            {'Talk - Alle Farben Remix', '56'},
            {'Kitipun', '54'},
            {'#Sádico', '53'},
            {'Body on My (feat. Brando, Pitbull & Nicky Jam)', '53'},
            {"Lámpara Pa' Mis Pies", '52'},
            {'La Plata (Los Ángeles Azules Remix) (Feat. Los Ángeles Azules, Lalo Ebratt)', '51'},
            {'Open Over Us (Live)', '50'},
            {'Corazón Enamorado', '49'},
            {'Spicy - Majestic Remix', '48'},
            {'Swing (Bonus Track)', '9'},
        ],
        ordered=True,
    )


@check50.check(exists)
def test8():
    """8.sql calcula la popularidad promedio de Michael Jackson"""
    check_single_cell_aprox(run_query("8.sql"), 63.7273)


@check50.check(exists)
def test9():
    """9.sql lista los músicos con álbumes publicados en 1980"""
    check_single_col(
        run_query("9.sql"),
        [
            'AC/DC',
            'Air Supply',
            'John Lennon',
            'Journey',
            'Robert Palmer',
            'Shaun Cassidy',
            'The Buggles',
        ],
        ordered=True,
    )


@check50.check(exists)
def test10():
    """10.sql lista las canciones de The Beatles y su año"""
    check_double_col(
        run_query("10.sql"),
        [
            {'Real Love - Anthology 2 Version', '1996'},
            {'Come Together - Remastered 2009', '1969'},
            {'Revolution - Remastered 2009', '1973'},
            {'I Saw Her Standing There - Remastered 2009', '1963'},
            {'I Want To Hold Your Hand - Remastered 2015', '2000'},
            {'Come Together - 2019 Mix', '2019'},
            {'Back In The U.S.S.R. - 2018 Mix', '2018'},
            {'Hey Jude - Remastered 2009', '1988'},
            {'Helter Skelter - Remastered 2009', '1968'},
            {'A Day In The Life - Remastered 2009', '1967'},
            {'Eight Days A Week - Remastered 2009', '1964'},
            {'In My Life - Remastered 2009', '1965'},
        ],
        ordered=False,
    )


@check50.check(exists)
def test11():
    """11.sql lista los músicos con canciones latinas muy populares"""
    check_single_col(
        run_query("11.sql"),
        {
            'Ava Max',
            'Billie Eilish',
            'KAROL G',
            'Khalid',
            'Kygo',
            'Mabel',
            'Regard',
            'Riton',
            'The Black Eyed Peas',
            'The Chainsmokers',
        },
        ordered=False,
    )


@check50.check(exists)
def test12():
    """12.sql lista las cinco canciones más populares de Queen"""
    check_double_col(
        run_query("12.sql"),
        [
            {'We Are The Champions - Remastered 2011', '76'},
            {"Don't Stop Me Now - 2011 Mix", '75'},
            {'We Will Rock You - Remastered', '70'},
            {'Killer Queen - 2011 Mix', '50'},
            {'Death On Two Legs (Dedicated To...) - Remastered 2011', '46'},
        ],
        ordered=True,
    )


@check50.check(exists)
def test13():
    """13.sql lista las canciones de Jason Derulo con Nicki Minaj"""
    check_single_col(
        run_query("13.sql"),
        {
            'Goodbye (feat. Nicki Minaj & Willy William)',
            'Swalla (feat. Nicki Minaj & Ty Dolla $ign)',
            'Swalla (feat. Nicki Minaj and Ty Dolla $ign) - Wideboys Remix',
        },
        ordered=False,
    )


@check50.check(exists)
def test14():
    """14.sql lista a quienes colaboraron junto a Daddy Yankee"""
    check_single_col(
        run_query("14.sql"),
        {
            'Anuel AA',
            'Arcangel',
            'Cosculluela',
            'De La Ghetto',
            'Farruko',
            'Nengo Flow',
            'Nicky Jam',
            'Wisin',
            'Zion',
        },
        ordered=False,
    )


@check50.check(exists)
def test15():
    """15.sql lista el segundo grado de Nicky Jam"""
    check_single_col(
        run_query("15.sql"),
        {
            'Anuel AA',
            'Cosculluela',
            'Darell',
            'Justin Quiles',
            'Mohombi',
            'Natti Natasha',
            'Ne-Yo',
            'Wisin',
        },
        ordered=False,
    )


def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL(f"sqlite:///{BD}")
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error al ejecutar consulta: {str(e)}")


def check_single_col(actual, expected, ordered=False):
    """
    Comprueba las consultas que devuelven una sola columna.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("La consulta no arrojó resultados")

    # Make sure there is only a single column
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {1}:
        raise check50.Failure("La consulta solo debe devolver una sola columna")

    # Get data from column
    try:
        result = [str(list(row.values())[0]) for row in actual]
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Check column data against expected values
    expected = [str(value) for value in expected]
    if not ordered:
        expected = set(expected)
    if result != expected:
        raise check50.Mismatch("\n".join(expected), "\n".join(list(result)))


def check_single_cell(actual, expected):
    return check_single_col(actual, [expected], ordered=True)


def check_single_cell_aprox(actual, expected, tolerancia=0.01):
    """
    Como check_single_cell, pero para promedios: compara numéricamente con una
    tolerancia, de modo que redondear el resultado no se considere un error.
    """

    if actual is None or actual == []:
        raise check50.Failure("La consulta no arrojó resultados")

    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {1}:
        raise check50.Failure("La consulta solo debe devolver una sola columna")

    if len(actual) != 1:
        raise check50.Failure(
            f"La consulta debe devolver una sola fila, devolvió {len(actual)}"
        )

    valor = list(actual[0].values())[0]
    try:
        valor = float(valor)
    except (TypeError, ValueError):
        raise check50.Mismatch(str(expected), str(valor))

    if abs(valor - expected) > tolerancia:
        raise check50.Mismatch(str(expected), str(valor))


def check_double_col(actual, expected, ordered=False):
    """
    Comprueba las consultas que devuelven exactamente dos columnas.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("La consulta no arrojó resultados")

    # Make sure there are only two columns
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {2}:
        raise check50.Failure("La consulta debe devolver exactamente dos columnas")

    # Get data from column
    try:
        result = []
        for row in actual:
            values = list(row.values())
            result.append(frozenset((str(values[0]), str(values[1]))))
        expected = [frozenset(fila) for fila in expected]
        result = result if ordered else set(result)
        expected = expected if ordered else set(expected)
    except IndexError:
        return None

    # Check column data against expected values
    if result != expected:
        raise check50.Mismatch(
            "\n".join([str(entry) for entry in list(expected)]),
            "\n".join([str(entry) for entry in list(result)]),
        )
