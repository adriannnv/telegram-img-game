from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
from selectolax.lexbor import LexborHTMLParser
from natsort import natsort, ns

@dataclass
class ImageEntity:
	file_path: Path
	timestamp: datetime
	sender: str
	file_size: int

class TelegramExportParser:
	def __init__(self, export_dir: str):
		# takes string input and converts it into a Path object.
		self.export_dir = Path(export_dir)
		self.images = []

	def get_html_files(self) -> list[Path]:
		# finds and naturally sorts all messages.html files
		# .glob returns a generator of path objects that we cast to a list
		files = list(self.export_dir.glob("messages*.html"))

		# import pdb; pdb.set_trace() # for dbugging.
		
		return natsort.natsorted(files, key= lambda p : p.name, alg=ns.IGNORECASE | ns.PATH)
	
	def parse_all(self):
		html_files = self.get_html_files()

		current_date = ""
		current_sender = "Unknown"

		for file_path in html_files:
			with open(file_path, "r", encoding="utf-8") as f:
				html_content = f.read()

			parser = LexborHTMLParser(html_content)

			for node in parser.css(".message, .service"):
				# 1: Update day
				if "service" in node.attributes.get("class", ""):
					date_node = node.css_first(".body") 
					if date_node:
						current_date = date_node.text(strip=True)
					continue
				# 2: Update sender
				sender_node = node.css_first(".from_name")
				if sender_node:
					current_sender = sender_node.text(strip=True)
				# 3: Extract image data
				photo_link = node.css_first("a.photo_wrap")
				if photo_link:
					# photo_link.attributes contains class and href
					relative_path = photo_link.attributes.get("href")
					if relative_path:
						full_path = self.export_dir / relative_path

						time_node = node.css_first(".date")
						time_str = time_node.attributes.get("title", "")

						try:
							timestamp = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S")
						except ValueError:
							timestamp = "you really shouldnt be here"
							
						if full_path.exists():
							self.images.append(ImageEntity(
								file_path=full_path,
								timestamp=timestamp,
								sender=current_sender,
								file_size=full_path.stat().st_size
							)
							)
		return self.images

	def debug_parser_files(export_path_str: str):
		print(f"Target directory: ", export_path_str)
		parser = TelegramExportParser(export_path_str)
		
		found_files = parser.get_html_files()
		print(f"Files found: (Sorted)\n", [f.name for f in found_files])

		results = parser.parse_all()
		print("Extracted ", len(results), " images")
		if results:
			first_result = results[2111]
			print("First image extracted:", first_result.file_path.name, "by", first_result.sender, "at", first_result.timestamp)

if __name__ == "__main__":
	test_path = "/home/guzun/Downloads/Telegram Desktop/ChatExport_2026-02-15"
	TelegramExportParser.debug_parser_files(test_path)