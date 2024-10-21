# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab 06
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical

letter_count = {
    'a' : random_string.count('a'),
    'b' : random_string.count('b'),
    'c' : random_string.count('c'),
    'd' : random_string.count('d'),
    'e' : random_string.count('e'),
    'f' : random_string.count('f'),
    'g' : random_string.count('g'),
    'h' : random_string.count('h'),
    'i' : random_string.count('i'),
    'j' : random_string.count('j'),
    'k' : random_string.count('k'),
    'l' : random_string.count('l'),
    'm' : random_string.count('m'),
    'n' : random_string.count('n'),
    'o' : random_string.count('o'),
    'p' : random_string.count('p'),
    'q' : random_string.count('q'),
    'r' : random_string.count('r'),
    's' : random_string.count('s'),
    't' : random_string.count('t'),
    'u' : random_string.count('u'),
    'v' : random_string.count('v'),
    'w' : random_string.count('w'),
    'x' : random_string.count('x'),
    'y' : random_string.count('y'),
    'z' : random_string.count('z'),

}


print(f"Below is the list of the number of times each letter occurs in the random string\n{letter_count}")

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

# Output: each letter and its corresponding occurrence in alphabetical order

print("*"*75)
# Output which letter occurred the most 

most_occurred = "h"
least_occurred = "n"

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the most is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical


letter_percent = {
    'a' : random_string.count('a')/2500*100,
    'b' : random_string.count('b')/2500*100,
    'c' : random_string.count('c')/2500*100,
    'd' : random_string.count('d')/2500*100,
    'e' : random_string.count('e')/2500*100,
    'f' : random_string.count('f')/2500*100,
    'g' : random_string.count('g')/2500*100,
    'h' : random_string.count('h')/2500*100,
    'i' : random_string.count('i')/2500*100,
    'j' : random_string.count('j')/2500*100,
    'k' : random_string.count('k')/2500*100,
    'l' : random_string.count('l')/2500*100,
    'm' : random_string.count('m')/2500*100,
    'n' : random_string.count('n')/2500*100,
    'o' : random_string.count('o')/2500*100,
    'p' : random_string.count('p')/2500*100,
    'q' : random_string.count('q')/2500*100,
    'r' : random_string.count('r')/2500*100,
    's' : random_string.count('s')/2500*100,
    't' : random_string.count('t')/2500*100,
    'u' : random_string.count('u')/2500*100,
    'v' : random_string.count('v')/2500*100,
    'w' : random_string.count('w')/2500*100,
    'x' : random_string.count('x')/2500*100,
    'y' : random_string.count('y')/2500*100,
    'z' : random_string.count('z')/2500*100,

}
print(f"Below are percentages each letter makes up of the string\n{letter_percent}")