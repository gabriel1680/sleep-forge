import os


class OsDirScanner:
    def scan_dir(self, dirname: str) -> list[str]:
        return [os.path.join(dirname, filename)
                for filename in os.listdir(dirname)
                if filename.endswith(".txt")]
