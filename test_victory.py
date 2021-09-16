import victory

def test_Day():

    assert victory.getDay('01')  == 'первое'
    assert victory.getDay('10') == 'десятое'
    assert victory.getDay('12') == 'двенадцатое'
    assert victory.getDay('20') == 'двадцатое'
    assert victory.getDay('25') == 'двадцать пятое'
    assert victory.getDay('30') == 'тридцатое'
    assert victory.getDay('31') == 'тридцать первое'

def test_Month():
    assert victory.getMonth('01') == 'января'
    assert victory.getMonth('12') == 'декабря'

def test_bDayOut():
    assert victory.bDayOut( '01.01.2012') == 'первое января 2012 года'

def test_errDay():
    assert not victory.getDay('hiuh')

def test_errMonth():
    assert not victory.getMonth('hiuh')

