import re


#txt = re.sub(r'([^0-9a-zA-Z])', r'\1 ', '!!!this, .is, 123, .a .test!!!' )

txt = re.sub('([^0-9a-zA-Z])',  r' \1 ', '<li>aaskdjfas</li> !!!this, .is, 123, .a .test!!!' )

print(txt)