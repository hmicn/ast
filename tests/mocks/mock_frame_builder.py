class MockFrameBuilder:
    def build(self, data):
        return [b'$', b'\xca', b"'", b'\xa0']
