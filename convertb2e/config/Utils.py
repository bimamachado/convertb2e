def month_string_to_number(string):
    m = {
        'jan': '01',
        'feb': '02',
        'fev': '02',
        'mar': '03',
        'apr':'04',
        'abr': '04',
        'may':'05',
        'mai': '05',
        'jun':'06',
         'jul':'07',
         'aug':'08',
        'ago': '08',
        'sep':'09',
        'set': '09',
        'oct':'10',
        'out': '10',
        'nov':'11',
         'dec':'12',
        'dez': '12'

    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

def category_of_desc(name):
    return "SEM CATEGORIA"
