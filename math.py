
# Math
# python Cheat Sheet
# Number Theoretic
# ceil(x) copysign(x,y)
# fabs(x) factorial(x)
# floor(x) fmod(x,y)
# Power & Logarithmic
# exp(x) log(x[, base]) log1p(x) log10(x) pow(x,y) sqrt(x)
# Angular Conversion degrees(x) radians(x)
# Hyperbolic Functions
# Trigonometric Functions acos(x) asin(x) atan(x) atan2(y,x) cos(x) hypot(x,y) sin(x) tan(x)
# frexp(x) fsum(iterable)
# isinf(x) isnan(x)
# Idexp(x,i) modf() trunc()
# String Formatting
# acosh(x) asinh(x) atanh(x) cosh(x) sinh(x) tanh(x)
# Formatting Operations
# math.pi
# {cc}
# Constants
# The mathmatical constant of pie 3.141592.... up to the available precision math.e
# The mathmatical constante = 2.718281.... up to the available precision
# 'd' Signed integer decimal 'Signed integer decimal 'o' Signed octal value 'u' Obsolete type - it was identical to 'd' 'x' Signed hexadecimal (lowercase) 'X' Signed hexidecimal (uppercase) 'e' Floating point exponential format (lowercase) 'E' Floating point exponential format (uppercase) 'f' Floating point decimal format 'F' Floating point decimal format 'g' Floating point format. Uses the lowercase exponential format if the exponent is less than -4 or not less than precision, otherwise it uses the decimal format
# 'G' Floating point format. Uses the uppercase exponential format if the exponent is less than -4 or not less than precision, otherwise it uses the decimal format
# 'c' Single character (accepts either integer or single character string) 'r' String (converts any Python object using repr()) 's' String (converts any Python object using str()) '%' No argument is converted, adds a % character in the end result
# File
# Methods
# close() flush() fileno()
# isatty) next() read([size])
# readline ([size]) readlines([size])
# xreadlines() seek(offset[, whence])
# tell() truncate([size])
# write(str) writelines(sequence)
# Random
# Functions
# Attributes
# closed encoding
# errors mode
# name newlines
# softspace
# seed([x]) getstate() vonmisesvariate (mu,kappa) setstate(state) jumpahead (n) paretovariate(alpha) getrandbits(k) randint(a,b) weibullvariate(alpha,beta) randrange([start], stop[, step]) lognormvariate (mu,sigma) choice(seq) shuffle(x[, random]) normalvariate(mu, sigma) sample(population,k) random() gammevariate(alpha,beta) uniform(a,b) triangular (low,high,mode) gauss(mu,sigma) betavariate(alpha,beta) expovariate (lambd)
# OS
# OS Variables
# altsep Alternative separator curdir Current dir string defpath Default search path devnull Path of null device extsep Extension separator
# String
# pardir Parent dir string pathsep Patch separator sep Path separator name name of OS linesep Line separator
# String Methods
# Class
# Special Methods
# new (cls) _It_(self, other)
# _le_(self, other)_del_(self)
# eq_(self, other)
# __init__(self, args)
# _gt_(self, other)
# _repr_(self) ge_(self, other) _str_(self)
# cmp_(self, other)
# _ne_(self, other) __index__(self) _nonzero_(self) _hash_(self)_getattr__(self, name)
# _getattribute_(self, name) _setattr_(self, name, attr) _delattr_(self, name) _call_(self, args, kwargs)
# Array
# Array Methods
# append(x) buffer_info() byteswap() count(x) extend(iterable) fromfile(f,n) fromlist (list) fromstring(s) fromunicode(s) index(x) insert(i,x) pop([i]) remove(x) reverse() tofile(f) tolist()
# tostring() tounicode()
# SYS
# SYS Variables
# Indexes & Slices
# a=[0,1,2,3,4,5]
# b=a[:] Shallow copy of a
# a[1:] [1,2,3,4,5]
# a[5:] [0,1,2,3,4]
# a[-2:] [0,1,2,3]
# len(a) 6
# a[1:3] [1,2]
# a[0] 0
# a[1:-1] [1,2,3,4]
# a[5] 5
# a[-1] 5
# a[-2] 4
# platform Current platform
# stdin, stdout, stderr File objects for I/O version_info Python version info
# winver Version number
# argy Command line args builtin_module_names Linked C modules check_-interval Signal check frequency exec_prefix Root directory
# executable Name of Executable exitfunc Exit function name modules Loaded modules path Search path
# Set & Mapping
# end Se
# capitalize() center(width), fillchar]) count(subl, start[, decode encode([encoding, errors]]) isalnum() endswith(suffix, start[, end]]) expandtabs([tabsize]) find(subl, start[, end]]) format(*args, **kwargs) isalpha() index(subl, start, end]]) isdigit() islower) isspace() istitle() isupper) join(iterable) ljust(width, fillchar]) lower() Istrip([chars]) partition(sep) replace(old, new, count]) rfind(sub[, start[, end]]) rindex(sub[, start[, end]]) rjust(width, fillchar]) rpartition(sep) rsplit([sepl, maxsplit]]) rstrip([chars]) split([sepl, maxsplit]]) splitlines([keepends]) startswith(prefix, start[, end]]) strip([chars]), swapcase, title() translate(tablel, deletechars]), upper() zfill(width) isnumeric() isdecimal()
# Date Time
# Time Object
# Date Object
# replace((year, month,day)) timetuple() toordinal() weekday00 isoweekday00 isocalendar00) isoformat() _str_0 ctime() strftime()
# replace([hour, minute, second, microsecond, tzinfo]]]]) isoformat) str_0) strftime() utcoffset dsto) tzname()
# Datetime Object
# date) time() timetz) toordinal() weekday) isoweekday() isocalendar() replace([year], month, day, hour, minute, secondl, microsecond, tzinfo]]]]]]]]> astimezone(tz) utcoffset() dst tzname() timetuple() utctimetuple() isoformat_str_0 ctime() strftime()
# Set Types
# len(s) xins x not in s isdisjoint(other) issubset(others) issuperset union(other...) intersection(other...) difference(other...) symmetric difference(other) copy) update() intersection_update() difference_update() symmetric difference_update() add(elem) remove() discard(elem) pop() clear()
# SYS Arg V
# sys.argv[0] foo.py
# sys.argv[1] bar
# sys.argv[2] -c
# sys.argv[3] qux sys.argv[4] --h
# Mapping Types
# len(d) d[key] d[key]=value del d[key] key in d key not in d iter(d) clear() copy0) items() fromkeys(seql, value]) keys() get(keyl, default]) has_key(key) iteritems() iterkeys() itervalues() popitem() pop(keyl, default]) setdefault(keyl, default]) update([other]) values
# Date Formatting
# %a Abbreviated weekday (Mon)
# %A Weekday (Monday)
# 9%b Abbreviated month name (Nov) %B Month name (November) 9%c Date and time %d Day (leading zeros) (01 to 31)
# 9%H 24 hour (leading zeros) (00 to 23) 9% 12 hour (leading zeros) (01 to 12) %j Day of year (001 to 366) %m Month (01 to 12) 9%M Minute (00 to 59) 9%p AM or PM %S Second (00 to 61?) 96U Week number1 (00 to 53) %w Weekday2 (0 to 6) %W Week number3 (00 to 53) 9%x Date 9%X Time %y Year without century (00 to 99) %Y Year (2016) %Z Time zone (EST) 96% A literal "%" character (9%)