 @ECHO OFF

ECHO Building the ePUB via pandoc.

SETLOCAL

SET "my_epub=Mage of Elements - Volume 2.epub"

SET my_front_matter="Title.md" "Index.md" "AUTHOR.md" "COPYING.md"

SET my_part_1="Part 1.md"
SET my_part_2="Part 2 - Be Brash.md" "Part 2 - Be Patient.md" "Part 2 - Leave Quietly.md" "Part 2 - Common.md"
SET my_part_3="Part 3 - Attack The Hunter.md" "Part 3 - Attack The Prick.md" "Part 3 - Common.md" "Part 3 - Kill Them All.md"


pandoc -s -o "%my_epub%" --epub-metadata Metadata.txt %my_front_matter% %my_part_1% %my_part_2% %my_part_3%