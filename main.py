from tuparser import TelegraphParser, run_parser, YAMLOutputFile, TELEGRAPH_URL


class LinkParser(TelegraphParser):
    def __init__(self, config, output_file):
        super().__init__(config)
        self.output_file = output_file

    async def parse(self, url, soup):
        links = [link['href'] for link in soup.findAll('a', href=True)]
        for link in links:
            if link.startswith('mailto:'):
                continue
            if link.startswith('/'):
                link = TELEGRAPH_URL + link
            self.output_file.write_data(link, url)


output_file = YAMLOutputFile({'link': {}, 'url': {}}, 'links-parser-out')
run_parser(LinkParser, parser_args=[output_file])
