from tuparser import TELEGRAPH_URL, TelegraphParser, run_parser


class LinkParser(TelegraphParser):
    async def parse(self, url, soup):
        links = [link['href'] for link in soup.findAll('a', href=True)]
        for link in links:
            if link.startswith('mailto:'):
                continue
            if link.startswith('/'):
                link = TELEGRAPH_URL + link
            self.output_file.write_data(link, url)


run_parser(LinkParser, titles=[''], output_file=[{'link': {}, 'url': {}}, 'links-parser-out'])
