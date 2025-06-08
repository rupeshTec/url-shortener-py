import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.counter = 1
        self.charset = string.digits + string.ascii_letters

    def encode_base62(self, num):
        if num == 0:
            return self.charset[0]
        base62 = []
        base = len(self.charset)
        while num > 0:
            num, rem = divmod(num, base)
            base62.append(self.charset[rem])
        return ''.join(reversed(base62))

    def shorten(self, original_url: str) -> str:
        if original_url in self.url_to_code:
            return self.url_to_code[original_url]

        short_code = self.encode_base62(self.counter)
        self.url_to_code[original_url] = short_code
        self.code_to_url[short_code] = original_url
        self.counter += 1
        return short_code

    def resolve(self, short_code: str) -> str | None:
        return self.code_to_url.get(short_code)
