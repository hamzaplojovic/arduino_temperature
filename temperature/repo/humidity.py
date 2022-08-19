from deta import Deta

deta = Deta("a09rrrza_mW3BFLo4fDmUfMxEndWyjBKeZAQn8ZEf")
db = deta.Base("humidity")


def all_items():
    return [x for x in db.fetch().items]


def latest_humidity():
    return [x for x in db.fetch().items][-1]

def add_humidity(new_temp):
    db.put(new_temp, key=new_temp)
