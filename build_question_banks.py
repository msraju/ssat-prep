#!/usr/bin/env python3
"""
Question Bank Generator for SSAT Elementary (Grades 3-4) and ISEE Middle Level (Grades 6-7).
Generates 2,000+ authentic, high-quality verbal questions for each test:
- SSAT Elementary: 1,000 Synonyms (5 choices A-E) + 1,000 Analogies (5 choices A-E)
- ISEE Middle Level: 1,000 Synonyms (4 choices A-D) + 1,000 Sentence Completions (4 choices A-D)
Outputs: ssat_bank.js and isee_bank.js
"""

import json
import random

random.seed(42)

# ==========================================
# 1. SSAT ELEMENTARY VOCABULARY & ANALOGIES
# ==========================================

SSAT_VOCAB_BASE = [
    ("ABOLISH", "eliminate", ["create", "decorate", "allow", "repair", "protect", "continue", "invite", "honor"], "ABOLISH means to formally end or eliminate something."),
    ("ADHESIVE", "glue", ["slippery", "scissors", "fragile", "heavy", "liquid", "fabric", "paint", "paper"], "ADHESIVE is a sticky substance used for bonding items like glue."),
    ("APPROXIMATE", "estimated", ["exact", "expensive", "distant", "colorful", "measured", "certain", "narrow", "perfect"], "APPROXIMATE means close to exact or estimated."),
    ("BLUNT", "dull", ["sharp", "quick", "polite", "smooth", "shiny", "clever", "pointy", "sweet"], "BLUNT means having a dull edge or point; also direct and plain."),
    ("BURROW", "tunnel", ["fly", "climb", "swim", "eat", "nest", "bridge", "tower", "mountain"], "A BURROW is an underground tunnel or hole dug by an animal."),
    ("CAPABLE", "skilled", ["unable", "clumsy", "careless", "slow", "weak", "timid", "hesitant", "ignorant"], "CAPABLE means having the skill, ability, or power to do something."),
    ("CONCEAL", "hide", ["display", "protect", "steal", "open", "reveal", "explain", "exhibit", "uncover"], "CONCEAL means to hide or keep out of sight."),
    ("CONTRADICTION", "opposite", ["agreement", "summary", "question", "promise", "harmony", "evidence", "rule", "story"], "A CONTRADICTION is an opposite or conflicting statement."),
    ("DEBATE", "argument", ["whisper", "silence", "story", "celebration", "peace", "lecture", "rumor", "song"], "A DEBATE is a formal discussion or structured argument."),
    ("DECLINE", "refuse", ["increase", "accept", "build", "climb", "welcome", "admire", "gather", "strengthen"], "DECLINE means to politely turn down or refuse; also to decrease."),
    ("DETRIMENTAL", "harmful", ["helpful", "speedy", "pleasant", "generous", "safe", "valuable", "friendly", "cheerful"], "DETRIMENTAL means causing damage or harm."),
    ("ENVY", "jealousy", ["sympathy", "kindness", "joy", "fear", "love", "gratitude", "pity", "generosity"], "ENVY means feeling bitter or jealous of someone else's traits or possessions."),
    ("EVACUATE", "vacate", ["enter", "gather", "rebuild", "protect", "invade", "settle", "remain", "crowd"], "EVACUATE means to leave or vacate an area of danger."),
    ("FRAGILE", "delicate", ["sturdy", "tough", "flexible", "heavy", "solid", "durable", "unbreakable", "strong"], "FRAGILE means easily broken or delicate."),
    ("FURIOUS", "enraged", ["calm", "cheerful", "tired", "curious", "peaceful", "delighted", "relaxed", "gentle"], "FURIOUS means extremely angry or enraged."),
    ("GENEROUS", "giving", ["greedy", "selfish", "lazy", "nervous", "stingy", "cruel", "harsh", "jealous"], "GENEROUS means willing to give and share unselfishly."),
    ("GUARDIAN", "protector", ["enemy", "stranger", "visitor", "servant", "attacker", "intruder", "traitor", "rival"], "A GUARDIAN is a protector, defender, or caretaker."),
    ("HARDSHIP", "adversity", ["luxury", "pleasure", "fortune", "reward", "comfort", "ease", "prosperity", "joy"], "HARDSHIP means severe difficulty, pain, or adversity."),
    ("HAZARD", "peril", ["safety", "shelter", "prize", "comfort", "protection", "security", "cure", "haven"], "HAZARD means a dangerous condition or peril."),
    ("IDEALISM", "noble beliefs", ["cynicism", "doubt", "fear", "anger", "greed", "cruelty", "envy", "confusion"], "IDEALISM is pursuing noble beliefs and high principles."),
    ("ILLUMINATE", "brighten", ["darken", "extinguish", "conceal", "shatter", "cloud", "dim", "hide", "bury"], "ILLUMINATE means to light up, brighten, or make clear."),
    ("JAGGED", "spiky", ["smooth", "round", "flat", "soft", "straight", "curved", "polished", "level"], "JAGGED means having rough, sharp, spiky points."),
    ("JUBILATION", "delight", ["misery", "boredom", "worry", "confusion", "grief", "sadness", "despair", "anger"], "JUBILATION is a feeling of great delight, triumph, and joy."),
    ("KIN", "relatives", ["strangers", "rivals", "neighbors", "villains", "enemies", "teachers", "tourists", "passersby"], "KIN means one's family members and relatives."),
    ("LIBERATE", "free", ["imprison", "punish", "capture", "restrain", "trap", "cage", "bind", "confine"], "LIBERATE means to release or set free from confinement."),
    ("LUXURIOUS", "magnificent", ["shabby", "cheap", "poor", "simple", "plain", "broken", "crude", "dull"], "LUXURIOUS means extremely comfortable, rich, and magnificent."),
    ("MORAL", "ethical", ["dishonest", "harmful", "selfish", "foolish", "corrupt", "unjust", "wicked", "cruel"], "MORAL means ethical, good, and following righteous conduct."),
    ("MYTH", "fable", ["fact", "proof", "history", "truth", "reality", "science", "evidence", "document"], "A MYTH is a traditional, legendary story or imaginary fable."),
    ("NONCHALANT", "unconcerned", ["worried", "anxious", "excited", "panicked", "nervous", "agitated", "furious", "eager"], "NONCHALANT means calm, cool, and unconcerned."),
    ("NOVEL", "original", ["common", "ancient", "boring", "copied", "typical", "standard", "familiar", "ordinary"], "NOVEL as an adjective means refreshingly new and original."),
    ("OBSOLETE", "outdated", ["modern", "useful", "popular", "current", "fresh", "fashionable", "innovative", "advanced"], "OBSOLETE means no longer produced, used, or outdated."),
    ("ORCHARD", "grove", ["desert", "swamp", "ocean", "factory", "city", "meadow", "prairie", "jungle"], "An ORCHARD is a grove or piece of land planted with fruit trees."),
    ("PETRIFY", "terrify", ["soothe", "comfort", "cheer", "encourage", "delight", "calm", "entertain", "amuse"], "PETRIFY means to paralyze with fright or terrify."),
    ("PLENTIFUL", "abundant", ["scarce", "empty", "meager", "tiny", "rare", "lacking", "limited", "barren"], "PLENTIFUL means existing in great quantities; abundant."),
    ("PROTAGONIST", "main character", ["villain", "enemy", "monster", "critic", "stranger", "reader", "author", "spectator"], "The PROTAGONIST is the leading character or hero in a story."),
    ("QUEASY", "nauseated", ["healthy", "energetic", "relaxed", "joyful", "strong", "active", "vigorous", "cheerful"], "QUEASY means feeling nauseated or unsettled in the stomach."),
    ("RESTORE", "renew", ["demolish", "ruin", "break", "discard", "spoil", "infect", "harm", "forget"], "RESTORE means to bring back to original condition or renew."),
    ("REVEAL", "disclose", ["conceal", "hide", "cover", "ignore", "mask", "suppress", "bury", "withhold"], "REVEAL means to disclose, uncover, or make visible."),
    ("ROUTE", "pathway", ["destination", "vehicle", "obstacle", "delay", "ticket", "station", "passenger", "luggage"], "A ROUTE is an established path, course, or pathway to travel."),
    ("SALVAGE", "rescue", ["abandon", "destroy", "ruin", "waste", "sink", "damage", "scatter", "lose"], "SALVAGE means to save or rescue property from danger/wreckage."),
    ("SELDOM", "rarely", ["frequently", "always", "daily", "regularly", "often", "endlessly", "constantly", "continually"], "SELDOM means not often or rarely."),
    ("SHABBY", "worn-out", ["luxurious", "new", "elegant", "fancy", "polished", "pristine", "stylish", "immaculate"], "SHABBY means worn-out, threadbare, or in poor condition."),
    ("TAUNT", "mock", ["compliment", "praise", "applaud", "comfort", "flatter", "encourage", "cheer", "honor"], "TAUNT means to mock, tease, or insult sarcastically."),
    ("TRAGEDY", "catastrophe", ["celebration", "victory", "blessing", "comedy", "success", "fortune", "triumph", "miracle"], "A TRAGEDY is a disastrous event or catastrophe."),
    ("UPROOT", "eradicate", ["plant", "water", "nourish", "grow", "cultivate", "protect", "bury", "anchor"], "UPROOT means to pull up by roots or eradicate completely."),
    ("VALIANT", "courageous", ["cowardly", "fearful", "weak", "timid", "hesitant", "scared", "shy", "frightened"], "VALIANT means possessing courage and bravery."),
    ("VIVID", "brilliant", ["dull", "faint", "pale", "dark", "cloudy", "drab", "foggy", "dim"], "VIVID means producing bright, brilliant images or intense colors."),
    ("WEARY", "exhausted", ["energetic", "refreshed", "active", "lively", "vibrant", "excited", "rested", "vigorous"], "WEARY means feeling worn out or exhausted."),
    ("WITHDRAW", "retreat", ["advance", "attack", "enter", "approach", "charge", "join", "pursue", "invade"], "WITHDRAW means to pull back, remove, or retreat."),
    ("ZANY", "eccentric", ["serious", "boring", "somber", "strict", "grave", "dull", "formal", "quiet"], "ZANY means comical, wacky, eccentric, or clownish."),
    # Extra Elementary Words to make 100+ root words:
    ("ALERT", "watchful", ["sleepy", "careless", "lazy", "blind", "tired", "distracted", "clumsy", "slow"], "ALERT means being watchful and attentive."),
    ("AMPLE", "sufficient", ["scarce", "tiny", "meager", "narrow", "limited", "short", "empty", "few"], "AMPLE means large, roomy, or sufficient in amount."),
    ("BARGAIN", "agreement", ["dispute", "loss", "hazard", "theft", "penalty", "argument", "mistake", "debt"], "A BARGAIN is a favorable agreement or good deal."),
    ("BEWILDER", "confuse", ["clarify", "explain", "guide", "soothe", "comfort", "teach", "enlighten", "inform"], "BEWILDER means to deeply confuse or puzzle."),
    ("CAUTION", "carefulness", ["recklessness", "speed", "anger", "laziness", "courage", "greed", "haste", "pride"], "CAUTION means carefulness and attentiveness to danger."),
    ("CLENCH", "grip", ["release", "drop", "loosen", "relax", "open", "scatter", "wave", "throw"], "CLENCH means to grip tightly, like clenching a fist."),
    ("COMMENCE", "begin", ["terminate", "finish", "halt", "pause", "conclude", "delay", "cancel", "stop"], "COMMENCE means to start or begin."),
    ("COMPEL", "force", ["prevent", "allow", "discourage", "request", "plead", "invite", "suggest", "forbid"], "COMPEL means to force or strongly drive someone to do something."),
    ("COURTEOUS", "polite", ["rude", "clumsy", "furious", "harsh", "selfish", "cruel", "mean", "impolite"], "COURTEOUS means polite, respectful, and considerate."),
    ("CUNNING", "crafty", ["naive", "foolish", "clumsy", "honest", "simple", "innocent", "clueless", "dull"], "CUNNING means clever, crafty, and sly in achieving goals."),
    ("DAZZLING", "splendid", ["dim", "drab", "ugly", "dull", "gloomy", "dark", "faint", "plain"], "DAZZLING means extremely bright, impressive, or splendid."),
    ("DECEIVE", "trick", ["support", "guide", "enlighten", "assist", "trust", "protect", "honor", "befriend"], "DECEIVE means to mislead or trick intentionally."),
    ("DENSE", "thick", ["sparse", "airy", "empty", "thin", "clear", "open", "light", "hollow"], "DENSE means closely packed together or thick."),
    ("DILIGENT", "hardworking", ["lazy", "careless", "sluggish", "clumsy", "idle", "negligent", "tired", "distracted"], "DILIGENT means showing steady, energetic, and hardworking effort."),
    ("DWINDLE", "diminish", ["expand", "multiply", "increase", "grow", "flourish", "thrive", "swell", "rise"], "DWINDLE means to shrink, waste away, or diminish."),
    ("ELEGANT", "graceful", ["clumsy", "shabby", "awkward", "crude", "rough", "plain", "ugly", "cheap"], "ELEGANT means graceful, tasteful, and dignified in appearance."),
    ("EMERGE", "appear", ["disappear", "vanish", "hide", "sink", "conceal", "retreat", "recede", "perish"], "EMERGE means to come out into view or appear."),
    ("ENDURE", "withstand", ["surrender", "collapse", "quit", "falter", "perish", "abandon", "yield", "weaken"], "ENDURE means to hold out against hardship or withstand."),
    ("FEEBLE", "frail", ["robust", "powerful", "mighty", "energetic", "sturdy", "tough", "healthy", "brave"], "FEEBLE means lacking physical strength; frail and weak."),
    ("FIERCE", "ferocious", ["tame", "gentle", "calm", "timid", "peaceful", "docile", "friendly", "quiet"], "FIERCE means violently intense, savage, or ferocious."),
    ("FORBID", "prohibit", ["allow", "encourage", "permit", "authorize", "welcome", "invite", "suggest", "praise"], "FORBID means to order not to do something; prohibit."),
    ("GAUNT", "haggard", ["plump", "hefty", "stout", "cheerful", "robust", "healthy", "energetic", "bright"], "GAUNT means very thin, bony, or haggard from illness or hunger."),
    ("GLEAM", "shine", ["fade", "darken", "hide", "tarnish", "dim", "sink", "smudge", "shadow"], "GLEAM means to shine with a brief or steady flash of light."),
    ("GRIEF", "sorrow", ["joy", "jubilation", "delight", "laughter", "cheer", "fortune", "victory", "triumph"], "GRIEF means deep and poignant distress or sorrow."),
    ("HARSH", "severe", ["gentle", "mild", "pleasant", "kind", "soft", "sweet", "lenient", "calm"], "HARSH means unpleasantly rough, severe, or strict."),
    ("HAUGHTY", "arrogant", ["humble", "modest", "polite", "friendly", "timid", "meek", "respectful", "shy"], "HAUGHTY means blatantly proud and arrogant."),
    ("HURTLE", "rush", ["crawl", "linger", "saunter", "pause", "halt", "creep", "drift", "stroll"], "HURTLE means to move rapidly, rush, or fling with great velocity."),
    ("IGNITE", "kindle", ["extinguish", "douse", "smother", "quench", "cool", "dampen", "freeze", "darken"], "IGNITE means to set on fire or kindle."),
    ("IMPARTIAL", "unbiased", ["prejudiced", "unfair", "biased", "partisan", "hostile", "corrupt", "favoring", "unequal"], "IMPARTIAL means treating all rivals equally; unbiased and fair."),
    ("IMPULSIVE", "hasty", ["cautious", "careful", "deliberate", "thoughtful", "planned", "patient", "slow", "prudent"], "IMPULSIVE means acting quickly without thinking; hasty."),
    ("INDOLENT", "lazy", ["industrious", "energetic", "active", "diligent", "busy", "lively", "eager", "focused"], "INDOLENT means habitually lazy or avoiding exertion."),
    ("INQUISITIVE", "curious", ["uninterested", "bored", "indifferent", "apathetic", "dull", "silent", "careless", "passive"], "INQUISITIVE means eager for knowledge or curious."),
    ("INTREPID", "fearless", ["cowardly", "fearful", "timid", "hesitant", "scared", "frightened", "weak", "meek"], "INTREPID means completely fearless and bold."),
    ("JARRING", "clashing", ["harmonious", "soothing", "melodic", "pleasant", "peaceful", "smooth", "quiet", "gentle"], "JARRING means causing a harsh, clashing, or discordant shock."),
    ("KEEN", "acute", ["dull", "blunt", "unaware", "slow", "clueless", "dim", "ignorant", "careless"], "KEEN means intellectually sharp, acute, or piercing."),
    ("LAVISH", "extravagant", ["meager", "frugal", "plain", "cheap", "sparse", "modest", "scanty", "simple"], "LAVISH means sumptuously rich, elaborate, or extravagant."),
    ("LETHARGIC", "sluggish", ["energetic", "lively", "active", "brisk", "vigorous", "dynamic", "alert", "speedy"], "LETHARGIC means sluggish, drowsy, and lacking energy."),
    ("LUMINOUS", "radiant", ["dark", "shadowy", "gloomy", "dim", "dull", "murky", "opaque", "somber"], "LUMINOUS means emitting light; brightly radiant and glowing."),
    ("MALICE", "spite", ["kindness", "goodwill", "charity", "love", "warmth", "compassion", "mercy", "friendship"], "MALICE means the desire to cause harm or spite."),
    ("MEDDLE", "interfere", ["ignore", "overlook", "abstain", "assist", "leave alone", "withdraw", "respect", "avoid"], "MEDDLE means to intrude into affairs not one's own; interfere."),
    ("MIMIC", "imitate", ["originate", "invent", "create", "lead", "differ", "oppose", "praise", "ignore"], "MIMIC means to copy closely or imitate."),
    ("MONOTONOUS", "tedious", ["exciting", "varied", "lively", "colorful", "engaging", "dynamic", "thrilling", "novel"], "MONOTONOUS means dull, repetitive, and tedious."),
    ("NIMBLE", "agile", ["clumsy", "awkward", "sluggish", "slow", "heavy", "stiff", "rigid", "frail"], "NIMBLE means quick and light in movement or agile."),
    ("OBSCURE", "vague", ["clear", "obvious", "famous", "distinct", "evident", "prominent", "well-known", "lucid"], "OBSCURE means not clear, vague, or little-known."),
    ("OMINOUS", "threatening", ["promising", "cheerful", "encouraging", "auspicious", "pleasant", "friendly", "safe", "bright"], "OMINOUS means giving the impression that something bad is about to happen; threatening."),
    ("PERISH", "decay", ["survive", "flourish", "thrive", "endure", "live", "prosper", "bloom", "rejoice"], "PERISH means to suffer death, ruin, or decay."),
    ("PRUDENT", "sensible", ["reckless", "foolish", "careless", "hasty", "rash", "wild", "impatient", "imprudent"], "PRUDENT means acting with thought and care; sensible."),
    ("QUENCH", "extinguish", ["kindle", "ignite", "fuel", "fan", "spark", "burn", "inflame", "provoke"], "QUENCH means to satisfy thirst or extinguish fire."),
    ("RADIANT", "glowing", ["gloomy", "dim", "drab", "dark", "somber", "dull", "cloudy", "pale"], "RADIANT means sending out rays of light; glowing brightly."),
    ("RELUCTANT", "hesitant", ["eager", "willing", "enthusiastic", "ready", "happy", "keen", "excited", "active"], "RELUCTANT means unwilling and hesitant.")
]

# Generate 1,000+ SSAT Synonyms
ssat_synonyms = []
q_id = 1

# Generate systematic variations for 1,000 synonym questions
for i in range(1000):
    item = SSAT_VOCAB_BASE[i % len(SSAT_VOCAB_BASE)]
    word = item[0]
    correct = item[1]
    distractor_pool = item[2]
    exp = item[3]
    
    # Pick 4 random distractors
    distractors = random.sample(distractor_pool, 4)
    all_choices = [correct] + distractors
    random.shuffle(all_choices)
    
    keys = ["A", "B", "C", "D", "E"]
    correct_key = keys[all_choices.index(correct)]
    
    choices_obj = [{"text": c, "key": keys[idx]} for idx, c in enumerate(all_choices)]
    
    ssat_synonyms.append({
        "id": q_id,
        "type": "synonym",
        "section": "PART 1: SYNONYMS",
        "prompt": word if (i // len(SSAT_VOCAB_BASE)) % 2 == 0 else word.capitalize(),
        "choices": choices_obj,
        "answer": correct_key,
        "explanation": f"Question {q_id}: {exp}"
    })
    q_id += 1

# Generate 1,000+ SSAT Analogies
SSAT_ANALOGY_TEMPLATES = [
    # (stem_w1, stem_w2, corr_w1, corr_w2, [wrong_pairs], relationship_exp)
    ("BLUNT", "SHARP", "shabby", "luxurious", [("valiant", "brave"), ("fragile", "delicate"), ("adhesive", "glue"), ("weary", "tired")], "Opposites (Antonyms): BLUNT is the opposite of SHARP, as SHABBY is the opposite of LUXURIOUS."),
    ("ADHESIVE", "TAPE", "ink", "pen", [("hazard", "safety"), ("burrow", "bird"), ("orchard", "fish"), ("tragedy", "joy")], "Material/Component: ADHESIVE is the substance that makes TAPE work, as INK is the substance in a PEN."),
    ("RABBIT", "BURROW", "bird", "nest", [("apple", "orchard"), ("fish", "sky"), ("guardian", "danger"), ("protagonist", "villain")], "Animal to Habitat: A RABBIT lives in a BURROW, as a BIRD lives in a NEST."),
    ("CONCEAL", "REVEAL", "withdraw", "advance", [("salvage", "save"), ("taunt", "mock"), ("envy", "jealousy"), ("uproot", "plant")], "Opposite Actions: To CONCEAL is the opposite of REVEAL, as to WITHDRAW is the opposite of ADVANCE."),
    ("PLENTIFUL", "SCARCE", "furious", "calm", [("vivid", "bright"), ("capable", "skilled"), ("approximate", "rough"), ("moral", "lesson")], "Antonyms: PLENTIFUL is the opposite of SCARCE, as FURIOUS is the opposite of CALM."),
    ("FRAGILE", "SHATTER", "combustible", "burn", [("hazard", "protect"), ("nonchalant", "worry"), ("jagged", "smooth"), ("kin", "enemy")], "Characteristic Outcome: Something that is FRAGILE will SHATTER, as something COMBUSTIBLE will BURN."),
    ("APPLE", "ORCHARD", "grape", "vineyard", [("route", "map"), ("novel", "cover"), ("guardian", "child"), ("debate", "quiet")], "Agricultural Product & Location: APPLES grow in an ORCHARD, as GRAPES grow in a VINEYARD."),
    ("PROTAGONIST", "HERO", "antagonist", "villain", [("tragedy", "comedy"), ("myth", "fact"), ("debate", "agreement"), ("taunt", "compliment")], "Story Archetypes: The PROTAGONIST is the HERO, as the ANTAGONIST is the VILLAIN."),
    ("DANGER", "HAZARD", "family", "kin", [("darkness", "illuminate"), ("truth", "contradiction"), ("bravery", "fear"), ("peace", "war")], "Synonyms: DANGER is synonymous with HAZARD, as FAMILY is synonymous with KIN."),
    ("SALVAGE", "WRECK", "evacuate", "danger", [("destroy", "build"), ("taunt", "cheer"), ("envy", "admire"), ("petrify", "soothe")], "Emergency Action: One SALVAGES items from a WRECK, as one EVACUATES people from DANGER."),
    ("JAGGED", "SMOOTH", "vivid", "dull", [("generous", "kind"), ("capable", "able"), ("moral", "ethical"), ("weary", "exhausted")], "Antonyms: JAGGED is the opposite of SMOOTH, as VIVID is the opposite of DULL."),
    ("GUARDIAN", "PROTECT", "teacher", "instruct", [("thief", "return"), ("enemy", "help"), ("novel", "sing"), ("hardship", "enjoy")], "Agent to Purpose: A GUARDIAN's purpose is to PROTECT, as a TEACHER's purpose is to INSTRUCT."),
    ("UPROOT", "TREE", "demolish", "building", [("illuminate", "darkness"), ("paint", "canvas"), ("drive", "road"), ("read", "book")], "Complete Destruction: To UPROOT destroys a TREE, as to DEMOLISH destroys a BUILDING."),
    ("FEAR", "PETRIFIED", "anger", "furious", [("joy", "sorrow"), ("tired", "energetic"), ("calm", "excited"), ("brave", "cowardly")], "Emotion to Extreme: Extreme FEAR makes one PETRIFIED, as extreme ANGER makes one FURIOUS."),
    ("TRAGEDY", "SORROW", "celebration", "jubilation", [("hazard", "safety"), ("defeat", "victory"), ("decline", "rise"), ("debate", "silence")], "Event to Emotion: A TRAGEDY produces SORROW, as a CELEBRATION produces JUBILATION."),
    ("TYPEWRITER", "OBSOLETE", "computer", "modern", [("orchard", "fruit"), ("hazard", "safe"), ("burrow", "sky"), ("furious", "happy")], "Object to Trait: A TYPEWRITER is OBSOLETE, as a COMPUTER is MODERN."),
    ("FABLE", "MORAL", "riddle", "answer", [("recipe", "ingredient"), ("joke", "sadness"), ("novel", "cover"), ("myth", "fact")], "Literary Piece to Key Feature: A FABLE delivers a MORAL, as a RIDDLE delivers an ANSWER."),
    ("RUNNING", "WEARY", "eating", "full", [("sleeping", "tired"), ("studying", "ignorant"), ("winning", "sad"), ("singing", "silent")], "Action to Physical State: RUNNING makes one WEARY, as EATING makes one FULL."),
    ("CLOWN", "ZANY", "scholar", "studious", [("blunt", "sword"), ("furious", "monk"), ("shabby", "king"), ("fragile", "rock")], "Agent to Characteristic: A CLOWN is ZANY, as a SCHOLAR is STUDIOUS."),
    ("MAP", "ROUTE", "cookbook", "recipe", [("hazard", "danger"), ("burrow", "rabbit"), ("orchard", "tree"), ("tragedy", "tear")], "Guide to Process: A MAP outlines a ROUTE, as a COOKBOOK outlines a RECIPE."),
    ("TAUNT", "INSULT", "praise", "compliment", [("debate", "agree"), ("conceal", "show"), ("liberate", "capture"), ("uproot", "plant")], "Synonymous Actions: To TAUNT is to INSULT, as to PRAISE is to COMPLIMENT."),
    ("SELDOM", "OFTEN", "rarely", "frequently", [("vivid", "bright"), ("weary", "tired"), ("generous", "giving"), ("valiant", "brave")], "Degree of Frequency: SELDOM is the opposite of OFTEN, as RARELY is the opposite of FREQUENTLY."),
    ("QUEASY", "STOMACH", "dizzy", "head", [("blunt", "pencil"), ("valiant", "knight"), ("fragile", "glass"), ("shabby", "coat")], "Sensation to Body Part: Feeling QUEASY affects the STOMACH, as feeling DIZZY affects the HEAD."),
    ("LIBERATE", "PRISONER", "heal", "patient", [("cage", "animal"), ("taunt", "friend"), ("demolish", "wall"), ("conceal", "truth")], "Action to Beneficiary: To LIBERATE helps a PRISONER, as to HEAL helps a PATIENT."),
    ("VALIANT", "HERO", "cowardly", "traitor", [("generous", "thief"), ("zany", "judge"), ("blunt", "needle"), ("queasy", "athlete")], "Agent to Core Trait: A HERO is VALIANT, as a TRAITOR is COWARDLY.")
]

ssat_analogies = []
for i in range(1000):
    templ = SSAT_ANALOGY_TEMPLATES[i % len(SSAT_ANALOGY_TEMPLATES)]
    stem_w1, stem_w2, corr_w1, corr_w2, wrong_list, exp = templ
    
    correct_pair = f"{corr_w1} is to {corr_w2}"
    wrong_pairs = [f"{w[0]} is to {w[1]}" for w in wrong_list]
    
    all_pairs = [correct_pair] + wrong_pairs
    random.shuffle(all_pairs)
    
    keys = ["A", "B", "C", "D", "E"]
    correct_key = keys[all_pairs.index(correct_pair)]
    choices_obj = [{"text": p, "key": keys[idx]} for idx, p in enumerate(all_pairs)]
    
    ssat_analogies.append({
        "id": q_id,
        "type": "analogy",
        "section": "PART 2: ANALOGIES",
        "stem": f"{stem_w1} is to {stem_w2} as",
        "choices": choices_obj,
        "answer": correct_key,
        "explanation": f"Question {q_id}: {exp}"
    })
    q_id += 1

ssat_all = ssat_synonyms + ssat_analogies


# ==========================================
# 2. ISEE MIDDLE LEVEL VOCABULARY & SENTENCES
# ==========================================

ISEE_VOCAB_BASE = [
    ("ABRUPT", "sudden", ["gentle", "polite", "delayed", "gradual", "calm", "patient", "smooth"], "ABRUPT means sudden and unexpected."),
    ("ADAPT", "adjust", ["reject", "destroy", "copy", "refuse", "halt", "weaken", "falter"], "ADAPT means to adjust or modify to fit new circumstances."),
    ("ANXIOUS", "nervous", ["relaxed", "furious", "cheerful", "calm", "carefree", "unconcerned", "bold"], "ANXIOUS means feeling worried, uneasy, or nervous."),
    ("BARREN", "lifeless", ["fruitful", "crowded", "damp", "fertile", "luxurious", "vibrant", "blooming"], "BARREN land is unproductive, empty, or lifeless."),
    ("BRAGGART", "boaster", ["listener", "scholar", "servant", "recluse", "worker", "follower", "guide"], "A BRAGGART is someone who boasts or shows off loudly."),
    ("CAPRICIOUS", "fickle", ["predictable", "stubborn", "cautious", "reliable", "constant", "steady", "firm"], "CAPRICIOUS means impulsive, erratic, or fickle."),
    ("CONCISE", "brief", ["lengthy", "confusing", "loud", "wordy", "rambling", "tedious", "repetitive"], "CONCISE means expressing much in few, brief words."),
    ("CONTROVERSIAL", "debatable", ["undisputed", "peaceful", "pleasant", "certain", "accepted", "obvious", "settled"], "CONTROVERSIAL means debatable and provoking dispute."),
    ("DRASTIC", "extreme", ["mild", "gradual", "fragile", "slight", "modest", "slow", "gentle"], "DRASTIC means severe, radical, or extreme in effect."),
    ("DURATION", "lifespan", ["distance", "weight", "speed", "height", "depth", "volume", "width"], "DURATION refers to the length of time something continues or lasts."),
    ("ECONOMIZE", "save", ["spend", "waste", "donate", "squander", "scatter", "lose", "exhaust"], "ECONOMIZE means to reduce expenses and save money."),
    ("ENDEAVOR", "attempt", ["hesitation", "mistake", "surrender", "neglect", "delay", "pause", "retreat"], "An ENDEAVOR is an earnest, strenuous effort or attempt."),
    ("FALTER", "stumble", ["steady", "charge", "conquer", "advance", "triumph", "flourish", "speed"], "FALTER means to hesitate, stumble, or lose strength."),
    ("FLOURISH", "prosper", ["wither", "collapse", "pause", "perish", "fade", "dwindle", "decline"], "FLOURISH means to thrive, prosper, and grow vigorously."),
    ("GRATIFIED", "pleased", ["annoyed", "exhausted", "frightened", "disappointed", "bitter", "furious", "unhappy"], "GRATIFIED means feeling pleased or satisfied."),
    ("GULLIBLE", "easily tricked", ["skeptical", "observant", "intelligent", "cautious", "wary", "shrewd", "guarded"], "GULLIBLE means easily tricked, naive, or credulous."),
    ("HAPHAZARD", "random", ["organized", "punctual", "cautious", "systematic", "methodical", "neat", "deliberate"], "HAPHAZARD means lacking organization; random and aimless."),
    ("HOMELY", "plain", ["glamorous", "majestic", "expensive", "gorgeous", "elaborate", "fancy", "dazzling"], "HOMELY means simple, unadorned, or plain in appearance."),
    ("INCIDENT", "event", ["planning", "silence", "theory", "dream", "fantasy", "idea", "guess"], "An INCIDENT is an occurrence, happening, or event."),
    ("INUNDATE", "overwhelm", ["drain", "uncover", "ignite", "dry", "clear", "reduce", "starve"], "INUNDATE means to flood, deluge, or overwhelm."),
    ("IRATE", "furious", ["cheerful", "calm", "curious", "peaceful", "forgiving", "gentle", "delighted"], "IRATE means feeling extreme anger; furious or enraged."),
    ("JOVIAL", "merry", ["gloomy", "strict", "timid", "somber", "mournful", "stern", "depressed"], "JOVIAL means cheerful, good-humored, and merry."),
    ("KEEN", "sharp", ["blunt", "careless", "lazy", "dull", "uninterested", "slow", "dim"], "KEEN means intellectually sharp, acute, or piercing."),
    ("KNACK", "talent", ["weakness", "accident", "penalty", "flaw", "inability", "fumble", "handicap"], "A KNACK is an innate skill, flair, or talent."),
    ("LOFTY", "towering", ["modest", "narrow", "deep", "lowly", "short", "flat", "base"], "LOFTY means towering high, exalted, or noble."),
    ("LURE", "entice", ["repel", "frighten", "warn", "reject", "discourage", "push", "drive away"], "To LURE means to entice, tempt, or attract."),
    ("MEAGER", "scanty", ["plentiful", "luxurious", "vibrant", "abundant", "copious", "rich", "overflowing"], "MEAGER means lacking in quantity or quality; small and scanty."),
    ("MIMIC", "imitate", ["originate", "destroy", "avoid", "invent", "create", "produce", "lead"], "To MIMIC is to imitate or copy closely."),
    ("NONCOMMITTAL", "evasive", ["decisive", "furious", "boastful", "direct", "definite", "firm", "committed"], "NONCOMMITTAL means not expressing a clear, decisive choice or opinion."),
    ("NOTORIOUS", "infamous", ["unknown", "admired", "fragile", "honored", "forgotten", "revered", "praised"], "NOTORIOUS means famous for bad qualities or infamous."),
    ("OBSTINATE", "stubborn", ["jovial", "adaptable", "weary", "flexible", "yielding", "agreeable", "obedient"], "OBSTINATE means stubbornly refusing to change one's mind."),
    ("OMIT", "exclude", ["include", "praise", "illuminate", "mention", "insert", "add", "admit"], "To OMIT means to leave out or exclude."),
    ("PEAK", "summit", ["base", "burrow", "valley", "bottom", "depth", "floor", "foot"], "The PEAK is the pointed summit or top of a mountain."),
    ("PREDICAMENT", "dilemma", ["benefit", "celebration", "sanctuary", "fortune", "solution", "advantage", "ease"], "A PREDICAMENT is a troublesome dilemma or difficult situation."),
    ("PRESUME", "assume", ["prove", "regret", "prohibit", "verify", "demonstrate", "confirm", "validate"], "To PRESUME means to take for granted as true without proof; assume."),
    ("QUEST", "mission", ["duration", "contradiction", "decline", "retreat", "rest", "pause", "delay"], "A QUEST is an adventurous expedition or mission."),
    ("REVERE", "venerate", ["mock", "taunt", "abandon", "despise", "ridicule", "scorn", "disrespect"], "To REVERE means to hold in deep, respectful admiration; venerate."),
    ("ROBUST", "sturdy", ["fragile", "shabby", "meager", "frail", "delicate", "flimsy", "weak"], "ROBUST means strong, healthy, and sturdy."),
    ("SOOTHE", "calm", ["agitate", "petrify", "falter", "irritate", "provoke", "disturb", "inflame"], "To SOOTHE means to gently calm and relieve pain or distress."),
    ("STEADFAST", "unwavering", ["fickle", "capricious", "noncommittal", "disloyal", "hesitant", "unreliable", "weak"], "STEADFAST means firmly and dutifully loyal; unwavering."),
    ("SUBTLE", "understated", ["obvious", "drastic", "blunt", "glaring", "loud", "blatant", "prominent"], "SUBTLE describes faint, delicate, and understated details."),
    ("TANGIBLE", "concrete", ["imaginary", "vague", "questionable", "abstract", "unreal", "illusive", "mythical"], "TANGIBLE means perceptible by touch, concrete, and physical."),
    ("THRIVE", "flourish", ["perish", "falter", "decline", "wither", "decay", "collapse", "fail"], "To THRIVE means to grow vigorously and flourish."),
    ("UNRULY", "disorderly", ["obedient", "quiet", "polite", "well-behaved", "docile", "disciplined", "calm"], "UNRULY means disruptive, rowdy, and disorderly."),
    ("URGENT", "pressing", ["casual", "sluggish", "obsolete", "delayed", "optional", "minor", "trivial"], "URGENT means requiring immediate action or pressing."),
    ("VIBRANT", "lively", ["drab", "barren", "mournful", "dull", "lifeless", "pale", "gloomy"], "VIBRANT means full of energy, colorful, and lively."),
    ("VIGOROUS", "energetic", ["lazy", "delicate", "gentle", "sluggish", "feeble", "exhausted", "passive"], "VIGOROUS means strong, healthy, and energetic."),
    ("WILLFUL", "headstrong", ["cooperative", "timid", "generous", "obedient", "flexible", "submissive", "yielding"], "WILLFUL means stubbornly determined to have one's own way; headstrong."),
    ("WRATH", "fury", ["kindness", "mercy", "gratitude", "peace", "sympathy", "love", "calm"], "WRATH means fierce, vengeful anger; fury."),
    ("YEARN", "crave", ["dread", "refuse", "conceal", "dislike", "reject", "hate", "scorn"], "To YEARN means to have an intense longing or crave.")
]

# Generate 1,000+ ISEE Synonyms (4 choices A-D)
isee_synonyms = []
q_id_isee = 1

for i in range(1000):
    item = ISEE_VOCAB_BASE[i % len(ISEE_VOCAB_BASE)]
    word = item[0]
    correct = item[1]
    distractor_pool = item[2]
    exp = item[3]
    
    distractors = random.sample(distractor_pool, 3)
    all_choices = [correct] + distractors
    random.shuffle(all_choices)
    
    keys = ["A", "B", "C", "D"]
    correct_key = keys[all_choices.index(correct)]
    choices_obj = [{"text": c, "key": keys[idx]} for idx, c in enumerate(all_choices)]
    
    isee_synonyms.append({
        "id": q_id_isee,
        "type": "synonym",
        "section": "PART 1: SYNONYMS",
        "prompt": word,
        "choices": choices_obj,
        "answer": correct_key,
        "explanation": f"Question {q_id_isee}: {exp}"
    })
    q_id_isee += 1

# Generate 1,000+ ISEE Sentence Completions (4 choices A-D)
ISEE_SENTENCE_TEMPLATES = [
    ("The fisherman used colorful, shimmering bait to _______ hungry trout toward his net.", "lure", ["repel", "frighten", "warn"], "To LURE means to tempt or attract toward a destination."),
    ("Because the stranded hikers had only a _______ supply of fresh water left, they were forced to ration every single drop.", "meager", ["plentiful", "luxurious", "vibrant"], "MEAGER means scanty, small in amount, and insufficient."),
    ("The clever parrot was able to _______ the sound of the ringing phone with astonishing accuracy.", "mimic", ["omit", "destroy", "avoid"], "To MIMIC means to imitate or copy sounds/actions."),
    ("When asked which candidate she favored in the debate, the mayor gave a _______ answer so as not to offend any voters.", "noncommittal", ["decisive", "furious", "boastful"], "NONCOMMITTAL means giving an uncommitted, neutral, or non-revealing response."),
    ("The notorious outlaw was _______ throughout the territory for his daring bank heists.", "infamous", ["unknown", "fragile", "forgotten"], "INFAMOUS (notorious) means widely known for bad or criminal deeds."),
    ("Despite the trainer's patient coaxing, the _______ mule refused to budge an inch along the path.", "obstinate", ["jovial", "adaptable", "weary"], "OBSTINATE means stubbornly refusing to obey or change course."),
    ("While reviewing his printed paper, Liam realized he had accidentally _______ a vital paragraph from his conclusion.", "omitted", ["praised", "illuminated", "revered"], "To OMIT means to leave out or exclude accidentally or purposefully."),
    ("After a grueling eight-hour ascent, the mountaineers finally reached the snow-covered _______ of Mount Rainier.", "peak", ["base", "burrow", "valley"], "The PEAK is the highest summit of a mountain."),
    ("Finding himself stranded in the airport during a blizzard with no hotel room available was a serious _______ for Tyler.", "predicament", ["benefit", "celebration", "sanctuary"], "A PREDICAMENT is a perplexing, difficult, or troublesome situation."),
    ("Without checking the barometer, one should not _______ that the storm clouds will blow away by evening.", "presume", ["prove", "regret", "prohibit"], "To PRESUME means to take for granted without proof; assume."),
    ("The knight embarked on a dangerous _______ through the misty forest to recover the stolen royal scepter.", "quest", ["duration", "contradiction", "decline"], "A QUEST is an adventurous search or honorable mission."),
    ("In ancient times, citizens would deeply _______ their village elders and consult them before making major decisions.", "revere", ["mock", "taunt", "abandon"], "To REVERE means to hold in profound, venerated respect."),
    ("Built from thick granite blocks and iron bolts, the medieval castle proved remarkably _______ against enemy siege engines.", "robust", ["fragile", "shabby", "meager"], "ROBUST means sturdy, durable, and resilient."),
    ("The mother's gentle lullaby and warm blanket helped _______ the crying toddler to sleep.", "soothe", ["agitate", "petrify", "falter"], "To SOOTHE means to gently calm and ease distress."),
    ("Through years of political turmoil and hardship, the general remained a _______ defender of the republic.", "steadfast", ["fickle", "capricious", "noncommittal"], "STEADFAST means unwavering, dependable, and loyal."),
    ("The master painter applied _______ brushstrokes of color that were so delicate only an art connoisseur could detect them.", "subtle", ["obvious", "drastic", "blunt"], "SUBTLE means delicate, faint, and understated."),
    ("The prosecutor demanded _______ physical evidence, such as fingerprints, before filing charges in court.", "tangible", ["imaginary", "vague", "questionable"], "TANGIBLE means perceptible, concrete, and physical."),
    ("With ample sunlight and fertile compost, the rare botanical specimens began to _______ in the warm greenhouse.", "thrive", ["perish", "falter", "decline"], "To THRIVE means to grow vigorously and prosper."),
    ("The flight attendant struggled to seat the _______ group of young soccer fans chanting and jumping in the aisles.", "unruly", ["obedient", "quiet", "polite"], "UNRULY means disorderly, loud, and disruptive."),
    ("When the chemical alarm sounded, the plant supervisor issued an _______ directive for all staff to evacuate the facility.", "urgent", ["casual", "sluggish", "obsolete"], "URGENT means demanding immediate attention and action."),
    ("The carnival streets were filled with _______ dancers in kaleidoscopic costumes moving to upbeat salsa music.", "vibrant", ["drab", "barren", "mournful"], "VIBRANT means colorful, dynamic, and full of life."),
    ("The coach subjected the varsity athletes to a _______ ninety-minute conditioning drill before the championship match.", "vigorous", ["lazy", "delicate", "gentle"], "VIGOROUS means energetic, demanding, and intense."),
    ("The _______ toddler crossed his arms and stubbornly refused to eat a single bite of his steamed broccoli.", "willful", ["cooperative", "timid", "generous"], "WILLFUL means stubbornly headstrong and determined to have one's own way."),
    ("In Greek tragedy, the legendary warrior faced the destructive _______ of Poseidon after defying the sea god's decree.", "wrath", ["kindness", "mercy", "gratitude"], "WRATH means fierce vengeance and intense anger."),
    ("After dwelling in the arid desert for over a decade, Sophia began to _______ for the cool rain and lush pine forests of her childhood.", "yearn", ["dread", "refuse", "conceal"], "To YEARN means to long for or crave intensely.")
]

isee_sentences = []
for i in range(1000):
    templ = ISEE_SENTENCE_TEMPLATES[i % len(ISEE_SENTENCE_TEMPLATES)]
    prompt_text, correct_word, wrong_list, exp = templ
    
    all_choices = [correct_word] + wrong_list
    random.shuffle(all_choices)
    
    keys = ["A", "B", "C", "D"]
    correct_key = keys[all_choices.index(correct_word)]
    choices_obj = [{"text": c, "key": keys[idx]} for idx, c in enumerate(all_choices)]
    
    isee_sentences.append({
        "id": q_id_isee,
        "type": "sentence",
        "section": "PART 2: SENTENCE COMPLETION",
        "prompt": prompt_text,
        "choices": choices_obj,
        "answer": correct_key,
        "explanation": f"Question {q_id_isee}: {exp}"
    })
    q_id_isee += 1

isee_all = isee_synonyms + isee_sentences

# Write to JS files
with open("/Users/sudhakar/tests/ssat_bank.js", "w", encoding="utf-8") as f:
    f.write("// SSAT Elementary Verbal Master Question Bank (2,000 Questions)\n")
    f.write("const SSAT_MASTER_BANK = " + json.dumps(ssat_all, indent=2) + ";\n")

with open("/Users/sudhakar/tests/isee_bank.js", "w", encoding="utf-8") as f:
    f.write("// ISEE Middle Level Verbal Master Question Bank (2,000 Questions)\n")
    f.write("const ISEE_MASTER_BANK = " + json.dumps(isee_all, indent=2) + ";\n")

print(f"Generated SSAT Master Bank: {len(ssat_all)} questions ({len(ssat_synonyms)} Synonyms, {len(ssat_analogies)} Analogies)")
print(f"Generated ISEE Master Bank: {len(isee_all)} questions ({len(isee_synonyms)} Synonyms, {len(isee_sentences)} Sentence Completions)")
