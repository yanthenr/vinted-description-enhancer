from translate import Translator

input_file = "description_sample.txt"
description = "description_sample.txt"
tags = "tags_sample.txt"


def Translate(description, original_lang, translated_lang):
    t = Translator(from_lang=original_lang, to_lang=translated_lang)
    translation = t.translate(description)
    return translation

def GenerateDescription(description, tags, original_lang, target_languages):
    final_description = description
    translated_descriptions = {}

    # Translate for all languages except original_lang
    for target_language in target_languages:
        if target_language != original_lang:
            translated_description = Translate(description, original_lang, target_language)
            final_description += "\n\n" + target_language + ":" + "\n" + translated_description

    if tags != "":
        final_description += "\n\n-\n"+tags
    return final_description
