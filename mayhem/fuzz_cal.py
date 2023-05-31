#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    import micawber

providers = micawber.bootstrap_basic()
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        if fdp.ConsumeBool():
            providers.parse_text(text=fdp.ConsumeRemainingString())
        else:
            providers.parse_html(fdp.ConsumeRemainingString())
    except Exception:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
