#USBkeysTranslator v1.0

import sys

#First byte values - Modifier masks.

usb_codes_1stByte = {
	"01":"key_mod_LCTRL", 
	"02":"key_mod_LSHIFT", 
	"04":"key_mod_LALT", 
	"08":"key_mod_LMETA", 
	"10":"key_mod_RCTRL", 
	"20":"key_mod_RSHIFT", 
	"40":"key_mod_RALT", 
	"80":"key_mod_RMETA"}

#The second byte in the report is reserved, "00"

usb_codes_2ndByte = "00"

#The third byte represents the key

usb_codes_3rdByte = { 
	"00":"key_NONE", # No key pressed
	"01":"key_ERR_OVF", #  keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")
	"02":"key_POST_FAIL", #  keyboard POST Fail
	"03":"key_ERROR_UNDEFINED", #  keyboard Error Undefined
	"04":"key_A", # keyboard a and A
	"05":"key_B", # keyboard b and B
	"06":"key_C", # keyboard c and C
	"07":"key_D", # keyboard d and D
	"08":"key_E", # keyboard e and E
	"09":"key_F", # keyboard f and F
	"0a":"key_G", # keyboard g and G
	"0b":"key_H", # keyboard h and H
	"0c":"key_I", # keyboard i and I
	"0d":"key_J", # keyboard j and J
	"0e":"key_K", # keyboard k and K
	"0f":"key_L", # keyboard l and L
	"10":"key_M", # keyboard m and M
	"11":"key_N", # keyboard n and N
	"12":"key_O", # keyboard o and O
	"13":"key_P", # keyboard p and P
	"14":"key_Q", # keyboard q and Q
	"15":"key_R", # keyboard r and R
	"16":"key_S", # keyboard s and S
	"17":"key_T", # keyboard t and T
	"18":"key_U", # keyboard u and U
	"19":"key_V", # keyboard v and V
	"1a":"key_W", # keyboard w and W
	"1b":"key_X", # keyboard x and X
	"1c":"key_Y", # keyboard y and Y
	"1d":"key_Z", # keyboard z and Z

	"1e":"key_1", # keyboard 1 and !
	"1f":"key_2", # keyboard 2 and @
	"20":"key_3", # keyboard 3 and #
	"21":"key_4", # keyboard 4 and $
	"22":"key_5", # keyboard 5 and %
	"23":"key_6", # keyboard 6 and ^
	"24":"key_7", # keyboard 7 and &
	"25":"key_8", # keyboard 8 and *
	"26":"key_9", # keyboard 9 and (
	"27":"key_0", # keyboard 0 and )

	"28":"key_ENTER", # keyboard Return (ENTER)
	"29":"key_ESC", # keyboard ESCAPE
	"2a":"key_BACKSPACE", # keyboard DELETE (Backspace)
	"2b":"key_TAB", # keyboard Tab
	"2c":"key_SPACE", # keyboard Spacebar
	"2d":"key_MINUS", # keyboard - and _
	"2e":"key_EQUAL", # keyboard = and +
	"2f":"key_LEFTBRACE", # keyboard [ and {
	"30":"key_RIGHTBRACE", # keyboard ] and }
	"31":"key_BACKSLASH", # keyboard \ and |
	"32":"key_HASHTILDE", # keyboard Non-US, # and ~
	"33":"key_SEMICOLON", # keyboard ; and :
	"34":"key_APOSTROPHE", # keyboard ' and "
	"35":"key_GRAVE", # keyboard ` and ~
	"36":"key_COMMA", # keyboard , and <
	"37":"key_DOT", # keyboard . and >
	"38":"key_SLASH", # keyboard / and ?
	"39":"key_CAPS_LOCK", # keyboard Caps Lock

	"3a":"key_F1", # keyboard F1
	"3b":"key_F2", # keyboard F2
	"3c":"key_F3", # keyboard F3
	"3d":"key_F4", # keyboard F4
	"3e":"key_F5", # keyboard F5
	"3f":"key_F6", # keyboard F6
	"40":"key_F7", # keyboard F7
	"41":"key_F8", # keyboard F8
	"42":"key_F9", # keyboard F9
	"43":"key_F10", # keyboard F10
	"44":"key_F11", # keyboard F11
	"45":"key_F12", # keyboard F12

	"46":"key_PRINTSCREEN", # keyboard Print Screen
	"47":"key_SCROLLLOCK", # keyboard Scroll Lock
	"48":"key_PAUSE", # keyboard Pause
	"49":"key_INSERT", # keyboard Insert
	"4a":"key_HOME", # keyboard Home
	"4b":"key_PAGEUP", # keyboard Page Up
	"4c":"key_DELETE", # keyboard Delete Forward
	"4d":"key_END", # keyboard End
	"4e":"key_PAGEDOWN", # keyboard Page Down
	"4f":"key_RIGHT", # keyboard Right Arrow
	"50":"key_LEFT", # keyboard Left Arrow
	"51":"key_DOWN", # keyboard Down Arrow
	"52":"key_UP", # keyboard Up Arrow

	"53":"key_NUMLOCK", # keyboard Num Lock and Clear
	"54":"key_KP_SLASH", # keypad /
	"55":"key_KP_ASTERISK", # keypad *
	"56":"key_KP_MINUS", # keypad -
	"57":"key_KP_PLUS", # keypad +
	"58":"key_KP_ENTER", # keypad ENTER
	"59":"key_KP_1_END", # keypad 1 and End
	"5a":"key_KP_2_DOWNARROW", # keypad 2 and Down Arrow
	"5b":"key_KP_3_PAGEDN", # keypad 3 and PageDn
	"5c":"key_KP_4_LEFTARROW", # keypad 4 and Left Arrow
	"5d":"key_KP_5", # keypad 5
	"5e":"key_KP_6_RIGHTARROW", # keypad 6 and Right Arrow
	"5f":"key_KP_7_HOME", # keypad 7 and Home
	"60":"key_KP_8_UPARROW", # keypad 8 and Up Arrow
	"61":"key_KP_9_PAGEUP", # keypad 9 and Page Up
	"62":"key_KP_0_INSERT", # keypad 0 and Insert
	"63":"key_KP_DOT_DELETE", # keypad . and Delete

	"64":"key_BACKSLASH_AND_NONUS", # keyboard Non-US \ and |
	"65":"key_COMPOSE", # keyboard Application
	"66":"key_POWER", # keyboard Power
	"67":"key_KP_EQUAL", # keypad =

	"68":"key_F13", # keyboard F13
	"69":"key_F14", # keyboard F14
	"6a":"key_F15", # keyboard F15
	"6b":"key_F16", # keyboard F16
	"6c":"key_F17", # keyboard F17
	"6d":"key_F18", # keyboard F18
	"6e":"key_F19", # keyboard F19
	"6f":"key_F20", # keyboard F20
	"70":"key_F21", # keyboard F21
	"71":"key_F22", # keyboard F22
	"72":"key_F23", # keyboard F23
	"73":"key_F24", # keyboard F24

	"74":"key_EXECUTE", # keyboard Execute
	"75":"key_HELP", # keyboard Help
	"76":"key_MENU", # keyboard Menu
	"77":"key_SELECT", # keyboard Select
	"78":"key_STOP", # keyboard Stop
	"79":"key_AGAIN", # keyboard Again
	"7a":"key_UNDO", # keyboard Undo
	"7b":"key_CUT", # keyboard Cut
	"7c":"key_COPY", # keyboard Copy
	"7d":"key_PASTE", # keyboard Paste
	"7e":"key_FIND", # keyboard Find
	"7f":"key_MUTE", # keyboard Mute
	"80":"key_VOLUMEUP", # keyboard Volume Up
	"81":"key_VOLUMEDOWN", # keyboard Volume Down
	"82":"key_LOCK_CAPS_LOCK", # keyboard Locking Caps Lock
	"83":"key_LOCK_NUM_LOCK", # keyboard Locking Num Lock
	"84":"key_LOCK_SCROLL_LOCK", # keyboard Locking Scroll Lock
	"85":"key_KP_COMMA",  # keypad Comma
	"86":"key_KP_EQUAL",  # keypad Equal Sign

	"87":"key_RO",  # keyboard International1
	"88":"key_KATAKANAHIRAGANA",  # keyboard International2
	"89":"key_YEN",  # keyboard International3
	"8a":"key_HENKAN", # keyboard International4
	"8b":"key_MUHENKAN", # keyboard International5
	"8c":"key_KPJPCOMMA", # keyboard International6
	"8d":"key_INTERNATIONAL7", # keyboard International7
	"8e":"key_INTERNATIONAL8", # keyboard International8
	"8f":"key_INTERNATIONAL9", # keyboard International9
	"90":"key_HANGEUL", # keyboard LANG1
	"91":"key_HANJA", # keyboard LANG2
	"92":"key_KATAKANA", # keyboard LANG3
	"93":"key_HIRAGANA", # keyboard LANG4
	"94":"key_ZENKAKUHANKAKU", # keyboard LANG5
	"95":"key_LANG6", # keyboard LANG6
	"96":"key_LANG7", # keyboard LANG7
	"97":"key_LANG8", # keyboard LANG8
	"98":"key_LANG9", # keyboard LANG9
	"99":"key_ALTERNATE_ERASE", # keyboard Alternate Erase
	"9a":"key_SYSREQ_ATTENTION", # keyboard SysReq/Attention

	"9b":"key_CANCEL", # keyboard Cancel
	"9c":"key_CLEAR", # keyboard Clear
	"9d":"key_PRIOR", # keyboard Prior
	"9e":"key_RETURN", # keyboard Return
	"9f":"key_SEPARATOR", # keyboard Separator
	"a0":"key_OUT", # keyboard Out
	"a1":"key_OPER", # keyboard Oper
	"a2":"key_CLEAR_AGAIN", # keyboard Clear/Again
	"a3":"key_CRSEL_PROPS", # keyboard CrSel/Props
	"a4":"key_EXSEL", # keyboard ExSel

	"b0":"key_KP_ZEROZERO", # keypad 00
	"b1":"key_KP_ZEROZEROZERO", # keypad 000
	"b2":"key_THOUSANDS_SEPARATOR", # Thousands Separator
	"b3":"key_DECIMAL_SEPARATOR", # Decimal Separator
	"b4":"key_CURRENCY_UNIT", # Currency Unit
	"b5":"key_CURRENCT_SUB_UNIT", # Currency Sub-unit
	"b6":"key_KP_LEFTPAREN_ROUND", # keypad (
	"b7":"key_KP_RIGHTPAREN_ROUND", # keypad )
	"b8":"key_KP_LEFTPAREN_CURLY", # keypad {
	"b9":"key_KP_RIGHTPAREN_CURLY", # keypad }
	"ba":"key_KP_TAB",  # keypad Tab
	"bb":"key_KP_BACKSPACE",  # keypad Backspace
	"bc":"key_KP_A",  # keypad A
	"bd":"key_KP_B",  # keypad B
	"be":"key_KP_C",  # keypad C
	"bf":"key_KP_D",  # keypad D
	"c0":"key_KP_E",  # keypad E
	"c1":"key_KP_F",  # keypad F
	"c2":"key_KP_XOR",  # keypad XOR
	"c3":"key_KP_CARET",  # keypad ^
	"c4":"key_KP_PERCENT",  # keypad %
	"c5":"key_KP_LEFTARROW",  # keypad <
	"c6":"key_KP_RIGHTARROW",  # keypad >
	"c7":"key_KP_AND",  # keypad &
	"c8":"key_KP_ANDAND",  # keypad &&
	"c9":"key_KP_OR",  # keypad |
	"ca":"key_KP_OROR",  # keypad ||
	"cb":"key_KP_COLON",  # keypad :
	"cc":"key_KP_HASH",  # keypad" #
	"cd":"key_KP_SPACE",  # keypad Space
	"ce":"key_KP_AT",  # keypad @
	"cf":"key_KP_EXCLMARK",  # keypad !

	"d0":"key_KP_MEM_STORE",  # keypad Memory Store
	"d1":"key_KP_MEM_RECALL",  # keypad Memory Recall
	"d2":"key_KP_MEM_CLEAR",  # keypad Memory Clear
	"d3":"key_KP_MEM_ADD",  # keypad Memory Add
	"d4":"key_KP_MEM_SUBSTRACT",  # keypad Memory Subtract
	"d5":"key_KP_MEM_MULTIPLY",  # keypad Memory Multiply
	"d6":"key_KP_MEM_DIVIDE",  # keypad Memory Divide
	"d7":"key_KP_PLUS_MINUS",  # keypad +/-
	"d8":"key_KP_CLEAR",  # keypad Clear
	"d9":"key_KP_CLEAR_ENTRY",  # keypad Clear Entry
	"da":"key_KP_BINARY",  # keypad Binary
	"db":"key_KP_OCTAL",  # keypad Octal
	"dc":"key_KP_DECIMAL",  # keypad Decimal
	"dd":"key_KP_HEXADECIMAL",  # keypad Hexadecimal

	"e0":"key_LEFTCTRL", #"keyboard Left Control
	"e1":"key_LEFTSHIFT", #"keyboard Left Shift
	"e2":"key_LEFTALT", #"keyboard Left Alt
	"e3":"key_LEFTMETA",#"keyboard Left GUI
	"e4":"key_RIGHTCTRL", #"keyboard Right Control
	"e5":"key_RIGHTSHIFT", #"keyboard Right Shift
	"e6":"key_RIGHTALT", #"keyboard Right Alt
	"e7":"key_RIGHTMETA", #"keyboard Right GUI

	"e8":"key_MEDIA_PLAYPAUSE",
	"e9":"key_MEDIA_STOPCD",
	"ea":"key_MEDIA_PREVIOUSSONG",
	"eb":"key_MEDIA_NEXTSONG",
	"ec":"key_MEDIA_EJECTCD",
	"ed":"key_MEDIA_VOLUMEUP",
	"ee":"key_MEDIA_VOLUMEDOWN",
	"ef":"key_MEDIA_MUTE",
	"f0":"key_MEDIA_WWW",
	"f1":"key_MEDIA_BACK",
	"f2":"key_MEDIA_FORWARD",
	"f3":"key_MEDIA_STOP",
	"f4":"key_MEDIA_FIND",
	"f5":"key_MEDIA_SCROLLUP",
	"f6":"key_MEDIA_SCROLLDOWN",
	"f7":"key_MEDIA_EDIT",
	"f8":"key_MEDIA_SLEEP",
	"f9":"key_MEDIA_COFFEE",
	"fa":"key_MEDIA_REFRESH",
	"fb":"key_MEDIA_CALC"
}

#Retains whether/when the Caps Lock is on during the capture. The result at the end will output 2 variants of the input anyway since we cannot know whether Caps was active before the capture.
caps_on = 0

#Translated USB keys
keys_captured = []

#Text typed
text_captured = []

#For a correct way to represent the text, a cursor position must be kept
cursor_position = 0

def key2Char(key, modifier):
	capital = caps_on
	if modifier!=None and modifier in ["key_mod_LSHIFT","key_mod_RSHIFT"]:
		capital+=1;
	if key == "key_A":
		if capital%2==0: return "a"
		else: return "A"
	if key == "key_B":
		if capital%2==0: return "b"
		else: return "B"
	if key == "key_C":
		if capital%2==0: return "c"
		else: return "C"
	if key == "key_D":
		if capital%2==0: return "d"
		else: return "D"
	if key == "key_E":
		if capital%2==0: return "e"
		else: return "E"
	if key == "key_F":
		if capital%2==0: return "f"
		else: return "F"
	if key == "key_G":
		if capital%2==0: return "g"
		else: return "G"
	if key == "key_H":
		if capital%2==0: return "h"
		else: return "H"
	if key == "key_I":
		if capital%2==0: return "i"
		else: return "I"
	if key == "key_J":
		if capital%2==0: return "j"
		else: return "J"
	if key == "key_K":
		if capital%2==0: return "k"
		else: return "K"
	if key == "key_L":
		if capital%2==0: return "l"
		else: return "L"
	if key == "key_M":
		if capital%2==0: return "m"
		else: return "M"
	if key == "key_N":
		if capital%2==0: return "n"
		else: return "N"
	if key == "key_O":
		if capital%2==0: return "o"
		else: return "O"
	if key == "key_P":
		if capital%2==0: return "p"
		else: return "P"
	if key == "key_Q":
		if capital%2==0: return "q"
		else: return "Q"
	if key == "key_R":
		if capital%2==0: return "r"
		else: return "R"
	if key == "key_S":
		if capital%2==0: return "s"
		else: return "S"
	if key == "key_T":
		if capital%2==0: return "t"
		else: return "T"
	if key == "key_U":
		if capital%2==0: return "u"
		else: return "U"
	if key == "key_V":
		if capital%2==0: return "v"
		else: return "V"
	if key == "key_W":
		if capital%2==0: return "w"
		else: return "W"
	if key == "key_X":
		if capital%2==0: return "x"
		else: return "X"
	if key == "key_Y":
		if capital%2==0: return "y"
		else: return "Y"
	if key == "key_Z":
		if capital%2==0: return "z"
		else: return "Z"
	if key == "key_1":
		if capital%2==0: return "1"
		else: return "!"
	if key == "key_2":
		if capital%2==0: return "2"
		else: return "@"
	if key == "key_3":
		if capital%2==0: return "3"
		else: return "#"
	if key == "key_4":
		if capital%2==0: return "4"
		else: return "$"
	if key == "key_5":
		if capital%2==0: return "5"
		else: return "%"
	if key == "key_6":
		if capital%2==0: return "6"
		else: return "^"
	if key == "key_7":
		if capital%2==0: return "7"
		else: return "&"
	if key == "key_8":
		if capital%2==0: return "8"
		else: return "*"
	if key == "key_9":
		if capital%2==0: return "9"
		else: return "("
	if key == "key_0":
		if capital%2==0: return "0"
		else: return ")"
	if key == "key_ENTER":
		return "\n"
	if key == "key_TAB":
		return "\t"
	if key == "key_SPACE":
		return " "
	if key == "key_MINUS":
		if capital%2==0: return "-"
		else: return "_"
	if key == "key_EQUAL":
		if capital%2==0: return "="
		else: return "+"
	if key == "key_LEFTBRACE":
		if capital%2==0: return "["
		else: return "{"
	if key == "key_RIGHTBRACE":
		if capital%2==0: return "]"
		else: return "}"
	if key == "key_BACKSLASH":
		if capital%2==0: return "\\"
		else: return "|"
	if key == "key_HASHTILDE":
		if capital%2==0: return "#"
		else: return "~"
	if key == "key_SEMICOLON":
		if capital%2==0: return ";"
		else: return ":"
	if key == "key_APOSTROPHE":
		if capital%2==0: return "'"
		else: return "\""
	if key == "key_GRAVE":
		return "`"
	if key == "key_COMMA":
		if capital%2==0: return ","
		else: return "<"
	if key == "key_DOT":
		if capital%2==0: return "."
		else: return ">"
	if key == "key_SLASH":
		if capital%2==0: return "/"
		else: return "?"
	return None

def processKey(key):
	global cursor_position
	if key == "key_BACKSPACE":
		if cursor_position > 0:
			cursor_position-=1
			del text_captured[cursor_position]
	if key == "key_CAPS_LOCK":
		caps_on = (caps_on + 1)%2
	if key == "key_RIGHT":
		cursor_position+=1
	if key == "key_LEFT":
		if cursor_position > 0:
			cursor_position-=1
filename = ""

#From pcap leftovers
try:
	filename = str(sys.argv[1])
except:
	print "Usage: $python USBkeysTranslator.py <hexvalues_file>"
	sys.exit()

with open(filename,"rb") as hexfile:
	for line in hexfile:
		firstByte = line[:2]
		secondByte = line[2:4]
		thirdByte = line[4:6]
		modifier = None
		key = None
		try:
			modifier = usb_codes_1stByte[firstByte]
		except:
			# no code for modifier found
			pass
		try:
			key = usb_codes_3rdByte[thirdByte]
		except:
			# no code for key found, go for the next line
			continue
	
		keys_captured.append(key)
		if key=="key_O":
			print "got o"
		# if the pressed key outputs a character, it will be retained
		character = key2Char(key,modifier)
		if character != None:
			text_captured.insert(cursor_position, character)
			cursor_position+=1
		else:
			# otherwise, the key is processed and any impact it can have on the printed text will be taken into consideration
			processKey(key)

#print "The following keys were retrieved:\n" 
#print keys_captured
#print "\n"

print "The keys produced the following text:\n"
text = ""
for char in text_captured:
	text+=char
print text
