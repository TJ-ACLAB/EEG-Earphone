#!/bin/bash

source ./ieee-license

DownloadAll(){
	while read paperid
	do
    		echo "File $paperid Downloading..."
    		paperurl="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=$paperid&ref=$ieeelicense"
		`wget $paperurl -q -O $paperid.pdf`
		echo "Finish"
	done < paperlist.txt
}

DownloadOne(){
	paperurl="https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=$1&ref=$ieeelicense"
	echo "File $1 Downloading..."
	`wget $paperurl -q -O $1.pdf`
	echo "Finish"
}
