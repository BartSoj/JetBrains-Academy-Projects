from bs4 import BeautifulSoup

fingers = '<?xmlversion="1.0"encoding="UTF-8"?><fingers><finger><name>Thumb</name><hand>Left</hand></finger><finger><name>Index</name><hand>Left</hand></finger><finger><name>Index</name><hand>Right</hand></finger><finger><name>Middle</name><hand>Right</hand></finger><finger><name>Little</name><hand>Left</hand></finger></fingers>'

bs_fingers = BeautifulSoup(fingers, "xml")
print(len(bs_fingers.find_all("finger")))
