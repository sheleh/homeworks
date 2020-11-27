# The greeting program.
name = 'Dmitriy'
day = 4
# variant of formatting 1
s = '"Good day {}! {} is a perfect day to learn some python."'
print((s.format(name, day)))
# variant of formatting 1.1
s = '"Good day {1}! {0} is a perfect day to learn some python."'
print((s.format(day, name)))
# variant of formatting 2
print(f'"Good day {name}! {day} is a perfect day to learn some python."')
# variant of formatting 3
print('"Good day %s! %s is a perfect day to learn some python."' % (name, day))
# variant of formatting 4
print('\"Good day ' + name + '!', str(day) + ' is a perfect day to learn some python.\"')

