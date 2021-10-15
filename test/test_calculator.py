from source.calculator import add,subtract


def test_add():
   assert add() == '+'

def test_subtract():
   assert subtract() == '-'