from tuparser import *
       
class LinkParser(TelegraphParser):
    def __init__(self, config, output_file):
        super().__init__(config)
        self.output_file = output_file
        
    async def parse(self, url, soup):
        raw_links = soup.findAll("a", href = True)
        for raw_link in raw_links:
            link = raw_link['href']
            if not link.startswith('mailto:'): 
                self.output_file.write_output((link,))
                

output_file = YAMLOutputFile({"link": {}}, "link-parser-out")
run_parser(
    config_class=Config,
    parser_args=(output_file,),
    parser_class=LinkParser
)