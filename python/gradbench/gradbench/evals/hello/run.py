from typing import Any

import numpy as np
from gradbench.eval import SingleModuleValidatedEval, assertion


def check(function: str, input: Any, output: Any) -> None:
    match function:
        case "double":
            assert np.isclose(output, input * 2)
        case "square":
            assert np.isclose(output, input * input)


def main():
    e = SingleModuleValidatedEval(module="hello", validator=assertion(check))
    e.start()
    if e.define().success:
        x = 1.0
        for _ in range(4):
            y = e.evaluate(function="square", input=x).output
            x = e.evaluate(function="double", input=y).output


if __name__ == "__main__":
    try:
        main()
    except (EOFError, BrokenPipeError):
        pass
