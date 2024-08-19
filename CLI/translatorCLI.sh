#!/bin/bash
source ./translate.sh
source ./language.sh

welcome(){
	clear
	echo "-------------------------------------------"
	echo "Welcome To The AI Translation Applicaion"
	echo "-------------------------------------------"
	echo ""
	echo "Currently translating from $from_lang to $to_lang"
	echo ""
	echo "What would you like to do?"
	echo "1. Change translation language"
	echo "2. Translate text"
	echo "3. Exit"
	read -p "" select
	if [[ "$select" == "1" ]]; then
		language
	elif [[ "$select" == "2" ]]; then
		translate
	elif [[ "$select" == "3" ]]; then
		clear
		echo "-------------------------------------------"
		echo "-----------------Goodbye-------------------"
		echo "-------------------------------------------"
		sleep 5
		clear
		exit
	fi
}
default_lang
welcome
