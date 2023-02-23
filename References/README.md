# Download Script 
This is a script to help you download specific papers from IEEE Xplore
## Usage
Find your personal download license from IEEE website.
1. open the download page by click "PDF"
2. F12 and find `src=....` in elements
3. copy the word after `&ref`, for instance `&ref=ABCDEFG......`, you copy `ABCDEFG`.
4. make a file called `ieee-license`, and paste what you copyed in 3. here.
5. in command 
```
source ./download.sh
```
6. use `DownloadAll` to download all the reference papers in the paperlist;use `DownloadOne <fileid>` to download a single file you want
7. you can change the paper list in paperlist.txt


