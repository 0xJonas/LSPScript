import argparse
import json
from pathlib import Path

import gen.schema.types as t
from gen.generate_capabilities import (generate_capabilities_py,
                                       parse_capabilities)
from gen.generate_client_requests import generate_client_requests_py
from gen.generate_enumerations import generate_enumerations_py
from gen.generate_structures import generate_structures_py
from gen.generator import Generator


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m gen.main",
        description="Generates source files for LSPScript from the LSP meta model.")
    parser.add_argument("input", help="Metamodel JSON file to use as input.")
    parser.add_argument("output", help="Output directory for the generated files.")
    return parser.parse_args()


def create_generator(input: Path) -> Generator:
    with open(input, encoding="utf-8") as file:
        raw = json.load(file)
        meta_model = t.MetaModel.from_json(raw)

    print(f"Structures: {len(meta_model.structures)}")
    print(f"Notifications: {len(meta_model.notifications)}")
    print(f"Requests: {len(meta_model.requests)}")
    print(f"Type aliases: {len(meta_model.type_aliases)}")
    print(f"Enumerations: {len(meta_model.enumerations)}")

    return Generator(meta_model)


def generate_output_files(out_dir: Path) -> None:
    if not out_dir.is_dir():
        out_dir.mkdir()

    static_dir = Path("./gen/static/")
    assert static_dir.is_dir()
    for f in static_dir.iterdir():
        if not f.suffix == ".py":
            continue
        with open(f) as input, open(out_dir.joinpath(f.name), "w", newline="\n") as output:
            output.write(input.read())

    with open(out_dir.joinpath("enumerations.py"), "w", encoding="utf-8", newline="\n") as file:
        file.write(generate_enumerations_py(generator))
    with open(out_dir.joinpath("structures.py"), "w", encoding="utf-8", newline="\n") as file:
        file.write(generate_structures_py(generator))
    with open(out_dir.joinpath("client_requests.py"), "w", encoding="utf-8", newline="\n") as file:
        file.write(generate_client_requests_py(generator))
    with open(out_dir.joinpath("capabilities.py"), "w", encoding="utf-8", newline="\n") as file:
        file.write(generate_capabilities_py(generator, feature_infos))
    with open(out_dir.joinpath("__init__.py"), "w", encoding="utf-8", newline="\n") as file:
        file.write(generator.generate_init_py())


if __name__ == "__main__":
    args = parse_arguments()

    input_dir = Path(args.input)
    generator = create_generator(input_dir/"metaModel.json")
    feature_infos = parse_capabilities(Path(input_dir/"capabilities.json"))

    generate_output_files(Path(args.output))
