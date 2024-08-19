#!/bin/bash
default_lang() {
	#setting the default language
	from_lang="Auto Detect"
	to_lang="English"
}
language(){
	clear
	echo "-------------------------------------------"
	echo "           Changing language"
	echo "-------------------------------------------"
	read -p "Enter the source language code (e.g., 'en' for English): " from_lang
	read -p "Enter the target language code (e.g., 'es' for Spanish): " to_lang
	welcome
}
