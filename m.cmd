 @ECHO OFF

ECHO Building the ePUB via pandoc.

SETLOCAL

SET "my_epub=Mage of Elements - Volume 2.epub"

SET my_front_matter="Title.md" "Index.md" "AUTHOR.md" "COPYING.md"

SET my_part_1="Part 1.md"
SET my_part_2="Part 2 - Be Brash.md" "Part 2 - Be Patient.md" "Part 2 - Leave Quietly.md" "Part 2 - Common.md"
SET my_part_3="Part 3 - Attack The Hunter.md" "Part 3 - Attack The Prick.md" "Part 3 - Common.md" "Part 3 - Kill Them All.md"
SET my_part_4="Part 4 - Run For The Inn.md" "Part 4 - Run For The Alley.md" "Part 4 - Improvise On The Spot.md" "Part 4 - Common.md"
SET my_part_5="Part 5 - Charge The Ninja.md" "Part 5 - Run Like Hell.md" "Part 5 - Common.md"

pandoc -s -o "%my_epub%" --epub-metadata Metadata.txt %my_front_matter% %my_part_1% %my_part_2% %my_part_3% %my_part_4% %my_part_5%
