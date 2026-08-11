import streamlit as st
import sys

class WebPrint:
    def write(self, text):
        if text.strip():
            st.text(text)
    def flush(self):
        pass

sys.stdout = WebPrint() 
import math
from collections import Counter, defaultdict
from functools import lru_cache
import random
import sys

class AdvancedWordleSolver:
    def __init__(self, word_list=None):
        """
        Initialize the advanced Wordle solver with a comprehensive dictionary.
        """
        if word_list is None:
            # Comprehensive list of 5-letter words for Wordle
            self.all_words = [
                'about', 'above', 'abuse', 'actor', 'acute', 'admit', 'adopt', 'adult', 'after', 'again',
                'agent', 'agree', 'ahead', 'alarm', 'album', 'alert', 'alike', 'alive', 'allow', 'alone',
                'along', 'alter', 'among', 'anger', 'angle', 'angry', 'apart', 'apple', 'apply', 'arena',
                'argue', 'arise', 'array', 'aside', 'asset', 'audio', 'audit', 'avoid', 'award', 'aware',
                'badly', 'baker', 'bases', 'basic', 'basis', 'beach', 'began', 'begin', 'begun', 'being',
                'below', 'bench', 'billy', 'birth', 'black', 'blame', 'blind', 'block', 'blood', 'board',
                'boost', 'booth', 'bound', 'brain', 'brand', 'bread', 'break', 'breed', 'brief', 'bring',
                'broad', 'broke', 'brown', 'build', 'built', 'buyer', 'cable', 'calif', 'carry', 'catch',
                'cause', 'chain', 'chair', 'chart', 'chase', 'cheap', 'check', 'chest', 'chief', 'child',
                'china', 'chose', 'civil', 'claim', 'class', 'clean', 'clear', 'click', 'clock', 'close',
                'coach', 'coast', 'could', 'count', 'court', 'cover', 'craft', 'crash', 'cream', 'crime',
                'cross', 'crowd', 'crown', 'curve', 'cycle', 'daily', 'dance', 'dated', 'dealt', 'death',
                'debut', 'delay', 'depth', 'doing', 'doubt', 'dozen', 'draft', 'drama', 'drawn', 'dream',
                'dress', 'drill', 'drink', 'drive', 'drove', 'dying', 'eager', 'early', 'earth', 'eight',
                'elite', 'empty', 'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'event', 'every',
                'exact', 'exist', 'extra', 'faith', 'false', 'fault', 'fiber', 'field', 'fifth', 'fifty',
                'fight', 'final', 'first', 'fixed', 'flash', 'fleet', 'floor', 'fluid', 'focus', 'force',
                'forth', 'forty', 'forum', 'found', 'frame', 'frank', 'fraud', 'fresh', 'front', 'fruit',
                'fully', 'funny', 'giant', 'given', 'glass', 'globe', 'going', 'grace', 'grade', 'grand',
                'grant', 'grass', 'great', 'green', 'gross', 'group', 'grown', 'guard', 'guess', 'guest',
                'guide', 'happy', 'harry', 'heart', 'heavy', 'hence', 'henry', 'horse', 'hotel', 'house',
                'human', 'ideal', 'image', 'index', 'inner', 'input', 'issue', 'japan', 'jimmy', 'joint',
                'jones', 'judge', 'known', 'label', 'large', 'laser', 'later', 'laugh', 'layer', 'learn',
                'lease', 'least', 'leave', 'legal', 'level', 'lewis', 'light', 'limit', 'links', 'lives',
                'local', 'logic', 'loose', 'lower', 'lucky', 'lunch', 'lying', 'magic', 'major', 'maker',
                'march', 'maria', 'match', 'maybe', 'mayor', 'meant', 'media', 'metal', 'might', 'minor',
                'minus', 'mixed', 'model', 'money', 'month', 'moral', 'motor', 'mount', 'mouse', 'mouth',
                'movie', 'music', 'needs', 'never', 'newly', 'night', 'noise', 'north', 'noted', 'novel',
                'nurse', 'occur', 'ocean', 'offer', 'often', 'order', 'other', 'ought', 'paint', 'panel',
                'paper', 'party', 'peace', 'peter', 'phase', 'phone', 'photo', 'piece', 'pilot', 'pitch',
                'place', 'plain', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price',
                'pride', 'prime', 'print', 'prior', 'prize', 'proof', 'proud', 'prove', 'queen', 'quick',
                'quiet', 'quite', 'radio', 'raise', 'range', 'rapid', 'ratio', 'reach', 'ready', 'refer',
                'right', 'rival', 'river', 'robin', 'roger', 'roman', 'rough', 'round', 'route', 'royal',
                'rural', 'scale', 'scene', 'scope', 'score', 'sense', 'serve', 'seven', 'shall', 'shape',
                'share', 'sharp', 'sheet', 'shelf', 'shell', 'shift', 'shirt', 'shock', 'shoot', 'short',
                'shown', 'sight', 'since', 'sixth', 'sixty', 'sized', 'skill', 'sleep', 'slide', 'small',
                'smart', 'smile', 'smith', 'smoke', 'solid', 'solve', 'sorry', 'sound', 'south', 'space',
                'spare', 'speak', 'speed', 'spend', 'spent', 'split', 'spoke', 'sport', 'staff', 'stage',
                'stake', 'stand', 'start', 'state', 'steam', 'steel', 'stick', 'still', 'stock', 'stone',
                'stood', 'store', 'storm', 'story', 'strip', 'stuck', 'study', 'stuff', 'style', 'sugar',
                'suite', 'super', 'sweet', 'table', 'taken', 'taste', 'taxes', 'teach', 'teeth', 'terry',
                'texas', 'thank', 'theft', 'their', 'theme', 'there', 'these', 'thick', 'thing', 'think',
                'third', 'those', 'three', 'threw', 'throw', 'tight', 'times', 'tired', 'title', 'today',
                'topic', 'total', 'touch', 'tough', 'tower', 'track', 'trade', 'train', 'treat', 'trend',
                'trial', 'tried', 'tries', 'truck', 'truly', 'trust', 'truth', 'twice', 'under', 'undue',
                'union', 'unity', 'until', 'upper', 'upset', 'urban', 'usage', 'usual', 'valid', 'value',
                'video', 'virus', 'visit', 'vital', 'voice', 'waste', 'watch', 'water', 'wheel', 'where',
                'which', 'while', 'white', 'whole', 'whose', 'woman', 'women', 'world', 'worry', 'worse',
                'worst', 'worth', 'would', 'wound', 'write', 'wrong', 'wrote', 'yield', 'young', 'youth',
                'aback', 'abase', 'abate', 'abbey', 'abbot', 'abhor', 'abide', 'abled', 'abode', 'abort',
                'about', 'above', 'abuse', 'abyss', 'acorn', 'acrid', 'actor', 'acute', 'adage', 'adapt',
                'adept', 'admin', 'admit', 'adobe', 'adopt', 'adore', 'adorn', 'adult', 'affix', 'afire',
                'afoot', 'afoul', 'after', 'again', 'agape', 'agate', 'agent', 'agile', 'aging', 'aglow',
                'agony', 'agree', 'ahead', 'aider', 'aisle', 'alarm', 'album', 'alert', 'algae', 'alibi',
                'alien', 'align', 'alike', 'alive', 'allay', 'alley', 'allot', 'allow', 'alloy', 'aloft',
                'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amaze', 'amber',
                'amble', 'amend', 'amiss', 'amity', 'among', 'ample', 'amply', 'amuse', 'angel', 'anger',
                'angle', 'angry', 'angst', 'anime', 'ankle', 'annex', 'annoy', 'annul', 'anode', 'antic',
                'anvil', 'aorta', 'apart', 'aphid', 'aping', 'apnea', 'apple', 'apply', 'apron', 'aptly',
                'arbor', 'ardor', 'arena', 'argue', 'arise', 'armor', 'aroma', 'arose', 'array', 'arrow',
                'arson', 'artsy', 'ascot', 'ashen', 'aside', 'askew', 'assay', 'asset', 'atoll', 'atone',
                'attic', 'audio', 'audit', 'augur', 'aunty', 'avail', 'avert', 'avian', 'avoid', 'await',
                'awake', 'award', 'aware', 'awash', 'awful', 'awoke', 'axial', 'axiom', 'axion', 'azure',
                'bacon', 'badge', 'badly', 'bagel', 'baggy', 'baker', 'baler', 'balmy', 'banal', 'banjo',
                'barge', 'baron', 'basal', 'basic', 'basil', 'basin', 'basis', 'baste', 'batch', 'bathe',
                'baton', 'batty', 'bawdy', 'bayou', 'beach', 'beady', 'beard', 'beast', 'beech', 'beefy',
                'befit', 'began', 'begat', 'beget', 'begin', 'begun', 'being', 'belch', 'belie', 'belle',
                'belly', 'below', 'bench', 'beret', 'berry', 'berth', 'beset', 'betel', 'bevel', 'bezel',
                'bible', 'bicep', 'biddy', 'bigot', 'bilge', 'billy', 'binge', 'bingo', 'biome', 'birch',
                'birth', 'bison', 'bitty', 'black', 'blade', 'blame', 'bland', 'blank', 'blare', 'blast',
                'blaze', 'bleak', 'bleat', 'bleed', 'bleep', 'blend', 'bless', 'blimp', 'blind', 'blink',
                'bliss', 'blitz', 'bloat', 'block', 'bloke', 'blond', 'blood', 'bloom', 'blown', 'bluer',
                'bluff', 'blunt', 'blurb', 'blurt', 'blush', 'board', 'boast', 'bobby', 'boney', 'bongo',
                'bonus', 'booby', 'boost', 'booth', 'booty', 'booze', 'boozy', 'borax', 'borne', 'bosom',
                'bossy', 'botch', 'bough', 'boule', 'bound', 'bowel', 'boxer', 'brace', 'braid', 'brain',
                'brake', 'brand', 'brash', 'brass', 'brave', 'bravo', 'brawl', 'brawn', 'bread', 'break',
                'breed', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brine', 'bring', 'brink', 'briny',
                'brisk', 'broad', 'broil', 'broke', 'brood', 'brook', 'broom', 'broth', 'brown', 'brunt',
                'brush', 'brute', 'buddy', 'budge', 'buggy', 'bugle', 'build', 'built', 'bulge', 'bulky',
                'bully', 'bunch', 'bunny', 'burly', 'burnt', 'burst', 'bused', 'bushy', 'butch', 'butte',
                'buxom', 'buyer', 'bylaw', 'cabal', 'cabby', 'cabin', 'cable', 'cacao', 'cache', 'cacti',
                'caddy', 'cadet', 'cagey', 'cairn', 'camel', 'cameo', 'canal', 'candy', 'canny', 'canoe',
                'canon', 'caper', 'caput', 'carat', 'cargo', 'carol', 'carry', 'carve', 'caste', 'catch',
                'cater', 'catty', 'caulk', 'cause', 'cavil', 'cease', 'cedar', 'cello', 'chafe', 'chaff',
                'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'chard', 'charm', 'chart', 'chase',
                'chasm', 'cheap', 'cheat', 'check', 'cheek', 'cheer', 'chess', 'chest', 'chick', 'chide',
                'chief', 'child', 'chili', 'chill', 'chime', 'china', 'chirp', 'chock', 'choir', 'choke',
                'chord', 'chore', 'chose', 'chuck', 'chump', 'chunk', 'churn', 'chute', 'cider', 'cigar',
                'cinch', 'circa', 'civic', 'civil', 'clack', 'claim', 'clamp', 'clang', 'clank', 'clash',
                'clasp', 'class', 'clean', 'clear', 'cleat', 'cleft', 'clerk', 'click', 'cliff', 'climb',
                'cling', 'clink', 'cloak', 'clock', 'clone', 'close', 'cloth', 'cloud', 'clout', 'clove',
                'clown', 'cluck', 'clued', 'clump', 'clung', 'coach', 'coast', 'cobra', 'cocoa', 'colon',
                'color', 'comet', 'comfy', 'comic', 'comma', 'conch', 'condo', 'conic', 'copse', 'coral',
                'corer', 'corny', 'couch', 'cough', 'could', 'count', 'coupe', 'court', 'coven', 'cover',
                'covet', 'covey', 'cower', 'coyly', 'crack', 'craft', 'cramp', 'crane', 'crank', 'crash',
                'crass', 'crate', 'crave', 'crawl', 'craze', 'crazy', 'creak', 'cream', 'credo', 'creed',
                'creek', 'creep', 'creme', 'crepe', 'crept', 'cress', 'crest', 'crick', 'cried', 'crier',
                'crime', 'crimp', 'crisp', 'croak', 'crock', 'crone', 'crony', 'crook', 'cross', 'croup',
                'crowd', 'crown', 'crude', 'cruel', 'crumb', 'crump', 'crush', 'crust', 'crypt', 'cubic',
                'cumin', 'curio', 'curly', 'curry', 'curse', 'curve', 'curvy', 'cutie', 'cyber', 'cycle',
                'cynic', 'daddy', 'daily', 'dairy', 'daisy', 'dally', 'dance', 'dandy', 'datum', 'daunt',
                'dealt', 'death', 'debar', 'debit', 'debug', 'debut', 'decal', 'decay', 'decor', 'decoy',
                'decry', 'defer', 'deign', 'deity', 'delay', 'delta', 'delve', 'demon', 'demur', 'denim',
                'dense', 'depot', 'depth', 'derby', 'deter', 'detox', 'deuce', 'devil', 'diary', 'dicey',
                'digit', 'dilly', 'dimly', 'diner', 'dingo', 'dingy', 'diode', 'dirge', 'dirty', 'disco',
                'ditch', 'ditto', 'ditty', 'diver', 'dizzy', 'dodge', 'dodgy', 'dogma', 'doing', 'dolly',
                'donor', 'donut', 'dopey', 'doubt', 'dough', 'dowdy', 'dowel', 'downy', 'dowry', 'dozen',
                'draft', 'drain', 'drake', 'drama', 'drank', 'drape', 'drawl', 'drawn', 'dread', 'dream',
                'dress', 'dried', 'drier', 'drift', 'drill', 'drink', 'drive', 'droit', 'droll', 'drone',
                'drool', 'droop', 'dross', 'drove', 'drown', 'druid', 'drunk', 'dryer', 'dryly', 'duchy',
                'dully', 'dummy', 'dumpy', 'dunce', 'dusky', 'dusty', 'dutch', 'duvet', 'dwarf', 'dwell',
                'dwelt', 'dying', 'eager', 'eagle', 'early', 'earth', 'easel', 'eaten', 'eater', 'ebony',
                'eclat', 'edict', 'edify', 'eerie', 'egret', 'eight', 'eject', 'eking', 'elate', 'elbow',
                'elder', 'elect', 'elegy', 'elfin', 'elide', 'elite', 'elope', 'elude', 'email', 'embed',
                'ember', 'emcee', 'empty', 'enact', 'endow', 'enema', 'enemy', 'enjoy', 'ennui', 'ensue',
                'enter', 'entry', 'envoy', 'epoch', 'epoxy', 'equal', 'equip', 'erase', 'erect', 'erode',
                'error', 'erupt', 'essay', 'ester', 'ether', 'ethic', 'ethos', 'etude', 'evade', 'event',
                'every', 'evict', 'evoke', 'exact', 'exalt', 'excel', 'exert', 'exile', 'exist', 'expel',
                'extol', 'extra', 'exult', 'eying', 'fable', 'facet', 'faint', 'fairy', 'faith', 'false',
                'fancy', 'fanny', 'farce', 'fatal', 'fatty', 'fault', 'fauna', 'favor', 'feast', 'fecal',
                'feign', 'fella', 'felon', 'femme', 'femur', 'fence', 'feral', 'ferry', 'fetal', 'fetch',
                'fetid', 'fetus', 'fever', 'fewer', 'fiber', 'ficus', 'field', 'fiend', 'fiery', 'fifth',
                'fifty', 'fight', 'filer', 'filet', 'filly', 'filmy', 'filth', 'final', 'finch', 'finer',
                'first', 'fishy', 'fixer', 'fizzy', 'fjord', 'flack', 'flail', 'flair', 'flake', 'flaky',
                'flame', 'flank', 'flare', 'flash', 'flask', 'fleck', 'fleet', 'flesh', 'flick', 'flier',
                'fling', 'flint', 'flirt', 'float', 'flock', 'flood', 'floor', 'flora', 'floss', 'flour',
                'flout', 'flown', 'fluff', 'fluid', 'fluke', 'flume', 'flung', 'flunk', 'flush', 'flute',
                'flyer', 'foamy', 'focal', 'focus', 'foggy', 'foist', 'folio', 'folly', 'foray', 'force',
                'forge', 'forgo', 'forte', 'forth', 'forty', 'forum', 'found', 'foyer', 'frail', 'frame',
                'frank', 'fraud', 'freak', 'freed', 'freer', 'fresh', 'friar', 'fried', 'frill', 'frisk',
                'fritz', 'frock', 'frond', 'front', 'frost', 'froth', 'frown', 'froze', 'fruit', 'fudge',
                'fugue', 'fully', 'fungi', 'funky', 'funny', 'furor', 'furry', 'fussy', 'fuzzy', 'gaffe',
                'gaily', 'gamer', 'gamma', 'gamut', 'gassy', 'gaudy', 'gauge', 'gaunt', 'gauze', 'gavel',
                'gawky', 'gayer', 'gayly', 'gazer', 'gecko', 'geeky', 'geese', 'genie', 'genre', 'ghost',
                'ghoul', 'giant', 'giddy', 'gipsy', 'girly', 'girth', 'given', 'giver', 'glade', 'gland',
                'glare', 'glass', 'glaze', 'gleam', 'glean', 'glide', 'glint', 'gloat', 'globe', 'gloom',
                'glory', 'gloss', 'glove', 'glyph', 'gnash', 'gnome', 'godly', 'going', 'golem', 'golly',
                'gonad', 'goner', 'goody', 'gooey', 'goofy', 'goose', 'gorge', 'gouge', 'gourd', 'grace',
                'grade', 'graft', 'grail', 'grain', 'grand', 'grant', 'grape', 'graph', 'grasp', 'grass',
                'grate', 'grave', 'gravy', 'graze', 'great', 'greed', 'green', 'greet', 'grief', 'grill',
                'grime', 'grimy', 'grind', 'gripe', 'groan', 'groin', 'groom', 'grope', 'gross', 'group',
                'grout', 'grove', 'growl', 'grown', 'gruel', 'gruff', 'grunt', 'guard', 'guava', 'guess',
                'guest', 'guide', 'guild', 'guile', 'guilt', 'guise', 'gulch', 'gully', 'gumbo', 'gummy',
                'guppy', 'gusto', 'gusty', 'gypsy', 'habit', 'hairy', 'halve', 'handy', 'happy', 'hardy',
                'harem', 'harpy', 'harry', 'harsh', 'haste', 'hasty', 'hatch', 'hater', 'haunt', 'haute',
                'haven', 'havoc', 'hazel', 'heady', 'heard', 'heart', 'heath', 'heave', 'heavy', 'hedge',
                'hefty', 'heist', 'helix', 'hello', 'hence', 'heron', 'hilly', 'hinge', 'hippo', 'hippy',
                'hitch', 'hoard', 'hobby', 'hoist', 'holly', 'homer', 'honey', 'honor', 'horde', 'horny',
                'horse', 'hotel', 'hotly', 'hound', 'house', 'hovel', 'hover', 'howdy', 'human', 'humid',
                'humor', 'humph', 'humus', 'hunch', 'hunky', 'hurry', 'husky', 'hussy', 'hutch', 'hydro',
                'hyena', 'hymen', 'hyper', 'icily', 'icing', 'ideal', 'idiom', 'idiot', 'idler', 'idyll',
                'igloo', 'iliac', 'image', 'imbue', 'impel', 'imply', 'inane', 'inbox', 'incur', 'index',
                'inept', 'inert', 'infer', 'ingot', 'inlay', 'inlet', 'inner', 'input', 'inter', 'intro',
                'ionic', 'irate', 'irony', 'islet', 'issue', 'itchy', 'ivory', 'jaunt', 'jazzy', 'jelly',
                'jerky', 'jetty', 'jewel', 'jiffy', 'joint', 'joist', 'joker', 'jolly', 'joust', 'judge',
                'juice', 'juicy', 'jumbo', 'jumpy', 'junta', 'junto', 'juror', 'kappa', 'karma', 'kayak',
                'kebab', 'khaki', 'kinky', 'kiosk', 'kitty', 'knack', 'knave', 'knead', 'kneed', 'kneel',
                'knelt', 'knife', 'knock', 'knoll', 'known', 'koala', 'krill', 'label', 'labor', 'laden',
                'ladle', 'lager', 'lance', 'lanky', 'lapel', 'lapse', 'large', 'larva', 'lasso', 'latch',
                'later', 'lathe', 'latte', 'laugh', 'layer', 'leach', 'leafy', 'leaky', 'leant', 'leapt',
                'learn', 'lease', 'leash', 'least', 'leave', 'ledge', 'leech', 'leery', 'lefty', 'legal',
                'leggy', 'lemon', 'lemur', 'leper', 'level', 'lever', 'libel', 'liege', 'light', 'liken',
                'lilac', 'limbo', 'limit', 'linen', 'liner', 'lingo', 'lipid', 'lithe', 'liver', 'livid',
                'llama', 'loamy', 'loath', 'lobby', 'local', 'locus', 'lodge', 'lofty', 'logic', 'login',
                'loopy', 'loose', 'lorry', 'loser', 'louse', 'lousy', 'lover', 'lower', 'lowly', 'loyal',
                'lucid', 'lucky', 'lumen', 'lumpy', 'lunar', 'lunch', 'lunge', 'lupus', 'lurch', 'lurid',
                'lusty', 'lying', 'lymph', 'lynch', 'lyric', 'macaw', 'macho', 'macro', 'madam', 'madly',
                'mafia', 'magic', 'magma', 'maize', 'major', 'maker', 'mambo', 'mamma', 'mammy', 'manga',
                'mange', 'mango', 'mangy', 'mania', 'manic', 'manly', 'manor', 'maple', 'march', 'marry',
                'marsh', 'mason', 'masse', 'match', 'matey', 'mauve', 'maxim', 'maybe', 'mayor', 'mealy',
                'meant', 'meaty', 'mecca', 'medal', 'media', 'medic', 'melee', 'melon', 'mercy', 'merge',
                'merit', 'merry', 'metal', 'meter', 'metro', 'micro', 'midge', 'midst', 'might', 'milky',
                'mimic', 'mince', 'miner', 'minim', 'minor', 'minty', 'minus', 'mirth', 'miser', 'missy',
                'mocha', 'modal', 'model', 'modem', 'mogul', 'moist', 'molar', 'moldy', 'money', 'month',
                'moody', 'moose', 'moral', 'moron', 'morph', 'mossy', 'motel', 'motif', 'motor', 'motto',
                'moult', 'mound', 'mount', 'mourn', 'mouse', 'mouth', 'mover', 'movie', 'mower', 'mucky',
                'mucus', 'muddy', 'mulch', 'mummy', 'munch', 'mural', 'murky', 'mushy', 'music', 'musky',
                'musty', 'myrrh', 'nadir', 'naive', 'nanny', 'nasal', 'nasty', 'natal', 'naval', 'navel',
                'needy', 'neigh', 'nerdy', 'nerve', 'never', 'newer', 'newly', 'nicer', 'niche', 'niece',
                'night', 'ninja', 'ninny', 'ninth', 'noble', 'nobly', 'noise', 'noisy', 'nomad', 'noose',
                'north', 'nosey', 'notch', 'novel', 'nudge', 'nurse', 'nutty', 'nylon', 'nymph', 'oaken',
                'obese', 'occur', 'ocean', 'octal', 'octet', 'odder', 'oddly', 'offal', 'offer', 'often',
                'olden', 'older', 'olive', 'ombre', 'omega', 'onion', 'onset', 'opera', 'opine', 'opium',
                'optic', 'orbit', 'order', 'organ', 'other', 'otter', 'ought', 'ounce', 'outdo', 'outer',
                'outgo', 'ovary', 'ovate', 'overt', 'ovine', 'ovoid', 'owing', 'owner', 'oxide', 'ozone',
                'paddy', 'pagan', 'paint', 'paler', 'palsy', 'panel', 'panic', 'pansy', 'papal', 'paper',
                'parer', 'parka', 'parry', 'parse', 'party', 'pasta', 'paste', 'pasty', 'patch', 'patio',
                'patsy', 'patty', 'pause', 'payee', 'payer', 'peace', 'peach', 'pearl', 'pecan', 'pedal',
                'penal', 'pence', 'penne', 'penny', 'perch', 'peril', 'perky', 'pesky', 'pesto', 'petal',
                'petty', 'phase', 'phone', 'phony', 'photo', 'piano', 'picky', 'piece', 'piety', 'piggy',
                'pilot', 'pinch', 'piney', 'pinky', 'pinto', 'piper', 'pique', 'pitch', 'pithy', 'pivot',
                'pixel', 'pixie', 'pizza', 'place', 'plaid', 'plain', 'plait', 'plane', 'plank', 'plant',
                'plate', 'plaza', 'plead', 'pleat', 'plied', 'plier', 'pluck', 'plumb', 'plume', 'plump',
                'plunk', 'plush', 'poesy', 'point', 'poise', 'poker', 'polar', 'polka', 'polyp', 'pooch',
                'poppy', 'porch', 'poser', 'posit', 'posse', 'pouch', 'pound', 'pouty', 'power', 'prank',
                'prawn', 'preen', 'press', 'price', 'prick', 'pride', 'pried', 'prime', 'primo', 'print',
                'prior', 'prism', 'privy', 'prize', 'probe', 'prone', 'prong', 'proof', 'prose', 'proud',
                'prove', 'prowl', 'proxy', 'prude', 'prune', 'psalm', 'pubic', 'pudgy', 'puffy', 'pulpy',
                'pulse', 'punch', 'pupal', 'pupil', 'puppy', 'puree', 'purer', 'purge', 'purse', 'pushy',
                'putty', 'pygmy', 'quack', 'quail', 'quake', 'qualm', 'quark', 'quart', 'quash', 'quasi',
                'queen', 'queer', 'quell', 'query', 'quest', 'queue', 'quick', 'quiet', 'quill', 'quilt',
                'quirk', 'quite', 'quota', 'quote', 'quoth', 'rabbi', 'rabid', 'racer', 'radar', 'radii',
                'radio', 'rainy', 'raise', 'rajah', 'rally', 'ralph', 'ramen', 'ranch', 'randy', 'range',
                'rapid', 'rarer', 'raspy', 'ratio', 'ratty', 'raven', 'rayon', 'razor', 'reach', 'react',
                'ready', 'realm', 'rearm', 'rebar', 'rebel', 'rebus', 'rebut', 'recap', 'recur', 'recut',
                'reedy', 'refer', 'refit', 'regal', 'rehab', 'reign', 'relax', 'relay', 'relic', 'remit',
                'renal', 'renew', 'repay', 'repel', 'reply', 'rerun', 'reset', 'resin', 'retch', 'retro',
                'retry', 'reuse', 'revel', 'revue', 'rhino', 'rhyme', 'rider', 'ridge', 'rifle', 'right',
                'rigid', 'rigor', 'rinse', 'ripen', 'riper', 'risen', 'riser', 'risky', 'rival', 'river',
                'rivet', 'roach', 'roast', 'robin', 'robot', 'rocky', 'rodeo', 'roger', 'rogue', 'roomy',
                'roost', 'rotor', 'rouge', 'rough', 'round', 'rouse', 'route', 'rover', 'rowdy', 'rower',
                'royal', 'ruddy', 'ruder', 'rugby', 'ruler', 'rumba', 'rumor', 'rupee', 'rural', 'rusty',
                'sadly', 'safer', 'saint', 'salad', 'sally', 'salon', 'salsa', 'salty', 'salve', 'salvo',
                'sandy', 'saner', 'sappy', 'sassy', 'satin', 'satyr', 'sauce', 'saucy', 'sauna', 'saute',
                'savor', 'savoy', 'savvy', 'scald', 'scale', 'scalp', 'scaly', 'scamp', 'scant', 'scare',
                'scarf', 'scary', 'scene', 'scent', 'scion', 'scoff', 'scold', 'scone', 'scoop', 'scope',
                'score', 'scorn', 'scour', 'scout', 'scowl', 'scram', 'scrap', 'scree', 'screw', 'scrub',
                'scrum', 'scuba', 'sedan', 'seedy', 'segue', 'seize', 'semen', 'sense', 'sepia', 'serif',
                'serum', 'serve', 'setup', 'seven', 'sever', 'sewer', 'shack', 'shade', 'shady', 'shaft',
                'shake', 'shaky', 'shale', 'shall', 'shalt', 'shame', 'shank', 'shape', 'shard', 'share',
                'shark', 'sharp', 'shave', 'shawl', 'shear', 'sheen', 'sheep', 'sheer', 'sheet', 'sheik',
                'shelf', 'shell', 'shied', 'shift', 'shine', 'shiny', 'shire', 'shirk', 'shirt', 'shoal',
                'shock', 'shone', 'shook', 'shoot', 'shore', 'shorn', 'short', 'shout', 'shove', 'shown',
                'showy', 'shrew', 'shrub', 'shrug', 'shuck', 'shunt', 'shush', 'shyly', 'siege', 'sieve',
                'sight', 'sigma', 'silky', 'silly', 'since', 'sinew', 'singe', 'siren', 'sissy', 'sixth',
                'sixty', 'skate', 'skier', 'skiff', 'skill', 'skimp', 'skirt', 'skulk', 'skull', 'skunk',
                'slack', 'slain', 'slang', 'slant', 'slash', 'slate', 'slave', 'sleek', 'sleep', 'sleet',
                'slept', 'slice', 'slick', 'slide', 'slime', 'slimy', 'sling', 'slink', 'sloop', 'slope',
                'slosh', 'sloth', 'slump', 'slung', 'slunk', 'slurp', 'slush', 'slyly', 'smack', 'small',
                'smart', 'smash', 'smear', 'smell', 'smelt', 'smile', 'smirk', 'smite', 'smith', 'smock',
                'smoke', 'smoky', 'smote', 'snack', 'snail', 'snake', 'snaky', 'snare', 'snarl', 'sneak',
                'sneer', 'snide', 'sniff', 'snipe', 'snoop', 'snore', 'snort', 'snout', 'snowy', 'snuck',
                'snuff', 'soapy', 'sober', 'soggy', 'solar', 'solid', 'solve', 'sonar', 'sonic', 'sooth',
                'sooty', 'sorry', 'sound', 'south', 'sower', 'space', 'spade', 'spank', 'spare', 'spark',
                'spasm', 'spawn', 'speak', 'spear', 'speck', 'speed', 'spell', 'spelt', 'spend', 'spent',
                'sperm', 'spice', 'spicy', 'spied', 'spiel', 'spike', 'spiky', 'spill', 'spilt', 'spine',
                'spiny', 'spire', 'spite', 'splat', 'split', 'spoil', 'spoke', 'spoof', 'spook', 'spool',
                'spoon', 'spore', 'sport', 'spout', 'spray', 'spree', 'sprig', 'spunk', 'spurn', 'spurt',
                'squad', 'squat', 'squib', 'stack', 'staff', 'stage', 'staid', 'stain', 'stair', 'stake',
                'stale', 'stalk', 'stall', 'stamp', 'stand', 'stank', 'stare', 'stark', 'start', 'stash',
                'state', 'stave', 'stead', 'steak', 'steal', 'steam', 'steed', 'steel', 'steep', 'steer',
                'stein', 'stern', 'stick', 'stiff', 'still', 'stilt', 'sting', 'stink', 'stint', 'stock',
                'stoic', 'stoke', 'stole', 'stomp', 'stone', 'stony', 'stood', 'stool', 'stoop', 'store',
                'stork', 'storm', 'story', 'stout', 'stove', 'strap', 'straw', 'stray', 'strip', 'strut',
                'stuck', 'study', 'stuff', 'stump', 'stung', 'stunk', 'stunt', 'style', 'suave', 'sugar',
                'suing', 'suite', 'sulky', 'sully', 'sumac', 'sunny', 'super', 'surer', 'surge', 'surly',
                'sushi', 'swami', 'swamp', 'swarm', 'swash', 'swath', 'swear', 'sweat', 'sweep', 'sweet',
                'swell', 'swept', 'swift', 'swill', 'swine', 'swing', 'swirl', 'swish', 'swoon', 'swoop',
                'sword', 'swore', 'sworn', 'swung', 'synod', 'syrup', 'tabby', 'table', 'taboo', 'tacit',
                'tacky', 'taffy', 'taint', 'taken', 'taker', 'tally', 'talon', 'tamer', 'tango', 'tangy',
                'taper', 'tapir', 'tardy', 'tarot', 'taste', 'tasty', 'tatty', 'taunt', 'tawny', 'teach',
                'teary', 'tease', 'teddy', 'teeth', 'tempo', 'tenet', 'tenor', 'tense', 'tenth', 'tepee',
                'tepid', 'terra', 'terse', 'testy', 'thank', 'theft', 'their', 'theme', 'there', 'these',
                'theta', 'thick', 'thief', 'thigh', 'thing', 'think', 'third', 'thong', 'thorn', 'those',
                'three', 'threw', 'throb', 'throw', 'thrum', 'thumb', 'thump', 'thyme', 'tiara', 'tibia',
                'tidal', 'tiger', 'tight', 'tilde', 'timer', 'timid', 'tipsy', 'titan', 'tithe', 'title',
                'toast', 'today', 'toddy', 'token', 'tonal', 'tonga', 'tonic', 'tooth', 'topaz', 'topic',
                'torch', 'torso', 'torus', 'total', 'totem', 'touch', 'tough', 'towel', 'tower', 'toxic',
                'toxin', 'trace', 'track', 'tract', 'trade', 'trail', 'train', 'trait', 'tramp', 'trash',
                'trawl', 'tread', 'treat', 'trend', 'triad', 'trial', 'tribe', 'trice', 'trick', 'tried',
                'tripe', 'trite', 'troll', 'troop', 'trope', 'trout', 'trove', 'truce', 'truck', 'truer',
                'truly', 'trump', 'trunk', 'truss', 'trust', 'truth', 'tryst', 'tubal', 'tuber', 'tulip',
                'tulle', 'tumor', 'tunic', 'turbo', 'tutor', 'twang', 'tweak', 'tweed', 'tweet', 'twice',
                'twine', 'twirl', 'twist', 'twixt', 'tying', 'udder', 'ulcer', 'ultra', 'umbra', 'uncle',
                'uncut', 'under', 'undid', 'undue', 'unfed', 'unfit', 'unify', 'union', 'unite', 'unity',
                'unlit', 'unmet', 'unset', 'untie', 'until', 'unwed', 'unzip', 'upper', 'upset', 'urban',
                'urine', 'usage', 'usher', 'using', 'usual', 'usurp', 'utile', 'utter', 'vague', 'valet',
                'valid', 'valor', 'value', 'valve', 'vapid', 'vapor', 'vault', 'vaunt', 'vegan', 'venom',
                'venue', 'verge', 'verse', 'verso', 'verve', 'vicar', 'video', 'vigil', 'vigor', 'villa',
                'vinyl', 'viola', 'viper', 'viral', 'virus', 'visit', 'visor', 'vista', 'vital', 'vivid',
                'vixen', 'vocal', 'vodka', 'vogue', 'voice', 'voila', 'vomit', 'voter', 'vouch', 'vowel',
                'vying', 'wacky', 'wafer', 'wager', 'wagon', 'waist', 'waive', 'waltz', 'warty', 'waste',
                'watch', 'water', 'waver', 'waxen', 'weary', 'weave', 'wedge', 'weedy', 'weigh', 'weird',
                'welch', 'welsh', 'wench', 'whack', 'whale', 'wharf', 'wheat', 'wheel', 'whelp', 'where',
                'which', 'whiff', 'while', 'whine', 'whiny', 'whirl', 'whisk', 'white', 'whole', 'whoop',
                'whose', 'widen', 'wider', 'widow', 'width', 'wield', 'wight', 'willy', 'wimpy', 'wince',
                'winch', 'windy', 'wiser', 'wispy', 'witch', 'witty', 'woken', 'woman', 'women', 'woody',
                'wooer', 'wooly', 'woozy', 'wordy', 'world', 'worry', 'worse', 'worst', 'worth', 'would',
                'wound', 'woven', 'wrack', 'wrath', 'wreak', 'wreck', 'wrest', 'wring', 'wrist', 'write',
                'wrong', 'wrote', 'wrung', 'wryly', 'yacht', 'yearn', 'yeast', 'yield', 'young', 'youth',
                'zebra', 'zesty', 'zonal'
            ]
        else:
            self.all_words = [w.strip().lower() for w in word_list if len(w.strip()) == 5]
        
        # Validate and filter words
        self.all_words = [word for word in self.all_words if len(word) == 5 and word.isalpha()]
        self.remaining_words = list(self.all_words)
        self.guess_history = []
        self.letter_frequency = self._calculate_letter_frequency()
        
    def _calculate_letter_frequency(self):
        """Calculate frequency of each letter in all words."""
        freq = defaultdict(int)
        for word in self.all_words:
            for letter in word:
                freq[letter] += 1
        return freq
    
    @staticmethod
    @lru_cache(maxsize=10000)
    def calculate_feedback(guess, target):
        """
        Calculates the Wordle feedback pattern for a guess against a target word.
        Returns a tuple of integers: 0 (gray), 1 (yellow), 2 (green)
        """
        feedback = [0] * 5
        target_list = list(target)
        guess_list = list(guess)
        
        # First pass: mark greens
        for i in range(5):
            if guess_list[i] == target_list[i]:
                feedback[i] = 2
                target_list[i] = None
                guess_list[i] = None
                
        # Second pass: mark yellows
        for i in range(5):
            if guess_list[i] is not None and guess_list[i] in target_list:
                feedback[i] = 1
                target_list[target_list.index(guess_list[i])] = None
                
        return tuple(feedback)
    
    def calculate_entropy(self, guess, current_pool):
        """
        Calculates the expected information (entropy) of a guess based on the current pool.
        Entropy = sum(p(x) * log2(1/p(x)))
        """
        if not current_pool:
            return 0
            
        feedback_counts = Counter()
        for word in current_pool:
            feedback = self.calculate_feedback(guess, word)
            feedback_counts[feedback] += 1
            
        total = len(current_pool)
        entropy = 0
        for count in feedback_counts.values():
            p = count / total
            if p > 0:  # Avoid log(0)
                entropy += p * math.log2(1 / p)
                
        return entropy
    
    def calculate_positional_score(self, word):
        """
        Calculate a score based on letter frequency at each position.
        """
        score = 0
        for i, letter in enumerate(word):
            # Count how many words have this letter at this position
            position_count = sum(1 for w in self.remaining_words if w[i] == letter)
            score += position_count / len(self.remaining_words)
        return score
    
    def calculate_vowel_consonant_balance(self, word):
        """
        Calculate a score based on vowel/consonant balance.
        """
        vowels = set('aeiou')
        vowel_count = sum(1 for letter in word if letter in vowels)
        consonant_count = 5 - vowel_count
        
        # Ideal balance is 2 vowels and 3 consonants or vice versa
        if vowel_count == 2 and consonant_count == 3:
            return 1.0
        if vowel_count == 3 and consonant_count == 2:
            return 1.0
        if vowel_count == 1 and consonant_count == 4:
            return 0.8
        if vowel_count == 4 and consonant_count == 1:
            return 0.8
        return 0.5
    
    def calculate_letter_diversity(self, word):
        """
        Calculate a score based on letter diversity (no repeated letters).
        """
        return len(set(word)) / 5  # 1.0 for all unique letters
    
    def get_advanced_best_guess(self):
        """
        Determines the best word to guess using multiple advanced heuristics.
        """
        # If this is the first guess, use a precomputed optimal word
        if len(self.guess_history) == 0:
            # "tares" is a well-known optimal first guess
            return "tares"
            
        # If only one word remains, guess it
        if len(self.remaining_words) == 1:
            return self.remaining_words[0]
            
        # If only two words remain, choose the one that gives more information
        if len(self.remaining_words) == 2:
            # Calculate entropy for each word against the remaining pool
            entropies = []
            for word in self.remaining_words:
                entropy = self.calculate_entropy(word, self.remaining_words)
                entropies.append((entropy, word))
            # Return the word with higher entropy
            return max(entropies)[1]
            
        # For general cases, calculate multiple scores for all words
        word_scores = []
        
        # To optimize performance, we limit the search space:
        # If the remaining pool is small, search all words
        # If the remaining pool is large, search only within the remaining words
        search_space = self.remaining_words if len(self.remaining_words) < 100 else self.all_words
        
        for word in search_space:
            # Calculate multiple metrics
            entropy = self.calculate_entropy(word, self.remaining_words)
            positional_score = self.calculate_positional_score(word)
            vowel_balance = self.calculate_vowel_consonant_balance(word)
            diversity = self.calculate_letter_diversity(word)
            
            # Weighted combination of metrics
            # Entropy is the most important (0.5), then positional score (0.3), 
            # then vowel balance (0.1), then diversity (0.1)
            total_score = (
                0.5 * entropy + 
                0.3 * positional_score + 
                0.1 * vowel_balance + 
                0.1 * diversity
            )
            
            # Slight preference for words in the remaining pool
            if word in self.remaining_words:
                total_score += 0.0001
                
            word_scores.append((total_score, word))
            
        # Return the word with the highest score
        return max(word_scores)[1]
    
    def update_pool(self, guess, feedback):
        """
        Filters the remaining dictionary based on user feedback.
        This method ensures that the pool never becomes empty by validating feedback.
        """
        # Store the guess and feedback
        self.guess_history.append((guess, feedback))
        
        # Filter the remaining words based on feedback
        new_pool = []
        for word in self.remaining_words:
            if self.calculate_feedback(guess, word) == feedback:
                new_pool.append(word)
                
        # If the new pool is empty, it means the feedback was inconsistent
        # In this case, we keep the current pool but issue a warning
        if not new_pool:
            print("Warning: The feedback seems inconsistent with previous guesses. Continuing with current possibilities.")
            return
            
        # Update the remaining words
        self.remaining_words = new_pool
        
    def reset(self):
        """
        Reset the solver to its initial state.
        """
        self.remaining_words = list(self.all_words)
        self.guess_history = []

def get_user_feedback():
    """
    Gets and validates user feedback input.
    Returns a tuple of integers representing the feedback.
    """
    while True:
        print("\nEnter feedback for the guess: ")
        print("  - 0 for Gray (letter not in word)")
        print("  - 1 for Yellow (letter in word but wrong position)")
        print("  - 2 for Green (letter in correct position)")
        print("Example: 01020")
        feedback_str = input("Feedback: ").strip()
        
        # Validate input
        if len(feedback_str) != 5:
            print("Error: Feedback must be exactly 5 characters long.")
            continue
            
        if not all(c in '012' for c in feedback_str):
            print("Error: Feedback can only contain 0, 1, or 2.")
            continue
            
        # Convert to tuple of integers
        feedback = tuple(int(c) for c in feedback_str)
        return feedback

def main():
    """
    Main function to run the advanced Wordle solver.
    """
    print("Advanced Wordle Solver using Information Theory")
    print("==============================================")
    print("Think of a 5-letter word and I'll try to guess it!")
    print("After each guess, tell me the feedback using: ")
    print("  0 = Gray (letter not in word)")
    print("  1 = Yellow (letter in word but wrong position)")
    print("  2 = Green (letter in correct position)")
    print("\nLet's start!\n")
    
    # Initialize the solver
    solver = AdvancedWordleSolver()
    
    # Game loop
    for attempt in range(1, 7):  # Wordle allows 6 attempts
        # Get the best guess using advanced heuristics
        guess = solver.get_advanced_best_guess()
        
        # If no guess could be determined, something went wrong
        if guess is None:
            print("Error: Could not determine a guess. This shouldn't happen!")
            break
            
        print(f"\nAttempt {attempt}: Is the word '{guess.upper()}'?")
        
        # Get user feedback
        feedback = get_user_feedback()
        
        # Check for win condition
        if feedback == (2, 2, 2, 2, 2):
            print(f"\nSuccess! The word is '{guess.upper()}'!")
            print(f"Solved in {attempt} attempts.")
            break
            
        # Update the solver with the feedback
        solver.update_pool(guess, feedback)
        
        # Check if we've run out of possibilities
        if not solver.remaining_words:
            print("\nHmm, I've run out of possibilities. There might be an inconsistency in the feedback.")
            break
            
        # Show progress
        print(f"Remaining possibilities: {len(solver.remaining_words)}")
        
        # Show some possible words if there are few left
        if len(solver.remaining_words) <= 5 and len(solver.remaining_words) > 1:
            print("Possible words: " + ", ".join([w.upper() for w in solver.remaining_words]))
        
    else:
        # If we've used all attempts
        print("\nI'm out of attempts. I couldn't guess the word.")
        if solver.remaining_words:
            print(f"There were {len(solver.remaining_words)} possible words left: ")
            if len(solver.remaining_words) <= 10:
                print(", ".join(word.upper() for word in solver.remaining_words))
            else:
                print(", ".join(word.upper() for word in solver.remaining_words[:10]) + ", ...")
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
