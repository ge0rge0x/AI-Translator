#!/bin/bash

translate() {
    # Prompt the user for input
    #read -p "Enter the source language code (e.g., 'en' for English): " from_lang
    #read -p "Enter the target language code (e.g., 'es' for Spanish): " to_lang
    clear
    read -p "Enter the text to translate: " text
    echo "Translating..."

    translated_text=$(tgpt -q --provider openai --key "translate from $from_lang to $to_lang this message '$text' output translated text only DO NOT CONTAIN ANY ADDITIONAL TEXT" | sed 's/"//g')
    
    if [ -n "$translated_text" ]; then
        clear
        echo "Original text: $text"
        echo "Translated text: $translated_text"
        read -p "Press enter to continue..."
        welcome
    else
        echo "!An error occurred during translation!"
        read -p "Press enter to continue..."
        welcome
    fi
}
